
<p align="center">
  <a href="https://github.com/syntaxp/PserverNA">
    <img src="https://user-images.githubusercontent.com/47280575/54013280-1b047200-41ab-11e9-8419-7d478f197228.png" alt="PserverNA logo" width="72" height="72">
  </a>
</p>
<h3 align="center">PserverNA</h3>

<p align="center">
  PserverNA is an custom client and intelligent automated assistant for Playservern.in.th
  <br>
   <a href="https://discord.gg/Mgu73TN">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSakv86QJPY-E6rxMEo_WzAwYUzyndjdY_d-Zu2ZOr9UuMjClxy5A" alt="discord logo" width="45" height="45">
  <a href="https://discord.gg/Mgu73TN">Discord</a>
   ·
       <a href="https://www.facebook.com/deerek.kantisriyanon.9">Facebook</a>
</p>

## คู่มือ การใช้งาน

- [Quick start](#quick-start)
- [การทำงานเบื้องต้นของโปรแกรม](Basic-work)
- [การตั่งค่า config.txt](#config)


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

