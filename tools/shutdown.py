#shutdown_tools
#MIT Licenses
#By Lijun_Network_Studio
#Made by fanjun

import os

def shutdown(set,time):
    if set=='1':
        cmd = 'shutdown /s /t '
        res = os.popen(cmd+time)
        output_str = res.read()   # 获得输出字符串
        print(output_str)
    else:
        cmd = 'shutdown /a'
        res = os.popen(cmd)
        output_str = res.read()   # 获得输出字符串
        print(output_str)