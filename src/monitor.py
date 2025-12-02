import time
import re
from rich import print
from src.event_queue import push
from src.correlator import Correlator

def tail(fname):
    with open(fname) as f:
        f.seek(0,2)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line


def parse(line):
    if "PTRACE" in line: return "ptrace"
    if "CLONE" in line: return "clone"
    if "WRITE-EXEC" in line: return "wx"
    return None


def main():
    corr = Correlator()

    for line in tail("/var/log/messages"):
        evt = parse(line)
        if not evt: continue

        proc = re.search(r"comm=([^ ]+)", line)
        proc = proc.group(1) if proc else "unknown"

        corr.add(proc, evt)
        corr.report()


if __name__ == "__main__":
    main()
