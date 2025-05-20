# coding: utf-8
from PyQt5.QtDesigner import QPyDesignerCustomWidgetPlugin
from x_widgets.components import Button,RadioButton,PrimaryButton,LinkButton,CheckBox
from plugin_base import PluginBase


class ButtonPlugin(PluginBase, QPyDesignerCustomWidgetPlugin):

    """自定义按钮插件"""

    def createWidget(self, parent):
        return Button("Button", parent)

    def name(self):
        return "Button"

    def group(self):
        return "sepflow buttons"

    def icon(self):

        return super().icon('Button')


    def domXml(self):
        return super().domXml(
            property_name="text",
            default_text="Button"
        )

    def includeFile(self):
        return "x_widgets.components"

class LinkButtonPlugin(PluginBase, QPyDesignerCustomWidgetPlugin):
    def createWidget(self, parent):
        return LinkButton("Link Button", parent)

    def name(self):
        return "LinkButton"
    
    def group(self):
        return "sepflow buttons"

    def icon(self):
        return super().icon('LinkButton')
    
    def domXml(self):
        return super().domXml(
            property_name="text",
            default_text="Link Button"
        )
    
    def includeFile(self):
        return "x_widgets.components"


class RadioButtonPlugin(PluginBase, QPyDesignerCustomWidgetPlugin):

    """自定义单选按钮插件"""

    def createWidget(self, parent):
        return RadioButton("Radio Button", parent)

    def name(self):
        return "RadioButton"

    def group(self):
        return "sepflow buttons"

    def icon(self):

        return super().icon('RadioButton')

    def domXml(self):
        return super().domXml(
            property_name="text",
            default_text="Radio Button"
        )

    def includeFile(self):
        return "x_widgets.components"

class PrimaryButtonPlugin(PluginBase, QPyDesignerCustomWidgetPlugin):
    def createWidget(self, parent):
        return PrimaryButton("Primary Button", parent)

    def name(self):
        return "PrimaryButton"

    def group(self):
        return "sepflow buttons"

    def icon(self):
        return super().icon('Button')

    def domXml(self):
        return super().domXml(
            property_name="text",
            default_text="Primary Button"
        )

    def includeFile(self):
        return "x_widgets.components"

# class CheckBoxPlugin(PluginBase, QPyDesignerCustomWidgetPlugin):
#     """自定义复选框插件"""
#
#     def createWidget(self, parent):
#         return CheckBox("Check Box", parent)
#
#     def name(self):
#         return "CheckBox"
#
#     def group(self):
#         return "sepflow buttons"
#
#     def icon(self):
#         return super().icon('CheckBox')
#
#     def domXml(self):
#         return super().domXml(
#             property_name="text",
#             default_text="Check Box"
#         )
#
#     def includeFile(self):
#         return "x_widgets.components"