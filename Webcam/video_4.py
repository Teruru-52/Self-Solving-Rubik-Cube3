import cv2
from usbVideoDevice import UsbVideoDevice

lateral = 10
dx = 80
dy = 65

x1 = 210
y1 = 50
xy_camera1 = [[x1, y1], [x1, y1+dy], [x1, y1+2*dy], [x1+dx, y1], [x1+dx, y1+dy], [x1+dx, y1+2*dy]]
x2 = 195
y2 = 50
xy_camera2 = [[x2, y2], [x2, y2+dy], [x2, y2+2*dy], [x2+dx, y2], [x2+dx, y2+dy], [x2+dx, y2+2*dy]]
x3 = 225
y3 = 50
xy_camera3 = [[x3, y3], [x3, y3+dy], [x3, y3+2*dy], [x3+dx, y3], [x3+dx, y3+dy], [x3+dx, y3+2*dy]]
x4 = 230
y4 = 45
xy_camera4 = [[x4, y4], [x4, y4+dy], [x4, y4+2*dy], [x4+dx, y4], [x4+dx, y4+dy], [x4+dx, y4+2*dy]]

FPS = 10
WIDTH = 544
HEIGHT = 288

#main
if __name__ == '__main__':
    try:
        usbVideoDevice = UsbVideoDevice()
        
        device1_id = usbVideoDevice.getId(1)
        device2_id = usbVideoDevice.getId(2)
        device3_id = usbVideoDevice.getId(3)
        device4_id = usbVideoDevice.getId(4)
        
        capture1 = cv2.VideoCapture(device1_id) # /dev/video*
        capture2 = cv2.VideoCapture(device2_id)
        capture3 = cv2.VideoCapture(device3_id)
        capture4 = cv2.VideoCapture(device4_id)
        
        capture1.set(cv2.CAP_PROP_FPS, FPS)
        capture1.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
        capture1.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
        print("video1 set")
        capture2.set(cv2.CAP_PROP_FPS, FPS)
        capture2.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
        capture2.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
        print("video2 set")
        capture3.set(cv2.CAP_PROP_FPS, FPS)
        capture3.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
        capture3.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
        print("video3 set")
        capture4.set(cv2.CAP_PROP_FPS, FPS)
        capture4.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
        capture4.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
        print("video4 set")
        
        while True:
            retval1, image1 = capture1.read()
            if image1 is None:
                continue
            retval2, image2 = capture2.read()
            if image2 is None:
                continue
            retval3, image3 = capture3.read()
            if image3 is None:
                continue
            retval4, image4 = capture4.read()
            if image4 is None:
                continue

            text1 = 'WIDTH={:.0f}'.format(capture1.get(cv2.CAP_PROP_FRAME_WIDTH))
            text2 = 'HEIGHT={:.0f}'.format(capture1.get(cv2.CAP_PROP_FRAME_HEIGHT))
            text3 = 'FPS={:.0f}'.format(capture1.get(cv2.CAP_PROP_FPS))
            # 元Image,文字列,位置,フォント,サイズ（スケール係数）,色,太さ,ラインの種類
            cv2.putText(image1, text1, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, 4)
            cv2.putText(image1, text2, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, 4)
            cv2.putText(image1, text3, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, 4)
            
            for i in range(len(xy_camera1)):
                cv2.rectangle(image1, (xy_camera1[i][0], xy_camera1[i][1]), (xy_camera1[i][0]+lateral, xy_camera1[i][1]+lateral), (255, 0, 0), thickness=2)
            for i in range(len(xy_camera2)):
                cv2.rectangle(image2, (xy_camera2[i][0], xy_camera2[i][1]), (xy_camera2[i][0]+lateral, xy_camera2[i][1]+lateral), (255, 0, 0), thickness=2)
            for i in range(len(xy_camera3)):
                cv2.rectangle(image3, (xy_camera3[i][0], xy_camera3[i][1]), (xy_camera3[i][0]+lateral, xy_camera3[i][1]+lateral), (255, 0, 0), thickness=2)
            for i in range(len(xy_camera4)):
                cv2.rectangle(image4, (xy_camera4[i][0], xy_camera4[i][1]), (xy_camera4[i][0]+lateral, xy_camera4[i][1]+lateral), (255, 0, 0), thickness=2)

            image12 = cv2.hconcat([image1, image2])
            image34 = cv2.hconcat([image3, image4])
            image = cv2.vconcat([image12, image34])
            # print("concat image")
            cv2.imshow('Webcam', image) # 表示
            cv2.waitKey(1)

    except KeyboardInterrupt:
        capture1.release()
        capture2.release()
        capture3.release()
        capture4.release()
        cv2.destroyAllWindows() # Window削除
    finally:
        capture1.release()
        capture2.release()
        capture3.release()
        capture4.release()
        cv2.destroyAllWindows() # Window削除