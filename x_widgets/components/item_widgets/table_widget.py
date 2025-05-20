from PyQt5.QtWidgets import QTableWidget, QHeaderView
from PyQt5.QtCore import pyqtProperty, Qt

class TableWidget(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # 设置列铺满整个widget
        self.horizontalHeader().setStretchLastSection(True)  # 最后一列拉伸填充
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列平均拉伸填充

        
        # 设置样式表
        style_sheet = """
        QTableView {
            background: transparent;
            outline: none;
            border: 1px solid rgba(0, 0, 0, 30);
            font: 13px 'Segoe UI', 'Microsoft YaHei';
            selection-background-color: transparent;
            alternate-background-color: #F4F4F4;
            gridline-color: rgba(0, 0, 0, 30);  /* 设置网格线颜色 */
        }

        QTableView[isBorderVisible=true] {
            border: 1px solid rgba(0, 0, 0, 30);
        }

        QTableView::item {
            background: transparent;
            border: none;
            color: black;
            padding-top: 0px;
            padding-bottom: 0px;
        }
        QTableView::item:selected {
            background-color: rgba(71, 174, 219, 80);
        }
        QTableView::item:hover {
            background-color: rgba(71, 174, 219, 40);
        }
        QTableView::item:selected:hover {
            background-color: rgba(71, 174, 219, 80);
        }
        QTableView::indicator {
            width: 18px;
            height: 18px;
            border-radius: 5px;
            border: none;
            background-color: transparent;
        }
        QHeaderView {
            background-color: transparent;
        }
        QHeaderView::section {
            background-color: transparent;
            color: rgb(96, 96, 96);
            padding-left: 5px;
            padding-right: 5px;
            border: 1px solid rgba(0, 0, 0, 30);
            font: 13px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';
        }
        QHeaderView::section:horizontal {
            border-left: none;
            height: 33px;
        }
        QTableView[isBorderVisible=true] QHeaderView::section:horizontal {
            border-top: none;
        }
        QHeaderView::section:horizontal:last {
            border-right: none;
        }
        QHeaderView::section:vertical {
            border-top: none;
        }
        QHeaderView::section:checked {
            background-color: transparent;
        }
        QHeaderView::down-arrow {
            subcontrol-origin: padding;
            subcontrol-position: center right;
            margin-right: 6px;
            image: url(:/widget/widget/down.png);
        }
        QHeaderView::up-arrow {
            subcontrol-origin: padding;
            subcontrol-position: center right;
            margin-right: 6px;
            image: url(:/widget/widget/up.png);
        }
        QTableCornerButton::section {
            background-color: transparent;
            border: 1px solid rgba(0, 0, 0, 30);
        }
        QTableCornerButton::section:pressed {
            background-color: rgba(0, 0, 0, 12);
        }
        
        /* 添加QLineEdit样式，用于表格单元格编辑 */
        QLineEdit {
            color: black;
            background-color: rgba(255, 255, 255, 0.7);
            border: 1px solid rgba(0, 0, 0, 13);
            border-bottom: 1px solid rgba(0, 0, 0, 100);
            border-radius: 0px;
            font: 14px "Segoe UI", "Microsoft YaHei";
            padding: 0px 10px;
            min-height: 30px;
            selection-background-color: #47aedb;
        }
        QLineEdit:hover {
            background-color: rgba(249, 249, 249, 0.5);
            border: 1px solid rgba(0, 0, 0, 13);
            border-bottom: 1px solid rgba(0, 0, 0, 100);
        }
        QLineEdit:focus {
            border-bottom: 2px solid #47aedb;
            background-color: white;
        }
        QLineEdit:disabled {
            color: rgba(0, 0, 0, 92);
            background-color: rgba(249, 249, 249, 0.3);
            border: 1px solid rgba(0, 0, 0, 13);
            border-bottom: 1px solid rgba(0, 0, 0, 13);
        }
        """
        self.setStyleSheet(style_sheet)
