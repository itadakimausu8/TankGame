# socket サーバを作成
import TCPData
import socket

# AF = IPv4 という意味
# TCP/IP の場合は、SOCK_STREAM を使う
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # IPアドレスとポートを指定
    s.bind(('127.0.0.1', 50007))
    # 1 接続
    s.listen()
    # connection するまで待つ
    while True:
        # 誰かがアクセスしてきたら、コネクションとアドレスを入れる
        conn1, addr1 = s.accept()
        conn2, addr2 = s.accept()
        
        data1 = ""
        data2 = ""
        with conn1,conn2:
            print("conn1")
            while True:
                # データを受け取る
                data1 = conn1.recv(1024)
                if data1:
                    break

            print("conn2")
            while True:
                # データを受け取る
                data2 = conn2.recv(1024)
                if data2:
                    break
        
            print("recive1")
            while True:
                if not data2:
                    break
                print('data2 : {}, addr: {}'.format(data2, addr1))
                # クライアントにデータを返す(b -> byte でないといけない)
                conn1.sendall(data2)
                break
        
            print("recive2")
            while True:
                if not data1:
                    break
                print('data1 : {}, addr: {}'.format(data1, addr2))
                # クライアントにデータを返す(b -> byte でないといけない)
                conn2.sendall(data1)
                break
