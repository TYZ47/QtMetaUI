from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit
from PyQt5.QtCore import Qt
import sys


class DockWidget(QDockWidget):
    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        self.init_ui()
        self.set_stylesheet()

    def init_ui(self):
        # 创建内容部件
        self.content = QTextEdit()
        self.setWidget(self.content)
        
        # 设置允许停靠的区域
        self.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)

    def set_stylesheet(self):
        pass
        # self.setStyleSheet("""
        #     /* 整个 QDockWidget 的样式 */
        #     QDockWidget {
        #         background-color: #f0f0f0; /* 背景颜色 */
        #         border: 1px solid #d0d0d0; /* 边框样式，1像素宽的灰色边框 */
        #         border-radius: 5px; /* 边框圆角 */
        #     }

        #     /* QDockWidget 标题栏的样式 */
        #     QDockWidget::title {
        #         background-color: #e0e0e0; /* 标题栏背景颜色 */
        #         color: #333333; /* 标题栏文字颜色 */
        #         font-size: 14px; /* 标题栏文字大小 */
        #         font-weight: bold; /* 标题栏文字加粗 */
        #         padding: 5px; /* 标题栏内边距 */
        #         text-align: center; /* 标题栏文字居中对齐 */
        #     }

        #     /* QDockWidget 关闭按钮的样式 */
        #     QDockWidget::close-button {
        #         image: url(:/widget/widget/dock_close.png); /* 关闭按钮的图标，需确保 close.png 文件存在 */
        #         padding: 2px; /* 关闭按钮内边距 */
        #     }

        #     /* QDockWidget 关闭按钮悬停时的样式 */
        #     QDockWidget::close-button:hover {
        #         background-color: #ff0000; /* 悬停时背景颜色变红 */
        #     }

        #     /* QDockWidget 浮动按钮的样式 */
        #     QDockWidget::float-button {
        #         image: url(float.png); /* 浮动按钮的图标，需确保 float.png 文件存在 */
        #         padding: 2px; /* 浮动按钮内边距 */
        #     }

        #     /* QDockWidget 浮动按钮悬停时的样式 */
        #     QDockWidget::float-button:hover {
        #         background-color: #00ff00; /* 悬停时背景颜色变绿 */
        #     }

        #     /* QDockWidget 内部内容区域的样式 */
        #     QDockWidget QWidget {
        #         background-color: #ffffff; /* 内部内容区域背景颜色 */
        #         color: #333333; /* 内部内容区域文字颜色 */
        #         font-size: 12px; /* 内部内容区域文字大小 */
        #     }
        # """)


# 测试代码
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # 创建主窗口
    main_window = QMainWindow()
    main_window.setWindowTitle("Dock Widget 示例")
    main_window.setGeometry(100, 100, 800, 600)
    
    # 创建自定义的 DockWidget
    dock_widget = DockWidget("可停靠面板", main_window)
    
    # 将 dock widget 添加到主窗口
    main_window.addDockWidget(Qt.LeftDockWidgetArea, dock_widget)
    
    main_window.show()
    sys.exit(app.exec_())

