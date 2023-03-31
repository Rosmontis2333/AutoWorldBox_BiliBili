import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
import untitled
import json

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = untitled.Ui_UI_Auto()
    ui.setupUi(MainWindow)
    MainWindow.show()
    import requests
    import time

    with open("config.json") as json_file:
        config = json.load(json_file)
    headers = config['headers']
    cookies = config["cookies"]
    token = cookies["bili_jct"]
    code_073 = headers["content-type"].lstrip("multipart/form-data; boundary=----WebKitFormBoundary")
    thetext = "{thetext}"
    roomid = "25191145"
    time = int(time.time())
    data = f'------WebKitFormBoundary{code_073}\r\nContent-Disposition: form-data; name="bubble"\r\n\r\n0\r\n------WebKitFormBoundary{code_073}\r\nContent-Disposition: form-data; name="msg"\r\n\r\n{thetext}\r\n------WebKitFormBoundary{code_073}\r\nContent-Disposition: form-data; name="color"\r\n\r\n16777215\r\n------WebKitFormBoundary{code_073}\r\nContent-Disposition: form-data; name="mode"\r\n\r\n1\r\n------WebKitFormBoundary{code_073}\r\nContent-Disposition: form-data; name="fontsize"\r\n\r\n25\r\n------WebKitFormBoundary{code_073}\r\nContent-Disposition: form-data; name="rnd"\r\n\r\n{time}\r\n------WebKitFormBoundary{code_073}\r\nContent-Disposition: form-data; name="roomid"\r\n\r\n{roomid}\r\n------WebKitFormBoundary{code_073}\r\nContent-Disposition: form-data; name="csrf"\r\n\r\n{token}\r\n------WebKitFormBoundary{code_073}\r\nContent-Disposition: form-data; name="csrf_token"\r\n\r\n{token}\r\n------WebKitFormBoundary{code_073}--\r\n'
    print(code_073)
    print(token)
    print(cookies)
    print(headers)
    print(time)



    def start():
        global data
        global cookies
        global headers
        target = ui.put_in.text()
        text = f"加入{target}"
        data233 = data.format(thetext=text)
        data_out = data233
        requests.post('https://api.live.bilibili.com/msg/send', cookies=cookies, headers=headers,
                      data=data_out.encode('utf-8'))
        ui.put_in.setText("")


    def xuanzhan():
        global data
        global cookies
        global headers
        target = ui.put_in.text()
        text = f"宣战{target}"
        data233 = data.format(thetext=text)
        data_out = data233.encode("utf-8").decode("latin1")
        requests.post('https://api.live.bilibili.com/msg/send', cookies=cookies, headers=headers, data=data_out)
        ui.put_in.setText("")


    def attack():
        global data
        global cookies
        global headers
        target = ui.put_in.text()
        text = f"进攻{target}"
        data233 = data.format(thetext=text)
        data_out = data233.encode("utf-8").decode("latin1")
        requests.post('https://api.live.bilibili.com/msg/send', cookies=cookies, headers=headers, data=data_out)


    def peace():
        global data
        global cookies
        global headers
        target = ui.put_in.text()
        text = f"和平{target}"
        data233 = data.format(thetext=text)
        data_out = data233.encode("utf-8").decode("latin1")
        requests.post('https://api.live.bilibili.com/msg/send', cookies=cookies, headers=headers, data=data_out)
        ui.put_in.setText("")


    def army():
        global data
        global cookies
        global headers
        target = ui.put_in.text()
        text = f"封将{target}"
        data233 = data.format(thetext=text)
        data_out = data233.encode("utf-8").decode("latin1")
        requests.post('https://api.live.bilibili.com/msg/send', cookies=cookies, headers=headers, data=data_out)
        ui.put_in.setText("")


    def lord():
        global data
        global cookies
        global headers
        target = ui.put_in.text()
        text = f"封侯{target}"
        data233 = data.format(thetext=text)
        data_out = data233.encode("utf-8").decode("latin1")
        requests.post('https://api.live.bilibili.com/msg/send', cookies=cookies, headers=headers, data=data_out)
        ui.put_in.setText("")


    def send():
        global data
        global cookies
        global headers
        target = ui.put_in.text()
        text = f"{target}"
        data233 = data.format(thetext=text)
        data_out = data233.encode("utf-8").decode("latin1")
        requests.post('https://api.live.bilibili.com/msg/send', cookies=cookies, headers=headers, data=data_out)
        ui.put_in.setText("")


    def help():
        global data
        global cookies
        global headers
        target = ui.put_in.text()
        text = f"协助{target}"
        data233 = data.format(thetext=text)
        data_out = data233.encode("utf-8").decode("latin1")
        requests.post('https://api.live.bilibili.com/msg/send', cookies=cookies, headers=headers, data=data_out)
        ui.put_in.setText("")


    def roomid():
        global code_073
        global thetext
        global time
        global token
        global data
        roomid = ui.put_in.text()
        ui.put_in.setText("")
        data = f'------WebKitFormBoundary{code_073}\r\nContent-Disposition: form-data; name="bubble"\r\n\r\n0\r\n------WebKitFormBoundary{code_073}\r\nContent-Disposition: form-data; name="msg"\r\n\r\n{thetext}\r\n------WebKitFormBoundary{code_073}\r\nContent-Disposition: form-data; name="color"\r\n\r\n16777215\r\n------WebKitFormBoundary{code_073}\r\nContent-Disposition: form-data; name="mode"\r\n\r\n1\r\n------WebKitFormBoundary{code_073}\r\nContent-Disposition: form-data; name="fontsize"\r\n\r\n25\r\n------WebKitFormBoundary{code_073}\r\nContent-Disposition: form-data; name="rnd"\r\n\r\n{time}\r\n------WebKitFormBoundary{code_073}\r\nContent-Disposition: form-data; name="roomid"\r\n\r\n{roomid}\r\n------WebKitFormBoundary{code_073}\r\nContent-Disposition: form-data; name="csrf"\r\n\r\n{token}\r\n------WebKitFormBoundary{code_073}\r\nContent-Disposition: form-data; name="csrf_token"\r\n\r\n{token}\r\n------WebKitFormBoundary{code_073}--\r\n'


    def count():
        global code_073
        global thetext
        global time
        global token
        roomid = "10594572"
        data = f'------WebKitFormBoundary{code_073}\r\nContent-Disposition: form-data; name="bubble"\r\n\r\n0\r\n------WebKitFormBoundary{code_073}\r\nContent-Disposition: form-data; name="msg"\r\n\r\n{thetext}\r\n------WebKitFormBoundary{code_073}\r\nContent-Disposition: form-data; name="color"\r\n\r\n16777215\r\n------WebKitFormBoundary{code_073}\r\nContent-Disposition: form-data; name="mode"\r\n\r\n1\r\n------WebKitFormBoundary{code_073}\r\nContent-Disposition: form-data; name="fontsize"\r\n\r\n25\r\n------WebKitFormBoundary{code_073}\r\nContent-Disposition: form-data; name="rnd"\r\n\r\n{time}\r\n------WebKitFormBoundary{code_073}\r\nContent-Disposition: form-data; name="roomid"\r\n\r\n{roomid}\r\n------WebKitFormBoundary{code_073}\r\nContent-Disposition: form-data; name="csrf"\r\n\r\n{token}\r\n------WebKitFormBoundary{code_073}\r\nContent-Disposition: form-data; name="csrf_token"\r\n\r\n{token}\r\n------WebKitFormBoundary{code_073}--\r\n'
        global cookies
        global headers
        text = "加入"
        data233 = data.format(thetext=text)
        data_out = data233.encode("utf-8").decode("latin1")
        requests.post('https://api.live.bilibili.com/msg/send', cookies=cookies, headers=headers, data=data_out)


    def back():
        global data
        global cookies
        global headers
        target = ui.put_in.text()
        text = f"回防"
        data233 = data.format(thetext=text)
        data_out = data233.encode("utf-8").decode("latin1")
        requests.post('https://api.live.bilibili.com/msg/send', cookies=cookies, headers=headers, data=data_out)
        ui.put_in.setText("")

    def goto():
        global data
        global cookies
        global headers
        target = ui.put_in.text()
        text = f"前往{target}"
        data233 = data.format(thetext=text)
        data_out = data233.encode("utf-8").decode("latin1")
        requests.post('https://api.live.bilibili.com/msg/send', cookies=cookies, headers=headers, data=data_out)
        ui.put_in.setText("")
count()
ui.pushButton_2.clicked.connect(roomid)
ui.pushButton.clicked.connect(start)
ui.XuanZhan.clicked.connect(xuanzhan)
ui.Attack.clicked.connect(attack)
ui.peace.clicked.connect(peace)
ui.army.clicked.connect(army)
ui.lord.clicked.connect(lord)
ui.send.clicked.connect(send)
ui.Help.clicked.connect(help)
ui.back.clicked.connect(back)
ui.goto_2.clicked.connect(goto)
sys.exit(app.exec_())
