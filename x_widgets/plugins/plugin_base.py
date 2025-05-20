# coding:utf-8
import re

from PyQt5.QtGui import QIcon
from PyQt5.QtDesigner import QDesignerFormEditorInterface


class PluginBase:

	Factory = None

	def __init__(self, parent=None):
		super().__init__(parent)
		self.initialized = False
		self.factory = None
		self.pattern = re.compile(r'(?<!^)(?=[A-Z])')

	def initialize(self, editor: QDesignerFormEditorInterface):
		if self.initialized:
			return

		self.initialized = True
		if not self.Factory:
			return

		manager = editor.extensionManager()
		self.factory = self.Factory(manager)
		manager.registerExtensions(self.factory, self.factory.IID)

	def isInitialized(self):
		return self.initialized

	# 设置边上的图片
	def icon(self, name: str):
		return QIcon(f":/icon/icon/{name}.png")

	# 设置控件的名称
	def name(self):
		return "PluginBase"

	# 设置控件的组
	def group(self):
		return "My Widgets"

	def toolTip(self):
		# 设置控件的提示
		return 'Sepflow Widgets'

	# 设置控件的详细信息
	def whatsThis(self):
		return 'Sepflow Widgets'

	# 设置控件是否为容器
	def isContainer(self):
		return False

	def domXml(self, property_name="text_", default_text=None):
		"""生成控件的XML描述
		
		参数:
			property_name: 属性名称, 默认为'text_'
			default_text: 默认文本, 如果为None则使用toolTip值
		"""
		text = default_text if default_text is not None else self.toolTip()
		return f"""
        <widget class="{self.name()}" name="{self.name()}">
            <property name="{property_name}">
                <string>{text}</string>
            </property>
        </widget>
        """

	def includeFile(self):
		return "my_widgets"
