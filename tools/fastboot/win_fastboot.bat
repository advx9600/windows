@echo off

set name=%1
set "str=bootloader=u-boot.bin:kernel=kernel.img:system=system.img"

setlocal ENABLEDELAYEDEXPANSION
for %%s in ("%str::=" "%") do (
 for /F "tokens=1,2 delims==" %%a in (%%s) do (
	set rep_str=!name:%%b=!
	if not !rep_str!==%name%  ( fastboot flash %%a %name% )
 )
)
endlocal

pause
exit