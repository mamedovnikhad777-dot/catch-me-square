import sys
import os
import random

from PySide6.QtCore import Qt, QTimer, QFile, QIODevice, Signal
from PySide6.QtWidgets import (
    QApplication, QFrame, QGraphicsDropShadowEffect
)
from PySide6.QtGui import QColor
from PySide6.QtUiTools import QUiLoader


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UI_DIR = os.path.join(BASE_DIR, "design")
RECORD_FILE = os.path.join(BASE_DIR, "record.txt")

DEFAULT_STYLE = "GridCell { background-color: #f5f8fa; border: 1px solid #e3e8ec; border-radius: 6px; }"
ACTIVE_STYLE = "GridCell { background-color: #1976d2; border: none; border-radius: 6px; }"


class GridCell(QFrame):
    clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._active = False
        self.setStyleSheet(DEFAULT_STYLE)

    def set_inactive(self):
        self._active = False
        self.setCursor(Qt.ArrowCursor)
        self.setStyleSheet(DEFAULT_STYLE)

    def set_active(self):
        self._active = True
        self.setCursor(Qt.PointingHandCursor)
        self.setStyleSheet(ACTIVE_STYLE)

    def mousePressEvent(self, event):
        if self._active and event.button() == Qt.LeftButton:
            self.clicked.emit()
        super().mousePressEvent(event)


class GameController:
    GAME_TIME = 15000
    SQUARE_LIFE = 1200
    GRID = 5

    def __init__(self):
        loader = QUiLoader()
        loader.registerCustomWidget(GridCell)
        self.main_window = self._load_ui(loader, "main_window.ui")
        self.game_window = self._load_ui(loader, "game_window.ui")
        self.end_window = self._load_ui(loader, "end_window.ui")

        self._add_shadow(self.main_window.findChild(QFrame, "card"))
        self._add_shadow(self.game_window.findChild(QFrame, "card"))
        self._add_shadow(self.end_window.findChild(QFrame, "card"))

        self.record = self._load_record()

        self.cells = []
        for r in range(self.GRID):
            for c in range(self.GRID):
                cell = self.game_window.findChild(GridCell, f"cell_{r}_{c}")
                cell.clicked.connect(self.on_cell_clicked)
                self.cells.append(cell)

        self.active_index = -1
        self.score = 0
        self.time_left = 0

        self.game_timer = QTimer()
        self.game_timer.setInterval(50)
        self.game_timer.timeout.connect(self.tick)

        self.move_timer = QTimer()
        self.move_timer.setSingleShot(True)
        self.move_timer.timeout.connect(self.move_square)

        self.main_window.btnStart.clicked.connect(self.start_game)
        self.end_window.btnPlayAgain.clicked.connect(self.start_game)
        self.end_window.btnRestart.clicked.connect(self.start_game)

        self.reset_cells()
        self.show_main()

    def _load_ui(self, loader, name):
        path = os.path.join(UI_DIR, name)
        if not os.path.exists(path):
            raise FileNotFoundError(path)
        f = QFile(path)
        if not f.open(QIODevice.ReadOnly):
            raise RuntimeError(path)
        w = loader.load(f)
        f.close()
        return w

    def _add_shadow(self, widget):
        if widget is None:
            return
        eff = QGraphicsDropShadowEffect(widget)
        eff.setBlurRadius(22)
        eff.setColor(QColor(0, 0, 0, 28))
        eff.setOffset(0, 4)
        widget.setGraphicsEffect(eff)

    def _load_record(self):
        try:
            with open(RECORD_FILE, "r", encoding="utf-8") as f:
                return int(f.read().strip() or 0)
        except Exception:
            return 0

    def _save_record(self, value):
        try:
            with open(RECORD_FILE, "w", encoding="utf-8") as f:
                f.write(str(value))
        except Exception:
            pass

    def reset_cells(self):
        for c in self.cells:
            c.set_inactive()
        self.active_index = -1

    def show_main(self):
        self.game_timer.stop()
        self.move_timer.stop()
        self.main_window.labelRecordValue.setText(str(self.record))
        self.game_window.hide()
        self.end_window.hide()
        self.main_window.show()

    def start_game(self):
        self.main_window.hide()
        self.end_window.hide()

        self.score = 0
        self.time_left = self.GAME_TIME

        self.game_window.labelScoreValue.setText("0")
        self.game_window.labelRecordValue.setText(str(self.record))
        self.game_window.progressBar.setValue(100)

        self.reset_cells()
        self.game_window.show()
        self.game_timer.start()
        self.spawn_square()

    def spawn_square(self):
        if self.active_index >= 0:
            self.cells[self.active_index].set_inactive()
        new_idx = random.randint(0, len(self.cells) - 1)
        if new_idx == self.active_index and len(self.cells) > 1:
            new_idx = (new_idx + 1) % len(self.cells)
        self.active_index = new_idx
        self.cells[new_idx].set_active()
        self.move_timer.start(self.SQUARE_LIFE)

    def move_square(self):
        if self.time_left > 0:
            self.spawn_square()

    def on_cell_clicked(self):
        if self.time_left <= 0:
            return
        self.score += 1
        self.game_window.labelScoreValue.setText(str(self.score))
        self.move_timer.stop()
        self.spawn_square()

    def tick(self):
        self.time_left -= self.game_timer.interval()
        if self.time_left < 0:
            self.time_left = 0
        pct = int(self.time_left / self.GAME_TIME * 100)
        self.game_window.progressBar.setValue(pct)
        if self.time_left <= 0:
            self.end_game()

    def end_game(self):
        self.game_timer.stop()
        self.move_timer.stop()
        if self.active_index >= 0:
            self.cells[self.active_index].set_inactive()
        self.active_index = -1

        new_record = False
        if self.score > self.record:
            self.record = self.score
            self._save_record(self.record)
            new_record = True

        self.end_window.labelScoreValue.setText(str(self.score))
        self.end_window.labelRecordValue.setText(str(self.record))
        self.end_window.labelFinalScore.setText(str(self.score))
        if new_record and self.score > 0:
            self.end_window.labelMessage.setText("Новый рекорд! Отличный результат!")
        else:
            self.end_window.labelMessage.setText("Попробуй поймать еще больше квадратов!")

        self.game_window.hide()
        self.end_window.show()


def main():
    app = QApplication(sys.argv)
    controller = GameController()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()