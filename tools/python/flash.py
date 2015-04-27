__author__ = 'Administrator'
import sys
import os
import time
import stat
from os import path
from os.path import basename

name=""
isUsed=0
# name 
# 1 loop flash u-boot,2 loop flash kernel

if  sys.argv.__len__() >1:
    name=sys.argv[1];

flashImg=["bootloader=u-boot.bin","kernel=zImage","kernel=kernel.img","ramdisk=ramdisk-uboot.img","system=system.img"]
csipLibs=["libcrypto.so", "libpj_opensl_dev.so", "libpj_silk_codec.so",  "libpjsipjni.so" ,"libstlport_shared.so"]

if  not isUsed and name.__len__() >0 :
    for i in flashImg:
        j=i.split("=",2);
        if basename(name)==(j[1]):
            isUsed=1
            os.system("fastboot flash "+j[0]+" \""+name+"\"")
            break

if not isUsed and name.__len__() > 0:
    for i in csipLibs:        
        if name.__contains__(i):
            isUsed=1
            os.system("adb shell am force-stop com.csipsimple")
            os.system("adb push "+name+" /data/data/com.csipsimple/lib")
            os.system("adb shell am start -n com.csipsimple/com.csipsimple.ui.SipHome")
            break

if not isUsed and name[-4:]=='.apk':
    isUsed=1
    os.system("adb install "+name)

if not isUsed and name == "1" or name == "2":
    isUsed=1
    cmd=["u-boot.bin","fastboot flash bootloader u-boot.bin"]
    cmd2=["zImage","fastboot flash kernel zImage"]
    if (int(name) ==2):
        cmd=cmd2
    fileModTime=0    
    file=cmd[0];
    flashCmd=cmd[1]
    while (True):
        if (path.exists(file)):
            st=os.stat(file)                        
            if fileModTime < 1:
                fileModTime = int(st[stat.ST_MTIME])
            if  fileModTime != int(st[stat.ST_MTIME]):
                fileModTime = int(st[stat.ST_MTIME])
                print ("begin fastboot")
                print (flashCmd)
                os.system(flashCmd)
                os.system("fastboot reboot")
                print ("end fastboot")
        time.sleep(1)
            
            
    
if not isUsed:
    print ("nothing to do")

input("click enter key to exit")