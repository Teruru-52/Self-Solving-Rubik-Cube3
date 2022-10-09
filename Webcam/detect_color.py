import cv2
import numpy as np
import knn

class ColorState:
    def __init__(self, cc, ec):
        self.cc = cc
        self.ec = ec

color_state = ColorState(
    [['','',''], ['','',''], ['','',''], ['','',''], ['','',''], ['','',''], ['','',''], ['','','']],
    [['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['','']]
)

# webcam1.jpg
correct_state = ColorState(
    [['','',''], ['','',''], ['','O','B'], ['','',''], ['','',''], ['O','',''], ['B','Y','R'], ['','','']],
    [['',''], ['',''], ['B','O'], ['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['O','G'], ['Y','B'], ['','']]
)

# webcam3.jpg
# correct_state = ColorState(
#     [['Y','',''], ['Y','R','B'], ['','',''], ['','',''], ['','',''], ['','G','R'], ['','',''], ['','','']],
#     [['',''], ['R','G'], ['',''], ['',''], ['W','R'], ['Y','B'], ['',''], ['',''], ['',''], ['',''], ['',''], ['','']]
# )

def Set_color_state(color, port, index):
    if port == 1:
        if index == 0:
            color_state.cc[2][2] = color
        elif index == 1:
            color_state.cc[2][1] = color
        elif index == 2:
            color_state.ec[2][0] = color
        elif index == 3:
            color_state.ec[2][1] = color
        elif index == 4:
            color_state.cc[6][1] = color
        elif index == 5:
            color_state.cc[6][2] = color
        elif index == 6:
            color_state.cc[6][0] = color
        elif index == 7:
            color_state.ec[10][1] = color
        elif index == 8:
            color_state.ec[10][0] = color
        elif index == 9:
            color_state.ec[9][1] = color
        elif index == 10:
            color_state.ec[9][0] = color
        elif index == 11:
            color_state.cc[5][0] = color

    elif port == 2:
        if index == 0:
            color_state.cc[0][2] = color
        elif index == 1:
            color_state.cc[0][1] = color
        elif index == 2:
            color_state.ec[0][0] = color
        elif index == 3:
            color_state.ec[0][1] = color
        elif index == 4:
            color_state.cc[4][1] = color
        elif index == 5:
            color_state.cc[4][2] = color
        elif index == 6:
            color_state.cc[4][0] = color
        elif index == 7:
            color_state.ec[8][1] = color
        elif index == 8:
            color_state.ec[8][0] = color
        elif index == 9:
            color_state.ec[11][1] = color
        elif index == 10:
            color_state.ec[11][0] = color
        elif index == 11:
            color_state.cc[7][0] = color

    elif port == 3:
        if index == 0:
            color_state.cc[1][0] = color
        elif index == 1:
            color_state.cc[1][1] = color
        elif index == 2:
            color_state.cc[1][2] = color
        elif index == 3:
            color_state.ec[5][0] = color
        elif index == 4:
            color_state.ec[5][1] = color
        elif index == 5:
            color_state.ec[4][0] = color
        elif index == 6:
            color_state.ec[4][1] = color
        elif index == 7:
            color_state.cc[0][0] = color
        elif index == 8:
            color_state.ec[1][0] = color
        elif index == 9:
            color_state.ec[1][1] = color
        elif index == 10:
            color_state.cc[5][2] = color
        elif index == 11:
            color_state.cc[5][1] = color

    elif port == 4:
        if index == 0:
            color_state.cc[3][0] = color
        elif index == 1:
            color_state.cc[3][1] = color
        elif index == 2:
            color_state.cc[3][2] = color
        elif index == 3:
            color_state.ec[7][0] = color
        elif index == 4:
            color_state.ec[7][1] = color
        elif index == 5:
            color_state.ec[6][0] = color
        elif index == 6:
            color_state.ec[6][1] = color
        elif index == 7:
            color_state.cc[0][0] = color
        elif index == 8:
            color_state.ec[3][0] = color
        elif index == 9:
            color_state.ec[3][1] = color
        elif index == 10:
            color_state.cc[7][2] = color
        elif index == 11:
            color_state.cc[7][1] = color

k_nn = knn.K_NN(k = 1) 
# webcam1
train_red = [[5.64, 164.77, 155.87]]
train_blue = [[107.05, 144.05, 220.48], [104.81, 179.99, 89.31], [105.99, 156.25, 188.84], [106.970625, 145.05375, 231.868125]]
train_green = [[55.04, 78.68, 151.31]]
train_orenge = [[7.94, 136.29, 254.84], [5.99375, 150.715, 254.775], [9.1575, 163.935, 168.3375], [11.07, 169.22, 155.98]]
train_yellow = [[35.15, 75.04, 254.41], [34.06, 63.27, 189.34]]
train_white = []
# webcam3
# train_red = [[3.93, 246.88, 133.07], [4.04, 246.06, 122.3], [4.23, 252.13, 93.78], [12.46, 252.04, 59.92]]
# train_blue = [[107.05, 243.13, 197.07], [104.29, 248.01, 79.38]]
# train_green = [[65.37, 218.34, 223.41], [65.18, 216.24, 206.59]]
# train_orenge = []
# train_yellow = [[32.02, 3.66, 255.0], [36.19, 125.51, 179.8], [32.97, 43.0, 238.78]]
# train_white = [[46.3, 16.95, 218.53]]

train_data = train_red + train_blue + train_green + train_orenge + train_yellow + train_white
label = ['R' for i in range(len(train_red))] + \
        ['B' for i in range(len(train_blue))] + \
        ['G' for i in range(len(train_green))] + \
        ['O' for i in range(len(train_orenge))] + \
        ['Y' for i in range(len(train_yellow))] + \
        ['W' for i in range(len(train_white))]

class Camera:
    def __init__(self, xy, port):
        self.xy = xy
        self.port = port

    def Get_hsv(self, imgBox):
        # BGRからHSVに変換
        imgBoxHsv = cv2.cvtColor(imgBox,cv2.COLOR_BGR2HSV)
        # HSV平均値を取得
        # flattenで一次元化しmeanで平均を取得 
        h = imgBoxHsv.T[0].flatten().mean()
        s = imgBoxHsv.T[1].flatten().mean()
        v = imgBoxHsv.T[2].flatten().mean()

        # HSV平均値を出力
        hsv = [h, s, v]
        # print(list(map(round, hsv, [2]*len(hsv))))

        return [h, s, v]

    def Identificate_color(self, hsv):
        k_nn.fit(train_data, label)
        color = k_nn.predict([hsv])

        # print(color)
        return color

    def camera2color_state(self):
        img = cv2.imread(f'picture/webcam{self.port}.jpg')

        lateral = 30        
        for i in range(len(self.xy)):
            # 対象範囲を切り出し
            imgBox = img[self.xy[i][1]: self.xy[i][1]+lateral, self.xy[i][0]: self.xy[i][0]+lateral]
            # HSVの平均値を取得
            hsv = self.Get_hsv(imgBox)
            print('')
            print('### index = ', i)
            color = self.Identificate_color(hsv)
            Set_color_state(color, self.port, i)

        # draw rectangle
        # cv2.rectangle(img, (self.xy[8][0], self.xy[8][1]), (self.xy[8][0]+lateral, self.xy[8][1]+lateral), (255, 0, 0), thickness=4)
        for i in range(len(self.xy)):
            cv2.rectangle(img, (self.xy[i][0], self.xy[i][1]), (self.xy[i][0]+lateral, self.xy[i][1]+lateral), (255, 0, 0), thickness=4)

        print("cc = ", color_state.cc)
        print("ccc = ", correct_state.cc)
        print("ec = ", color_state.ec)
        print("cec = ", correct_state.ec)
        cv2.imwrite(f'picture/result{self.port}.jpg', img)

def Get_color_state():
    return color_state

xy_camera1 = [[460, 50], [590, 50], [460, 190], [590, 190], [460, 330], [590, 330]]

# xy_camera1 = [[460, 50], [590, 50], [460, 190], [590, 190], [460, 330], [590, 330]]

# xy_camera3 = [[260, 170], [300, 230], [220, 230], [180, 130], [140, 190], [340, 130], [380, 190],
#               [400, 110], [300, 340], [220, 340], [300, 430], [220, 430]]

#main
if __name__ == '__main__':
    try:
        camera1 = Camera(xy_camera1, 1)
        camera1.camera2color_state()
        # camera3 = Camera(xy_camera3, 3)
        # camera3.camera2color_state()

    except KeyboardInterrupt:
        pass