from PyQt5.QtWidgets import QCheckBox

class CheckBox(QCheckBox):
    def __init__(self, parent=None, text=""):
        super().__init__(parent)
        if text:
            self.setText(text)
        self._updateStyleSheet()

    def _updateStyleSheet(self):
        style_sheet = """
        QCheckBox {
            color: black;
            font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';
            spacing: 8px;
            min-width: 28px;
            min-height: 22px;
            outline: none;
            margin-left: 1px;
        }
        
        QCheckBox::indicator {
            width: 18px;
            height: 18px;
            border-radius: 5px;
            border: 2px solid grey;
            background-color: grey;
        }
        
        QCheckBox:disabled {
            color: rgba(0, 0, 0, 110);
        }
        
        QCheckBox::indicator:unchecked {
            background-color: rgba(0, 0, 0, 6);
            border: 2px solid rgba(153, 153, 153, 255);
        }
        
        QCheckBox::indicator:unchecked:hover {
            background-color: rgba(0, 0, 0, 0);
        }
        
        QCheckBox::indicator:unchecked:pressed {
            background-color: rgba(0, 0, 0, 31);
            border: 2px solid #bbbbbb;
        }
        
        QCheckBox::indicator:checked {
            background-color: rgba(71, 174, 219, 255);
            border: 2px solid rgba(71, 174, 219, 255);
            image: url(:/widget/widget/accept.svg);
        }
        
        QCheckBox::indicator:checked:hover {
            background-color: rgba(75, 183, 230, 255);
            border: 2px solid rgba(75, 183, 230, 255);
        }
        
        QCheckBox::indicator:checked:pressed {
            background-color: rgba(113, 195, 230, 255);
            border: 2px solid rgba(113, 195, 230, 255);
        }
        
        QCheckBox::indicator:disabled {
            background-color: rgba(0, 0, 0, 0);
            border: 2px solid #bbbbbb;
        }
        
        QCheckBox::indicator:checked:disabled {
            background-color: rgba(0, 0, 0, 56);
            border: 2px solid #C2C2C2;
        }
        
        QCheckBox::indicator:indeterminate {
            background-color: rgba(71, 174, 219, 255);
            border: 2px solid rgba(71, 174, 219, 255);
            image: url(:/widget/widget/PartialAccept.svg);
        }
        
        QCheckBox::indicator:indeterminate:disabled {
            background-color: rgba(0, 0, 0, 56);
            border: 2px solid #C2C2C2;
        }
        
        QCheckBox::indicator:indeterminate:hover {
            background-color: rgba(75, 183, 230, 255);
            border: 2px solid rgba(75, 183, 230, 255);
        }
        
        QCheckBox::indicator:indeterminate:pressed {
            background-color: rgba(113, 195, 230, 255);
            border: 2px solid rgba(113, 195, 230, 255);
        }
        """
        self.setStyleSheet(style_sheet)