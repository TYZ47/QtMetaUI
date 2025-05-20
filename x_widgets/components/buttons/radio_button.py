from PyQt5.QtWidgets import QRadioButton, QWidget

class RadioButton(QRadioButton):
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
        style_sheet = """
        QRadioButton {
            min-height: 24px;
            max-height: 24px;
            background-color: transparent;
            font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';
            color: black;
        }
        
        QRadioButton::indicator {
            width: 18px;
            height: 18px;
            border-radius: 11px;
            border: 2px solid #999999;
            background-color: rgba(0, 0, 0, 5);
            margin-right: 4px;
        }
        
        QRadioButton::indicator:hover {
            background-color: rgba(0, 0, 0, 0);
        }
        
        QRadioButton::indicator:pressed {
            border: 2px solid #bbbbbb;
            background-color: qradialgradient(
                spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,
                stop:0 rgb(255, 255, 255),
                stop:0.5 rgb(255, 255, 255),
                stop:0.6 rgb(225, 224, 223),
                stop:1 rgb(225, 224, 223)
            );
        }
        
        QRadioButton::indicator:checked {
            height: 22px;
            width: 22px;
            border: none;
            border-radius: 11px;
            background-color: qradialgradient(
                spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,
                stop:0 rgb(255, 255, 255),
                stop:0.5 rgb(255, 255, 255),
                stop:0.6 #47aedb,
                stop:1 #47aedb
            );
        }
        
        QRadioButton::indicator:checked:hover {
            background-color: qradialgradient(
                spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,
                stop:0 rgb(255, 255, 255),
                stop:0.6 rgb(255, 255, 255),
                stop:0.7 #47aedb,
                stop:1 #47aedb
            );
        }
        
        QRadioButton::indicator:checked:pressed {
            background-color: qradialgradient(
                spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,
                stop:0 rgb(255, 255, 255),
                stop:0.5 rgb(255, 255, 255),
                stop:0.6 #47aedb,
                stop:1 #47aedb
            );
        }
        
        QRadioButton:disabled {
            color: rgba(0, 0, 0, 110);
        }
        
        QRadioButton::indicator:disabled {
            border: 2px solid #bbbbbb;
            background-color: transparent;
        }
        
        QRadioButton::indicator:disabled:checked {
            border: none;
            background-color: qradialgradient(
                spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,
                stop:0 rgb(255, 255, 255),
                stop:0.5 rgb(255, 255, 255),
                stop:0.6 rgba(0, 0, 0, 0.2169),
                stop:1 rgba(0, 0, 0, 0.2169)
            );
        }
        """
        self.setStyleSheet(style_sheet)