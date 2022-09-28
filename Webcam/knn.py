import numpy as np
import scipy.spatial.distance as distance
import scipy.stats as stats

class K_NN:
    def __init__(self, k):
        self.k = k
        self.training_data = None  # 既存データを格納 
        self.classes = None  #
        self._y = None

    def fit(self, training_data, label):
        # training_dataは元のデータ点で、shape(data_num, feature_num)
        # print("original data:\n", training_data)
        print("label:\n", label)
        self.training_data = training_data
        # ラベルデータからクラスを抽出、またラベルをindexとした配列を作成
        # self.classes[self.label_indices] == label のように復元できるのでreturn_inverseという
        self.classes, self.label_indices = np.unique(label, return_inverse=True)
        print("classes:\n", self.classes)
        print("label_indices:\n", self.label_indices)
        # print("classes[label_indices]で復元されるか確認:\n", self.classes[self.label_indices])
    
    def neighbors(self, validation_data):
        dist = distance.cdist(validation_data, self.training_data)
        print("訓練データと検証データとの距離:\n", dist)

        # 距離を測定したらk番目までに含まれるindexをもとめる
        # argpartitionはk番目までと、それ以降にデータを分ける関数
        # argsortだと距離の順位もわかるが、素のk-nnでは距離順位の情報はいらないので、argpartitionを使う
        neigh_ind = np.argpartition(dist, self.k)
        # neigh_indのshapeは(test_num, feature_num)となる
        # 上のdistでk=2でargpartitionしたときの結果
        # 例えば1行目だと index 2,1 が上位2要素になっている。上の距離をみると、0.5と1.5が相当する
        # 2行目だと index 3, 2 が上位2要素で、1.73と1.80が相当する
        #[[1 0 3 2]
        # [3 2 1 0]
        # [2 3 1 0]]
        # k番目までの情報だけを取り出す
        neigh_ind = neigh_ind[:, :self.k]
        # neigh_indのshapeは(test_num, self.k)となる
        #[[1 0]   テスト点1に近い元データ点のindexのリスト
        # [3 2]   テスト点2に近い元データ点のindexのリスト
        # [2 3]]  テスト点3に近い元データ点のindexのリスト
        return neigh_ind
    
    def predict(self, validation_data):
        # k番目までのindexを求める shape(test_num, self.k)となる
        print("verification data:\n",validation_data)
        neigh_ind = self.neighbors(validation_data)
        # stats.modeでその最頻値を求める. shape(test_num, 1) . _は最頻値のカウント数
        # self.label_indices は [0 0 1 1] で、元データの各点のラベルを表す
        # neigh_indは各テスト点に近い元データのindexのリストで shape(est_num, k)となる
        # self.label_indices[neigh_ind] で、以下のような各テスト点に近いラベルのリストを取得できる
        # [[0 0]  テスト点1に近い元データ点のラベルのリスト
        #  [1 1]  テスト点2に近い元データ点のラベルのリスト
        #  [1 1]] テスト点3に近い元データ点のラベルのリスト
        # 上記データの行方向(axis=1)に対してmode(最頻値)をとり、各テスト点が属するラベルとする
        # _はカウント数
        mode, _ = stats.mode(self.label_indices[neigh_ind], axis=1)
        # modeはaxis=1で集計しているのでshape(test_num, 1)となるので、ravel(=flatten)してやる
        # [[0]
        #  [1]
        #  [1]]
        # なおnp.intpはindexに使うデータ型
        mode = np.asarray(mode.ravel(), dtype=np.intp)
        print("test dataの各ラベルindexの最頻値:\n",mode)
        # index表記からラベル名表記にする. self.classes[mode] と同じ
        result = self.classes.take(mode)
        return (' '.join(result.tolist()))

#main
if __name__ == '__main__':
    k_nn = K_NN(k = 1)
    training_red = [[5.64, 164.77, 155.87]]
    training_blue = [[107.05, 144.05, 220.48]]
    training_green = [[55.04, 78.68, 151.31]]
    training_orenge = [[7.94, 136.29, 254.84]]
    training_yellow = [[35.15, 75.04, 254.41]]
    # 元のデータとラベルをセット
    training_data = training_red + training_blue + training_green + training_orenge + training_yellow
    label = ['R' for i in range(len(training_red))] + \
             ['B' for i in range(len(training_blue))] + \
             ['G' for i in range(len(training_green))] + \
             ['O' for i in range(len(training_orenge))] + \
             ['Y' for i in range(len(training_yellow))]

    k_nn.fit(training_data, label)
    # 予測したいデータ
    validation_data = training_yellow
    result = k_nn.predict(validation_data)
    print("result:\n", result)