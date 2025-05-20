from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtGui import QColor

class BorderTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._borderRadius = 0
        self._borderWidth = 1
        self._borderColor = QColor(0, 0, 0, 50)
        self._focusColor = QColor(71, 174, 219)
        self._updateStyleSheet()

    def _updateStyleSheet(self):
        style_sheet = f'''
QTextEdit {{
    color: black;
    background-color: rgba(255, 255, 255, 0.7);
    border: {self._borderWidth}px solid rgba({self._borderColor.red()}, {self._borderColor.green()}, {self._borderColor.blue()}, {self._borderColor.alpha()});
    border-radius: {self._borderRadius}px;
    font: 14px "Segoe UI", "Microsoft YaHei";
    padding: 0px 10px;
    selection-background-color: #47aedb;
}}
QTextEdit:hover {{
    background-color: rgba(249, 249, 249, 0.5);
    border: {self._borderWidth}px solid rgba({self._borderColor.red()}, {self._borderColor.green()}, {self._borderColor.blue()}, {self._borderColor.alpha()});
}}
QTextEdit:focus {{
    border: {self._borderWidth}px solid rgba({self._focusColor.red()}, {self._focusColor.green()}, {self._focusColor.blue()}, {self._focusColor.alpha()});
    background-color: white;
}}
QTextEdit:disabled {{
    color:#cdcdcd;
}}
'''
        self.setStyleSheet(style_sheet)

    @pyqtProperty(int)
    def borderRadius(self):
        return self._borderRadius

    @borderRadius.setter
    def borderRadius(self, radius):
        self._borderRadius = max(0, radius)
        self._updateStyleSheet()
        
    @pyqtProperty(int)
    def borderWidth(self):
        return self._borderWidth
        
    @borderWidth.setter
    def borderWidth(self, width):
        self._borderWidth = max(0, width)
        self._updateStyleSheet()
        
    @pyqtProperty(QColor)
    def focusColor(self):
        return self._focusColor
        
    @focusColor.setter
    def focusColor(self, color):
        self._focusColor = color
        self._updateStyleSheet()
