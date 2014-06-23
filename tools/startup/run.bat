
::定时关机检测
start "shutdown" "C:\Users\Administrator\Documents\Visual Studio 2012\Projects\ShutDown\Debug\ShutDown.exe"
:: sunday shutdown
set now_date=%date:~11,12%
if %now_date% == 周日 (
	shutdown -s -t 300
	exit 1
)

::start "goagent" "F:\tools\goagent-goagent-88748e9\local\goagent.exe"
::start "android studio" "E:\Users\Administrator\AppData\Local\Android\android-studio\bin\studio64.exe"
start "eclipse" "E:\Program Files\eclipse\eclipse.exe"

:: cocos2d wiki
set "pages="github.com/advx9600/csipsimple-git" "github.com/advx9600/csipsimple-git/commit/24377c299a6b3a13bc7a7ac29aa509b267a9f511" "
::github kernel
set "pages=%pages% "https://github.com/advx9600/kernel-s5pv210/commits/master" "
:: cocos api
::set "pages=%pages% "www.cocos2d-x.org/reference/native-cpp/V3.0/de/d8f/class_cocos_denshion_1_1_simple_audio_engine.html" "
:: box2d api
::set "pages=%pages% "hodade.adam.ne.jp/box2d/API/html/structb2_fixture_def.html""
:: 翻译日语江沪
set "pages=%pages% "dict.hjenglish.com/jp/" "
::百度英语翻译  
set "pages=%pages% "fanyi.baidu.com/translate#zh/en/" "
::set "pages=%pages% "fanyi.baidu.com/translate#zh/jp/" "
::google翻译
::set "pages=%pages% "https://translate.google.com.hk/?hl=zh-CN&tab=wT" "
:: 翻译英文 google网站
set "pages=%pages% "www.iciba.com"  "www.baidu.com""
::start "firefox" "C:\Program Files (x86)\Mozilla Firefox\firefox.exe" %pages%

::start "visual studio 2012  TVMain" "E:\Program Files (x86)\Microsoft Visual Studio 11.0\Common7\IDE\devenv.exe"  ^
::"E:\cygwin64\home\Administrator\cocos2d\cocos2d-x-3.0rc2\dafeng_cocos\MyGames\proj.win32\MyGames.sln"
::start "vmware" "G:\vmware\vmware.exe"
::start "cocos studio" "E:\Program Files (x86)\CocoStudio\CocoStudio.exe"

::E:
::cd "cygwin64\home\Administrator\cocos2d\cocos2d-x-3.0rc2\dafeng_cocos\MyGames"
::cmd
::pause