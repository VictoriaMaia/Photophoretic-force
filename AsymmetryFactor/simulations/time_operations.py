import time


def convert_time_to_more_readable(seconds):
    struct_time = time.gmtime(seconds)
    print("\033[7m {}h:{}m:{}s \033[0m".format(struct_time.tm_hour, struct_time.tm_min, struct_time.tm_sec))


def time_average(values_of_time):
    return sum(values_of_time) / len(values_of_time)
