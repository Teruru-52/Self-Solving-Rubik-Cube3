import cv2
from usbVideoDevice import UsbVideoDevice

#main
if __name__ == '__main__':
    try:
        for port in range(4):
            usbVideoDevice = UsbVideoDevice()
            device_id = usbVideoDevice.getId(port + 1)
            print("video{}".format(device_id))
            capture = cv2.VideoCapture(device_id) # /dev/video*
            capture.set(cv2.CAP_PROP_FPS, 10)
            while True:
                if(capture.isOpened()): # Open
                    retval, image = capture.read() # キャプチャー
                    if retval is False:
                        raise IOError
                    text = 'WIDTH={:.0f} HEIGHT={:.0f} FPS={:.0f}'.format(capture.get(cv2.CAP_PROP_FRAME_WIDTH),capture.get(cv2.CAP_PROP_FRAME_HEIGHT),capture.get(cv2.CAP_PROP_FPS))
                    # 元Image,文字列,位置,フォント,サイズ（スケール係数）,色,太さ,ラインの種類
                    cv2.putText(image, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1, 4)
                    # cv2.imshow(f'Webcam{i}', image) # 表示
                    cv2.imwrite(f'picture/webcam_test{port + 1}.jpg', image)
                    capture.release()
                    cv2.destroyAllWindows()
                    break
    except KeyboardInterrupt:
        pass
    finally:
        cv2.destroyAllWindows() # Window削除