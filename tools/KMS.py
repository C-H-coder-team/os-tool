#KMS_activation_windows10_tools
#MIT Licenses
#By Lijun_Network_Studio
#Made by fanjun

import os
def kmswin10(con):
    
    cmd1='slmgr /ipk '
    cmd2='slmgr /skms kms.03k.org'
    cmd3='slmgr /ato'

    key1='NW6C2-QMPVW-D7KKK-3GKT6-VCFB2'
    key2='M7XTQ-FN8P6-TTKYV-9D4CC-J462D'
    key3='DCPHK-NFMTC-H88MJ-PFHPY-QJ4BJ'
    key4='NPPR9-FWDCX-D2C8J-H872K-2YT43'
    key5='W269N-WFGWX-YVC9B-4J6C9-T83GX'
    key6='37GNV-YCQVD-38XP9-T848R-FC2HD'

    if con=='1':
        res1 = os.popen(cmd1+key1)
        output_str1 = res1.read()
        print(output_str1)
        print('密钥安装完毕！')
        res2 = os.popen(cmd2)
        output_str2 = res2.read()
        print(output_str2)
        print('KMS服务器已指定kms.03k.org')
        res3 = os.popen(cmd3)
        output_str3 = res3.read()
        print(output_str3)
        print('安装完毕！')

    elif con=='2':
        res1 = os.popen(cmd1+key2)
        output_str1 = res1.read()
        print(output_str1)
        print('密钥安装完毕！')
        res2 = os.popen(cmd2)
        output_str2 = res2.read()
        print(output_str2)
        print('KMS服务器已指定kms.03k.org')
        res3 = os.popen(cmd3)
        output_str3 = res3.read()
        print(output_str3)
        print('安装完毕！')

    elif con=='3':
        res1 = os.popen(cmd1+key3)
        output_str1 = res1.read()
        print(output_str1)
        print('密钥安装完毕！')
        res2 = os.popen(cmd2)
        output_str2 = res2.read()
        print(output_str2)
        print('KMS服务器已指定kms.03k.org')
        res3 = os.popen(cmd3)
        output_str3 = res3.read()
        print(output_str3)
        print('安装完毕！')

    elif con=='4':
        res1 = os.popen(cmd1+key4)
        output_str1 = res1.read()
        print(output_str1)
        print('密钥安装完毕！')
        res2 = os.popen(cmd2)
        output_str2 = res2.read()
        print(output_str2)
        print('KMS服务器已指定kms.03k.org')
        res3 = os.popen(cmd3)
        output_str3 = res3.read()
        print(output_str3)
        print('安装完毕！')

    elif con=='5':
        res1 = os.popen(cmd1+key5)
        output_str1 = res1.read()
        print(output_str1)
        print('密钥安装完毕！')
        res2 = os.popen(cmd2)
        output_str2 = res2.read()
        print(output_str2)
        print('KMS服务器已指定kms.03k.org')
        res3 = os.popen(cmd3)
        output_str3 = res3.read()
        print(output_str3)
        print('安装完毕！')

    elif con=='6':
        res1 = os.popen(cmd1+key6)
        output_str1 = res1.read()
        print(output_str1)
        print('密钥安装完毕！')
        res2 = os.popen(cmd2)
        output_str2 = res2.read()
        print(output_str2)
        print('KMS服务器已指定kms.03k.org')
        res3 = os.popen(cmd3)
        output_str3 = res3.read()
        print(output_str3)
        print('安装完毕！')