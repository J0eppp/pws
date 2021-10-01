from datetime import datetime

def uprint(msg: str):
    time = datetime.now().strftime("%H:%M:%S")
    print(f"[{time}] {msg}")