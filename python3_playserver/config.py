import os ,configparser,requests,re,sys,ctypes
sys.path.insert(0, 'python3_anticaptcha/')
import urllib.parse
from msvcrt import getch
from python3_anticaptcha import GETbalance,GETbalance

loadconfig = configparser.RawConfigParser()
loadconfig.readfp(open(r'control/config.txt'))
key = loadconfig.get('default', 'key_anticap')
userid = loadconfig.get('default', 'userid')
server_id = loadconfig.get('default', 'server_id')
proxy = loadconfig.get('default', 'proxy')
maxvote = loadconfig.get('default','maxvote')
VPN = loadconfig.get('VPN','VPN')
USERVPN = loadconfig.get('VPN','USER')
PASSVPN = loadconfig.get('VPN','PASS')
url_server = ('https://playserver.in.th/index.php/Server/')
url_vote = ("https://playserver.in.th/index.php/Vote/prokud/")
url_image = ("http://playserver.co/index.php/VoteGetImage/")

try:
    rquest_unpack = requests.get(url_server+str(server_id))
    unpack_text = re.search(url_vote+'(.+?)"',rquest_unpack.text)
    unpack_unicode = (unpack_text.group(1))
    unpack_Entities = urllib.parse.quote(unpack_unicode)
except:
    print('\n Please Check you config.txt/[server_id]  !! ')
    junk = getch()
    sys.exit()
url_getpic = ("http://playserver.co/index.php/Vote/ajax_getpic/"+unpack_Entities)
url_submitpic = ("http://playserver.co/index.php/Vote/ajax_submitpic/"+unpack_Entities)
header = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
"Accept-Encoding": "gzip, deflate",
"Referer": (url_vote+unpack_Entities)
}

LOGSET = ('\n PROXY    : {0} \n IMAGE ID : {1}\n CAPTCHA  : {2} \n STATUS   : {3}   DELAY : {4}   REPORT : {5}')
def titlechang(self):
    balance = GETbalance(key)

    if self.true != 0 or self.fail != 0:
        fianl = self.true+self.fail
        self.persen = self.true/fianl*100
    j = (' {0} :  S{1} - Proxy:[ {2} ]  ,True_ ({3}) ,False_ ({4}) ,SUCCESS({5}%),  {6}$   - PserverN').format(userid,server_id,self.proxywork,self.true,self.fail,"%.2f"%self.persen,balance)
    ctypes.windll.kernel32.SetConsoleTitleW(j)
