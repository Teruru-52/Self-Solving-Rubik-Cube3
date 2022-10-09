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
        self.training_data = training_data
        # ラベルデータからクラスを抽出、またラベルをindexとした配列を作成
        # self.classes[self.label_indices] == label のように復元できるのでreturn_inverseという
        self.classes, self.label_indices = np.unique(label, return_inverse=True)
    
    def neighbors(self, validation_data):
        dist = distance.cdist(validation_data, self.training_data)
        # k番目までに含まれるindexをもとめる
        # argpartitionはk番目までと、それ以降にデータを分ける関数
        neigh_ind = np.argpartition(dist, self.k)
        # neigh_indのshapeは(test_num, feature_num)となる
        # 上のdistでk=2でargpartitionしたときの結果
        # k番目までの情報だけを取り出す
        neigh_ind = neigh_ind[:, :self.k]
        # neigh_indのshapeは(test_num, self.k)となる
        return neigh_ind
    
    def predict(self, validation_data):
        # k番目までのindexを求める shape(test_num, self.k)となる
        # print("verification data:\n",validation_data)
        neigh_ind = self.neighbors(validation_data)
        # stats.modeでその最頻値を求める. shape(test_num, 1) . _は最頻値のカウント数
        # self.label_indices は [0 0 1 1] で、元データの各点のラベルを表す
        # neigh_indは各テスト点に近い元データのindexのリストで shape(est_num, k)となる
        # self.label_indices[neigh_ind] で、以下のような各テスト点に近いラベルのリストを取得できる
        # 上記データの行方向(axis=1)に対してmode(最頻値)をとり、各テスト点が属するラベルとする
        mode, _ = stats.mode(self.label_indices[neigh_ind], axis=1)
        # np.intpはindexに使うデータ型
        mode = np.asarray(mode.ravel(), dtype=np.intp)
        result = self.classes.take(mode)
        return (' '.join(result.tolist()))