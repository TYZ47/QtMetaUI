from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtCore import pyqtProperty

class TextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._borderRadius = 0  # 默认边框半径为0
        self._updateStyleSheet()

    def _updateStyleSheet(self):
        style_sheet = '''
QTextEdit {
color: black;
background-color: rgba(255, 255, 255, 0.7);
border: 1px solid rgba(0, 0, 0, 13);
border-bottom: 1px solid rgba(0, 0, 0, 100);
border-radius: ''' + str(self._borderRadius) + '''px;
font: 14px "Segoe UI", "Microsoft YaHei";
padding: 0px 10px;
min-height: 30px;
selection-background-color: #47aedb;
}
QTextEdit:hover {
background-color: rgba(249, 249, 249, 0.5);
border: 1px solid rgba(0, 0, 0, 13);
border-bottom: 1px solid rgba(0, 0, 0, 100);
}
QTextEdit:focus {
border-bottom: 3px solid #47aedb;
background-color: white;
}
QTextEdit:disabled {
color: rgba(0, 0, 0, 92);
background-color: rgba(249, 249, 249, 0.3);
border: 1px solid rgba(0, 0, 0, 13);
border-bottom: 1px solid rgba(0, 0, 0, 13);
}
'''
        self.setStyleSheet(style_sheet)

    @pyqtProperty(int)
    def borderRadius(self):
        """获取文本框边框半径"""
        return self._borderRadius

    @borderRadius.setter
    def borderRadius(self, radius):
        """设置文本框边框半径"""
        self._borderRadius = radius
        self._updateStyleSheet()