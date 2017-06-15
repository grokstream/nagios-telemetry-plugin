try:
    import psutil
except:
    print "You do not have python package 'psutil' installed."

import sys

if __name__ == '__main__':
    arguments = sys.argv
    script = arguments[0]
    if len(arguments) >= 3:
        disk_type = arguments[1]
        if disk_type == '--disk_usage':
            data = psutil.disk_usage('/')
            result = {
                '--total':data[0],
                '--used':data[1],
                '--free':data[2],
                '--percent':data[3],
            }.get(arguments[2])

        if disk_type == '--disk_io_counters':
            data = psutil.disk_io_counters(perdisk=False)
            result = {
                '--read_count':data[0],
                '--write_count':data[1],
                '--read_bytes':data[2],
                '--write_time':data[3],
                '--read_merged_count':data[4],
                '--write_merged_count':data[5],
                '--busy_time':data[6]
            }.get(arguments[2])

        print result
