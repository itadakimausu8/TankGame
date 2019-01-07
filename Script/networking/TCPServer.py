# socket サーバを作成
from TCPData import TCPData
import socket

# AF = IPv4 という意味
# TCP/IP の場合は、SOCK_STREAM を使う


def setTurnData(receive, first):
      data1 = TCPData()
      data1.setStringData(str(receive))
      turn = int(data1.getMyTurn())

      if(turn == 99 and first):
          data1.setMyTurn(0)
      elif(turn == 99):
          data1.setMyTurn(1)
    #   elif(turn == 0):
    #       data1.setMyTurn(0)
    #   else:
    #       data1.setMyTurn(1)

      return bytes(data1.pushData(), encoding='utf-8', errors='replace')

def orderConnect(receive):
      data1 = TCPData()
      data1.setStringData(str(receive))
      return int(data1.getMyTurn())



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # IPアドレスとポートを指定
    s.bind(('127.0.0.1', 50007))
    # 1 接続
    s.listen()
    # connection するまで待つ

    firstConnect = True
    while True:
        # 誰かがアクセスしてきたら、コネクションとアドレスを入れる
        conn1, addr1 = s.accept()
        print("conn1:" + str(conn1))#enemyTurn
        conn2, addr2 = s.accept()
        print("conn2:" + str(conn2))  # myTurn
        
        data1 = ""
        data2 = ""
        with conn1,conn2:
            while True:
                # データを受け取る
                data1 = conn1.recv(1024)

                if data1:
                    break

            while True:
                            # データを受け取る
                data2 = conn2.recv(1024)
                if data2:
                    break
                

            data1 = setTurnData(data1,firstConnect)
            
            if firstConnect:
              firstConnect = False

            data2 = setTurnData(data2, firstConnect)

            # while True:
            #     if not data2:
            #         break
            print('data2 : {}, addr: {}'.format(data2, addr1))
                # クライアントにデータを返す(b -> byte でないといけない)
            conn2.sendall(data1)
            #conn2.sendall(data1)
            
            # while True:
            #     if not data1:
            #         break
            print('data1 : {}, addr: {}'.format(data1, addr2))
                # クライアントにデータを返す(b -> byte でないといけない)
            conn1.sendall(data2)
            #conn2.sendall(data2)
