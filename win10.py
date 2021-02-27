# Program: Random Selection for TryHackMe
# Author: R.
# Original creation date: 2021-02-26
# Version: 1
# Updated:
# for Windows based OS
# pip install win10toast

#!/usr/bin/env python3
import random
import time
import subprocess as s
from win10toast import ToastNotifier

def countdown(mins, secs=0):
    t = (mins*60) + secs
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

print("TryHackMe?"),
print("The topics are:\n"),
study_topics = ["TryHackMe[1]"]

for topic in study_topics:
    print(topic)
    print()
question = input("Select topic: ")

if question == "1":
    tryhackme = []
    with open("thm.txt", "r") as f:
        tryhackme = f.readlines()
        print("How about?:", random.choice(tryhackme)),

else:
    print("Topic entered not in the list!")
    print("Goodbye")
    exit()

input("Press Enter to Start timer")
countdown(30),

toaster = ToastNotifier()
toaster.show_toast("Finished!", "Well done, have a Great Day!",
threaded=True,
icon_path=None, duration=4)  # 4 seconds
