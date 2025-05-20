

import sys
import subprocess

# 指定 Python 解释器路径
python_exe = r"D:\Anaconda3\envs\sepflow\python.exe"

# 指定 designer.py 路径
designer_script = r"D:\gitea\sepflow_project\designer.py"

args = []
for arg in sys.argv[1:]:

    if arg.lower().endswith('.ui'):
        args.append(arg)


cmd = [python_exe, designer_script] + args


subprocess.Popen(cmd)


# 打包成.exe,即可像正常的desiger一样