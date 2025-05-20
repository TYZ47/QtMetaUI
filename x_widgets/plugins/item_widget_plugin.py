# coding: utf-8
from PyQt5.QtDesigner import QPyDesignerCustomWidgetPlugin
from x_widgets.components import TableWidget
from plugin_base import PluginBase


class TableWidgetPlugin(PluginBase, QPyDesignerCustomWidgetPlugin):

    """自定义表格控件插件"""

    def createWidget(self, parent):
        return TableWidget(parent)

    def name(self):
        return "TableWidget"

    def group(self):
        return "sepflow item widgets"

    def icon(self):
        return super().icon('Table')

    def domXml(self):
        # 使用自定义的XML定义，添加showGrid属性
        return f"""
        <widget class="{self.name()}" name="{self.name()}">
            <property name="objectName">
                <string>TableWidget</string>
            </property>
            <property name="showGrid">
                <bool>false</bool>
            </property>
        </widget>
        """

    def includeFile(self):
        return "x_widgets.components"

