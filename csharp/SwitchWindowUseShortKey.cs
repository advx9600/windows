using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Runtime.InteropServices;

namespace ConsoleApp3
{
    // ���ڿ�ݼ��л�����õ��Ѿ��򿪵ĳ�����Ҫ�����������

    // �ο�url https://blog.csdn.net/csdn_joker/article/details/53365012
    // https://www.cnblogs.com/xiaochun126/p/4516822.html
    // https://stackoverflow.com/questions/257879/using-findwindow-with-multiple-root-windows

    // �ѱ���õĳ������ "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Administrative Tools" ���棬������ÿ�ݷ�ʽ
    // ������ٰ�����õİ��������л�����Ҫ�Ŀ�ݷ�ʽ������򿪳�����ٰ� j�������л���android studio,���߰�f�����ļ���

    class Program
    {
        private static void addData()
        {
            A("CabinetWClass", "f");// �ļ���
            A("SunAwtFrame", "j");// android studio
            A("MozillaWindowClass", "l", true); // firefox
            A("Notepad++", "n");    //
            A("Qt5QWindowIcon", "k"); // android ģ����
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
            if (isMultiWin) // �������ʱ����Ҫ�ҵ�������һ��
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