import numpy as np
import matplotlib.pyplot as plt
import os
from math import *
from scipy.interpolate import griddata

prediction=np.load('prediction.npy')

print(prediction.shape)

theta=np.linspace(atan(0.5)-np.pi, np.pi-atan(0.5), 32)*180.0/np.pi   #-150~150
fai=np.linspace(-85/180.0*np.pi, 85/180.0*np.pi, 24)*180.0/np.pi          #0~150
X_theta, Y_fai = np.meshgrid(theta, fai)



x1=np.linspace(-30,30,32)
y1=np.linspace(-10,10,24)

'''
x = np.linspace(theta[0], theta[-1], 1000)
y = np.linspace(fai[0], fai[-1], 1000)
X_theta1, Y_fai1 = np.meshgrid(x, y)
prediction1 = griddata((X_theta.flatten(), Y_fai.flatten()), prediction[0,:,:,0].flatten(), (X_theta1.flatten(), Y_fai1.flatten()), method='nearest')
'''

#print(X_theta.flatten())

for i in range(200):
    fig = plt.figure(figsize=(7, 5))
    plt.rcParams['font.size'] = 16

    #pcm=plt.pcolor(x,y,prediction1.reshape([1000,1000]),cmap='RdYlBu_r')

    pcm=plt.pcolor(theta,fai,prediction[i,:,:,0],clim=[0,1.0],cmap='plasma')
    plt.colorbar(pcm, extend='both')
    plt.xlabel(r'$\theta$(°)',fontsize=18)
    plt.ylabel(r'$\phi$(°)',fontsize=18)
    plt.subplots_adjust(top=0.95,bottom=0.18,left=0.13,right=0.98)
    plt.savefig('predict1/surf%d.png' %i,dpi=300)
    #plt.show()



    fig = plt.figure(figsize=(3, 6.5))
    plt.rcParams['font.size'] = 16

    pcm=plt.pcolor(y1,x1,prediction[i,:,:,1].transpose(),clim=[0,1.0],cmap='plasma')

    #plt.colorbar(pcm, extend='both')
    plt.yticks([]) 
    plt.xticks([]) 
    #plt.xlabel(r'$\theta$(°)',fontsize=18)
    #plt.ylabel(r'$\phi$(°)',fontsize=18)
    plt.savefig('predict1/sub%d.png' %i,dpi=300)
    #plt.show()

