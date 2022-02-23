import psutil
import serial
import time
import os

ser = serial.Serial('/dev/ttyUSB0') #define serial port.
line = ""
sep1 = '.'

while True:
    t = os.popen('uptime -p').read()[:-1] #open the file /proc/uptime and read it
    up = str(t)
    
    cpu = psutil.cpu_percent(interval=10) #reads the cpu percentage
    temp = int(psutil.sensors_temperatures().get('coretemp')[0].current)
    cpu = str(cpu)
    cpu = str(cpu).replace('"', "")
    cpu = str(cpu).replace("'", "")
    cpu = str(cpu).replace(' ', "")
    cpu = 'CPU ' + cpu
    cpu = str(cpu) + '% ' + str(temp) + 'C'
    
    amount_of_ram = str(psutil.virtual_memory()[2]).split(sep1, 1)[0]
    ram = 'RAM', str(amount_of_ram)
    ram = str(ram) + "%"

    disk = 'DISK ' + str(psutil.disk_usage('/')[3]) + '%'

    up = up.replace("(", "") #replace all unecessary characters from the strings
    up = up.replace(",", "")
    up = up.replace("'", "")
    up = up.replace(")", "")
    up = up.replace("up", "UP")
    up = up.replace(" week", "w")
    up = up.replace(" minute", "m")
    up = up.replace(" hour", "h")
    up = up.replace(" day", "d")
    up = up.replace("s", "") # get rid of plurals
    ram = ram.replace("(", "")
    ram = ram.replace(")", "")
    ram = ram.replace(",", "")
    ram = ram.replace("'", "")

    combined = up + "\n\n" + cpu + "\n\n" + ram + "\n\n" + disk
    print(combined)

    ser.write(combined.encode()) # Write the data 
    line = ser.readline() # Read the serial output
    time.sleep(2) # Wait two seconds

