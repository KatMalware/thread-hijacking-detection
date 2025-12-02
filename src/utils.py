from datetime import datetime

def ts():
    return datetime.now().strftime("%H:%M:%S")


def score_event(evt):
    if evt == "ptrace":
        return 3
    if evt == "clone":
        return 2
    if evt == "wx":
        return 5
    return 0
