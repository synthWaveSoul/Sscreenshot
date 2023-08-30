# Screenshot script

A very small script that saves the screenshot to a file on disk

# Background story

One of the PCs that collects data has an automatic reboot set up every night, because sometimes errors occur and after the reboot everything works fine. However, the error message is helpful to find the cause of the problem. So, I created this script to automatically save a screenshot before reboot. The script is run in Windows scheduler just before PC restart.

# How to use

If you want to use it yourself, just adjust the path where the file is to be saved as you like and possibly change the file name, my script creates the file name from the date the script was executed. At the end you still need to export the script to an exe file using e.g., *“auto-py-to-exe”*  
https://pypi.org/project/auto-py-to-exe/