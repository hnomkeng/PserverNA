
<p align="center">
  <a href="https://github.com/syntaxp/PserverNA">
    <img src="https://user-images.githubusercontent.com/47280575/54013280-1b047200-41ab-11e9-8419-7d478f197228.png" alt="PserverNA logo" width="72" height="72">
  </a>
</p>
<h3 align="center">PserverNA</h3>

<p align="center"> 
  PserverNA เป็นเพียงซอฟแวร์ที่ให้บริการเชื่อมต่อ API ของAntiCaptcha กับ เว็ป Playserver เราไม่มีการเรียกเก็บเงินใดๆ
  เพียงแต่ผู้ใช้จำเป็นต้องเช่า KEY ของเว็ป AntiCaptcha เพื่อใช้บริการ แกะรหัส รูปภาพ เราไม่มีส่วนเกี่ยวของ กับ AntiCaptcha ในทางใดทั้งสิ้น
  <br>

   <a href="https://discord.gg/Mgu73TN">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSakv86QJPY-E6rxMEo_WzAwYUzyndjdY_d-Zu2ZOr9UuMjClxy5A" alt="discord logo" width="45" height="45">
  <a href="https://discord.gg/Mgu73TN">Discord</a>
   ·
       <a href="https://www.facebook.com/deerek.kantisriyanon.9">Facebook</a>
</p>

## คู่มือ การใช้งาน

