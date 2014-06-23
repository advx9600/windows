// ShutDown.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "time.h"
#include <windows.h>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	time_t now_time;		
	struct tm local;

	HWND hwnd;
	
	if(hwnd=::FindWindow(_T("ConsoleWindowClass"),NULL)) //找到控制台句柄
	{
		::ShowWindow(hwnd,SW_HIDE); //隐藏控制台窗口
	}

	while(1)
	{		
		printf("sleep\n");
		Sleep(1000*60*5);// must > 5 minutes
		time(&now_time);
		localtime_s(&local,&now_time);

		const int maxShutdownTimes=2;
		int curShutCount=0;
		// sunday
		if (local.tm_wday ==0){
			if (local.tm_hour ==8){
				if (local.tm_min>0 && local.tm_min <30){
					printf("shutdown\n");
					system("shutdown -t 60 -s");
				}
			}
		}else if (local.tm_wday ==6){
			if (local.tm_hour==12 && curShutCount<maxShutdownTimes){
				if (local.tm_min>7 ){
					curShutCount++;
					system("shutdown -t 60 -s");
				}
			}
		}else {
			if (local.tm_hour==17 && curShutCount<maxShutdownTimes){
				if (local.tm_min>35  ){
					curShutCount++;
					system("shutdown -t 60 -s");
				}
			}
		}

	}

	return 0;
}

