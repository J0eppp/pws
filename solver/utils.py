from datetime import datetime


def uprint(msg: str, end: str = None):
    time = datetime.now().strftime("%H:%M:%S")
    print(f"[{time}] {msg}", end=end)
