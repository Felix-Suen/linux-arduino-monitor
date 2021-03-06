#! /bin/python3

import pyudev
import os

# change this value to your specific arduino board #
# run usb-devices command to find that information #
vendor = '1a86'

def main():
    path = os.path.dirname(os.path.realpath(__file__))
    # runs as a daemon to check if the arduino is connected via usb tty
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem="tty")
    for action, device in monitor:
        vendor_id = device.get('ID_VENDOR_ID')
        # get the vendor id by running the command "lsusb"
        if (action == 'add' and vendor_id == vendor):
            print("device is connected")
            os.system(path + '/system.py') # system.py is in the same directory

main()
