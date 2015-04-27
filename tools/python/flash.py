__author__ = 'Administrator'
import sys
import os
import time
import stat
from os import path
from os.path import basename
import ctypes

name=""
isUsed=False
# name 
# flashImg: loop flash img

if  sys.argv.__len__() >1:
    name=sys.argv[1];

flashImg=["bootloader=u-boot.bin","kernel=zImage","kernel=kernel.img","ramdisk=ramdisk-uboot.img","system=system.img"]
csipLibs=["libcrypto.so", "libpj_opensl_dev.so", "libpj_silk_codec.so",  "libpjsipjni.so" ,"libstlport_shared.so"]

if  not isUsed and name.__len__() >0 :
    for i in flashImg:
        j=i.split("=",2);
        if basename(name)==(j[1]):
            isUsed=True
            os.system("fastboot flash "+j[0]+" \""+name+"\"")
            break

if not isUsed and name.__len__() > 0:
    for i in csipLibs:        
        if name.__contains__(i):
            isUsed=True
            os.system("adb shell am force-stop com.csipsimple")
            os.system("adb push "+name+" /data/data/com.csipsimple/lib")
            os.system("adb shell am start -n com.csipsimple/com.csipsimple.ui.SipHome")
            break

if not isUsed and name[-4:]=='.apk':
    isUsed=True
    os.system("adb install "+name)

def loopFlashImg(topDir):
    if (len(topDir) <1):
        topDir="."
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd != 0:
        ctypes.windll.user32.ShowWindow(whnd, 0)
        ctypes.windll.kernel32.CloseHandle(whnd)
    cmdFastBoot="fastboot flash"
    cmd=[["u-boot.bin","bootloader","0"],["zImage","kernel","0"],["kernel.img","kernel","0"],["ramdisk.img","ramdisk","0"],["ramdisk-uboot.img","ramdisk","0"],["system","system","0"]]
    while (True):
        for  data in cmd:
            file = topDir + "/" + data[0]
            if (path.exists(file)):
                lastTime=os.stat(file)[stat.ST_MTIME]
                if (int(data[2]) <1):
                    data[2]=lastTime
                if (int(data[2]) != lastTime):
                    data[2]=lastTime
                    print ("begin fastboot")
                    flashCmd=cmdFastBoot+" "+data[1]+ " "+topDir+"/"+ data[0]
                    print (flashCmd)
                    os.system(flashCmd)
                    os.system("fastboot reboot")
                    print ("end fastboot")
        time.sleep(1)
        
if not isUsed and name == "flashImg":
    isUsed=True
    loopFlashImg("C:/Users/Administrator/Desktop/temp/img")
        
if not isUsed and len(name) ==0:
    name = input("input command:")
    if (name == "linux"):
        isUsed = True
        topDir = "G:/BaiduYunDownload/qt_news_system"
        os.system("fastboot flash kernel "+topDir+"/zImage")       
        os.system("fastboot flash ramdisk "+topDir+"/ramdisk-uboot.img")
        os.system("fastboot flash system "+topDir+"/system.img")
    elif (name == "cancel"):
        os.system("shutdown -a")
        
if not isUsed:
    print ("nothing to do")

input("click enter key to exit")