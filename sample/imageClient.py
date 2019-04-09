import socket
import cv2
import numpy as np

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#ソケットオブジェクト作成

soc.connect(("127.0.0.1", 9001))#サーバー側のipと使用するポート(ポートはサーバーと同じにする。)

print("接続完了")

while(1):
    data = soc.recv(921600)#引数は下記注意点参照

    data = np.fromstring(data, dtype=np.uint8)#バイトデータ→ndarray変換

    data = np.reshape(data,(480,640,3))#形状復元(これがないと一次元行列になってしまう。)　reshapeの第二引数の(480,640,3)は引数は送られてくる画像の形状

    cv2.imshow("", data)

    k = cv2.waitKey(1)
    if k == 13:
        break

cv2.destroyAllWindows() # 作成したウィンドウを破棄

'''
https://qiita.com/DIODE/items/cb19d0f7d699c19cf4b2
'''