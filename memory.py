try:
    import psutil
except:
    print "You do not have python package 'psutil' installed."

import sys

if __name__ == '__main__':
    arguments = sys.argv
    script = arguments[0]
    if len(arguments) >= 3:
        memory_type = arguments[1]
        if memory_type == '--virtual':
            data = psutil.virtual_memory()
            result = {
                    '--total':data[0],
                    '--available':data[1],
                    '--percent':data[2],
                    '--free':data[3],
                    '--active':data[4],
                    '--inactive':data[5],
                    '--buffers':data[6],
                    '--cached':data[7],
                    '--shared':data[8]
            }.get(arguments[2])
            
        if memory_type == '--swap':
            data = psutil.swap_memory()
            result = {
                '--total':data[0],
                '--used':data[1],
                '--free':data[2],
                '--percent':data[3],
                '--sin':data[4],
                '--sout':data[5],
            }.get(arguments[2])

        print result
        

    


