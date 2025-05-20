from PyQt5.QtWidgets import QComboBox
from PyQt5.QtCore import pyqtProperty

class ComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._borderRadius = 0  # 默认边框半径为0
        self._updateStyleSheet()

    def _updateStyleSheet(self):
        style_sheet = f"""
        QComboBox {{
            border: 1px solid rgba(0, 0, 0, 0.073);
            border-radius: {self._borderRadius}px;
            border-bottom: 1px solid rgba(0, 0, 0, 0.183);
            padding: 5px 10px 6px 10px;
            font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';
            color: black;
            background-color: rgba(255, 255, 255, 0.7);
            text-align: left;
            outline: none;
            min-height: 19px;
        }}
        
        QComboBox:hover {{
            background-color: rgba(249, 249, 249, 0.5);
        }}
        
        QComboBox:pressed {{
            background-color: rgba(249, 249, 249, 0.3);
            border-bottom: 1px solid rgba(0, 0, 0, 0.073);
        }}
        
        QComboBox:disabled {{
            color: rgba(0, 0, 0, 0.36);
            background: rgba(249, 249, 249, 0.3);
            border: 1px solid rgba(0, 0, 0, 0.06);
            border-bottom: 1px solid rgba(0, 0, 0, 0.06);
        }}
        
        QComboBox[isPlaceholderText=true] {{
            color: rgba(0, 0, 0, 0.6063);
        }}
        
        QComboBox::drop-down {{
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 25px;
            border-left: none;
        }}
        
        QComboBox::down-arrow {{
            image: url(:/widget/widget/ComboBox.png);
        }}
        
        QComboBox::down-arrow:disabled {{
            image: url(:/widget/widget/ComboBoxDisabled.png);
        }}
        
        QComboBox::down-arrow:on {{
            top: 2px;
        }}

        QComboBox QAbstractItemView {{
            padding: 5px 10px 6px 10px;
            background: #FFFFFF;
            border: 1px solid #DADADA;
            border-radius: {self._borderRadius}px;
            font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';
            outline: 0px;
            selection-background-color: #F2F2F2;
            selection-color: #5e9cff;
        }}
        """
        self.setStyleSheet(style_sheet)

    @pyqtProperty(int)
    def borderRadius(self):
        """获取下拉框边框半径"""
        return self._borderRadius

    @borderRadius.setter
    def borderRadius(self, radius):
        """设置下拉框边框半径"""
        self._borderRadius = radius
        self._updateStyleSheet()