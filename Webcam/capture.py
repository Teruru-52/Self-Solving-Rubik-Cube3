# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:42:59 2021

・Raspberry Pi にUSB接続したカメラの映像をキャプチャーする

@author: Souichirou Kikuchi
"""

import cv2
from usbVideoDevice import UsbVideoDevice

#main
if __name__ == '__main__':
    try:
        usbVideoDevice = UsbVideoDevice()
        port = 1
        device_id = usbVideoDevice.getId(port)
        print("video{}".format(device_id))
        capture = cv2.VideoCapture(device_id) # /dev/video*
        while True:
            if (capture.isOpened()): # Open
                retval, image = capture.read() # キャプチャー
                if retval is False:
                    raise IOError
                text = 'WIDTH={:.0f} HEIGHT={:.0f} FPS={:.0f}'.format(capture.get(cv2.CAP_PROP_FRAME_WIDTH),capture.get(cv2.CAP_PROP_FRAME_HEIGHT),capture.get(cv2.CAP_PROP_FPS))
                # 元Image,文字列,位置,フォント,サイズ（スケール係数）,色,太さ,ラインの種類
                cv2.putText(image, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, 4)
                # print(image)
                cv2.imwrite(f'picture/webcam_test{port}.jpg', image)
                break
        capture.release() # VideoCaptureのClose
        cv2.destroyAllWindows() # Window削除
    except KeyboardInterrupt:
        pass