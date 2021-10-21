import platform
import subprocess
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent


def run(script_name):
    script_ext = OS_SPECIFIC[platform.system()]
    full_script_name = str(BASE_DIR / (script_name + script_ext))
    subprocess.run([full_script_name])


prompt = \
    """ 
Please enter a selection:
    1: Build Docker Image
    2: Run Docker Container
    0: Quit
"""

OS_SPECIFIC = {
    'Linux': '.sh',
    'Windows': '.bat',
}

CMD_SCRIPTS = {
    '1': lambda: run('build'),
    '2': lambda: run('launch'),
    '0': exit,
}

if __name__ == '__main__':
    os.chdir(BASE_DIR.parent)

    while True:
        try:
            cmd = input(prompt)

            CMD_SCRIPTS[cmd]()

        except KeyboardInterrupt:
            break

    print('Exiting!')
