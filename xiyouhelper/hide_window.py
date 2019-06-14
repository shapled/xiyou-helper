# -*- coding: utf-8 -*-

import os

import win32gui
import win32process

# self_pid = os.getpid()
parent_pid = os.getppid()
hidden = {"hwnd": None}


def enumWindowFunc(hwnd, my_windows):
    """ win32gui.EnumWindows() callback """
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    if pid == parent_pid:
        my_windows.append(hwnd)


def hide_self():
    if not hidden["hwnd"]:
        hwnds = []
        win32gui.EnumWindows(enumWindowFunc, hwnds)
        if not hwnds:
            print("Didn't find self-window.")
            return
        hidden["hwnd"] = hwnds[0]
        win32gui.ShowWindow(hidden["hwnd"], False)


def show_self():
    if hidden["hwnd"]:
        win32gui.ShowWindow(hidden["hwnd"], True)
        hidden["hwnd"] = None


if __name__ == "__main__":
    import time

    print("我要消失了")
    time.sleep(1)
    hide_self()
    time.sleep(2)
    show_self()
    print("我又出现了")
    input("按任意键继续")
