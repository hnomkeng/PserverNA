```text
PserverNA
└── update 
      └── version.json @ version 2.0.3.2
          ├────── control/config.txt
          |          └── @ option /เพิ่ม หัวข้อ option
          |                     ├── maxvote   / จำนวนโหวตที่ต้องการ ควรมากกว่ ip ที่มีใน list
          |                     ├── failvote  / จำนวนครั้งที่ ip โหวตพลาด ระบบจะเตะ ip ออก
          |                     ├── requestfail  / จำนวครั้งที่ ip พยามเชื่อมต่อไม่สำเร็จ ระบบจะเตะ ip ออก
          |                     └── requesttimeout / ระยะเวลาในการทำงานเรียกข้อมูล ส่งข้อมูล ควรตั่งให้มากกว่า 3 ขึ้นไป
          |
          ├────── main.py & PserverNA.exe 
          |          └──  @ commands /เพิ่ม commands ในการ call function
          |                     ├── 0 = Call Proxy_checker.py
          |                     └── 1 = Call Playserver_/Playserver.py
          |
          |
          |
          └──────── @ ProxyChecker / เพิ่มโฟเดอร์ ProxyChecker
                        ├── @ Proxy_checker.py / เพิ่ม Proxy Checker Mode เช็ค proxy ไหนสามารถใช้งานได้
                        └── @ list.txt         / ไฟล์สำหรับเก็บ proxy ที่ต้องการเช็ค                            
```
