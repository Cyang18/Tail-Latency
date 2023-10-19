#Version 0.1: This is prototype that simulates the shortest job first.
def shortest_job_first(packages):
    current_time = 0
    schedule = []

    # Sort the jobs by burst time (the time required to complete each job)
    # Assuming (job_id, burst_time)
    packages.sort(key=lambda x: x[1])

    #iterate through the array
    for job_id, burst_time in packages:

        # re-schedule the schedule after being sorted
        schedule.append((job_id, current_time))

        # Update the current time and subtract the job's burst time
        # Gets the time frame of when each package is gonna be sent
        current_time += burst_time

    return schedule


 # List of jobs, each represented as (job_id, burst_time)
packages = [(1, 6), (4, 3), (5, 2)]
schedule = shortest_job_first(packages)

print("Schedule of each Job being processed (Job ID, Start Time):")
for job_id, start_time in schedule:
    print(f"Job_ID {job_id}: Wait time {start_time}")

