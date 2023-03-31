import json
import os.path

from misaka import MisakaII


def get_data_from_har(path):
    headers = None
    cookies = None
    with open(path, 'r', encoding='utf-8') as f:
        har_json = json.load(f)
        for i in har_json["log"]["entries"]:
            if i["request"]["url"].endswith("msg/send"):
                headers = {j["name"]: j["value"] for j in i["request"]["headers"]}
                cookies = {j["name"]: j["value"] for j in i["request"]["cookies"]}
                break
    return headers, cookies


if __name__ == '__main__':
    if not os.path.exists('config.json'):
        if not os.path.exists('bilibili.har'):
            print('uh?你似乎是第一次启动这个程序...')
            print(
                '请在发弹幕后选择"将此请求保存为har文件", 然后在以下输入框中输入har文件的路径, 留空则为程序所在目录下的"弹幕.har"')
            print('如果你不知道如何使用开发者工具, 请自行百度')
            print('注: 必须先打开开发者工具, 然后再发弹幕,否则无法获取到cookie')
            text_inp = input('>')
            if text_inp == '':
                text_inp = 'bilibili.har'
            if not os.path.exists(text_inp):
                print('似乎并没有这个文件呢...')
                input()
                exit()
        else:
            text_inp = 'bilibili.har'

        hds, cks = get_data_from_har(text_inp)
        if hds is None or cks is None:
            print('程序找不到所需的信息哦, 再试试吧. ')
            input()
            exit()
        else:
            print('信息获取成功! 正在保存...')
            config = {
                "headers": hds,
                "cookies": cks
            }
            with open('config.json', 'w') as f:
                json.dump(config, f)

with open("config.json") as json_file:
    config = json.load(json_file)
    MisakaII(config)
