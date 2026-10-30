# Day 38 - Python Multithreading

import threading
import time

# First task
def task_one():
    for i in range(1, 4):
        print("Task One:", i)
        time.sleep(1)

# Second task
def task_two():
    for i in range(1, 4):
        print("Task Two:", i)
        time.sleep(1)

# Create threads
thread1 = threading.Thread(target=task_one)
thread2 = threading.Thread(target=task_two)

# Start threads
print("Starting Threads...")

thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both Tasks Completed.")