import time

seconds = int(input("Enter the amount of seconds"))
minutes = int(input("Enter the amount of minutes"))
hours = int(input("Enter the amount of hours"))
total_time = seconds+(minutes*60)+(hours*3600)
print(f"Timer set for {hours} hour(s), {minutes} minute(s) and {seconds} second(s).")
time.sleep(total_time)
print("Time's up!")