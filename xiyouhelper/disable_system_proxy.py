#-*- coding: utf-8 -*-

import os
import time
import shutil

import win32api
import win32con


def change_ie_proxy(keyName, keyValue):
    pathInReg = r'Software\Microsoft\Windows\CurrentVersion\Internet Settings'
    key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, pathInReg, 0, win32con.KEY_ALL_ACCESS)
    win32api.RegSetValueEx(key, keyName, 0, win32con.REG_DWORD, keyValue)
    win32api.RegCloseKey(key)


def get_proxy_status():
    pathInReg = r'Software\Microsoft\Windows\CurrentVersion\Internet Settings'
    key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, pathInReg, 0, win32con.KEY_ALL_ACCESS)
    value, _ = win32api.RegQueryValueEx(key, 'ProxyEnable')
    print("Proxy status: " + ("opened" if value else "closed"))
    return value


def disable_proxy():
    if get_proxy_status() == 1:
        print("try to close proxy ...")
        change_ie_proxy('ProxyEnable', 0)
        get_proxy_status()
        print("Done.")


if __name__ == "__main__":
    disable_proxy()
    input("按任意键结束")
