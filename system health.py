#!/usr/bin/env python3
import shutil
import psutil

def check_disk_usage(disk):
    di=shutil.disk_usage(disk)
    free=di.free/di.total *100
    print(free)
    return free>20

def check_cpu_usage():
    usage=psutil.cpu_percent(1)
    print("hi",usage)

    return usage<75
check_cpu_usage()
if not check_disk_usage("/") or not check_cpu_usage():
    print("Cpu health is at Risk")
else:
    print("Everything is running Smoothely")
