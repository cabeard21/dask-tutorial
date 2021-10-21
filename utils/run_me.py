import platform
import subprocess
from pathlib import Path

prompt = \
    """ 
Please enter a selection:
    1: Build Docker Image
    2: Run Docker Container
"""

OS_SPECIFIC = {
    'Linux': '.sh',
    'Windows': '.bat',
}

CMD_SCRIPTS = {
    '1': 'build',
    '2': 'launch',
}

if __name__ == '__main__':
    p = Path(__file__).resolve().parent

    while True:
        try:
            cmd = input(prompt)

            script_ext = OS_SPECIFIC[platform.system()]
            full_script_name = str(p / (CMD_SCRIPTS[cmd] + script_ext))
            subprocess.run([full_script_name])

        except KeyboardInterrupt:
            break

    print('Exiting!')
