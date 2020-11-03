import os
import platform

def getMotherboardSerialNumber():
	currentOS = platform.system()
	currentOS = currentOS.lower()

	if(currentOS == "windows"):
		command = "wmic bios get serialnumber"
	elif(currentOS == "linux"):
		command = "hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid"
	else:
		command = "ioreg -l | grep IOPlatformSerialNumber"

	serialNumber = os.popen(command).read().replace("\n", "").replace("	", "").replace(" ", "")
	return serialNumber[12::]



print("Motherboard Serial Number is: ",getMotherboardSerialNumber())
