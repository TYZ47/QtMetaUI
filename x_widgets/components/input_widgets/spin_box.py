from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtCore import pyqtProperty

class SpinBox(QSpinBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._borderRadius = 0  # 默认边框半径为0
        self._updateStyleSheet()

    def _updateStyleSheet(self):
        style_sheet = '''
QSpinBox {
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
SpinBox:read-only,
SpinBox[symbolVisible=false] {
padding: 0px 10px 0 10px;
}
QSpinBox:hover {
background-color: rgba(249, 249, 249, 0.5);
border: 1px solid rgba(0, 0, 0, 13);
border-bottom: 1px solid rgba(0, 0, 0, 100);
}
QSpinBox::focus {
border-bottom: 1px solid rgba(0, 0, 0, 13);
background-color: white;
border-bottom: 2px solid  #47aedb;
}
QSpinBox::up-button {
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
QSpinBox::up-button:hover {
background-color: rgba(0, 0, 0, 10);
}
QSpinBox::up-button:pressed {
background-color: rgba(0, 0, 0, 5);
}
QSpinBox::down-button {
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
QSpinBox::down-button:hover {
background-color: rgba(0, 0, 0, 10);
}
QSpinBox::down-button:pressed {
background-color: rgba(0, 0, 0, 5);
}
QSpinBox::drop-down {
background-color: transparent;
width: 50px;
}
QSpinBox:disabled {
color: rgba(0, 0, 0, 150);
background-color: rgba(249, 249, 249, 0.5);
border: 1px solid rgba(0, 0, 0, 13);
border-bottom: 1px solid rgba(0, 0, 0, 13);
}
QSpinBox::up-button:disabled {
image: url(:/widget/widget/SpinBoxUpDisabled.png);
}
QSpinBox::down-button:disabled {
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

