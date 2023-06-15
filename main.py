import sys
import threading

import keyboard
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import ctypes

from ystools import YsFuck

version = "1.0.1"
thread = None  # 全局变量，用于存储线程对象



# 检查用户是否是管理员
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


class FuckerUI(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.runState_ui = None
        self.pack(fill=BOTH, expand=YES)



        self.runStateStr = ttk.StringVar(value="")
        self.isFuckPlot = ttk.BooleanVar(value=True)
        self.isPickUp = ttk.BooleanVar(value=False)
        self.setupUI().pack(fill=BOTH, expand=YES)
        # self.bagel = setup_demo()
        # self.bagel.pack(fill=BOTH, expand=YES)

    def setupUI(self):
        root = ttk.Frame(self, padding=10)
        style = ttk.Style()
        theme_names = style.theme_names()

        theme_selection = ttk.Frame(root, padding=(10, 10, 10, 0))
        theme_selection.pack(fill=X, expand=YES)

        theme_selected = ttk.Label(
            master=theme_selection,
            text="FuckYsPlotTools",
            font="-size 24 -weight bold"
        )
        theme_selected.pack(side=LEFT)

        lframe = ttk.Frame(root, padding=5)
        lframe.pack(side=LEFT, fill=BOTH, expand=YES)

        rframe = ttk.Frame(root, padding=5)
        rframe.pack(side=RIGHT, fill=BOTH, expand=YES)

        color_group = ttk.Labelframe(
            master=lframe,
            text="操作按钮支持快捷键",
            padding=10
        )
        color_group.pack(fill=X, side=BOTTOM)

        cb1 = ttk.Button(color_group, text='F10-开始', bootstyle='primary', command=self.on_start)
        cb2 = ttk.Button(color_group, text='F11-停止', bootstyle='info', command=self.on_pause)
        cb3 = ttk.Button(color_group, text='退出', bootstyle='danger', command=self.on_exit)
        if is_admin():
            self.runStateStr.set("当前软件可以运行，已获得管理员权限")
            self.runState_ui = ttk.Label(color_group, textvariable=self.runStateStr, foreground='#00ff00')
        else:
            self.runStateStr.set("请退出软件后，点击右键已管理员身份运行")
            self.runState_ui = ttk.Label(color_group, textvariable=self.runStateStr, foreground='#ff0000')

        self.runState_ui.pack(pady=5, fill=X)
        cb1.pack(side=LEFT, expand=YES, padx=5, fill=X)
        cb2.pack(side=LEFT, expand=YES, padx=5, fill=X)
        cb3.pack(side=LEFT, expand=YES, padx=5, fill=X)

        ttframe = ttk.Frame(lframe)
        ttframe.pack(pady=5, fill=X, side=TOP)

        # # notebook with table and text tabs
        lfOperation = ttk.Labelframe(
            master=lframe,
            text="操作区",
            padding=(10, 5)
        )
        lfOperation.pack(fill=BOTH, expand=YES)

        operationStr = '软件名为:FuckYsPlot 软件版本：' + version + \
                       '该软件为免费使用，如果您花钱够买了那抱歉！\n' + \
                       '欢迎使用原神自动跳剧情工具Hosea制作\n' + \
                       '图像识别模拟鼠标点击，鼠标点击地方也是随机的，不改内存理论上不会有封号的风险。\n' + \
                       '需要右键以管理员身份运行否则无效\n' + \
                       '使用方法:\n' + \
                       '暂时只支持2560*1440分辨率\n' + \
                       '图像->图像质量为：中      |       显示模式:2560x1440'
        ttk.Label(lfOperation, text=operationStr).pack(pady=5, fill=X)

        btn_group = ttk.Labelframe(
            master=rframe,
            text="功能开关",
            padding=(10, 10),
        )
        btn_group.pack(fill=X, pady=10)
        cb1 = ttk.Checkbutton(
            master=btn_group,
            text="开启过剧情",
            bootstyle=(SUCCESS, ROUND, TOGGLE),
            variable=self.isFuckPlot
        )
        # cb1.invoke()
        # cb1.invoke()
        cb1.pack(fill=X, pady=5)
        cb2 = ttk.Checkbutton(
            master=btn_group,
            text="开启点击自动探索和自动结束(开发中...)",
            bootstyle=(SUCCESS, ROUND, TOGGLE),

        )
        cb2.pack(fill=X, pady=5)
        cb3 = ttk.Checkbutton(
            master=btn_group,
            text="自动F拾取物品(开发中...)",
            bootstyle=(SUCCESS, ROUND, TOGGLE),

        )
        cb3.pack(fill=X, pady=5)
        cb4 = ttk.Checkbutton(
            master=btn_group,
            text="辅助强化+4胚子(开发中...)",
            bootstyle=(SUCCESS, ROUND, TOGGLE),

        )
        cb4.pack(fill=X, pady=5)
        # cb.config.text="123456"

        return root

    def on_start(self):
        global thread  # 引用全局变量
        print("开始。。")
        print(self.isFuckPlot.get())
        self.runStateStr.set("软件运行中...")
        self.runState_ui.configure(foreground='#00ff00')
        # 创建线程池
        if not thread or not thread.is_alive():  # 检查是否已经存在线程
            # 创建线程并启动
            if self.isFuckPlot.get():
                yf.isPlotRun = True
            else:
                yf.isPlotRun = False

            print('fuck%b', yf.isPlotRun)
            thread = threading.Thread(target=yf.startFuck)
            thread.start()
        else:
            print('已存在线程')

    def on_pause(self):
        print('暂停')
        self.runStateStr.set("软件已停止")
        self.runState_ui.configure(foreground= '#ff0000')
        yf.isPlotRun = False
        global thread  # 引用全局变量
        if thread and thread.is_alive():
            # thread.join()
            thread = None
        print('已暂停')

    def on_exit(self):
        sys.exit("See you !")


def on_press(key):
    # 当按键按下时，调用此函数。
    print(f'{key.name} is pressed')
    if key.name == 'f10':
        fui.on_start()

    if key.name == 'f11':
        fui.on_pause()


if __name__ == '__main__':
    app = ttk.Window("FuckYSPlot")
    # 在原神窗口中启动监听器
    keyboard.on_press(on_press)
    # keyboard.on_release(on_release)
    yf = YsFuck(True)
    fui = FuckerUI(app)
    app.mainloop()
