# クライアントを作成
from TCPData import TCPData
import socket
import re


class TCPClient:

    def connecting(self,data):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # サーバを指定
            s.connect(('127.0.0.1', 50007))
            # サーバにメッセージを送る
            s.sendall(bytes(data.pushData(), encoding='utf-8', errors='replace'))
            # ネットワークのバッファサイズは1024。サーバからの文字列を取得する
            receive = s.recv(1024).decode('utf-8')
            reData = TCPData()
            reData.setStringData(receive)
            return reData




# Data = TCPData()
# Data.setData(1, 1, 1, [1, 5], [1, 5], [1, 2],
#              1, 1, 1, [1, 1], [1, 2], [1, 3])
# con = TCPClient()
# Data = con.connecting(Data)
# print("client2" + Data.pushData())