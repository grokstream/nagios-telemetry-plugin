from subprocess import check_output
import unittest

class TestPlugin(unittest.TestCase):

    def test_cpu_times(self):

        out = check_output("./telemetry.py --cpu_times='user'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --cpu_times='nice'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --cpu_times='system'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --cpu_times='idle'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --cpu_times='iowait'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --cpu_times='irq'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --cpu_times='softirq'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --cpu_times='steal'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

    def test_cpu_percent(self):
        out = check_output("./telemetry.py --cpu_percent='percent'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')


    def test_cpu_freq(self):
        out = check_output("./telemetry.py --cpu_freq='current'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --cpu_freq='min'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --cpu_freq='max'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')


    def test_cpu_stats(self):
        out = check_output("./telemetry.py --cpu_stats='ctx_switches'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --cpu_stats='interrupts'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --cpu_stats='soft_interrupts'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --cpu_stats='syscalls'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

    def test_disk_usage(self):
        out = check_output("./telemetry.py --disk_usage='disk_total'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --disk_usage='disk_usage_used'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --disk_usage='disk_usage_free'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --disk_usage='disk_usage_percent'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

    def test_disk_io(self):
        out = check_output("./telemetry.py --disk_io_counters='read_count'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --disk_io_counters='write_count'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --disk_io_counters='read_bytes'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --disk_io_counters='write_time'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --disk_io_counters='read_merged_count'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --disk_io_counters='write_merged_count'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --disk_io_counters='busy_time'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

    def test_virtual_memory(self):
        out = check_output("./telemetry.py --virtual_memory='total'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --virtual_memory='available'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --virtual_memory='virt_percent'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --virtual_memory='free'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --virtual_memory='active'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --virtual_memory='inactive'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --virtual_memory='buffers'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --virtual_memory='cached'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --virtual_memory='shared'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')


    def test_network(self):
        out = check_output("./telemetry.py --network='bytes_sent'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --network='bytes_sent'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --network='bytes_recv'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --network='bytes_sent'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --network='packets_sent'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --network='errin'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --network='errout'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --network='dropin'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')

        out = check_output("./telemetry.py --network='dropout'", shell=True)
        try:
            out = float(out)
            self.assertTrue(isinstance(out, float))
        except:
            self.assertEqual(out[:22], 'You do not have access')








if __name__ == '__main__':
    unittest.main()
