def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x[1])

    completion_time = []
    turnaround_time = []
    waiting_time = []

    current_time = 0

    for process in processes:
        process_id, arrival_time, burst_time = process

        if current_time < arrival_time:
            current_time = arrival_time

        completion_time.append(current_time + burst_time)
        turnaround_time.append(completion_time[-1] - arrival_time)
        waiting_time.append(turnaround_time[-1] - burst_time)

        current_time = completion_time[-1]

    print("Process ID | Arrival Time | Burst Time | Completion Time | Turnaround Time | Waiting Time")
    for i in range(len(processes)):
        print(f" {processes[i][0]} |  {processes[i][1]} | {processes[i][2]} | {completion_time[i]} | {turnaround_time[i]} | {waiting_time[i]}")

processes = [(0, 2, 5), (1, 0, 3), (2, 4, 4)]
fcfs_scheduling(processes)
