import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QVBoxLayout
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtGui import QColor


def adjust_color(color: QColor, flag: int) -> QColor:
    h, s, v, _ = color.getHsvF()

    # 悬浮状态
    if flag == 2:
        v *= 1.05
    # 边框状态
    elif flag == 3:
        s *= 0.75
        v *= 1.05
    # 按压状态
    elif flag == 4:
        s *= 0.65
        v *= 1.05

    return QColor.fromHsvF(h, min(s, 1), min(v, 1))


class PrimaryButton(QPushButton):
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
        self._themeColor = QColor(71, 174, 219)  # 默认主题色
        self._updateStyleSheet()

    def _updateStyleSheet(self):
        # 基于主题色计算其他颜色变体
        theme_color_primary = self._themeColor
        theme_color_light1 = adjust_color(theme_color_primary, 2)  # 悬浮状态颜色
        theme_color_light2 = adjust_color(theme_color_primary, 3)  # 边框颜色
        theme_color_light3 = adjust_color(theme_color_primary, 4)  # 按压状态颜色
        theme_color_dark1 = QColor(theme_color_primary.red() * 0.9, 
                                   theme_color_primary.green() * 0.9,
                                   theme_color_primary.blue() * 0.9)

        style_sheet = f"""
        QPushButton {{
            color: white;
            background-color: rgba({theme_color_primary.red()}, {theme_color_primary.green()}, {theme_color_primary.blue()}, 255);
            border: 1px solid rgba({theme_color_light1.red()}, {theme_color_light1.green()}, {theme_color_light1.blue()}, 255);
            border-bottom: 1px solid rgba({theme_color_dark1.red()}, {theme_color_dark1.green()}, {theme_color_dark1.blue()}, 255);
            border-radius: {self._borderRadius}px;
            font: 14px 'Segoe UI', 'Microsoft YaHei';
            padding: 5px 10px 6px 10px;
            outline: none;
            min-height: 19px;
        }}
        
        QPushButton:hover {{
            background-color: rgba({theme_color_light1.red()}, {theme_color_light1.green()}, {theme_color_light1.blue()}, 255);
            border: 1px solid rgba({theme_color_light2.red()}, {theme_color_light2.green()}, {theme_color_light2.blue()}, 255);
            border-bottom: 1px solid rgba({theme_color_dark1.red()}, {theme_color_dark1.green()}, {theme_color_dark1.blue()}, 255);
        }}
        
        QPushButton:pressed {{
            color: rgba(255, 255, 255, 0.63);
            background-color: rgba({theme_color_light3.red()}, {theme_color_light3.green()}, {theme_color_light3.blue()}, 255);
            border: 1px solid rgba({theme_color_light3.red()}, {theme_color_light3.green()}, {theme_color_light3.blue()}, 255);
        }}
        
        QPushButton:disabled {{
            color: rgba(255, 255, 255, 0.9);
            background-color: rgb(205, 205, 205);
            border: 1px solid rgb(205, 205, 205);
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
        
    @pyqtProperty(QColor)
    def themeColor(self):
        """获取主题颜色"""
        return self._themeColor
        
    @themeColor.setter
    def themeColor(self, color):
        """设置主题颜色"""
        self._themeColor = color
        self._updateStyleSheet()



