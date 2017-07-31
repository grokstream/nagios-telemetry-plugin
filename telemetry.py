#!/usr/bin/python


API_KEY = 'AtxhdCsZgRtCzRajYVWqccZJYxY5eZKK'
GROK_HOST = 'taurus-bivc.arategroup.com'


try:
    import psutil
    import requests
    requests.packages.urllib3.disable_warnings()
except:
    print "You do not have the correct python packages installed."
    sys.exit(2)

import argparse
import sys
import socket
import time

def cpu_time_user():
    data = psutil.cpu_times()
    if not data.user:
        print "Could not determine metric value."
        sys.exit(3)
    return data[0]

def cpu_time_nice():
    data = psutil.cpu_times()
    if not data.nice:
        print "Could not determine metric value."
        sys.exit(3)
    return data[1]

def cpu_time_system():
    data = psutil.cpu_times()
    if not data.system:
        print "Could not determine metric value."
        sys.exit(3)
    return data[2]

def cpu_time_idle():
    data = psutil.cpu_times()
    if not data.idle:
        print "Could not determine metric value."
        sys.exit(3)
    return data[3]

def cpu_time_iowait():
    data = psutil.cpu_times()
    if not data.iowait:
        print "Could not determine metric value."
        sys.exit(3)
    return data[4]

def cpu_time_irq():
    data = psutil.cpu_times()
    if not data.irq:
        print "Could not determine metric value."
        sys.exit(3)
    return data[5]

def cpu_time_softirq():
    data = psutil.cpu_times()
    if not data.softirq:
        print "Could not determine metric value."
        sys.exit(3)
    return data[6]

def cpu_time_steal():
    data = psutil.cpu_times()
    if not data.steal:
        print "Could not determine metric value."
        sys.exit(3)
    return data[7]

def cpu_time_guest():
    data = psutil.cpu_times()
    if not data.guest:
        print "Could not determine metric value."
        sys.exit(3)
    return data[8]

def cpu_percent():
    data = psutil.cpu_timees_percent()
    if not data.percent:
        print "Could not determine metric value."
        sys.exit(3)
    return data[0]

def cpu_freq_current():
    data = psutil.cpu_freq()
    if not data.current:
        print "Could not determine metric value."
        sys.exit(3)
    return data[0]

def cpu_freq_min():
    data = psutil.cpu_freq()
    if not data.min:
        print "Could not determine metric value."
        sys.exit(3)
    return data[1]

def cpu_freq_max():
    data = psutil.cpu_freq()
    if not data.max:
        print "Could not determine metric value."
        sys.exit(3)
    return data[2]

def cpu_stats_ctx_switches():
    data = psutil.cpu_stats()
    if not data.ctx_switches:
        print "Could not determine metric value."
        sys.exit(3)
    return data[0]

def cpu_stats_interrupts():
    data = psutil.cpu_stats()
    if not data.interrupts:
        print "Could not determine metric value."
        sys.exit(3)
    return data[1]

def cpu_stats_soft_interrupts():
    data = psutil.cpu_stats()
    if not data.soft_interrupts:
        print "Could not determine metric value."
        sys.exit(3)
    return data[2]

def cpu_stats_syscalls():
    data = psutil.cpu_stats()
    if not data.syscalls:
        print "Could not determine metric value."
        sys.exit(3)
    return data[3]




def disk_usage_total():
    data = psutil.disk_usage('/')
    if not data.total:
        print "Could not determine metric value."
        sys.exit(3)
    return data[0]

def disk_usage_used():
    data = psutil.disk_usage('/')
    if not data.used:
        print "Could not determine metric value."
        sys.exit(3)
    return data[1]

def disk_usage_free():
    data = psutil.disk_usage('/')
    if not data.free:
        print "Could not determine metric value."
        sys.exit(3)
    return data[2]

def disk_usage_percent():
    data = psutil.disk_usage('/')
    if not data.percent:
        print "Could not determine metric value."
        sys.exit(3)
    return data[3]


#disk I/O
def disk_io_read_count():
    data = psutil.disk_io_counters(perdisk=False)
    if not data.read_count:
        print "Could not determine metric value."
        sys.exit(3)
    return data[0]

def disk_io_write_count():
    data = psutil.disk_io_counters(perdisk=False)
    if not data.write_count:
        print "Could not determine metric value."
        sys.exit(3)
    return data[1]

def disk_io_read_bytes():
    data = psutil.disk_io_counters(perdisk=False)
    if not data.read_bytes:
        print "Could not determine metric value."
        sys.exit(3)
    return data[2]

def disk_io_write_time():
    data = psutil.disk_io_counters(perdisk=False)
    if not data.write_time:
        print "Could not determine metric value."
        sys.exit(3)
    return data[3]

def disk_io_read_merged_count():
    data = psutil.disk_io_counters(perdisk=False)
    if not data.read_merged_count:
        print "Could not determine metric value."
        sys.exit(3)
    return data[4]

