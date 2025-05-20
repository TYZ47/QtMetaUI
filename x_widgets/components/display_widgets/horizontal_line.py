from PyQt5.QtWidgets import QFrame, QWidget, QVBoxLayout, QApplication
from PyQt5.QtCore import Qt
import sys

class HorizontalLine(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # 设置为水平线
        self.setFrameShape(QFrame.HLine)
        
        # 设置最小最大高度都是1px
        self.setMaximumHeight(2)
        self.setMinimumHeight(2)
        
        # 设置样式
        self._updateStyleSheet()
    
    def _updateStyleSheet(self):
        style_sheet = """
        HorizontalLine {
            border: none;
            background-color: #E4E4E4;
        }
        """
        self.setStyleSheet(style_sheet)

