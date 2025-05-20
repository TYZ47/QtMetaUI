import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import pyqtProperty



class Button(QPushButton):
    def __init__(self, text_or_parent=None, parent=None):
        # 检查第一个参数是否是QWidget类型
        if parent is None and isinstance(text_or_parent, QWidget):
            # 如果第一个参数是QWidget且没有提供parent
            # 则将第一个参数作为parent，text设为空
            super().__init__(parent=text_or_parent)
            text = ""
        else:
            # 否则按正常方式处理参数
            super().__init__(text_or_parent, parent)
            text = text_or_parent if isinstance(text_or_parent, str) else ""
            
        self._borderRadius = 0  # 默认边框半径为0
        self._updateStyleSheet()

    def _updateStyleSheet(self):
        style_sheet = f"""
        QPushButton {{
            color: black;
            background: rgba(255, 255, 255, 0.7);
            border: 1px solid rgba(0, 0, 0, 0.073);
            border-bottom: 1px solid rgba(0, 0, 0, 0.183);
            border-radius: {self._borderRadius}px;
            font: 14px 'Segoe UI', 'Microsoft YaHei';
            padding: 5px 10px 6px 10px;
            outline: none;
            min-height: 19px; /*19 + 2 + 5 + 6*/
        }}
        QPushButton[isPlaceholderText=true] {{
            color: rgba(0, 0, 0, 0.6063);
        }}
        QPushButton[hasIcon=false] {{
            padding: 5px 12px 6px 12px;
        }}
        QPushButton[hasIcon=true] {{
            padding: 5px 12px 6px 36px;
        }}
        QPushButton:hover {{
            background: rgba(249, 249, 249, 0.5);
        }}
        QPushButton:pressed {{
            color: rgba(0, 0, 0, 0.63);
            background: rgba(249, 249, 249, 0.3);
            border-bottom: 1px solid rgba(0, 0, 0, 0.073);
        }}
        QPushButton:disabled {{
            color: rgba(0, 0, 0, 0.36);
            background: rgba(249, 249, 249, 0.3);
            border: 1px solid rgba(0, 0, 0, 0.06);
            border-bottom: 1px solid rgba(0, 0, 0, 0.06);
        }}
        """
        self.setStyleSheet(style_sheet)

    @pyqtProperty(int)
    def borderRadius(self):
        """获取按钮边框半径"""
        return self._borderRadius

    @borderRadius.setter
    def borderRadius(self, radius):
        """设置按钮边框半径"""
        self._borderRadius = radius
        self._updateStyleSheet()


