from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
import numpy as np

class FeatureExtractor:
    def __init__(self, n):
        self.n = n

    def correlogram(self, m):
        corr = np.zeros((256, 256))
        for i in range(self.n, len(m)-self.n):
            for j in range(self.n, len(m[0])-self.n):
                res = ""
                for k in range(i-self.n, i+self.n+1):
                    for r in range(j-self.n, j+self.n+1):
                        if k==i and r ==j :
                            res = res+"    "
                        else :          
                            corr[m[i][j], m[k][r]] = corr[m[i][j], m[k][r]] + 1
        return corr

    def extract(self, img):
        img = img.resize((250, 250))
        img = np.asarray(img.convert('RGB'))
        blue = img[:, :, 0]
        corr_blue = self.correlogram(blue)
        feature = np.diag(corr_blue)
        green = img[:, :, 1]
        green = self.correlogram(green)
        feature = np.append(feature, np.diag(green))
        mat_red = img[:, :, 2]
        corr_red = self.correlogram(mat_red)
        feature = np.append(feature, np.diag(corr_red))
        return feature


