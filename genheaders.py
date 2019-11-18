# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 19:47:53 2019

@author: pNser copy from CSDN https://blog.csdn.net/u011648373/article/details/82979478
"""
def genHeader(s):

    ls = s.split('\n')
    
    lsl = []
   
    headers = {}
    
    for l in ls:
        
        l = l.split(': ')
        lsl.append(l)
        
    for x in lsl:
        
        headers[str(x[0]).strip('    ')] = x[1]
        
    return headers

if __name__ == "__main__":
    
    s = '''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
Cookie: BAIDUID=85413135F7A889310C951EB2199B430D:FG=1; BIDUPSID=85413135F7A889310C951EB2199B430D; PSTM=1566826294; Hm_lvt_35d1e71f4c913c126b8703586f1d2307=1567695145,1568209244,1568806917; Hm_lpvt_35d1e71f4c913c126b8703586f1d2307=1568809897
Host: gupiao.baidu.com
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'''
        
    print(genHeader(s))