def disk_io_write_merged_count():
    data = psutil.disk_io_counters(perdisk=False)
    if not data.write_merged_count:
        print "Could not determine metric value."
        sys.exit(3)
    return data[5]

def disk_io_busy_time():
    data = psutil.disk_io_counters(perdisk=False)
    if not data.busy_time:
        print "Could not determine metric value."
        sys.exit(3)
    return data[6]





def virtual_memory_total():
    data = psutil.virtual_memory()
    if not data.total:
        print "Could not determine metric value."
        sys.exit(3)
    return data[0]

def virtual_memory_available():
    data = psutil.virtual_memory()
    if not data.available:
        print "Could not determine metric value."
        sys.exit(3)
    return data[1]

def virtual_memory_percent():
    data = psutil.virtual_memory()
    if not data.percent:
        print "Could not determine metric value."
        sys.exit(3)
    return data[2]

def virtual_memory_free():
    data = psutil.virtual_memory()
    if not data.free:
        print "Could not determine metric value."
        sys.exit(3)
    return data[3]

def virtual_memory_active():
    data = psutil.virtual_memory()
    if not data.active:
        print "Could not determine metric value."
        sys.exit(3)
    return data[4]

def virtual_memory_inactive():
    data = psutil.virtual_memory()
    if not data.inactive:
        print "Could not determine metric value."
        sys.exit(3)
    return data[5]

def virtual_memory_buffers():
    data = psutil.virtual_memory()
    if not data.buffers:
        print "Could not determine metric value."
        sys.exit(3)
    return data[6]

def virtual_memory_cached():
    data = psutil.virtual_memory()
    if not data.cached:
        print "Could not determine metric value."
        sys.exit(3)
    return data[7]

def virtual_memory_shared():
    data = psutil.virtual_memory()
    if not data.shared:
        print "Could not determine metric value."
        sys.exit(3)
    return data[8]



#swap memory

def swap_memory_total():
    data = psutil.swap_memory()
    if not data.total:
        print "Could not determine metric value."
        sys.exit(3)
    return data[0]

def swap_memory_used():
    data = psutil.swap_memory()
    if not data.used:
        print "Could not determine metric value."
        sys.exit(3)
    return data[1]

def swap_memory_free():
    data = psutil.swap_memory()
    if not data.free:
        print "Could not determine metric value."
        sys.exit(3)
    return data[2]

def swap_memory_percent():
    data = psutil.swap_memory()
    if not data.percent:
        print "Could not determine metric value."
        sys.exit(3)
    return data[3]

def swap_memory_sin():
    data = psutil.swap_memory()
    if not data.sin:
        print "Could not determine metric value."
        sys.exit(3)
    return data[4]

def swap_memory_sout():
    data = psutil.swap_memory()
    if not data.sout:
        print "Could not determine metric value."
        sys.exit(3)
    return data[5]

interface = ''

def network_bytes_sent():
    data = psutil.net_io_counters()
    if not data.bytes_sent:
        print "Could not determine metric value."
        sys.exit(3)
    return data[0]

def network_bytes_recv():
    data = psutil.net_io_counters()
    if not data.bytes_recv:
        print "Could not determine metric value."
        sys.exit(3)
    return data[1]

def network_packets_sent():
    data = psutil.net_io_counters()
    if not data.packets_sent:
        print "Could not determine metric value."
        sys.exit(3)
    return data[2]

def network_packets_recv():
    data = psutil.net_io_counters()
    if not data.packets_recv:
        print "Could not determine metric value."
        sys.exit(3)
    return data[3]

def network_errin():
    data = psutil.net_io_counters()
    if not data.errin:
        print "Could not determine metric value."
        sys.exit(3)
    return data[4]

def network_errout():
    data = psutil.net_io_counters()
    if not data.errout:
        print "Could not determine metric value."
        sys.exit(3)
    return data[5]

def network_dropin():
    data = psutil.net_io_counters()
    if not data.dropin:
        print "Could not determine metric value."
        sys.exit(3)
    return data[6]

def network_dropout():
    data = psutil.net_io_counters()
    if not data.dropout:
        print "Could not determine metric value."
        sys.exit(3)
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

def post_data(data, metric_name):
    hostname = socket.getfqdn()
    timestamp = int(time.time())
    GROK_ENDPOINT = "https://{}:@{}/_metrics/custom/".format(API_KEY, GROK_HOST)
    endpoint = "{}{}".format(GROK_ENDPOINT, 'nagios_'+hostname+'_'+metric_name)
    r = requests.post(endpoint, json={'timestamp':timestamp, 'value':data}, verify=False)

def main():
    try:
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
        metric_name = str(func).split(' ')[1]
        result = func()
        post_data(result, metric_name)
	print 'Sending data...'
	sys.exit(0)
    except:
        print 'There was a problem running the plugin.'
        sys.exit(3)


if __name__ == '__main__':
    main()
