from PyQt5.QtWidgets import QTabWidget, QWidget
from PyQt5.QtCore import pyqtProperty, QRegExp
from PyQt5.QtGui import QColor, QRegExpValidator

class TabWidget(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 不在这里添加默认页面，而是通过domXml方法定义
        self._updateStyleSheet()
        
    def _updateStyleSheet(self):
        style_sheet = """
        QTabWidget {
        }
        QTabWidget::pane {
        border: 1px solid rgba(0, 0, 0, 13);
        border-radius: 0px;
        }
        QTabWidget::tab-bar {
        left: 0px;
        }
        QTabBar::tab {
        font: 12px 'Segoe UI', 'Microsoft YaHei';
        background-color: rgba(0, 0, 0, 0);
        padding: 0px 20px;
        margin-right: 0px;
        border: 1px solid rgba(0, 0, 0, 13);
        min-height:20px;
        /*  min-width 看具体的文本  */
        min-width: 100px;
        }
        QTabBar::tab:hover {
        background-color: rgba(0, 0, 0, 13);
        border-radius: 0px;
        }
        QTabBar::tab:selected {
        color:white;
        border-radius: 0px;
        background-color: #47aedb;
        border: 1px solid #4bb7e6;
        }
        QTabBar::tab:disabled {
        color: rgba(0, 0, 0, 150)
        }
        QTabBar::tab:selected:disabled {
        color: rgba(255, 255, 255, 0.9);
        background-color: rgba(205, 205, 205);
        border: 1px solid rgba(205, 205, 205);
        }
        """
        self.setStyleSheet(style_sheet)

