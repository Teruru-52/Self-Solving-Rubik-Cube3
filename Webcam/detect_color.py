import cv2
import numpy as np

class ColorState:
    def __init__(self, cc, ec):
        self.cc = cc
        self.ec = ec

color_state = ColorState(
            [['','',''], ['','',''], ['','',''], ['','',''], ['','',''], ['','',''], ['','',''], ['','','']],
            [['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['',''], ['','']]
        )

def Set_color_state(color, camera_no, index):
    if camera_no == 1:
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

def Mask_color():
    img = cv2.imread('picture/001.jpg')
    #BGR色空間からHSV色空間への変換
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #色検出しきい値の設定
    lower = np.array([90, 64, 0])
    upper = np.array([150,255,255])

    #色検出しきい値範囲内の色を抽出するマスクを作成
    frame_mask = cv2.inRange(hsv, lower, upper)

    #論理演算で色検出
    dst = cv2.bitwise_and(img, img, mask=frame_mask)
    cv2.imwrite('picture/blue.jpg', dst)
    

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

        return [h, s, v]

    def Identificate_color(self, hsv):
        # 各色のHSV値のしきい値
        red_lower = [255, 255, 180]
        red_upper = [230, 150, 255]
        blue_lower = [0, 100, 80]
        blue_upper = [0, 100, 80]
        green_lower = [0, 100, 80]
        green_upper = [0, 100, 80]
        orenge_lower = [0, 100, 80]
        orenge_upper = [0, 100, 80]
        white_lower = [0, 100, 80]
        white_upper = [0, 100, 80]
        yellow_lower = [0, 100, 80]
        yellow_upper = [0, 100, 80]

        # if (hsv > red_lower) & (hsv < red_upper):
        #     color = 'R'
        # else:
        #     color = 'N'

        # cube_color = {'R':red, 'B':blue, 'G':green, 'O':orenge, 'W':white, 'Y':yellow}
        # 0にiterationを代入する
        # color = list(cube_color.keys())[0]
        color = 'R'
        # print(color)
        return color

    def camera2color_state(self):
        img = cv2.imread('picture/001.jpg')

        lateral = 40
        # draw rectangle
        for i in range(12):
            cv2.rectangle(img, (self.xy[i][0], self.xy[i][1]), (self.xy[i][0]+lateral, self.xy[i][1]+lateral), (255, 0, 0), thickness=4)
        
        for i in range(12):
            # 対象範囲を切り出し
            imgBox = img[self.xy[i][1]: self.xy[i][1]+lateral, self.xy[i][0]: self.xy[i][0]+lateral]
            # HSVの平均値を取得
            hsv = self.Get_hsv(imgBox)
            color = self.Identificate_color(hsv)
            Set_color_state(color, self.cam_no, i)

        print("cc = ", color_state.cc)
        print("ec = ", color_state.ec)
        cv2.imwrite('picture/result.jpg', img)

def Get_color_state():
    return color_state

xy_camera1 = [[460, 50], [590, 50], [460, 190], [590, 190], [460, 330], [590, 330], [525, 450],
              [360, 380], [400, 490], [690, 380], [650, 490], [710, 515]]

#main
if __name__ == '__main__':
    try:
        Mask_color()
        # camera1 = Camera(xy_camera1, 1)
        # camera1.camera2color_state()

    except KeyboardInterrupt:
        pass