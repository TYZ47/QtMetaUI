import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import pyqtProperty



class LinkButton(QPushButton):
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
            

        self._updateStyleSheet()

    def _updateStyleSheet(self):
        style_sheet = f"""
        QPushButton {{
            color: #47AEDB;
            background: transparent;
            border: 0px solid red;
            border-radius: 5px;

            font: 14px 'Segoe UI', 'Microsoft YaHei';
            padding: 5px 10px 6px 10px;
            outline: none;
            min-height: 19px; /*19 + 2 + 5 + 6*/
        }}

        QPushButton:hover {{
            background: rgba(249, 249, 249, 0.9);
        }}
        QPushButton:pressed {{
            color: #47AEDB;
            background: rgba(249, 249, 249, 0.5);

        }}
        QPushButton:disabled {{
            color: rgba(0, 0, 0, 0.36);
            background: rgba(249, 249, 249, 0.3);
            font-wight: 500;
        }}
        """
        self.setStyleSheet(style_sheet)

