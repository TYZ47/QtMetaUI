# coding: utf-8
from PyQt5.QtDesigner import QPyDesignerCustomWidgetPlugin
from x_widgets.components import Label, HorizontalLine, VerticalLine
from plugin_base import PluginBase


class LabelPlugin(PluginBase, QPyDesignerCustomWidgetPlugin):

    """自定义标签插件"""

    def createWidget(self, parent):
        return Label("Label", parent)

    def name(self):
        return "Label"

    def group(self):
        return "sepflow display widgets"

    def icon(self):
        return super().icon('Label')

    def domXml(self):
        return super().domXml(
            property_name="text",
            default_text="Label"
        )

    def includeFile(self):
        return "x_widgets.components"


class HorizontalLinePlugin(PluginBase, QPyDesignerCustomWidgetPlugin):

    """水平线插件"""

    def createWidget(self, parent):
        return HorizontalLine(parent)

    def name(self):
        return "HorizontalLine"

    def group(self):
        return "sepflow display widgets"

    def icon(self):
        return super().icon('Line')

    def domXml(self):
        return super().domXml(
            property_name="",
            default_text=""
        )

    def includeFile(self):
        return "x_widgets.components"


class VerticalLinePlugin(PluginBase, QPyDesignerCustomWidgetPlugin):

    """垂直线插件"""

    def createWidget(self, parent):
        return VerticalLine(parent)

    def name(self):
        return "VerticalLine"

    def group(self):
        return "sepflow display widgets"

    def icon(self):
        return super().icon('VerticalLine')

    def domXml(self):
        return super().domXml(
            property_name="",
            default_text=""
        )

    def includeFile(self):
        return "x_widgets.components"
