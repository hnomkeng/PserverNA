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
strartpy  = """\n    PserverNA(Anti - captcha) VERSION ("""+version+""")
    Note: PserverNA is an custom client and intelligent automated assistant for Playservern.in.th
    SUPORT : https://discord.gg/ZyPsMS
    website : https://github.com/syntaxp/PserverNA"""
checkver = requests.get(path.version).json()
if version != checkver['ver_']:
    print('PATH UPDATE NEW VERSION : '+checkver['ver_'] )
    init_anti = requests.get(path.init_anti).content
    time.sleep(0.5)
    config_anti = requests.get(path.config_anti).content
    time.sleep(0.5)
    request_anti = requests.get(path.request_anti).content
    time.sleep(0.5)
    init_pay = requests.get(path.init_pay).content
    time.sleep(0.5)
    delay_pay = requests.get(path.delay_pay).content
    time.sleep(0.5)
    Playserver_pay = requests.get(path.Playserver_pay).content
    time.sleep(0.5)
    config_pay = requests.get(path.config_pay).content
    time.sleep(0.5)
    request_pay = requests.get(path.request_pay).content
    data = {
        init_anti : "python3_anticaptcha/__init__.py",
        config_anti : "python3_anticaptcha/config.py",
        request_anti : "python3_anticaptcha/request_anitcapcha.py",
        init_pay : "python3_playserver/__init__.py",
        delay_pay : "python3_playserver/DELAY.py",
        Playserver_pay : "python3_playserver/Playserver.py",
        config_pay : "python3_playserver/config.py",
        request_pay : "python3_playserver/request_playserver.py"
    }
    for pathx in data:
        with open(data[pathx],'wb') as w:
            print('UPDATE :' +data[pathx])
            w.write(pathx)
    with open('version.json','w') as wilr:
        json.dump(checkver,wilr)
    restart_program()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

from python3_playserver import Playserver

if __name__=='__main__':
    cls()
    print(strartpy)
    Playserver.POST_ANTICAPTCHA()
