import pyautogui
import time
import sys
import datetime

"""
pyautogui perfoms *much* faster with opencv-python installed
opencv-python also seems to be a requirement for the pyautogui grayscale and
confidence arguments to work properly
"""

begin_time = datetime.datetime.now()

# Ensure OpenCV is installed
try:
    import cv2
except ModuleNotFoundError as err:
    print("OpenCV not installed? pyautogui performs much better with OpenCV. Exiting.")
    print(err)
    sys.exit(1)

pyautogui.FAILSAFE = True

positive_clicks = 0
negative_finds = 0
iterations = 0

wait_interval = {
    "zero" : 0,
    "low" : 10, 
    "medium" : 20,
    "high" : 30
}

# Adjust time between looking for chests: zero, low, medium, or high
wait_time_selected = "zero"

wait_time_negative = wait_interval[wait_time_selected]
wait_time_positive = wait_time_negative * 2

# Set higher for less "spammy" results output
modulo_num = 20

def report():
    print(f"iterations: {iterations}")
    print(f"positive_clicks: {positive_clicks}")
    print(f"negative_finds: {negative_finds}")
    try:
        chests_found_percent = float(positive_clicks) / float(negative_finds) 
    except ZeroDivisionError as err:
        chests_found_percent = float(0.0)
    print(f"chests_found_percent: {chests_found_percent} %")
    runtime = datetime.datetime.now() - begin_time
    dt_runtime = (datetime.datetime.min + runtime).time()
    strf_dt_runtime = dt_runtime.strftime("%H:%M:%S") 
    print(f"strf_dt_runtime: {strf_dt_runtime}")

try:
    while True:
        mouse_x, mouse_y = pyautogui.position()
        if iterations % modulo_num == 0:
            print()
        try:
            x, y = pyautogui.locateCenterOnScreen("chest.png", grayscale=True, confidence=.95)
            pyautogui.moveTo(x, y)
            pyautogui.click()
            positive_clicks += 1
            pyautogui.moveTo(mouse_x, mouse_y)
            print("found and clicked on a chest")
            time.sleep(wait_time_positive)
        except TypeError as err: 
            if iterations % modulo_num == 0:
                print("couldn't find a chest")
            negative_finds += 1
            time.sleep(wait_time_negative)
        # How many chests are we seeing anyway?
        if iterations % modulo_num == 0:
            report()
        iterations += 1
except KeyboardInterrupt:
    print()
    report()
    print("Exiting.")
    sys.exit() 
