#!/usr/local/bin/python

try:
    import psutil
except:
    print "You do not have python package 'psutil' installed."

import argparse
import sys

def cpu_time_user():
    data = psutil.cpu_times()
    if 'user' not in vars(data).keys():
        return "You do not have access to 'user' CPU data."
        sys.exit()
    return data[0]

def cpu_time_nice():
    data = psutil.cpu_times()
    if 'nice' not in vars(data).keys():
        return "You do not have access to 'nice' CPU data."
        sys.exit()
    return data[1]

def cpu_time_system():
    data = psutil.cpu_times()
    if 'system' not in vars(data).keys():
        return "You do not have access to 'system' CPU data."
        sys.exit()
    return data[2]

def cpu_time_idle():
    data = psutil.cpu_times()
    if 'idle' not in vars(data).keys():
        return "You do not have access to 'idle' CPU data."
        sys.exit()
    return data[3]

def cpu_time_iowait():
    data = psutil.cpu_times()
    if 'iowait' not in vars(data).keys():
        return "You do not have access to 'iowait' CPU data."
        sys.exit()
    return data[4]

def cpu_time_irq():
    data = psutil.cpu_times()
    if 'irq' not in vars(data).keys():
        return "You do not have access to 'irq' CPU data."
        sys.exit()
    return data[5]

def cpu_time_softirq():
    data = psutil.cpu_times()
    if 'softirq' not in vars(data).keys():
        return "You do not have access to 'softirq' CPU data."
        sys.exit()
    return data[6]

def cpu_time_steal():
    data = psutil.cpu_times()
    if 'steal' not in vars(data).keys():
        return "You do not have access to 'steal' CPU data."
        sys.exit()
    return data[7]

def cpu_time_guest():
    data = psutil.cpu_times()
    if 'guest' not in vars(data).keys():
        return "You do not have access to 'guest' CPU data."
        sys.exit()
    return data[8]




def cpu_percent():
    data = psutil.cpu_timees_percent()
    if 'percent' not in vars(data).keys():
        return "You do not have access to 'percent' CPU data."
        sys.exit()
    return data[0]


def cpu_freq_current():
    data = psutil.cpu_freq()
    if 'current' not in vars(data).keys():
        return "You do not have access to 'current' CPU freq data."
        sys.exit()
    return data[0]

def cpu_freq_min():
    data = psutil.cpu_freq()
    if 'min' not in vars(data).keys():
        return "You do not have access to 'min' CPU freq data."
        sys.exit()
    return data[1]

def cpu_freq_max():
    data = psutil.cpu_freq()
    if 'max' not in vars(data).keys():
        return "You do not have access to 'max' CPU freq data."
        sys.exit()
    return data[2]




#CPU stats

def cpu_stats_ctx_switches():
    data = psutil.cpu_stats()
    if 'ctx_switches' not in vars(data).keys():
        return "You do not have access to 'ctx_switches' CPU stats data."
        sys.exit()
    return data[0]

def cpu_stats_interrupts():
    data = psutil.cpu_stats()
    if 'ctx_switches' not in vars(data).keys():
        return "You do not have access to 'interrupts' CPU stats data."
        sys.exit()
    return data[1]

def cpu_stats_soft_interrupts():
    data = psutil.cpu_stats()
    if 'ctx_switches' not in vars(data).keys():
        return "You do not have access to 'soft_interrupts' CPU stats data."
        sys.exit()
    return data[2]

def cpu_stats_syscalls():
    data = psutil.cpu_stats()
    if 'ctx_switches' not in vars(data).keys():
        return "You do not have access to 'syscalls' CPU stats data."
        sys.exit()
    return data[3]




def disk_usage_total():
    data = psutil.disk_usage('/')
    if 'total' not in vars(data).keys():
        return "You do not have access to 'total' disk data."
        sys.exit()
    return data[0]

def disk_usage_used():
    data = psutil.disk_usage('/')
    if 'used' not in vars(data).keys():
        return "You do not have access to 'used' disk data."
        sys.exit()
    return data[1]

def disk_usage_free():
    data = psutil.disk_usage('/')
    if 'free' not in vars(data).keys():
        return "You do not have access to 'free' disk data."
        sys.exit()
    return data[2]

def disk_usage_percent():
    data = psutil.disk_usage('/')
    if 'percent' not in vars(data).keys():
        return "You do not have access to 'percent' disk data."
        sys.exit()
    return data[3]




#disk I/O
def disk_io_read_count():
    data = psutil.disk_io_counters(perdisk=False)
    if 'read_count' not in vars(data).keys():
        return "You do not have access to 'read_count' disk data."
        sys.exit()
    return data[0]

def disk_io_write_count():
    data = psutil.disk_io_counters(perdisk=False)
    if 'write_count' not in vars(data).keys():
        return "You do not have access to 'write_count' disk data."
        sys.exit()
    return data[1]

def disk_io_read_bytes():
    data = psutil.disk_io_counters(perdisk=False)
    if 'read_bytes' not in vars(data).keys():
        return "You do not have access to 'read_bytes' disk data."
        sys.exit()
    return data[2]

