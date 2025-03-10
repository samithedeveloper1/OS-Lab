processes = [
("P1", 6, 2),
("P2", 2, 5),
("P3", 8, 1),
("P4", 3, 0),
("P5", 4, 4)
]
processes.sort(key=lambda x: x[2])
time = 0
completed = []
remaining_processes = processes.copy()
while remaining_processes:
available = [p for p in remaining_processes if p[2] <= time]
if available:
shortest = min(available, key=lambda x: x[1])
remaining_processes.remove(shortest)

time += shortest[1]
completion_time = time
turnaround_time = completion_time - shortest[2]
waiting_time = turnaround_time - shortest[1]

completed.append((shortest[0], shortest[1], shortest[2],

completion_time, turnaround_time, waiting_time))
else:
time += 1

print("Process | Burst Time | Arrival Time | Completion Time | Turnaround
Time | Waiting Time")
for p in completed:
print(f"{p[0]} | {p[1]} ms | {p[2]} ms | {p[3]} ms | {p[4]}ms | {p[5]}
ms")
