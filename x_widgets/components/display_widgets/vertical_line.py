from PyQt5.QtWidgets import QFrame, QWidget, QHBoxLayout, QApplication
from PyQt5.QtCore import Qt
import sys

class VerticalLine(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setFrameShape(QFrame.VLine)
        
        self.setMaximumWidth(3)
        self.setMinimumWidth(3)

        self._updateStyleSheet()
    
    def _updateStyleSheet(self):
        style_sheet = """
        VerticalLine {
            border: none;
            background-color: #E4E4E4;
        }
        """
        self.setStyleSheet(style_sheet)

