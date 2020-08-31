import os
import time
os.system('@Rasdial 宽带连接 /DISCONNECT') # 先断开宽带连接（这个宽带连接是你的网络名字，可以叫做别的）
# 然后重新拨号
with open('u_a_p.txt','r') as f:
    cfg = f.read()
n = cfg.split('\n')[0]
u = cfg.split('\n')[1]
p = cfg.split('\n')[2]
order = '@Rasdial {} {} {}'.format(n,u,p)

os.system(order)
# 检查是否连接，已经连接就退出
res = os.system('ping 8.8.8.8')
if not res :
    print('连接成功')
