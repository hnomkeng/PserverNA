import base64, requests, os, json, threading,time,sys,re
from python3_playserver import url_getpic,url_image,header,proxy,GETIMAGE,titlechang,key,userid,server_id,url_submitpic,POSTIMAGE,SETDELAY,SLEEPDELAY,LOGSET,maxvote,VPN,USERVPN,PASSVPN
from colorama import init, Fore, Back, Style
sys.path.insert(0, 'python3_anticaptcha/')
from python3_anticaptcha import GETCAPCHA,reportIncorrectImageCaptcha


class POST_ANTICAPTCHA:

    def __init__(self):
        init(convert=True)
        self.method_1()
    def method_1(self):
        def run(self):
            self.true = 0
            self.fail = 0
            self.persen = 0
            self.proxywork = 0
            with open('control/'+proxy,'r') as loadsproxy:
                proxylist = loadsproxy.read().splitlines()
                for IP in proxylist:
                    self.proxywork += 1
                    proxies = {'http': ('http://'+IP),
                               'https': ('https://'+IP)}
                    proxymoade = 0
                    threading.Thread(target = check_proxy, args = (self,proxies,proxymoade)).start()
            if int(VPN) == 1:
                with open('control/VPN.txt','r') as loadVPN:
                    proxyVPN = loadVPN.read().splitlines()
                    for PVPN in proxyVPN:
                        self.proxywork += 1
                        proxiesVPN = {'http': ('http://'+USERVPN+':'+PASSVPN+'@'+PVPN),
                                    'https': ('http://'+USERVPN+':'+PASSVPN+'@'+PVPN)}
                        vpnmoade = 1
                        threading.Thread(target = check_proxy, args = (self,proxiesVPN,vpnmoade)).start()


        def check_proxy(self,IP,moade):
            myip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', IP['http'] )
            if int(moade) == 1:
                myip = (str(myip)+' [ VPN ]')
            DELAY = 0
            PRoxyDie = 0
            while (self.true < int(maxvote)):
                if PRoxyDie > 3:
                    self.proxywork -= 1
                    return 0
                titlechang(self)
                IMAGE = GETIMAGE(self,IP,url_getpic,url_image,header)
                if IMAGE != 0:
                    captcha = GETCAPCHA(key,IMAGE['base64'])
                    if captcha['status'] != False:
                        MYSLEEP = SLEEPDELAY(DELAY)
                        DELAY = 0
                        e = threading.Event()
                        e.wait(timeout=MYSLEEP)
                        vote_data = {"server_id":server_id,"captcha": captcha['text'], "gameid": userid, "checksum": IMAGE['id']}
                        vote = POSTIMAGE(self,IP,vote_data,url_submitpic,header)
                        DELAY = SETDELAY(vote['wait'])
                        if vote['status'] == True:
                            log = LOGSET.format(myip,IMAGE['id'],captcha['text'],vote['status'],vote['wait'],vote['error_mesg'])
                            print(Fore.GREEN+log, flush=True)
                            print(Style.RESET_ALL, flush=True)
                        elif vote['status'] == False:
                            PRoxyDie += 1
                            log = LOGSET.format(myip,IMAGE['id'],captcha['text'],vote['status'],vote['wait'],vote['error_mesg'])
                            print(Fore.YELLOW+log, flush=True)
                            print(Style.RESET_ALL, flush=True)
                        else:
                            if vote['error_mesg'] == 'b4ecb33fc4dd1515eae17c9afcf8b90d': #The image has expired or has been used.
                                log = LOGSET.format(myip,IMAGE['id'],captcha['text'],vote['status'],vote['wait'],vote['error_mesg'])
                                print(Fore.RED+log, flush=True)
                                print(Style.RESET_ALL, flush=True)
                                break
                            else:
                                if vote['error_mesg'] == '47b84f936cfa1a104fa5d44821639363': # The code in the image is incorrect.
                                    reprot = reportIncorrectImageCaptcha(key,captcha['taskId'])
                                    if reprot['errorId'] == 0:
                                        log = LOGSET.format(myip,IMAGE['id'],captcha['text'],vote['status'],vote['wait'],vote['error_mesg'])
                                        print(Fore.RED+log, flush=True)
                                        print(Style.RESET_ALL, flush=True)

                    else:
                        print('this captcha time out ')
                else:
                    PRoxyDie += 1



        run(self)
