import sys,requests,json,time,os
from path import*
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)
with open('version.json','r') as r:
    ver = json.load(r)
    version = ver['ver_']
strartpy  = """\nPserverNA(Anti - captcha) VERSION ("""+version+""")
Note: PserverNA is an custom client and intelligent automated assistant for Playservern.in.th
SUPORT : https://discord.gg/ZyPsMS
website : https://github.com/syntaxp/PserverNA\n"""
checkver = requests.get(path.version).json()
if version != checkver['ver_']:
    print('PATH UPDATE NEW VERSION : '+checkver['ver_'] )
    print('Note Update : ' + checkver['Note_'])
    data_anti = requests.get(path.data_anti).content
    time.sleep(0.2)
    requests_A = requests.get(path.requests_A).content
    time.sleep(0.2)
    data = requests.get(path.data).content
    time.sleep(0.2)
    DELAY = requests.get(path.DELAY).content
    time.sleep(0.2)
    Playserver = requests.get(path.Playserver).content
    time.sleep(0.2)
    requests_P = requests.get(path.requests_P).content
    time.sleep(0.2)
    Proxy_checker = requests.get(path.ProxyChecker).content
    time.sleep(0.2)
    datasmuf = {
        data_anti : "Anticapcha_/data_anti.py",
        requests_A : "Anticapcha_/requests_A.py",
        data : "Playserver_/data.py",
        DELAY : "Playserver_/DELAY.py",
        Playserver : "Playserver_/Playserver.py",
        requests_P : "Playserver_/requests_P.py",
    }
    for pathx in datasmuf:
        with open(datasmuf[pathx],'wb') as w:
            print('UPDATE :' +datasmuf[pathx])
            w.write(pathx)
    with open('version.json','w') as wilr:
        json.dump(checkver,wilr)
    restart_program()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


sys.path.insert(0, "Playserver_/")
from Playserver import *
sys.path.insert(0, "ProxyChecker/")
from Proxy_checker import Proxychecker
if __name__ == '__main__':
    cls()
    print(strartpy)
    print('[0] ProxyChecker \n[1] PserverNA Anticapcha')
    b = input('Call function : ')
    if b == '0':
        cls()
        print('[ProxyChecker Mode]')
        Proxychecker()
    elif b == '1':
        cls()
        print('[Anticapcha Mode]')
        POST_ANTICAPTCHA()
    else:
        print('[' +b+' ] this not commands list ...')
