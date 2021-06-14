#tools_main
#MIT Licenses
#By Lijun_Network_Studio
#Made by fanjun

from tools import pym_install
from tools import shutdown
from tools import KMS

print('''
功能选择：
1.定时关机
2.python模块安装
3.win10系统激活
''')

s=input()

if s=='1':
    con=input("""
    1.关机
    2.取消任务
    请输入任务：""")
    if con=='1':
        time=input('请输入时间：')
        shutdown.shutdown(con,time)
    else:
        shutdown.shutdown(con,0)


elif s=='2':
    con=input('''
    1.安装
    2.升级
    请输入安装类型：''')
    pym_install.installer(con)

elif s=='3':
    con=input('''
    1.win10 edu 教育版
    2.win10 ltsc 缩减版
    3.win10 ltsb 阉割版
    4.win10 ltd 企业版
    5.win10 专业版
    6.win10 home 家庭版
    请选择对应系统：''')
    KMS.kmswin10(con)