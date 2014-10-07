__author__ = 'Administrator'
import sys
import os
from os.path import basename

name=""
isUsed=0

if  sys.argv.__len__() >1:
    name=sys.argv[1];

flashImg=["bootloader=u-boot.bin","kernel=kernel.img","system=system.img"]
csipLibs=["libcrypto.so", "libpj_opensl_dev.so", "libpj_silk_codec.so",  "libpjsipjni.so" ,"libstlport_shared.so"]

if  not isUsed and name.__len__() >0 :
    for i in flashImg:
        j=i.split("=",2);
        if basename(name).startswith(j[1].split(".")[0]) and basename(name).endswith("."+j[1].split(".")[1]):
            isUsed=1
            os.system("fastboot flash "+j[0]+" "+name)
            break

if not isUsed and name.__len__() > 0:
    for i in csipLibs:
        print i
        print name
        if name.__contains__(i):
            isUsed=1
            os.system("adb shell am force-stop com.csipsimple")
            os.system("adb push "+name+" /data/data/com.csipsimple/lib")
            os.system("adb shell am start -n com.csipsimple/com.csipsimple.ui.SipHome")
            break

if not isUsed and name[-4:]=='.apk':
    isUsed=1
    os.system("adb install "+name)

if not isUsed:
    print "nothing to do"

raw_input("click enter key to exit")