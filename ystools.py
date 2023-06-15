import os
import random
import sys
import threading

import pyautogui
import time


class YsFuck:
    def __init__(self, isPlotRun):
        self.isPlotRun = isPlotRun

    def generateRandomLocation(self):
        x = random.randint(200, 1600)
        y = random.randint(100, 850)
        return x, y

    def get_resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

    def startFuck(self):
        pyautogui.FAILSAFE = True  # 启用自动防故障功能，左上角的坐标为（0，0），将鼠标移到屏幕的左上角，来抛出failSafeException异常
        width, height = pyautogui.size()  # 屏幕的宽度和高度
        print(width, height)
        # 在指定区域内查找图像
        while self.isPlotRun:
            # 当在原神中的时候才开始找图
            if '原神' in pyautogui.getActiveWindowTitle():
                print('当前原神窗口 %s' % threading.current_thread().name)
                # time.sleep(1)
                # print(is_run)
                # 查找头像如果有图像剧情结束
                avatarLocation = pyautogui.locateOnScreen(self.get_resource_path(
                    "./images/avatar.png"), region=(60, 50, 20, 20), confidence=0.8)
                # 没有进入剧情什么都不做
                if avatarLocation is not None:
                    print('找到头像。')
                    time.sleep(1)
                    continue

                    # 查找头像如果有图像剧情结束
                plotStartLocation = pyautogui.locateOnScreen(self.get_resource_path(
                    "./images/plot_start.png"), region=(84, 48, 25, 33), confidence=0.8)
                if plotStartLocation is not None:
                    # 如果找到了，则获取其中心坐标并鼠标移动到其上方
                    print('进入剧情模式...')
                    time.sleep(0.3)
                    # 随机点击
                    (x,y)= self.generateRandomLocation()
                    print('x=%s',x)
                    print('y=%s',y)
                    pyautogui.click(x=x, y=y)
                    # pyautogui.moveTo(0,0)
                    dialogLocation = pyautogui.locateOnScreen(self.get_resource_path(
                        "./images/dialog.png"), region=(1688, 739, 69, 393), confidence=0.7)
                    dialogLocation2 = pyautogui.locateOnScreen(self.get_resource_path(
                        "./images/dialog2.png"), region=(1689, 749, 69, 393), confidence=0.7)
                    if dialogLocation is not None:
                        self.clickDialog(dialogLocation)
                    elif dialogLocation2 is not None:
                        self.clickDialog(dialogLocation2)

            else:
                time.sleep(2)
                # pyautogui.click(50,50)
                print('当前活动窗口不是原神  %s', threading.current_thread().name)

    def clickDialog(self, dl):
        # 如果找到了，则获取其中心坐标并鼠标移动到其上方
        print('点击对话')
        print(dl)
        time.sleep(0.3)

        # pyautogui.moveTo(image_center)
        pyautogui.click(dl)
