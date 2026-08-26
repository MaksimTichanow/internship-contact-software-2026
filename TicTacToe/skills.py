import sys
import os
import random
import string
import json
import shutil
import zipfile
from pathlib import Path
from typing import Any
import platform
import subprocess
import time


class MyNumberUtils:
    @staticmethod
    def is_even(num):
        if num % 2 == 0:
            return True
        else:
            return False


    @staticmethod
    def is_odd(num):
        if num % 2 != 0:
            return True
        else:
            return False


    @staticmethod
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


    @staticmethod
    def random_string(length):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(length))


    @staticmethod
    def random_number(min_value, max_value):
        return random.randint(min_value, max_value)

    @staticmethod
    def setListValue(your_list, index, value):
        if 0 <= index < len(your_list):
            your_list[index] = value
        else:
            raise IndexError("Index out of range")



class MyFileUtils:
    @staticmethod
    def exists(path) -> bool:
        return os.path.exists(path)

    @staticmethod
    def is_file(path) -> bool:
        return Path(path).is_file()

    @staticmethod
    def is_dir(path) -> bool:
        return Path(path).is_dir()

    @staticmethod
    def read_text(path, encoding) -> str:
        with open(path, 'r', encoding=encoding) as file:
            return file.read()

    @staticmethod
    def write_text(path, text, encoding) -> None:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding=encoding)

    @staticmethod
    def delete(path) -> None:
        path = Path(path)
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            shutil.rmtree(path)

    @staticmethod
    def get_file_size(path) -> int:
        return Path(path).stat().st_size


class MySystemUtils:

    @staticmethod
    def exit() -> None:
        sys.exit()

    @staticmethod
    def os() -> str:
        return platform.system()

    @staticmethod
    def os_version() -> str:
        return platform.version()

    @staticmethod
    def architecture() -> str:
        return platform.machine()

    @staticmethod
    def hostname() -> str:
        return platform.node()

    @staticmethod
    def username() -> str:
        return os.getlogin()

    @staticmethod
    def current_directory() -> str:
        return os.getcwd()

    @staticmethod
    def run_command(command: str) -> Any:
        try:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode('utf-8').strip()
        except subprocess.CalledProcessError as e:
            return e.stderr.decode('utf-8').strip()

    @staticmethod
    def open_file(path: str) -> None:
        if MySystemUtils.os() == "Windows":
            os.startfile(path)
        elif MySystemUtils.os() == "Darwin":  # macOS
            subprocess.run(["open", path])
        else:  # Linux and other OSes
            subprocess.run(["xdg-open", path])



class MyEventUtils:
    def __init__(self):
        self._events = {}

        def on(self, event, callback):
            self._events.setdefault(event, []).append(callback) 
            return callback

        def once(self, event, callback):
            def wrapper(*args, **kwargs):
                self.off(event, wrapper)
                return callback(*args, **kwargs)
            self.on(event, wrapper)

        def off(self, event, callback):
            if event in self._events:
                if callback in self._events[event]:
                    self._events[event].remove(callback)

        def emit(self, event, *args, **kwargs):
            for callback in self._events.get(event, []):
                callback(*args, **kwargs)

        def clear(self, event):
            if event is None:
                self._events.clear()
            else:
                self._events.pop(event, None)

        def listeners(self, event):
            return self._events.get(event, []).copy()
        

class MyTimerUtils:
    def __init__(self):
        self._start = None
        self._end = None

    def start(self):
        self._start = time.perf_counter()
        self._end = None
        return self 

    def stop(self):
        if self._start is None:
            raise RuntimeError("Timer has not been started.")
        self._end = time.perf_counter()
        return self.elapsed() 

    @property
    def elapsed(self):
        if self._start is None: 
            return 0.0

        end = self._end or time.perf_counter()
        return end - self._start

    def reset(self):
        self._start = None
        self._end = None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.stop()


class MyTerminalUtils:

    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def title(text):
        if os.name == 'nt':
            os.system(f'title {text}')

    @staticmethod
    def banner(text):
        line = "="* (len(text) + 8)
        print(line)
        print(f"    {text}")
        print(line)

    @staticmethod
    def success(text):
        print(f"[+] {text}")

    @staticmethod
    def info(text):
        print(f"[i] {text}")

    @staticmethod
    def warning(text):
        print(f"[!] {text}")

    @staticmethod
    def error(text):
        print(f"[-] {text}")

    @staticmethod
    def ask(text):
        return input(f"[?] {text}: ")

    @staticmethod
    def confirm(text) -> bool:
        answer = input(f"{text} (y/n): ").lower()
        return answer in ['y', 'yes']

    @staticmethod
    def progress(current, total, bar_length=40):
        if total <= 0:
            return
        percentage = current / total
        filled = int(bar_length * percentage)

        bar = ("█" * filled + "-" * (bar_length - filled))

        sys.stdout.write(
            f"\r[{bar}]"
            f"{percentage * 100:6.2f}% "
                         )
        sys.stdout.flush()

        if current >= total:
            print()


    @staticmethod
    def print_table(data, headers=None):
        if not data:
            print("No data to display.")
            return

        if headers is None:
            headers = [f"Column {i+1}" for i in range(len(data[0]))]

        col_widths = [max(len(str(item)) for item in col) for col in zip(*data, headers)]
        total_width = sum(col_widths) + len(col_widths) * 3 + 1

        print("-" * total_width)
        print("| " + " | ".join(f"{header:<{col_widths[i]}}" for i, header in enumerate(headers)) + " |")
        print("-" * total_width)

        for row in data:
            print("| " + " | ".join(f"{str(item):<{col_widths[i]}}" for i, item in enumerate(row)) + " |")

        print("-" * total_width)
