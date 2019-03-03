import base64, requests, os, json, threading,time,sys,re
from data import proxy,USEprivate,PASSprivate,private,titlechang,logger,key,server_id,userid,logger,failvote,maxvote
from requests import*
from colorama import init, Fore, Back, Style
from requests_P import GETIMAGE,POSTIMAGE
from DELAY import *
sys.path.insert(0, "Anticapcha_/")
from requests_A import GETCAPCHA,reportIncorrectImageCaptcha
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
                for Iproxy in proxylist:
                    public_proxy = {'http': ('http://'+Iproxy),
                               'https': ('https://'+Iproxy)}
                    #setmode
                    public_ = 0
                    #start threading
                    threading.Thread(target = PserverNA, args = (self,public_proxy,public_)).start()
                    self.proxywork += 1
            if int(private) == 1:
                with open('control/private.txt','r') as loadVPN:
                    privatelist = loadVPN.read().splitlines()
                    for Pproxy in privatelist:
                        private_proxy = {'http': ('http://'+USEprivate+':'+PASSprivate+'@'+Pproxy),
                                    'https': ('http://'+USEprivate+':'+PASSprivate+'@'+Pproxy)}
                        private_ = 1
                        self.proxywork += 1
                        threading.Thread(target = PserverNA, args = (self,private_proxy,private_)).start()
                        e.wait(timeout=0.2)

        def PserverNA(self,proxyX,moade):
            My_proxy = re.findall( r'[0-9]+(?:\.[0-9]+){3}', proxyX['http'] )
            if int(moade) == 1:
                My_proxy = (str(My_proxy)+' [ VPN ]')
            DELAY = 0
            PRoxyDie = 0
            startloop = 0
            waitkick = 0
            e = threading.Event()
            while startloop == 0:
                #set name
                titlechang(self)
                try:
                    IMAGE = GETIMAGE(proxyX)
                    if IMAGE != 0:
                        captcha = GETCAPCHA(key,IMAGE['base64'])
                        if captcha['status'] != False:
                            MYSLEEP = SLEEPDELAY(DELAY)
                            DELAY = 0
                            e.wait(timeout=MYSLEEP)
                            MYSLEEP = 0
                            Playload_ = {"server_id":server_id,"captcha": captcha['text'], "gameid": userid, "checksum": IMAGE['id']}
                            vote = POSTIMAGE(self,Playload_,proxyX)
                            DELAY = SETDELAY(vote['wait'])
                            if vote['status'] == True:
                                log = logger.format(My_proxy,IMAGE['id'],captcha['text'],vote['status'],vote['wait'],vote['error_mesg'])
                                print(Fore.GREEN+log, flush=True)
                                print(Style.RESET_ALL, flush=True)
                            if vote['status'] == False:
                                log = logger.format(My_proxy,IMAGE['id'],captcha['text'],vote['status'],vote['wait'],vote['error_mesg'])
                                print(Fore.YELLOW+log, flush=True)
                                print(Style.RESET_ALL, flush=True)
                                waitkick += 1
                                if waitkick > int(failvote):
                                    self.proxywork -=1
                                    startloop = 1
                            else:
                                if vote['error_mesg'] == 'b4ecb33fc4dd1515eae17c9afcf8b90d': #The image has expired or has been used.
                                    log = logger.format(My_proxy,IMAGE['id'],captcha['text'],vote['status'],vote['wait'],vote['error_mesg'])
                                    print(Fore.RED+log, flush=True)
                                    print(Style.RESET_ALL, flush=True)
                                    self.proxywork -= 1
                                    startloop = 1
                                else:
                                    if vote['error_mesg'] == '47b84f936cfa1a104fa5d44821639363': # The code in the image is incorrect.
                                        reprot = reportIncorrectImageCaptcha(key,captcha['taskId'])
                                        if reprot['errorId'] == 0:
                                            log = logger.format(My_proxy,IMAGE['id'],captcha['text'],vote['status'],vote['wait'],vote['error_mesg'])
                                            print(Fore.RED+log, flush=True)
                                            print(Style.RESET_ALL, flush=True)
                        else:
                            PRoxyDie += 1
                            if PRoxyDie > 10:
                                print(('{0} thsi proxy has error 101').format(My_proxy))
                                self.proxywork -= 1
                                startloop = 1
                    else:
                        PRoxyDie += 1
                        if PRoxyDie > 10:
                            print(('{0} thsi proxy has error 102').format(My_proxy))
                            self.proxywork -= 1
                            startloop = 1
                except:
                    PRoxyDie += 1
                    if PRoxyDie > 10:
                        print(('{0} thsi proxy has error 103').format(My_proxy))
                        self.proxywork -= 1
                        startloop = 1

                if self.true > int(maxvote):
                    startloop += 1
        run(self)

if __name__=='__main__':

    POST_ANTICAPTCHA()
