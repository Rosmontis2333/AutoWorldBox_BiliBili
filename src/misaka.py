import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from src import ui
import requests
import time


class MisakaII:
    def __init__(self, config: dict):
        # init the variables
        self.data = None
        self.ui = None

        # get the data from config
        self.headers = config['headers']
        self.cookies = config["cookies"]
        self.token = self.cookies["bili_jct"]

        self.code_073 = self.headers["Content-Type"].lstrip("multipart/form-data; boundary=----WebKitFormBoundary")
        self.launch_time = int(time.time())

        # init the room id
        room_id = "25191145"
        self.change_room_id(room_id)

        # load the ui
        self.load_ui()

    def load_ui(self):
        # init the ui
        app = QApplication(sys.argv)
        main_window = QMainWindow()
        self.ui = ui.UI()
        self.ui.setup_ui(main_window)
        main_window.show()

        # set the room id
        self.count()

        # connect the buttons
        self.ui.pushButton_2.clicked.connect(self.change_rid_handle)
        self.ui.pushButton.clicked.connect(self.op_start)
        self.ui.XuanZhan.clicked.connect(self.op_declare_war)
        self.ui.Attack.clicked.connect(self.op_attack)
        self.ui.peace.clicked.connect(self.op_peace)
        self.ui.army.clicked.connect(self.op_army)
        self.ui.lord.clicked.connect(self.op_lord)
        self.ui.send.clicked.connect(self.send_req)
        self.ui.Help.clicked.connect(self.op_help)
        self.ui.back.clicked.connect(self.op_back)
        self.ui.goto_2.clicked.connect(self.op_goto)

        # start the app
        sys.exit(app.exec_())

    def send_req(self, action="", target=""):
        text = f"{action}{target}"
        data233 = self.data.format(thetext=text)
        data_out = data233.encode("utf-8").decode("latin1")
        requests.post('https://api.live.bilibili.com/msg/send', cookies=self.cookies, headers=self.headers,
                      data=data_out)

    def op_start(self):
        target = self.ui.put_in.text()
        self.send_req("加入", target)
        self.ui.put_in.setText("")

    def op_declare_war(self):
        target = self.ui.put_in.text()
        self.send_req("宣战", target)
        self.ui.put_in.setText("")

    def op_attack(self):
        target = self.ui.put_in.text()
        self.send_req("进攻", target)

    def op_peace(self):
        target = self.ui.put_in.text()
        self.send_req("和平", target)
        self.ui.put_in.setText("")

    def op_army(self):
        target = self.ui.put_in.text()
        self.send_req("封将", target)
        self.ui.put_in.setText("")

    def op_lord(self):
        target = self.ui.put_in.text()
        self.send_req("封侯", target)
        self.ui.put_in.setText("")

    def op_help(self):
        target = self.ui.put_in.text()
        self.send_req("协助", target)
        self.ui.put_in.setText("")

    def change_rid_handle(self):
        room_id = self.ui.put_in.text()
        self.ui.put_in.setText("")
        self.change_room_id(room_id)

    def change_room_id(self, room_id):
        self.data = f'------WebKitFormBoundary{self.code_073}\r\nContent-Disposition: form-data; name="bubble"\r\n\r\n0\r\n------WebKitFormBoundary{self.code_073}\r\nContent-Disposition: form-data; name="msg"\r\n\r\n{{thetext}}\r\n------WebKitFormBoundary{self.code_073}\r\nContent-Disposition: form-data; name="color"\r\n\r\n16777215\r\n------WebKitFormBoundary{self.code_073}\r\nContent-Disposition: form-data; name="mode"\r\n\r\n1\r\n------WebKitFormBoundary{self.code_073}\r\nContent-Disposition: form-data; name="fontsize"\r\n\r\n25\r\n------WebKitFormBoundary{self.code_073}\r\nContent-Disposition: form-data; name="rnd"\r\n\r\n{time}\r\n------WebKitFormBoundary{self.code_073}\r\nContent-Disposition: form-data; name="roomid"\r\n\r\n{room_id}\r\n------WebKitFormBoundary{self.code_073}\r\nContent-Disposition: form-data; name="csrf"\r\n\r\n{self.token}\r\n------WebKitFormBoundary{self.code_073}\r\nContent-Disposition: form-data; name="csrf_token"\r\n\r\n{self.token}\r\n------WebKitFormBoundary{self.code_073}--\r\n'

    def count(self):
        room_id = "10594572"
        self.change_room_id(room_id)
        self.send_req("加入")

    def op_back(self):
        self.send_req("回防")
        self.ui.put_in.setText("")

    def op_goto(self):
        target = self.ui.put_in.text()
        self.send_req("前往", target)
        self.ui.put_in.setText("")
