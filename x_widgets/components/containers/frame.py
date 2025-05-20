

from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import pyqtProperty, QRegExp
from PyQt5.QtGui import QColor, QRegExpValidator

class Frame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._borderWidth = 2  # 默认边框宽度为2px
        self._borderColor = "#CCCCCC"  # 默认边框颜色为浅灰色
        self._updateStyleSheet()
        
    def _updateStyleSheet(self):
        # 使用固定的 CSS 选择器 "Widget"，而不是使用 objectName
        style_sheet = f"""
        Frame {{
            background-color: #FFFFFF;
            border: {self._borderWidth}px solid {self._borderColor};
        }}
        """
        self.setStyleSheet(style_sheet)
    

    # 边框宽度属性
    @pyqtProperty(int)
    def borderWidth(self):
        """获取边框宽度"""
        return self._borderWidth
    
    @borderWidth.setter
    def borderWidth(self, width):
        """设置边框宽度"""
        try:
            width_val = int(width)
            if width_val >= 0:  # 确保宽度非负
                self._borderWidth = width_val
        except (ValueError, TypeError):
            # 如果不符合格式，保持默认值
            pass
        self._updateStyleSheet()
    
    # 边框颜色属性
    @pyqtProperty(str)
    def borderColor(self):
        """获取边框颜色"""
        return self._borderColor
    
    @borderColor.setter
    def borderColor(self, color):
        """设置边框颜色，如果符合格式则自动添加#前缀"""
        # 检查颜色格式是否有效
        if color.startswith('#'):
            self._borderColor = color
        else:
            # 检查是否是有效的6位十六进制颜色代码
            color_regex = QRegExp("^[0-9A-Fa-f]{6}$")
            if QRegExpValidator(color_regex, self).validate(color, 0)[0] == QRegExpValidator.Acceptable:
                self._borderColor = f"#{color.upper()}"
            # 如果不符合格式，保持默认值
        self._updateStyleSheet()
    
