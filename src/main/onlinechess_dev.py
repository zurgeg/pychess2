import time
print("DEVELOPER MODE")
log = open("log.txt", "a")
log.write(time.strftime("%M/%D/%Y") + ": DEVELOPER MODE")
print("THE SYSTEM LOGS WHATEVER APPEARS HERE AND WHATEVER YOU TYPE ALONG WITH THE TIME") 
log.write(time.strftime("%M/%D/%Y") + ": THE SYSTEM LOGS WHATEVER APPEARS HERE AND WHATEVER YOU TYPE ALONG WITH THE TIME")
log.close()
print("Finished")