def disk_io_write_time():
    data = psutil.disk_io_counters(perdisk=False)
    if 'write_time' not in vars(data).keys():
        return "You do not have access to 'write_time' disk data."
        sys.exit()
    return data[3]

def disk_io_read_merged_count():
    data = psutil.disk_io_counters(perdisk=False)
    if 'read_merged_count' not in vars(data).keys():
        return "You do not have access to 'read_merged_count' disk data."
        sys.exit()
    return data[4]

def disk_io_write_merged_count():
    data = psutil.disk_io_counters(perdisk=False)
    if 'write_merged_count' not in vars(data).keys():
        return "You do not have access to 'write_merged_count' disk data."
        sys.exit()
    return data[5]

def disk_io_busy_time():
    data = psutil.disk_io_counters(perdisk=False)
    if 'busy_time' not in vars(data).keys():
        return "You do not have access to 'busy_time' disk data."
        sys.exit()
    return data[6]





def virtual_memory_total():
    data = psutil.virtual_memory()
    if 'total' not in vars(data).keys():
        return "You do not have access to 'total' virtual memory data."
        sys.exit()
    return data[0]

def virtual_memory_available():
    data = psutil.virtual_memory()
    if 'available' not in vars(data).keys():
        return "You do not have access to 'available' virtual memory data."
        sys.exit()
    return data[1]

def virtual_memory_percent():
    data = psutil.virtual_memory()
    if 'percent' not in vars(data).keys():
        return "You do not have access to 'percent' virtual memory data."
        sys.exit()
    return data[2]

def virtual_memory_free():
    data = psutil.virtual_memory()
    if 'free' not in vars(data).keys():
        return "You do not have access to 'free' virtual memory data."
        sys.exit()
    return data[3]

def virtual_memory_active():
    data = psutil.virtual_memory()
    if 'active' not in vars(data).keys():
        return "You do not have access to 'active' virtual memory data."
        sys.exit()
    return data[4]

def virtual_memory_inactive():
    data = psutil.virtual_memory()
    if 'inactive' not in vars(data).keys():
        return "You do not have access to 'inactive' virtual memory data."
        sys.exit()
    return data[5]

def virtual_memory_buffers():
    data = psutil.virtual_memory()
    if 'buffers' not in vars(data).keys():
        return "You do not have access to 'buffers' virtual memory data."
        sys.exit()
    return data[6]

def virtual_memory_cached():
    data = psutil.virtual_memory()
    if 'cached' not in vars(data).keys():
        return "You do not have access to 'cached' virtual memory data."
        sys.exit()
    return data[7]

def virtual_memory_shared():
    data = psutil.virtual_memory()
    if 'shared' not in vars(data).keys():
        return "You do not have access to 'shared' virtual memory data."
        sys.exit()
    return data[8]



#swap memory

def swap_memory_total():
    data = psutil.swap_memory()
    if 'total' not in vars(data).keys():
        return "You do not have access to 'shared' swap memory data."
        sys.exit()
    return data[0]

def swap_memory_used():
    data = psutil.swap_memory()
    if 'used' not in vars(data).keys():
        return "You do not have access to 'used' swap memory data."
        sys.exit()
    return data[1]

def swap_memory_free():
    data = psutil.swap_memory()
    if 'free' not in vars(data).keys():
        return "You do not have access to 'free' swap memory data."
        sys.exit()
    return data[2]

def swap_memory_percent():
    data = psutil.swap_memory()
    if 'percent' not in vars(data).keys():
        return "You do not have access to 'percent' swap memory data."
        sys.exit()
    return data[3]

def swap_memory_sin():
    data = psutil.swap_memory()
    if 'sin' not in vars(data).keys():
        return "You do not have access to 'sin' swap memory data."
        sys.exit()
    return data[4]

def swap_memory_sout():
    data = psutil.swap_memory()
    if 'sout' not in vars(data).keys():
        return "You do not have access to 'sout' swap memory data."
        sys.exit()
    return data[5]

interface = ''

def network_bytes_sent():
    data = psutil.net_io_counters()
    if 'bytes_sent' not in vars(data).keys():
        return "You do not have access to 'bytes_sent' network data."
        sys.exit()
    return data[0]

def network_bytes_recv():
    data = psutil.net_io_counters()
    if 'bytes_recv' not in vars(data).keys():
        return "You do not have access to 'bytes_recv' network data."
        sys.exit()
    return data[1]

def network_packets_sent():
    data = psutil.net_io_counters()
    if 'packets_sent' not in vars(data).keys():
        return "You do not have access to 'packets_sent' network data."
        sys.exit()
    return data[2]

def network_packets_recv():
    data = psutil.net_io_counters()
    if 'packets_recv' not in vars(data).keys():
        return "You do not have access to 'packets_recv' network data."
        sys.exit()
    return data[3]

def network_errin():
    data = psutil.net_io_counters()
    if 'errin' not in vars(data).keys():
        return "You do not have access to 'errin' network data."
        sys.exit()
    return data[4]

def network_errout():
    data = psutil.net_io_counters()
    if 'errout' not in vars(data).keys():
        return "You do not have access to 'errout' network data."
        sys.exit()
    return data[5]

