import pyautogui
import datetime

dt = datetime.datetime.now()
d = dt.strftime("%d")
m = dt.strftime("%m")
y = dt.strftime("%Y")

current_date = d+m+y

myScreenshot = pyautogui.screenshot()
myScreenshot.save(f'C:\screen\{current_date}.png')