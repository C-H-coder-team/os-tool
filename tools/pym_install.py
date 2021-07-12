#python_module_install_tools
#MIT Licenses
#By Lijun_Network_Studio
#Made by fanjun

import os

list = ['pygame','django','flask','tornado','setuptool','pillow','pymongo','mysql-connector','cp','SQLAlchemy','girlfriend','boyfriend','pygal','matplotlib','robot','pyos','cpython','pyftp','line','pyserver','math','download','port','language','geometry','pyapp','pycode','pyhttp','pyline','upload','pyinstaller']
def installer(set):
    if set=='1':
        for l in list:
            cmd = 'pip install '
            res = os.popen(cmd+l)
            output_str = res.read()   # 获得输出字符串
            print(output_str)
    else:
        for l in list:
            cmd = 'pip install -U '
            res = os.popen(cmd+l)
            output_str = res.read()   # 获得输出字符串
            print(output_str)