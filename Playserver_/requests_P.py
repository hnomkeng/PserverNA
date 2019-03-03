import requests, json, base64, os, time, hashlib, binascii, threading
from data import url_image, url_submitpic, header, url_getpic

def GETIMAGE(proxy):
    try:
        requestid = (requests.post(url_getpic, headers=header, proxies=proxy)).json()
        IMAGE_ID = requestid['checksum']
        IMAGECT = requests.post(url_image + IMAGE_ID, headers=header, proxies=proxy)
        base64pic = base64.b64encode(IMAGECT.content).decode('utf-8')
        if base64pic.find('iVBORw0KGgoAAAANSUhE') > -1:
            IMAGE = {'id':IMAGE_ID,
             'base64':base64pic}
            return IMAGE
    except:
        return 0


def POSTIMAGE(votedata, proxy):
    for timeout in range(60):
        try:
            vote = (requests.post(url_submitpic, headers=header, data=votedata, proxies=proxy)).json()
            if vote['success'] == True:
                self.true += 1
                datax = {'status':True,  'wait':vote['wait'],  'error_mesg':0}
                return datax
                if vote['wait'] != 0:
                    self.fail += 1
                    erro_message = vote['error_msg'].encode('utf8').hex()
                    md5_error = hashlib.md5(binascii.unhexlify(erro_message)).hexdigest()
                    datax = {'status':False,  'wait':vote['wait'],  'error_mesg':md5_error}
                    return datax
                    self.fail += 1
                    erro_message = vote['error_msg'].encode('utf8').hex()
                    md5_error = hashlib.md5(binascii.unhexlify(erro_message)).hexdigest()
                    datax = {'status':'error_mesg',  'error_mesg':md5_error,  'wait':vote['wait']}
                    return datax
        except:
            e = threading.Event()
            e.wait(timeout=1)
