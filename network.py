try:
    import psutil
except:
    print "You do not have python package 'psutil' installed."

import sys

if __name__ == '__main__':
    arguments = sys.argv
    if len(arguments) >= 3:
        cpu_type = arguments[1]
        if cpu_type == '--times':
            data = psutil.cpu_times()
            result = {
                '--user':data[0],
                '--nice':data[1],
                '--system':data[2],
                '--idle':data[3],
                '--iowait':data[4],
                '--irq':data[5],
                '--softirq':data[6],
                '--steal':data[7],
                '--guest':data[8]
            }.get(arguments[2])

        if cpu_type == '--percents':
            data = psutil.cpu_percent()
            result = {
                '--user':data[0],
                '--nice':data[1],
                '--system':data[2],
                '--idle':data[3],
                '--iowait':data[4],
                '--irq':data[5],
                '--softirq':data[6],
                '--steal':data[7],
                '--guest':data[8],
                '--guest-nice':data[9]
            }.get(arguments[2])

        if cpu_type == '--frequency':
            data = psutil.cpu_freq()
            result = {
                '--current':data[0],
                '--min':data[1],
                '--max':data[2],
            }.get(arguments[2])

        if cpu_type == '--stats':
            data = psutil.cpu_stats()
            result = {
                '--ctx_switches':data[0],
                '--interrupts':data[1],
                '--soft_interrupts':data[2],
                '--syscalls':data[3]
            }.get(arguments[2])

        print result