def network_dropin():
    data = psutil.net_io_counters()
    if 'dropin' not in vars(data).keys():
        return "You do not have access to 'dropin' network data."
        sys.exit()
    return data[6]

def network_dropout():
    data = psutil.net_io_counters()
    if 'dropout' not in vars(data).keys():
        return "You do not have access to 'dropout' network data."
        sys.exit()
    return data[7]

parser = argparse.ArgumentParser()

MAP = {

    #cpu time
    'user':cpu_time_user,
    'nice':cpu_time_nice,
    'system':cpu_time_system,
    'idle':cpu_time_idle,
    'iowait':cpu_time_iowait,
    'irq':cpu_time_irq,
    'softirq':cpu_time_softirq,
    'steal':cpu_time_steal,
    'guest':cpu_time_guest,

    #cpu freq
    'current':cpu_freq_current,
    'min':cpu_freq_min,
    'max':cpu_freq_max,

    #cpu percent
    'percent':cpu_time_user,

    #cpu stats
    'ctx_switches':cpu_stats_ctx_switches,
    'interrupts':cpu_stats_interrupts,
    'soft_interrupts':cpu_stats_soft_interrupts,
    'syscalls':cpu_stats_syscalls,

    #disk usage
    'disk_total':disk_usage_total,
    'disk_usage_used':disk_usage_used,
    'disk_usage_free':disk_usage_free,
    'disk_usage_percent':disk_usage_percent,

    #disk I/O
    'read_count':disk_io_read_count,
    'write_count':disk_io_write_count,
    'read_bytes':disk_io_read_bytes,
    'write_time':disk_io_write_time,
    'read_merged_count':disk_io_read_merged_count,
    'write_merged_count':disk_io_write_merged_count,
    'busy_time':disk_io_busy_time,

    #virtual_memory
    'total':virtual_memory_total,
    'available':virtual_memory_available,
    'virt_percent':virtual_memory_percent,
    'free':virtual_memory_free,
    'active':virtual_memory_active,
    'inactive':virtual_memory_inactive,
    'buffers':virtual_memory_buffers,
    'cached':virtual_memory_cached,
    'shared':virtual_memory_shared,

    #swap memory
    'swap_total':swap_memory_total,
    'swap_used':swap_memory_used,
    'swap_free':swap_memory_free,
    'swap_percent':swap_memory_percent,
    'sin':swap_memory_sin,
    'sout':swap_memory_sout,


    #network data
    'bytes_sent':network_bytes_sent,
    'bytes_recv':network_bytes_recv,
    'packets_sent':network_packets_sent,
    'packets_recv':network_packets_recv,
    'errin':network_errin,
    'errout':network_errout,
    'dropin':network_dropin,
    'dropout':network_dropout,

}

def main():
    parser.add_argument('--cpu_times', nargs='?', choices=['user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq', 'steal', 'guest'], help="Get CPU time data")
    parser.add_argument('--cpu_freq', nargs='?', choices=['current', 'min', 'max'], help="Get CPU frequency data")
    parser.add_argument('--cpu_stats', nargs='?', choices=['ctx_switches', 'interrupts', 'soft_interrupts', 'syscalls'], help="Get CPU stats data")
    parser.add_argument('--cpu_percent', nargs='?', choices=['percent'], help="Get CPU percent data")
    parser.add_argument('--disk_usage', nargs='?', choices=['disk_total', 'disk_usage_used', 'disk_usage_free', 'disk_usage_percent'], help="Get disk usage data")
    parser.add_argument('--disk_io_counters', nargs='?', choices=['read_count', 'write_count', 'read_bytes', 'write_time', 'read_merged_count', 'write_merged_count', 'busy_time'], help="Get disk I/O data")
    parser.add_argument('--virtual_memory', nargs='?', choices=['total', 'available', 'virt_percent', 'free', 'active', 'inactive', 'buffers', 'cached', 'shared'], help="Get disk virtual memory data")
    parser.add_argument('--swap_memory', nargs='?', choices=['swap_total', 'swap_used', 'swap_free', 'swap_percent', 'sin', 'sout'], help="Get swap memory data")
    parser.add_argument('--network', nargs='?', choices=['bytes_sent', 'bytes_recv', 'packets_sent', 'packets_recv', 'errin', 'errout', 'dropin', 'dropout'], help="Get network data")

    args = parser.parse_args()
    if args.cpu_times != None:
        func = MAP[args.cpu_times]
    if args.cpu_freq != None:
        func = MAP[args.cpu_freq]
    if args.cpu_stats != None:
        func = MAP[args.cpu_stats]
    if args.cpu_percent != None:
        func = MAP[args.cpu_percent]
    if args.disk_usage != None:
        func = MAP[args.disk_usage]
    if args.disk_io_counters != None:
        func = MAP[args.disk_io_counters]
    if args.virtual_memory != None:
        func = MAP[args.virtual_memory]
    if args.swap_memory != None:
        func = MAP[args.swap_memory]
    if args.network != None:
        func = MAP[args.network]
    result = func()
    print result


if __name__ == '__main__':
    main()
