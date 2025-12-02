from collections import defaultdict
from src.utils import score_event

class Correlator:
    def __init__(self):
        self.scores = defaultdict(int)

    def add(self, proc, evt):
        self.scores[proc] += score_event(evt)

    def report(self):
        print("\n=== Threat Scores ===")
        for proc, score in self.scores.items():
            if score > 5:
                print(f"[!] {proc}: {score} (suspicious)")
            else:
                print(f"[*] {proc}: {score}")
