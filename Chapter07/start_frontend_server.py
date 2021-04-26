import subprocess
import shlex
import os
import pathlib

cmd = "python ./start_frontend_server.py"
cmd_list = shlex.split(cmd)
print(cmd_list)
env = os.environ.copy()
env["README"] = "../README_frontend.md"

subprocess.run(cmd_list, shell=False, env=env, cwd=pathlib.Path(__file__).parent / "rasa_web_client")