- [Quick start](#quick-start)
- [การทำงานเบื้องต้นของโปรแกรม](#basic-work)
- [KEY](#key)
- [การตั่งค่า config.txt](#config)
- [Proxylist.txt](#proxy)
- [Private Proxy](#private-proxy)
- [Proxy Checker](#proxy-checker)

## Quick start
- [Download the latest release.](https://github.com/syntaxp/PserverNA/archive/master.zip)
- สมัครสมาชิก [anti-captcha.com](http://getcaptchasolution.com/e80kqlwlmw) 



## Basic work

```text
PserverN
|
└──> ดึงข้อมูลจาก / Playserver.in.th
        ├── รหัสรูปภาพ, รูปภาพ 
        | 
        └── > ส่งต่อรูปภาพต่อไปยัง / anti-captcha.com
                   ├── แกะรหัสรูปภาพ
                   |
                   └──> ส่งกลับมาที่ PserverN ──> ส่งคำตอบไปยัง Playserver.in.th
                            
```


## Key
KEY จะถูกสร้างให้อัตโนมัติ หลังจากที่เราเป็นสมาชิกของ ของ [anti-captcha.com](http://getcaptchasolution.com/e80kqlwlmw) 

สามารถเช็ค key ของตัวเองได้ที่ [apisetup](https://anti-captcha.com/clients/settings/apisetup) (`* ต้อง login ก่อนถึงจะเข้าชมหน้าเว็ปได้`)

![key](https://user-images.githubusercontent.com/47280575/54017688-5d34b000-41b9-11e9-9840-cbbcb38cf9f8.png)


## Config
**การตั่งค่า  [config.txt](https://github.com/syntaxp/PserverNA/blob/master/control/config.txt)**

```python
[default]
key_anticap = # key ของ Anticaptcha
server_id = # sever id ตัวอย่าง url <playserver.in.th/index.php/Vote/prokud/PserverN-15282> id sever คือ 15282
userid  = #user id ของเกม
proxy = proxylist.txt # ไฟล์ที่ทำการเก็บ List proxy ไว้

[private] # ระะบบ private proxy หรือ proxy ที่เช่าจากเว็ป
private = # 0 = ปิด 1 = เปิด
USER = #user ของเว็ปที่เช่า (ส่วนมากใช่เป็น email)
PASS = #pssword ของเว็ปที่เช่า

[option]
maxvote = # จำนวนโหวตที่ต้องการ ควรมากกว่ ip ที่มีใน list
failvote = # จำนวนครั้งที่ ip โหวตพลาด ระบบจะเตะ ip ออก
requestfail = # จำนวครั้งที่ ip พยามเชื่อมต่อไม่สำเร็จ ระบบจะเตะ ip ออก
requesttimeout = # ระยะเวลาในการทำงานเรียกข้อมูล ส่งข้อมูล ควรตั่งให้มากกว่า 3 ขึ้นไป
```
***example: config.txt***
```java
[default]
key_anticap = d2ed549112be82d92add5c9bf7f1cb57
server_id = 15282
userid  = pserverna
proxy = proxylist.txt

[private] 
private = 0
USER = off
PASS = off

[option]
maxvote = 1000
failvote = 3
requestfail = 10
requesttimeout = 3
```
## Proxy
**[proxylist.txt](https://github.com/syntaxp/PserverNA/blob/master/control/proxylist.txt)**
```text
proxylist.txt จะเป็นไฟล์ txt ที่ใช้สำหรับเก็บรายชื่อ proxy ต่างๆที่ใช้สำหรับโหวต
เนื้องจาก การโหวต Playserver ปกติ เมื่อโหวตสำเร็จ จะติดดีเลเป็นเวล 61 วิ
เราจึงจำเป็นต้องมี proxy ใช้สำหรับโหวตเพิ่มขึ้นเพื่อการทำงานโหวตที่ไวขึ้น
Playserver กำจัดสิทธ์โหวตให้เพียง IP ที่ให้บริการในไทย นั้นหมายความว่า เราเลือกเฉพาะ Proxy ไทยในการโหวต

- สามารถหา Proxy ได้จากไหน ?
proxy จะมี 2 แบบ 
แบบปกติคือแจกตามเว็ปทั่วไปสามารถ search ได้จาก google 'proxy list' , 'proxy list thai'
แบบที่ 2 จะเป็น proxy แบบเช่า ซึ่งจะยกประเด็นนี้ไปในหัวข้อ private proxy

หลังจากที่เราได้ proxy มาแล้วให้เราก๊อปแล้วนำไปวางใน proxylist.txt
```
***example: proxylist.txt***
```text
103.15.140.141:44759
103.15.140.142:44759
103.15.140.177:44759
103.15.226.124:80
103.15.241.161:8080
103.15.245.26:8080
103.15.51.160:8080
103.15.83.73:58486
103.15.83.82:8080
103.16.61.46:52424
103.17.38.24:8080
103.18.243.154:8080
103.18.32.242:46734
103.19.110.177:8080
```

## Private Proxy
**[private.txt](https://github.com/syntaxp/PserverNA/blob/master/control/private.txt)**

**[config.txt](https://github.com/syntaxp/PserverNA/blob/master/control/config.txt)**

```text
ในส่วนของ Private Proxy จะเป็นการรองรับระบบ proxy เช่า ตามเว็ปต่างๆซึ่งมีความส่วนตัวในการใช้
หมายความว่าเวลาเราใช้โหวต proxy จะไม่ไปชนกับคนอื่น แต่ต้องดูด้วยว่าเจ้าของเว็ปที่ให้บริการเช่า ปล่อย proxy เป็นแบบ public สำหรับสมาชิกรึป่าว
การตั่งค่าเราจำเป็นต้องเปิดใช้งานในส่วนของ config.txt หัวข้อ private เป็น 1 และใส่ email หรือ username /pass ที่เราสมัครกับทางเว็ป
```
***example: config.txt***
```java
[private] 
private = 1
USER = pserverna@proxyweb.com
PASS = 12345678
```

```text
ในส่วนของ proxy เราจะเก็บ proxy พวกนี้ไว้ใน private.txt
```
***example: private.txt***
```text
103.15.140.141:44759
103.15.140.142:44759
103.15.140.177:44759
103.15.226.124:80
103.15.241.161:8080
103.15.245.26:8080
103.15.51.160:8080
103.15.83.73:58486
103.15.83.82:8080
103.16.61.46:52424
103.17.38.24:8080
103.18.243.154:8080
103.18.32.242:46734
103.19.110.177:8080
```
## Proxy Checker
proxy checker mode จะเป็นการ เช็ค proxy ที่อยู่ในไฟล์ **[list.txt](https://github.com/syntaxp/PserverNA/blob/master/ProxyChecker/list.txt)**

โดย proxy ที่ใช้งานได้จะถูกเก็บไปยัง ไฟล์ **[proxylist.txt](https://github.com/syntaxp/PserverNA/blob/master/control/proxylist.txt)** อัตโนมัติ

![proxy checker](https://user-images.githubusercontent.com/47280575/54040675-8c1e4680-41f8-11e9-8a7b-79fe3147d1cd.png)


