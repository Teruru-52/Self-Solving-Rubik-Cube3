import cv2
import numpy as np
from algorithm import knn
from algorithm import usbVideoDevice

class ColorState:
    def __init__(self, cc, ec):
        self.cc = cc
        self.ec = ec

color_state = ColorState(
    [['','',''], ['','',''], ['','',''], ['','',''], ['','',''], ['','',''], ['','',''], ['','','']],
    [['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['','']]
)

red = []
blue = []
green = []
yellow = []
orenge = []
white = []

def Set_train_data(hsv, port, train_no, index):
    global red
    global blue
    global green
    global yellow
    global orenge
    global white

    if train_no == 1:
        if port == 1:
            if index in [0, 1, 2]:
                green += [hsv]
            elif index in [3, 4, 5]:
                red += [hsv]

        elif port == 2:
            if index in [0, 1, 2]:
                blue += [hsv]
            elif index in [3, 4, 5]:
                orenge += [hsv]

    elif train_no == 2:
        if port == 1:
            if index in [0, 1, 2]:
                yellow += [hsv]
        elif port == 3:
            if index in [3, 4, 5]:
                white += [hsv]
    
def Set_color_state(color, port, detect_no, index):
    if detect_no == 1:
        if port == 1:
            if index == 0:
                color_state.cc[2][2] = color
            elif index == 1:
                color_state.ec[2][0] = color
            elif index == 2:
                color_state.cc[6][1] = color
            elif index == 3:
                color_state.cc[2][1] = color
            elif index == 4:
                color_state.ec[2][1] = color
            elif index == 5:
                color_state.cc[6][2] = color
        elif port == 2:
            if index == 0:
                color_state.cc[0][2] = color
            elif index == 1:
                color_state.ec[0][0] = color
            elif index == 2:
                color_state.cc[4][1] = color
            elif index == 3:
                color_state.cc[0][1] = color
            elif index == 4:
                color_state.ec[0][1] = color
            elif index == 5:
                color_state.cc[4][2] = color
        elif port == 3:
            if index == 0:
                color_state.cc[1][2] = color
            elif index == 1:
                color_state.ec[1][1] = color
            elif index == 2:
                color_state.cc[5][1] = color
            elif index == 3:
                color_state.cc[1][1] = color
            elif index == 4:
                color_state.ec[1][0] = color
            elif index == 5:
                color_state.cc[5][2] = color
        elif port == 4:
            if index == 0:
                color_state.cc[3][2] = color
            elif index == 1:
                color_state.ec[3][1] = color
            elif index == 2:
                color_state.cc[7][1] = color
            elif index == 3:
                color_state.cc[3][1] = color
            elif index == 4:
                color_state.ec[3][0] = color
            elif index == 5:
                color_state.cc[7][2] = color
    if detect_no == 2:
        if port == 1:
            if index == 0:
                color_state.cc[6][0] = color
            elif index == 1:
                color_state.ec[9][0] = color
            elif index == 2:
                color_state.cc[5][0] = color
            elif index == 4:
                color_state.ec[9][1] = color
        if port == 2:
            if index == 0:
                color_state.cc[4][0] = color
            elif index == 1:
                color_state.ec[11][0] = color
            elif index == 2:
                color_state.cc[7][0] = color
            elif index == 4:
                color_state.ec[11][1] = color
        if port == 3:
            if index == 1:
                color_state.ec[5][1] = color
            elif index == 3:
                color_state.cc[2][0] = color
            elif index == 4:
                color_state.ec[5][0] = color
            elif index == 5:
                color_state.cc[1][0] = color
        if port == 4:
            if index == 1:
                color_state.ec[7][1] = color
            elif index == 3:
                color_state.cc[0][0] = color
            elif index == 4:
                color_state.ec[7][0] = color
            elif index == 5:
                color_state.cc[3][0] = color
    elif detect_no == 3:
        if port == 1:
            if index == 1:
                color_state.ec[6][1] = color
            elif index == 4:
                color_state.ec[6][0] = color
        if port == 2:
            if index == 1:
                color_state.ec[4][1] = color
            elif index == 4:
                color_state.ec[4][0] = color
        if port == 3:
            if index == 1:
                color_state.ec[4][0] = color
            elif index == 4:
                color_state.ec[4][1] = color
        if port == 4:
            if index == 1:
                color_state.ec[10][0] = color
            elif index == 4:
                color_state.ec[10][1] = color

k_nn = knn.K_NN(k = 1)
train_red = [[5.64, 164.77, 155.87]]
train_blue = [[107.05, 144.05, 220.48], [104.81, 179.99, 89.31]]
train_green = [[55.04, 78.68, 151.31]]
train_orenge = [[7.94, 136.29, 254.84], [34.06, 63.27, 189.34]]
train_yellow = [[35.15, 75.04, 254.41], [11.07, 169.22, 155.98]]
train_white = [[46.3, 16.95, 218.53]]

train_data = train_red + train_blue + train_green + train_orenge + train_yellow + train_white
label = ['R' for i in range(len(train_red))] + \
        ['B' for i in range(len(train_blue))] + \
        ['G' for i in range(len(train_green))] + \
        ['O' for i in range(len(train_orenge))] + \
        ['Y' for i in range(len(train_yellow))] + \
        ['W' for i in range(len(train_white))]

class Camera:
    def __init__(self, xy, port, device_id):
        self.xy = xy
        self.port = port
        self.device_id = device_id

    def Get_hsv(self, imgBox):
        # BGRからHSVに変換
        imgBoxHsv = cv2.cvtColor(imgBox,cv2.COLOR_BGR2HSV)
        # HSV平均値を取得
        # flattenで一次元化しmeanで平均を取得 
        h = imgBoxHsv.T[0].flatten().mean()
        s = imgBoxHsv.T[1].flatten().mean()
        v = imgBoxHsv.T[2].flatten().mean()

        # HSV平均値を出力
        # hsv = [h, s, v]
        # print(list(map(round, hsv, [2]*len(hsv))))

        return [round(h, 3), round(s, 3), round(v, 3)]

    def Identificate_color(self, hsv):
        k_nn.fit(train_data, label)
        color = k_nn.predict([hsv])

        # print(color)
        return color

    def camera2color_state(self, detect_no):
        img = cv2.imread(f'picture/webcam{self.port}.jpg')

        lateral = 30        
        for i in range(len(self.xy)):
            # 対象範囲を切り出し
            imgBox = img[self.xy[i][1]: self.xy[i][1]+lateral, self.xy[i][0]: self.xy[i][0]+lateral]
            # HSVの平均値を取得
            hsv = self.Get_hsv(imgBox)
            # print('')
            # print('### index = ', i)
            color = self.Identificate_color(hsv)
            Set_color_state(color, self.port, detect_no, i)

        # draw rectangle
        # cv2.rectangle(img, (self.xy[6][0], self.xy[6][1]), (self.xy[6][0]+lateral, self.xy[][1]+lateral), (255, 0, 0), thickness=4)
        for i in range(len(self.xy)):
            cv2.rectangle(img, (self.xy[i][0], self.xy[i][1]), (self.xy[i][0]+lateral, self.xy[i][1]+lateral), (255, 0, 0), thickness=2)

        # print("cc = ", color_state.cc)
        # print("ec = ", color_state.ec)
        cv2.imwrite(f'picture/webcam{self.port}.jpg', img)

    def camera2train_data(self, train_no):
        img = cv2.imread(f'picture/webcam{self.port}.jpg')

        lateral = 30        
        for i in range(len(self.xy)):
            # 対象範囲を切り出し
            imgBox = img[self.xy[i][1]: self.xy[i][1]+lateral, self.xy[i][0]: self.xy[i][0]+lateral]
            # HSVの平均値を取得
            hsv = self.Get_hsv(imgBox)
            Set_train_data(hsv, self.port, train_no, i)


        # draw rectangle
        # cv2.rectangle(img, (self.xy[6][0], self.xy[6][1]), (self.xy[6][0]+lateral, self.xy[][1]+lateral), (255, 0, 0), thickness=4)
        for i in range(len(self.xy)):
            cv2.rectangle(img, (self.xy[i][0], self.xy[i][1]), (self.xy[i][0]+lateral, self.xy[i][1]+lateral), (255, 0, 0), thickness=2)

        cv2.imwrite(f'picture/webcam{self.port}.jpg', img)

    def Take_picture(self):
        capture = cv2.VideoCapture(self.device_id) # /dev/video*
        capture.set(cv2.CAP_PROP_FPS, 10)
        while True:
            if(capture.isOpened()): # Open
                retval, image = capture.read()
                if retval is False:
                    raise IOError
                text = 'WIDTH={:.0f} HEIGHT={:.0f} FPS={:.0f}'.format(capture.get(cv2.CAP_PROP_FRAME_WIDTH),capture.get(cv2.CAP_PROP_FRAME_HEIGHT),capture.get(cv2.CAP_PROP_FPS))
                cv2.putText(image, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1, 4)
                # cv2.imshow(f'Webcam{self.port}', image)
                cv2.imwrite(f'picture/webcam{self.port}.jpg', image)
                capture.release()
                cv2.destroyAllWindows()
                print(f"finish Webcam{self.port}")
                break

x1 = 280
y1 = 60
xy_camera1 = [[x1, y1], [x1, y1+100], [x1, y1+200], [x1+100, y1], [x1+100, y1+100], [x1+100, y1+200]]

xy_camera3 = [[260, 170], [300, 230], [220, 230], [180, 130], [140, 190], [340, 130]]

usb_device = usbVideoDevice.UsbVideoDevice()
camera1 = Camera(xy_camera1, 1, usb_device.getId(1))
camera2 = Camera(xy_camera1, 2, usb_device.getId(2))
camera3 = Camera(xy_camera3, 3, usb_device.getId(3))
camera4 = Camera(xy_camera3, 4, usb_device.getId(4))

def Take_pictures():
    camera1.Take_picture()
    camera2.Take_picture()
    camera3.Take_picture()
    camera4.Take_picture()

def Detect_colors(detect_no):
    camera1.camera2color_state(detect_no)
    camera2.camera2color_state(detect_no)
    camera3.camera2color_state(detect_no)
    camera4.camera2color_state(detect_no)

def Detect_color_state(detect_no):
    Take_pictures()
    Detect_colors(detect_no)

def Get_color_state():
    return color_state

def Print_train_data():
    print("train_red =", red)
    print("train_blue =", blue)
    print("train_green =", green)
    print("train_yellow =", yellow)
    print("train_orenge =", orenge)
    print("train_white =", white)

def Train_data(train_no):
    if train_no == 1:
        print("set train data1")
        camera1.Take_picture()
        camera2.Take_picture()
        camera1.camera2train_data(train_no)
        camera2.camera2train_data(train_no)
    elif train_no == 2:
        print("set train data2")
        camera1.Take_picture()
        camera3.Take_picture()
        camera1.camera2train_data(train_no)
        camera3.camera2train_data(train_no)

