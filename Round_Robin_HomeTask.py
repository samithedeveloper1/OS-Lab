from collections import deque
num_processes = 4
processes = ["p1", "p2", "p3", "p4"]
arrival_times = [0, 1, 2, 4]
burst_times = [5, 4, 2, 1]
time_quantum = 2
n = num_processes
remaining_burst = burst_times[:]
completion_time = [0] * n
turnaround_time = [0] * n
waiting_time = [0] * n
response_time = [-1] * n
queue = deque()
current_time = 0
index = 0
while index < n or queue:
while index < n and arrival_times[index] <= current_time:
queue.append(index)
index += 1
if queue:
i = queue.popleft()

if response_time[i] == -1:
response_time[i] = current_time - arrival_times[i]
exec_time = min(time_quantum, remaining_burst[i])
remaining_burst[i] -= exec_time
current_time += exec_time
while index < n and arrival_times[index] <= current_time:
queue.append(index)
index += 1
if remaining_burst[i] > 0:
queue.append(i)
else:
completion_time[i] = current_time
turnaround_time[i] = completion_time[i] - arrival_times[i]
waiting_time[i] = turnaround_time[i] - burst_times[i]
else:
current_time = arrival_times[index]
print("Process\tArrivalTime\tBurstTime\tCompletionTime\tTurnaroundTime\tWaitingTim
e")
for i in range(n):
print(f"{processes[i]}\t\t{arrival_times[i]}\t\t{burst_times[i]}\t\t{completion_time[i]}\t\t{turnar
ound_time[i]}\t\t{waiting_time[i]}")
