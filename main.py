import sys
import os
import random

from PySide6.QtCore import Qt, QTimer, QFile, QIODevice, QObject, QEvent, Signal
from PySide6.QtWidgets import (
    QApplication, QFrame, QGraphicsDropShadowEffect
)
from PySide6.QtGui import QColor
from PySide6.QtUiTools import QUiLoader


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UI_DIR = BASE_DIR
RECORD_FILE = os.path.join(BASE_DIR, "record.txt")

DEFAULT_STYLE = "QFrame { background-color: #f5f8fa; border: 1px solid #e3e8ec; border-radius: 6px; }"
ACTIVE_STYLE = "QFrame { background-color: #1976d2; border: 1px solid #1976d2; border-radius: 6px; }"


class CellFilter(QObject):
    clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._active = False

    def set_active(self, value):
        self._active = value
        widget = self.parent()
        if value:
            widget.setCursor(Qt.PointingHandCursor)
            widget.setStyleSheet(ACTIVE_STYLE)
        else:
            widget.setCursor(Qt.ArrowCursor)
            widget.setStyleSheet(DEFAULT_STYLE)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress and self._active:
            if event.button() == Qt.LeftButton:
                self.clicked.emit()
                return True
        return super().eventFilter(obj, event)


class GameController:
    GAME_TIME = 15000
    SQUARE_LIFE = 1200
    GRID = 5

    def __init__(self):
        loader = QUiLoader()
        self.main_window = self._load_ui(loader, "main_window.ui")
        self.game_window = self._load_ui(loader, "game_window.ui")
        self.end_window = self._load_ui(loader, "end_window.ui")

        self._add_shadow(self.main_window.findChild(QFrame, "card"))
        self._add_shadow(self.game_window.findChild(QFrame, "card"))
        self._add_shadow(self.end_window.findChild(QFrame, "card"))

        self.record = self._load_record()

        self.cells = []
        self.filters = []
        for r in range(self.GRID):
            for c in range(self.GRID):
                name = f"cell_{r}_{c}"
                cell = self.game_window.findChild(QFrame, name)
                if cell is None:
                    raise RuntimeError(f"Не найден {name} в game_window.ui")

                flt = CellFilter(cell)
                flt.clicked.connect(self.on_cell_clicked)
                cell.installEventFilter(flt)
                flt.set_active(False)

                self.cells.append(cell)
                self.filters.append(flt)

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

    def set_cell_active(self, idx, value):
        self.filters[idx].set_active(value)

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

        for i in range(len(self.cells)):
            self.set_cell_active(i, False)
        self.active_index = -1

        self.game_window.show()
        self.game_timer.start()
        self.spawn_square()

    def spawn_square(self):
        if self.active_index >= 0:
            self.set_cell_active(self.active_index, False)
        new_idx = random.randint(0, len(self.cells) - 1)
        if new_idx == self.active_index and len(self.cells) > 1:
            new_idx = (new_idx + 1) % len(self.cells)
        self.active_index = new_idx
        self.set_cell_active(new_idx, True)
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
            self.set_cell_active(self.active_index, False)
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