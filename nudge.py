import random
from datetime import datetime

tasks = [
    "Practice voice pitch for 2-3 min (e.g., hum or pitch slides)",
    "Practice voice resonance for 2-3 min (e.g., say 'eee' with face vibration)",
    "Practice voice articulation for 2-3 min (e.g., read a sentence softly)",
    "Study 5 driving theory signs or rules for 5 min",
    "Study hazard perception for 5 min (e.g., watch a video)",
    "Do a 5-min cleaning task (e.g., wipe kitchen counter, sweep a room)",
    "Do a 5-min organizing task (e.g., sort laundry, tidy desk)",
    "Do a 5-min maintenance task (e.g., take out trash, water plants)"
]

task = random.choice(tasks)
print(f"Next task: {task}")
with open("tasks.md", "a") as f:
    f.write(f"- [ ] {task} # {random.randint(1000, 9999)} @ {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")