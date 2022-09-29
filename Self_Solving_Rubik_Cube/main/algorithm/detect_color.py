import cv2
import numpy as np
from algorithm import knn

class ColorState:
    def __init__(self, cc, ec):
        self.cc = cc
        self.ec = ec

color_state = ColorState(
    [['','',''], ['','',''], ['','',''], ['','',''], ['','',''], ['','',''], ['','',''], ['','','']],
    [['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['','']]
)

# 要求する完成状態に合わせてここを場合分けする
def Set_color_state(color, camera_no, index):
    if camera_no == 0:
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

    elif camera_no == 2:
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

k_nn = knn.K_NN(k = 1) 
training_red = [[5.64, 164.77, 155.87]]
training_blue = [[107.05, 144.05, 220.48], [104.81, 179.99, 89.31]]
training_green = [[55.04, 78.68, 151.31]]
training_orenge = [[7.94, 136.29, 254.84], [34.06, 63.27, 189.34]]
training_yellow = [[35.15, 75.04, 254.41], [11.07, 169.22, 155.98]]
training_data = training_red + training_blue + training_green + training_orenge + training_yellow
label = ['R' for i in range(len(training_red))] + \
        ['B' for i in range(len(training_blue))] + \
        ['G' for i in range(len(training_green))] + \
        ['O' for i in range(len(training_orenge))] + \
        ['Y' for i in range(len(training_yellow))]

class Camera:
    def __init__(self, xy, cam_no):
        self.xy = xy
        self.cam_no = cam_no

    def Get_hsv(self, imgBox):
        # BGRからHSVに変換
        imgBoxHsv = cv2.cvtColor(imgBox,cv2.COLOR_BGR2HSV)
        # HSV平均値を取得
        # flattenで一次元化しmeanで平均を取得 
        h = imgBoxHsv.T[0].flatten().mean()
        s = imgBoxHsv.T[1].flatten().mean()
        v = imgBoxHsv.T[2].flatten().mean()

        # HSV平均値を出力
        # print("Hue: %.2f" % (h))
        # print("Saturation: %.2f" % (s))
        # print("Value: %.2f" % (v))
        hsv = [h, s, v]
        print(list(map(round, hsv, [2]*len(hsv))))

        return [h, s, v]

    def Identificate_color(self, hsv):
        k_nn.fit(training_data, label)
        color = k_nn.predict([hsv])

        # print(color)
        return color

    def camera2color_state(self):
        img = cv2.imread(f'picture/webcam{self.cam_no}.jpg')

        lateral = 40        
        for i in range(12):
            # 対象範囲を切り出し
            imgBox = img[self.xy[i][1]: self.xy[i][1]+lateral, self.xy[i][0]: self.xy[i][0]+lateral]
            # HSVの平均値を取得
            hsv = self.Get_hsv(imgBox)
            print('')
            print('### index = ', i)
            color = self.Identificate_color(hsv)
            Set_color_state(color, self.cam_no, i)

        # draw rectangle
        # cv2.rectangle(img, (self.xy[6][0], self.xy[6][1]), (self.xy[6][0]+lateral, self.xy[][1]+lateral), (255, 0, 0), thickness=4)
        for i in range(12):
            cv2.rectangle(img, (self.xy[i][0], self.xy[i][1]), (self.xy[i][0]+lateral, self.xy[i][1]+lateral), (255, 0, 0), thickness=4)

        print("cc = ", color_state.cc)
        print("ec = ", color_state.ec)
        cv2.imwrite(f'picture/webcam{self.cam_no}.jpg', img)

    def Take_picture(self):
        capture = cv2.VideoCapture(self.cam_no) # /dev/video*
        capture.set(cv2.CAP_PROP_FPS, 10)
        while True:
            if(capture.isOpened()): # Open
                retval, image = capture.read()
                if retval is False:
                    raise IOError
                text = 'WIDTH={:.0f} HEIGHT={:.0f} FPS={:.0f}'.format(capture.get(cv2.CAP_PROP_FRAME_WIDTH),capture.get(cv2.CAP_PROP_FRAME_HEIGHT),capture.get(cv2.CAP_PROP_FPS))
                cv2.putText(image, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1, 4)
                # cv2.imshow(f'Webcam{self.cam_no}', image)
                cv2.imwrite(f'picture/webcam{self.cam_no}.jpg', image)
                capture.release ()
                cv2.destroyAllWindows()
                break

xy_camera0 = [[460, 50], [590, 50], [460, 190], [590, 190], [460, 330], [590, 330], [525, 450],
              [360, 380], [400, 490], [690, 380], [650, 490], [710, 515]]

camera0 = Camera(xy_camera0, 0)
camera2 = Camera(xy_camera0, 2)
camera4 = Camera(xy_camera0, 4)
camera6 = Camera(xy_camera0, 6)

def Take_pictures():
    camera0.Take_picture()
    camera2.Take_picture()
    camera4.Take_picture()
    camera6.Take_picture()

def Get_color_state():
    # camera0.camera2color_state()
#     camera2.camera2color_state()
#     camera4.camera2color_state()
#     camera6.camera2color_state()
    return color_state