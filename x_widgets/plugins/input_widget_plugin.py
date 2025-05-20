# coding: utf-8
from PyQt5.QtDesigner import QPyDesignerCustomWidgetPlugin
from x_widgets.components import ComboBox, LineEdit, TextEdit, BorderLineEdit, BorderTextEdit, SpinBox, DoubleSpinBox
from plugin_base import PluginBase


class ComboBoxPlugin(PluginBase, QPyDesignerCustomWidgetPlugin):

    """自定义下拉框插件"""

    def createWidget(self, parent):
        return ComboBox(parent)

    def name(self):
        return "ComboBox"

    def group(self):
        return "sepflow input widgets"

    def icon(self):
        return super().icon('ComboBox')

    def domXml(self):
        return super().domXml(
            property_name="currentText",
            default_text=""
        )

    def includeFile(self):
        return "x_widgets.components"


class LineEditPlugin(PluginBase, QPyDesignerCustomWidgetPlugin):

    """自定义输入框插件"""

    def createWidget(self, parent):
        return LineEdit(parent)

    def name(self):
        return "LineEdit"

    def group(self):
        return "sepflow input widgets"

    def icon(self):
        return super().icon('LineEdit')

    def domXml(self):
        return super().domXml(
            property_name="text",
            default_text=""
        )

    def includeFile(self):
        return "x_widgets.components"


class TextEditPlugin(PluginBase, QPyDesignerCustomWidgetPlugin):

    """自定义多行文本框插件"""

    def createWidget(self, parent):
        return TextEdit(parent)

    def name(self):
        return "TextEdit"

    def group(self):
        return "sepflow input widgets"

    def icon(self):
        return super().icon('LineEdit')

    def domXml(self):
        return super().domXml(
            property_name="plainText",
            default_text=""
        )

    def includeFile(self):
        return "x_widgets.components"


class BorderLineEditPlugin(PluginBase, QPyDesignerCustomWidgetPlugin):

    """自定义边框输入框插件"""

    def createWidget(self, parent):
        return BorderLineEdit(parent)

    def name(self):
        return "BorderLineEdit"

    def group(self):
        return "sepflow input widgets"

    def icon(self):
        return super().icon('LineEdit')

    def domXml(self):
        return super().domXml(
            property_name="text",
            default_text=""
        )

    def includeFile(self):
        return "x_widgets.components"


class BorderTextEditPlugin(PluginBase, QPyDesignerCustomWidgetPlugin):

    """自定义边框多行文本框插件"""

    def createWidget(self, parent):
        return BorderTextEdit(parent)

    def name(self):
        return "BorderTextEdit"

    def group(self):
        return "sepflow input widgets"

    def icon(self):
        return super().icon('LineEdit')

    def domXml(self):
        return super().domXml(
            property_name="plainText",
            default_text=""
        )

    def includeFile(self):
        return "x_widgets.components"


class SpinBoxPlugin(PluginBase, QPyDesignerCustomWidgetPlugin):

    """自定义数字输入框插件"""

    def createWidget(self, parent):
        return SpinBox(parent)

    def name(self):
        return "SpinBox"

    def group(self):
        return "sepflow input widgets"

    def icon(self):
        return super().icon('NumberBox')

    def domXml(self):
        return super().domXml(
            property_name="value",
            default_text="0"
        )

    def includeFile(self):
        return "x_widgets.components"


class DoubleSpinBoxPlugin(PluginBase, QPyDesignerCustomWidgetPlugin):

    def createWidget(self, parent):
        return DoubleSpinBox(parent)

    def name(self):
        return "DoubleSpinBox"

    def group(self):
        return "sepflow input widgets"

    def icon(self):
        return super().icon('NumberBox')

    def domXml(self):
        return super().domXml(
            property_name="value",
            default_text="0.0"
        )
    
    def includeFile(self):
        return "x_widgets.components"


