# coding: utf-8
from PyQt5.QtDesigner import QPyDesignerCustomWidgetPlugin
from x_widgets.components import Frame, TabWidget
from plugin_base import PluginBase


class FramePlugin(PluginBase, QPyDesignerCustomWidgetPlugin):

    def createWidget(self, parent):
        widget = Frame(parent)
        widget.setObjectName("Frame")
        return widget

    def name(self):
        return "Frame"

    def group(self):
        return "sepflow containers"

    def icon(self):
        return super().icon('Border')

    def domXml(self):
        return f"""
        <widget class="{self.name()}" name="{self.name()}">
            <property name="geometry">
                <rect>
                    <x>0</x>
                    <y>0</y>
                    <width>50</width>
                    <height>50</height>
                </rect>
            </property>
        </widget>
        """

    def includeFile(self):
        return "x_widgets.components"

    def isContainer(self):
        return True

class TabWidgetPlugin(PluginBase, QPyDesignerCustomWidgetPlugin):
    def createWidget(self, parent):
        widget = TabWidget(parent)
        widget.setObjectName("TabWidget")
        return widget
    def name(self):
        return "TabWidget"
    def group(self):
        return "sepflow containers"

    def icon(self):
        return super().icon('Tab')

    def domXml(self):
        return f"""
        <widget class="{self.name()}" name="{self.name()}">
            <property name="geometry">
                <rect>
                    <x>0</x>
                    <y>0</y>
                    <width>200</width>
                    <height>200</height>
                </rect>
            </property>
            <widget class="QWidget" name="tab1">
                <attribute name="title">
                    <string>Page 1</string>
                </attribute>
            </widget>
            <widget class="QWidget" name="tab2">
                <attribute name="title">
                    <string>Page 2</string>
                </attribute>
            </widget>
        </widget>
        """

    def includeFile(self):
        return "x_widgets.components"

    def isContainer(self):
        return True