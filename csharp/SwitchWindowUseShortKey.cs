using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Runtime.InteropServices;

namespace ConsoleApp3
{
    // 用于快捷键切换定义好的已经打开的程序（需要多次启动程序）

    // 参考url https://blog.csdn.net/csdn_joker/article/details/53365012
    // https://www.cnblogs.com/xiaochun126/p/4516822.html
    // https://stackoverflow.com/questions/257879/using-findwindow-with-multiple-root-windows

    // 把编译好的程序放在 "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Administrative Tools" 下面，并定义好快捷方式
    // 打程序，再按定义好的按键就能切换到需要的快捷方式，比如打开程序后再按 j，就是切换到android studio,或者按f就是文件夹

    class Program
    {
        private static void addData()
        {
            A("CabinetWClass", "f");// 文件夹
            A("SunAwtFrame", "j");// android studio
            A("MozillaWindowClass", "l", true); // firefox
            A("Notepad++", "n");    //
            A("Qt5QWindowIcon", "k"); // android 模拟器
            A("VirtualConsoleClassWork", "m"); // conEmu
        }
        public class ClsBase
        {

            public ClsBase(string name, string key, bool isMultiWin)
            {
                this.name = name;
                this.key = key;
                this.isMultiWin = isMultiWin;
            }
            public string name { get; }
            public string key { get; }
            public bool isMultiWin { get; }
        }


        private static List<ClsBase> TotalList = new List<ClsBase>();

        private static void A(string name, string key, bool isMultiWin = false)
        {
            TotalList.Add(new ClsBase(name, key, isMultiWin));
        }


        static void Main(string[] args)
        {

            addData();
            var inputKey = Console.ReadKey().KeyChar.ToString();
            foreach (var baseCls in TotalList)
            {
                // Console.WriteLine(inputKey + "," + baseCls.key+","+baseCls.name+","+baseCls.isMultiWin);
                if (inputKey.Equals(baseCls.key))
                {
                    Console.WriteLine(baseCls.name);
                    diskplayWindow(baseCls.name, baseCls.isMultiWin);
                    break;
                }
            }


        }

        private static void diskplayWindow(string lpszClass, bool isMultiWin)
        {
            IntPtr ParenthWnd = new IntPtr(0);
            ParenthWnd = FindWindow(lpszClass, null);
            if (isMultiWin) // 多个窗口时，需要找到最下面一个
            {
                for (var i = 0; i < 30; i++)
                {
                    IntPtr childHwnd = FindWindowEx(IntPtr.Zero, ParenthWnd, lpszClass, null);
                    Console.WriteLine("childHwnd:" + childHwnd);
                    if (!childHwnd.Equals(IntPtr.Zero) || childHwnd.Equals(ParenthWnd))
                    {
                        ParenthWnd = childHwnd;
                        Console.WriteLine(i + " Ptr:" + ParenthWnd + "," + ParenthWnd.ToString("x2"));
                    }
                    else break;
                }
            }
            //ParenthWnd = new IntPtr(0x00010600);
            Console.WriteLine("Ptr:" + ParenthWnd + "," + ParenthWnd.ToString("x2"));

            if (!ParenthWnd.Equals(IntPtr.Zero))
            {
                ShowWindow(ParenthWnd, 1);
                SwitchToThisWindow(ParenthWnd, true);
            }
            else
            {
                Console.Write("there is no avalable application");
            }
        }

        [DllImport("user32.dll ", SetLastError = true)]
        private static extern void SwitchToThisWindow(IntPtr hWnd, bool fAltTab);

        [DllImport("user32.dll", EntryPoint = "ShowWindow", CharSet = CharSet.Auto)]
        private static extern int ShowWindow(IntPtr hwnd, int nCmdShow);

        [DllImport("user32.dll", EntryPoint = "ShowWindowAsync", SetLastError = true)]
        private static extern bool ShowWindowAsync(IntPtr hWnd, int cmdShow);

        [DllImport("User32.dll", EntryPoint = "FindWindow")]
        private static extern IntPtr FindWindow(string lpClassName, string lpWindowName);

        [DllImport("user32.dll", EntryPoint = "FindWindowEx", SetLastError = true)]
        private static extern IntPtr FindWindowEx(IntPtr hwndParent, IntPtr hwndChildAfter, string lpszClass, string lpszWindow);

        [DllImport("User32.dll", EntryPoint = "SendMessage")]
        private static extern int SendMessage(IntPtr hWnd, int Msg, IntPtr wParam, string lParam);

        const int WM_GETTEXT = 0x000D;
        const int WM_SETTEXT = 0x000C;
        const int WM_CLICK = 0x00F5;
    }
}