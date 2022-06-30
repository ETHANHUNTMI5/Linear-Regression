import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


X = pd.read_csv(r"C:\Users\pujit\OneDrive\Desktop\PYTHON\DATASET\Linear_X_Train.csv")
Y = pd.read_csv(r"C:\Users\pujit\OneDrive\Desktop\PYTHON\DATASET\Linear_Y_Train.csv")

theta = np.load("ThetaList.npy")


T0 = theta[:,0]
T1 = theta[:,1]

plt.ion()
# i.e i + on where i is interactive
for i in range(0,100,3):
    y_ = T1[i]*X + T0[i]
    plt.scatter(X,Y)
    plt.plot(X,y_,"red")
    plt.draw()
    plt.pause(1)
    plt.clf()
    