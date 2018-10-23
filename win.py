import psutil
disk = psutil.disk_io_counters()#利用psutil模块的disk_partitions()方法
print("读速率：　" +str(disk.read_bytes / 1028 / 1028 / (disk.read_time/1000)) + "MB/S")
print("写速率：　" +str(disk.write_bytes / 1028 / 1028 / (disk.write_time / 1000)) + "MB/S")