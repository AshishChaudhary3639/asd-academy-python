# import time
# print("Welcome")
# time.sleep(5)
# print("Showing time Module")

import schedule
import time

def task():
    print("Task is running!")

schedule.every(2).minutes.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)
