import requests,sys,os,re
import threading
sys.path.insert(0, "Playserver_/")
from requests_P import GETIMAGE
e = threading.Event()
class Proxychecker:
    def __init__(self):
        self.method_1()
    def method_1(self):
        def run(self):
            with open('ProxyChecker/list.txt','r') as loadsproxy:
                proxylist = loadsproxy.read().splitlines()
                for Iproxy in proxylist:
                    public_proxy = {'http': ('http://'+Iproxy),
                               'https': ('https://'+Iproxy)}
                    threading.Thread(target = checkproxy, args = (self,public_proxy)).start()
        def checkproxy(self,proxyX):

            barbarpoxy = re.findall( r'[0-9]+(?:\.[0-9]+){3}.+', proxyX['http'] )
            p = re.search(("'(.+?)'"),str(barbarpoxy))
            h = p.group(1)
            fail_check = 0
            checkstatus = 0
            while checkstatus == 0:
                IMAGE = GETIMAGE(proxyX)
                if IMAGE != 0:
                    with open('control/proxylist.txt','r') as checkproxy_mad:
                        mad_proxy = checkproxy_mad.read().splitlines()
                        if h not in mad_proxy:
                            with open('control/proxylist.txt','a') as w:
                                w.write(h+'\n')
                                print(('{0} this proxy working').format(h))
                                checkstatus += 1
                        else:
                            checkstatus += 1
                else:
                    fail_check += 1
                    if fail_check >= 3:
                        checkstatus += 1


        run(self)
