from PyQt5.QtWidgets import QLabel, QWidget
from PyQt5.QtCore import pyqtProperty

class Label(QLabel):
    def __init__(self, text_or_parent=None, parent=None):
        # 如果第一个参数是QWidget，则认为是parent
        if parent is None and isinstance(text_or_parent, QWidget):
            super().__init__(parent=text_or_parent)
            text = ""
        else:
            super().__init__(text_or_parent, parent)
            text = text_or_parent if isinstance(text_or_parent, str) else ""
            
        self._fontSize = 14  # 默认字体大小
        self._isBold = False  # 默认不加粗
        self._updateStyleSheet()

    def _updateStyleSheet(self):
        # 根据是否加粗决定 font-weight
        font_weight = "500" if self._isBold else "normal"
        
        style_sheet = f"""
        QLabel {{
            font: {self._fontSize}px 'Segoe UI', 'Microsoft YaHei';
            font-weight: {font_weight};
        }}
        """
        self.setStyleSheet(style_sheet)

    @pyqtProperty(int)
    def fontSize(self):
        """获取字体大小"""
        return self._fontSize

    @fontSize.setter
    def fontSize(self, size):
        """设置字体大小"""
        self._fontSize = size
        self._updateStyleSheet()

    @pyqtProperty(bool)
    def isBold(self):
        """获取是否加粗"""
        return self._isBold

    @isBold.setter
    def isBold(self, bold):
        """设置是否加粗"""
        self._isBold = bold
        self._updateStyleSheet()