from PyQt5.QtWidgets import QDoubleSpinBox
from PyQt5.QtCore import pyqtProperty

class DoubleSpinBox(QDoubleSpinBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._borderRadius = 0  # 默认边框半径为0
        self._updateStyleSheet()

    def _updateStyleSheet(self):
        style_sheet = '''
QDoubleSpinBox {
color: black;
background-color: rgba(255, 255, 255, 0.7);
border: 1px solid rgba(0, 0, 0, 13);
border-bottom: 1px solid rgba(0, 0, 0, 100);
border-radius: ''' + str(self._borderRadius) + '''px;
font: 14px "Segoe UI", "Microsoft YaHei";
padding-left: 10px;
selection-background-color: #4bb7e6;
min-height: 30px;
}

QDoubleSpinBox:read-only,
QDoubleSpinBox[symbolVisible=false] {
padding: 0px 10px 0 10px;
}

QDoubleSpinBox:hover {
background-color: rgba(249, 249, 249, 0.5);
border: 1px solid rgba(0, 0, 0, 13);
border-bottom: 1px solid rgba(0, 0, 0, 100);
}

QDoubleSpinBox::focus {
border-bottom: 1px solid rgba(0, 0, 0, 13);
background-color: white;
border-bottom: 2px solid #47aedb;
}

QDoubleSpinBox::up-button {
image: url(:/widget/widget/SpinBoxUp.png);
background-color: rgba(0, 0, 0, 0);
border: 1px solid rgba(0, 0, 0, 0);
border-radius: 4px;
margin-top: 1px;
margin-bottom: 1px;
margin-right: 2px;
min-width: 30px;
max-width: 30px;
min-height: 16px;
}

QDoubleSpinBox::up-button:hover {
background-color: rgba(0, 0, 0, 10);
}

QDoubleSpinBox::up-button:pressed {
background-color: rgba(0, 0, 0, 5);
}

QDoubleSpinBox::down-button {
image: url(:/widget/widget/SpinBoxDown.png);
background-color: rgba(0, 0, 0, 0);
border: 1px solid rgba(0, 0, 0, 0);
border-radius: 4px;
margin-top: 1px;
margin-bottom: 1px;
margin-right: 2px;
min-width: 30px;
max-width: 30px;
min-height: 16px;
}
QDoubleSpinBox::down-button:hover {
background-color: rgba(0, 0, 0, 10);
}
QDoubleSpinBox::down-button:pressed {
background-color: rgba(0, 0, 0, 5);
}
QDoubleSpinBox::drop-down {
background-color: transparent;
width: 50px;
}
QDoubleSpinBox:disabled {
color: rgba(0, 0, 0, 150);
background-color: rgba(249, 249, 249, 0.5);
border: 1px solid rgba(0, 0, 0, 13);
border-bottom: 1px solid rgba(0, 0, 0, 13);
}
QDoubleSpinBox::up-button:disabled {
image: url(:/widget/widget/SpinBoxUpDisabled.png);
}
QDoubleSpinBox::down-button:disabled {
image: url(:/widget/widget/SpinBoxDownDisabled.png);
}
'''
        self.setStyleSheet(style_sheet)

    @pyqtProperty(int)
    def borderRadius(self):
        """获取输入框边框半径"""
        return self._borderRadius

    @borderRadius.setter
    def borderRadius(self, radius):
        """设置输入框边框半径"""
        self._borderRadius = radius
        self._updateStyleSheet()



