# -*- coding: utf-8 -*-

import time
import glob
import datetime
import traceback
import itertools
from threading import Thread

from xiyouhelper.tray import SysTrayIcon
from xiyouhelper.disable_system_proxy import disable_proxy
from xiyouhelper.hide_window import hide_self, show_self


def show_window(sysTrayIcon):
    show_self()


def hide_window(sysTrayIcon):
    hide_self()


def start(sysTrayIcon):
    if not control["run"]:
        control["run"] = True
        print("已启动")
    else:
        print("运行中，无需操作")


def stop(sysTrayIcon):
    if control["run"]:
        control["run"] = False
        print("已暂停")
    else:
        print("暂停中，无需操作")


def bye(sysTrayIcon): 
    print('Bye.')


def run_once(sysTrayIcon=None):
    print("-*-" * 10)
    print("Datetime: %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("Running: %s" % control["run"])
    if control["run"]:
        try:
            disable_proxy()
        except:
            print(traceback.format_exc())


def run():
    while True:
        run_once()
        time.sleep(60)


control = {"run": True}
t = Thread(target=run)
t.setDaemon(True)
t.start()
icons = itertools.cycle(glob.glob('*.ico'))
hover_text = "西游代理辅助 - 周期性关闭系统代理"
menu_options = (
    ('运行一次', next(icons), run_once),
    ('启动', next(icons), start),
    ('暂停', next(icons), stop),
    ('显示', next(icons), show_window),
    ('隐藏', next(icons), hide_window),
)
SysTrayIcon(next(icons), hover_text, menu_options, on_quit=bye, default_menu_index=1)
