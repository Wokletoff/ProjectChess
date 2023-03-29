import subprocess

class Pusher:
 def Push(self):
    files = ["Chat.py"]  # файлы, которые нужно запустить
    for file in files:
        subprocess.Popen(args=["start", "python", file], shell=True, stdout=subprocess.PIPE)


























