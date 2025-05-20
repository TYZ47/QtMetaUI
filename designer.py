# coding: utf-8
import os
import sys
import shutil
import warnings
from pathlib import Path
import PyQt5
from PyQt5.QtCore import QProcessEnvironment, QProcess

# 检查是否存在pyqt5.dll，如果存在则返回designer.exe路径
def get_designer_path():
    env_path = sys.prefix
    
    designer_path = env_path + r"/Lib/site-packages/qt5_applications/Qt/bin/designer.exe"

    if not os.path.exists(designer_path):
        raise Exception("无法找到可用的Qt Designer。请尝试安装PyQt5-tools: `pip install pyqt5-tools`")

    
    dll_path = env_path + r"/Lib/site-packages/qt5_applications/Qt/plugins/designer/pyqt5.dll"
    plugin_dll_path = env_path + r"/Lib/site-packages/pyqt5_plugins/Qt/plugins/designer/pyqt5.dll"
    if not os.path.exists(dll_path):
        if os.path.exists(plugin_dll_path):
            shutil.copy(plugin_dll_path, dll_path)
            return designer_path
        else:
            raise Exception("无法找到可用的pyqt5.dll。自定义控件不可以见")
    else:
        return designer_path


# 项目路径
project_dir = Path(__file__).absolute().parent



# 设置环境变量
env = QProcessEnvironment.systemEnvironment()
PATH = f"{os.path.dirname(PyQt5.__file__)};{sys.prefix};{env.value('PATH', '')}"


env.insert('PATH', PATH)
env.insert('PYQTDESIGNERPATH', str(project_dir / 'x_widgets/plugins'))
env.insert('PYTHONPATH', str(project_dir))


# 启动Qt Designer
designer = QProcess()
designer.setProcessEnvironment(env)

# 打开UI文件(如果有传入)
ui_files = [i for i in sys.argv[1:] if i.lower().endswith(".ui")]



designer.start(get_designer_path(), ui_files)

designer.waitForFinished(-1)
sys.exit(designer.exitCode())
