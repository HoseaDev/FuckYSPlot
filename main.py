import os
import random
import sys
import threading
import time

import keyboard
import pyautogui

# 软件开始


def main():
    print('欢迎使用原神自动跳剧情工具Hosea制作')
    print('如需其他定制VX:HoseaDev')
    print('图像识别模拟鼠标点击，鼠标点击地方也是随机的，不改内存不会有封号的风险。')
    print('需要右键以管理员身份运行否则无效！！！')
    print('需要右键以管理员身份运行否则无效！！！')
    print('需要右键以管理员身份运行否则无效！！！')
    print('使用方法:')
    print('暂时只支持2560*1440分辨率')
    print('暂时只支持2560*1440分辨率')
    print('图像->图像质量为：中      |       显示模式:2560x1440独占全屏')
    print('按F10开始   按F11停止  按F12退出')
    # 在原神窗口中启动监听器
    keyboard.on_press(on_press)
    # keyboard.on_release(on_release)
    keyboard.wait('f12')
    print('end!!')


def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def randomSleep():
    t = random.randint(1, 3)
    time.sleep(t)
    print('睡眠了 %s 秒' % t)


def clickDialog(dl):
    # 如果找到了，则获取其中心坐标并鼠标移动到其上方
    print('点击对话')
    print(dl)
    time.sleep(0.3)
    # pyautogui.moveTo(image_center)
    pyautogui.click(dl)

def generateRandomLocation():
    x = random.randint(200, 1600)
    y = random.randint(100, 1100)
    return x, y


def startFuck():
    pyautogui.FAILSAFE = True  # 启用自动防故障功能，左上角的坐标为（0，0），将鼠标移到屏幕的左上角，来抛出failSafeException异常
    width, height = pyautogui.size()  # 屏幕的宽度和高度
    print(width, height)
    # 在指定区域内查找图像
    global is_run
    while is_run:
        # 当在原神中的时候才开始找图
        if '原神' in pyautogui.getActiveWindowTitle():
            # print('当前原神窗口 %s' % threading.current_thread().name)
            # time.sleep(1)
            # print(is_run)
            # 查找头像如果有图像剧情结束
            avatarLocation = pyautogui.locateOnScreen(get_resource_path(
                "./images/avatar.png"), region=(60, 50, 20, 20), confidence=0.8)
            # 没有进入剧情什么都不做
            if avatarLocation is not None:
                print('找到头像。')
                time.sleep(1)
                continue

                # 查找头像如果有图像剧情结束
            plotStartLocation = pyautogui.locateOnScreen(get_resource_path(
                "./images/plot_start.png"), region=(84, 48, 25, 33), confidence=0.8)
            if plotStartLocation is not None:
                # 如果找到了，则获取其中心坐标并鼠标移动到其上方
                print('进入剧情模式...')
                time.sleep(0.3)
                # 随机点击
                pyautogui.click(generateRandomLocation())
                dialogLocation = pyautogui.locateOnScreen(get_resource_path(
                    "./images/dialog.png"), region=(1688, 739, 69,393), confidence=0.7)
                dialogLocation2 = pyautogui.locateOnScreen(get_resource_path(
                    "./images/dialog2.png"), region=(1689, 749,  69,393), confidence=0.7)
                if dialogLocation is not None:
                   clickDialog(dialogLocation)
                elif dialogLocation2 is not None:
                   clickDialog(dialogLocation2)

        else:
            time.sleep(2)
            print('当前活动窗口不是原神')


class Fucker(threading.Thread):
    def run(self):
        global is_run
        is_run = True
        # print('start fuck')
        startFuck()
        pass


def on_press(key):
    # 当按键按下时，调用此函数。
    # print(f'{key.name  } is pressed')
    if key.name == 'f10':
        print('开启软件')
        fucker = Fucker()
        fucker.start()


    if key.name == 'f11':
        global is_run
        is_run = False
        print('暂停')
    # if key.name == 'f12':
    #     global  is_run
    #     is_run = False
    #
    #     print('终止')


is_run = False
# 监听按键事件
# 检查当前窗口是否为原神窗口，如果是，开始监听按键
if __name__ == '__main__':
    main()

