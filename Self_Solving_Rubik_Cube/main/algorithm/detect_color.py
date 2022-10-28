import cv2
import numpy as np
from algorithm import knn
from algorithm import usbVideoDevice
import copy

class ColorState:
    def __init__(self, cc, ec):
        self.cc = cc
        self.ec = ec

color_state = ColorState(
    [['','',''], ['','',''], ['','',''], ['','',''], ['','',''], ['','',''], ['','',''], ['','','']],
    [['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['','']]
)

copy_color_state = ColorState(
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
        elif port == 3:
            if index in [0, 1, 2]:
                red += [hsv]
            elif index in [3, 4, 5]:
                blue += [hsv]
        elif port == 4:
            if index in [0, 1, 2]:
                orenge += [hsv]
            elif index in [3, 4, 5]:
                green += [hsv]
    elif train_no == 2:
        if port == 1:
            if index in [0, 1, 2]:
                yellow += [hsv]
        elif port == 2:
            if index in [0, 1, 2]:
                yellow += [hsv]
        elif port == 3:
            if index in [3, 4, 5]:
                white += [hsv]
        elif port == 4:
            if index in [3, 4, 5]:
                white += [hsv]
    elif train_no == 3:
        if port == 1:
            if index in [0, 1, 2]:
                blue += [hsv]
            elif index in [3, 4, 5]:
                red += [hsv]
        elif port == 2:
            if index in [0, 1, 2]:
                green += [hsv]
            elif index in [3, 4, 5]:
                orenge += [hsv]
        elif port == 3:
            if index in [0, 1, 2]:
                red += [hsv]
            elif index in [3, 4, 5]:
                green += [hsv]
        elif port == 4:
            if index in [0, 1, 2]:
                orenge += [hsv]
            elif index in [3, 4, 5]:
                blue += [hsv]
    elif train_no == 4:
        if port == 1:
            if index in [0, 1, 2]:
                white += [hsv]
        elif port == 2:
            if index in [0, 1, 2]:
                white += [hsv]
        elif port == 3:
            if index in [3, 4, 5]:
                yellow += [hsv]
        elif port == 4:
            if index in [3, 4, 5]:
                yellow += [hsv]
    elif train_no == 5:
        if port == 1:
            if index in [3, 4, 5]:
                white += [hsv]
        elif port == 2:
            if index in [3, 4, 5]:
                white += [hsv]
        elif port == 3:
            if index in [0, 1, 2]:
                yellow += [hsv]
        elif port == 4:
            if index in [0, 1, 2]:
                yellow += [hsv]
    elif train_no == 6:
        if port == 1:
            if index in [0, 1, 2]:
                green += [hsv]
            elif index in [3, 4, 5]:
                orenge += [hsv]
        elif port == 2:
            if index in [0, 1, 2]:
                blue += [hsv]
            elif index in [3, 4, 5]:
                red += [hsv]
        elif port == 3:
            if index in [0, 1, 2]:
                orenge += [hsv]
            elif index in [3, 4, 5]:
                blue += [hsv]
        elif port == 4:
            if index in [0, 1, 2]:
                red += [hsv]
            elif index in [3, 4, 5]:
                green += [hsv]
    elif train_no == 7:
        if port == 1:
            if index in [3, 4, 5]:
                yellow += [hsv]
        elif port == 2:
            if index in [3, 4, 5]:
                yellow += [hsv]
        elif port == 3:
            if index in [0, 1, 2]:
                white += [hsv]
        elif port == 4:
            if index in [0, 1, 2]:
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
                color_state.ec[8][0] = color
            elif index == 4:
                color_state.ec[8][1] = color
        if port == 4:
            if index == 1:
                color_state.ec[10][0] = color
            elif index == 4:
                color_state.ec[10][1] = color

k_nn = knn.K_NN(k = 3)
# hsv
# without LED
# train_red = [[4.02, 197.08, 255.0], [3.89, 203.94, 255.0], [4.29, 193.35, 255.0]]
# train_blue = [[96.32, 183.89, 255.0], [93.09, 181.09, 255.0], [94.22, 185.66, 255.0]]
# train_green = [[89.85, 65.9, 255.0], [90.0, 97.87, 255.0], [87.14, 26.87, 255.0]]
# train_yellow = [[52.0, 4.0, 255.0], [52.0, 4.0, 255.0], [50.66, 5.72, 255.0]]
# train_orenge = [[29.69, 83.52, 255.0], [28.38, 87.5, 255.0], [30.77, 59.74, 255.0]]
# train_white = [[90.0, 3.0, 255.0], [88.2, 4.33, 255.0], [89.0, 3.75, 255.0]]

train_red = [[3.68, 194.41, 255.0], [3.76, 201.79, 255.0], [3.98, 206.75, 255.0], [11.49, 73.11, 255.0], [3.95, 170.45, 255.0], [3.32, 192.11, 255.0], [3.59, 191.85, 255.0], [3.54, 200.81, 255.0], [3.72, 204.7, 255.0], [9.39, 84.63, 254.85], [3.31, 164.96, 255.0], [3.23, 192.82, 255.0], [4.26, 197.99, 189.1], [3.91, 158.91, 216.24], [3.84, 197.64, 183.22], [6.74, 117.69, 197.15], [7.43, 128.16, 175.68], [6.04, 190.66, 130.34]]
train_blue = [[104.98, 206.41, 253.66], [106.64, 201.41, 255.0], [103.15, 220.66, 255.0], [105.96, 214.46, 255.0], [104.0, 219.85, 255.0], [102.23, 221.4, 255.0], [99.26, 209.13, 255.0], [96.73, 203.69, 255.0], [96.05, 209.6, 255.0], [105.42, 222.66, 255.0], [98.9, 158.16, 255.0], [100.78, 198.58, 255.0], [105.35, 205.99, 248.76], [105.85, 190.83, 229.37], [104.01, 223.0, 255.0], [106.69, 217.13, 235.47], [106.91, 221.51, 255.0], [105.1, 225.67, 255.0]]
train_green = [[81.56, 129.26, 255.0], [89.7, 110.68, 255.0], [90.0, 103.87, 255.0], [69.13, 189.22, 254.11], [74.64, 156.4, 254.89], [71.47, 173.7, 255.0], [70.18, 190.44, 251.83], [68.19, 189.98, 252.78], [71.72, 195.48, 255.0], [66.93, 182.92, 255.0], [69.16, 182.42, 255.0], [72.15, 169.62, 255.0], [69.38, 176.39, 255.0], [72.27, 165.73, 255.0], [74.93, 160.37, 255.0], [68.74, 196.38, 255.0], [79.1, 129.41, 255.0], [73.96, 165.32, 255.0]]
train_yellow = [[30.0, 4.0, 255.0], [30.0, 4.0, 255.0], [30.0, 4.0, 255.0], [35.86, 33.67, 255.0], [31.83, 114.61, 255.0], [30.76, 8.54, 255.0], [30.73, 69.92, 255.0], [31.19, 27.42, 255.0], [30.92, 4.82, 255.0], [38.0, 104.68, 255.0], [40.68, 29.97, 255.0], [44.4, 13.7, 255.0], [48.22, 16.62, 250.84], [52.89, 4.47, 255.0], [52.59, 4.33, 255.0], [31.0, 63.0, 255.0], [30.7, 68.56, 255.0], [31.49, 94.73, 255.0], [52.0, 4.0, 255.0], [31.6, 5.4, 255.0], [32.0, 5.5, 255.0], [30.07, 6.95, 255.0], [31.56, 5.64, 255.0], [31.98, 6.91, 254.99]]
train_orenge = [[21.39, 135.93, 255.0], [27.22, 91.66, 255.0], [21.27, 139.12, 255.0], [11.38, 106.22, 255.0], [12.0, 115.44, 255.0], [11.68, 140.2, 255.0], [25.2, 144.05, 255.0], [30.17, 81.16, 255.0], [24.23, 148.25, 255.0], [15.86, 90.55, 255.0], [15.57, 105.17, 255.0], [13.87, 135.37, 255.0], [27.34, 102.42, 255.0], [29.7, 98.77, 255.0], [30.1, 100.79, 255.0], [51.56, 4.34, 255.0], [37.54, 19.54, 255.0], [30.99, 37.74, 255.0]]
train_white = [[88.02, 9.14, 255.0], [88.1, 4.37, 255.0], [88.75, 3.86, 255.0], [88.13, 35.73, 255.0], [89.24, 10.03, 255.0], [88.93, 4.02, 255.0], [90.0, 3.0, 255.0], [90.0, 3.0, 255.0], [90.0, 3.0, 255.0], [87.6, 15.58, 251.93], [86.48, 46.16, 254.56], [90.0, 3.0, 255.0], [52.0, 4.0, 255.0], [88.0, 4.4, 255.0], [87.5, 4.5, 255.0], [52.0, 4.0, 255.0], [55.0, 6.0, 255.0], [84.0, 5.0, 255.0], [52.0, 4.0, 255.0], [52.83, 4.45, 255.0], [89.7, 3.27, 255.0], [86.6, 23.46, 255.0], [87.91, 34.92, 255.0], [95.16, 62.91, 232.94]]

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

    def Get_rgb(self, imgBox):
        # RGB
        # flattenで一次元化しmeanで平均を取得 
        b = imgBox.T[0].flatten().mean()
        g = imgBox.T[1].flatten().mean()
        r = imgBox.T[2].flatten().mean()
        
        return [round(r, 3), round(g, 3), round(b, 3)]

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

    def Identificate_color(self, data):
        k_nn.fit(train_data, label)
        color = k_nn.predict([data])

        # print(color)
        return color
    
    def Take_picture(self):
        capture = cv2.VideoCapture(self.device_id) # /dev/video*
        capture.set(cv2.CAP_PROP_FRAME_WIDTH, 544)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 288)
        capture.set(cv2.CAP_PROP_FPS, 10)
        
        while True:
            retval, image = capture.read()
            if image is None:
                continue
            else:
                break
            
        text1 = 'WIDTH={:.0f}'.format(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        text2 = 'HEIGHT={:.0f}'.format(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        text3 = 'FPS={:.0f}'.format(capture.get(cv2.CAP_PROP_FPS))
        cv2.putText(image, text1, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, 4)
        cv2.putText(image, text2, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, 4)
        cv2.putText(image, text3, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, 4)
        
        capture.release()
        cv2.destroyAllWindows()
        return image

    def camera2color(self, mode, detect_no, train_no):
        image = self.Take_picture()
                
        lateral = 10  
        colors = []      
        for i in range(len(self.xy)):
            # 対象範囲を切り出し
            imgBox = image[self.xy[i][1]: self.xy[i][1]+lateral, self.xy[i][0]: self.xy[i][0]+lateral]
            # HSVの平均値を取得
            data = self.Get_hsv(imgBox)
            # RGBの平均値を取得
            # data = self.Get_rgb(imgBox)
            
            if mode == 'solve':
                color = self.Identificate_color(data)
                Set_color_state(color, self.port, detect_no, i)
                colors += color
            elif mode == 'train':
                Set_train_data(data, self.port, train_no, i)
                
        for i in range(len(self.xy)):
            cv2.rectangle(image, (self.xy[i][0], self.xy[i][1]), (self.xy[i][0]+lateral, self.xy[i][1]+lateral), (255, 0, 0), thickness=2)
            if mode == 'solve':
                cv2.putText(image, colors[i], (self.xy[i][0]-20, self.xy[i][1]+20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2, 4)
                
        # cv2.imshow(f'Webcam{self.port}', image)
        cv2.imwrite(f'picture/webcam{self.port}.jpg', image)
        print(f"finish Webcam{self.port}")

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

usb_device = usbVideoDevice.UsbVideoDevice()
camera1 = Camera(xy_camera1, 1, usb_device.getId(1))
camera2 = Camera(xy_camera2, 2, usb_device.getId(2))
camera3 = Camera(xy_camera3, 3, usb_device.getId(3))
camera4 = Camera(xy_camera4, 4, usb_device.getId(4))

def Detect_color_state(mode, detect_no):
    camera1.camera2color(mode, detect_no, 0)
    camera2.camera2color(mode, detect_no, 0)
    camera3.camera2color(mode, detect_no, 0)
    camera4.camera2color(mode, detect_no, 0)

def Get_color_state():
    # print("cc =", color_state.cc)
    # print("ec =", color_state.ec)
    return color_state

def Print_train_data():
    print("train_red =", red)
    print("train_blue =", blue)
    print("train_green =", green)
    print("train_yellow =", yellow)
    print("train_orenge =", orenge)
    print("train_white =", white)

def Train_data(mode, train_no):
    print(f"set train data{train_no}")
    camera1.camera2color(mode, 0, train_no)
    camera2.camera2color(mode, 0, train_no)
    camera3.camera2color(mode, 0, train_no)
    camera4.camera2color(mode, 0, train_no)

