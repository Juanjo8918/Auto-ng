import os
import subprocess, signal, time
import colored
from colored import fg


print("                                             ")
print("    ___         __              _   ________ ")
print("   /   | __  __/ /_____        / | / / ____/ ")
print("  / /| |/ / / / __/ __ \______/  |/ / / __   ")
print(" / ___ / /_/ / /_/ /_/ /_____/ /|  / /_/ /   ")
print("/_/  |_\__,_/\__/\____/     /_/ |_/\____/    ")
print("                                             ")
print("                                             ")
print("                                             ")
mm = str(input("Interface you want to put into Monitor Mode: "))
print("                                             ")
print("Selected interface: " + mm)
print("                                             ")
print("                                             ")
print("                                             ")
print("                                             ")

DEVNULL = open(os.devnull, 'wb')
subprocess.run('ifconfig ',stdout=DEVNULL,shell=True)
subprocess.Popen('ifconfig ' + mm + ' down',shell=True)
subprocess.Popen('iwconfig ' + mm + ' mode monitor',shell=True)
subprocess.Popen('airmon-ng start'+mm,shell=True,stdout=DEVNULL)
subprocess.Popen('ifconfig ' + mm + ' up',shell=True)

f = subprocess.run('iwconfig',shell=True)
cg = fg('green')
print("Interface set to Monitor mode "+ cg +"successfully")
print("                                             ")
print("                                             ")
time.sleep(.5)
print('Number of what you want to do next: ')
print('    1. Airodump-ng')
print("                                             ")
print("                                             ")
option = int(input('Number: '))

p = subprocess.Popen('airodump-ng '+mm, shell=True)
time.sleep(5) #Wait 5 secs before killing
p.send_signal(signal.CTRL_C_EVENT)



print(f.returncode)

