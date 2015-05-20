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
    cmd=[["u-boot.bin","bootloader","0"],["zImage","kernel","0"],["kernel.img","kernel","0"],["ramdisk.img","ramdisk","0"],["ramdisk-uboot.img","ramdisk","0"],["system.img","system","0"]]
    while (True):
        for  data in cmd:
            file = topDir + "/" + data[0]
            if (path.exists(file)):
                lastTime=os.stat(file)[stat.ST_MTIME]                
                if (int(data[2]) <1):
                    data[2]=lastTime
                if (int(data[2]) != lastTime):
                    data[2]=lastTime
                    # 当前状态可能还在copy当中                    
                    while True:
                        lastSize = os.stat(file)[stat.ST_SIZE] 
                        time.sleep(1)
                        if (lastSize == os.stat(file)[stat.ST_SIZE]):
                            break                    
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
        isUsed = True
        os.system("shutdown -a")
    elif (name == "android"):
        isUsed = True
        topDir = "G:/BaiduYunDownload/cdrom-4412-4.4/cdrom_4412_4.4/Tools/Image & update tools/usb update tools"
        os.system("mmc erase boot 0 0 0")
        os.system("mmc erase user 0 0 0")
        os.system("fdisk -c 0 512 1000 200")
        os.system("fastboot flash fwbl1 \""+topDir+"/4412/bl1.bin\"")
        os.system("fastboot flash bl2 \""+topDir+"/4412/bl2.bin\"")
        os.system("fastboot flash tzsw \""+topDir+"/4412/tzsw.bin\"")
        os.system("fastboot flash bootloader \""+topDir+"/4412/u-boot.bin\"")
        os.system("fastboot flash kernel \""+topDir+"/4412/zImage\"")
        os.system("fastboot flash ramdisk \""+topDir+"/4412/ramdisk-uboot.img\"")
        os.system("fastboot -w")
        os.system("fastboot flash system \""+topDir+"/4412/system.img\"")
    elif (name == "cmd"):
        os.system("cmd")
        
if not isUsed:
    print ("nothing to do")

input("click enter key to exit")