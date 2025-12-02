import queue

event_queue = queue.Queue()

def push(evt):
    event_queue.put(evt)

def pull():
    try:
        return event_queue.get_nowait()
    except:
        return None
