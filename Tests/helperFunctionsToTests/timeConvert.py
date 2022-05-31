import time

def convertTimeToMoreReadable(seconds):
    structTime = time.gmtime(seconds)
    print("\033[7m {}h:{}m:{}s \033[0m".format(structTime.tm_hour, structTime.tm_min, structTime.tm_sec))
