from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
import os
from math import *

model = load_model('UNet_model/FTEM.h5')
model.load_weights('UNet_model/FTEM.ckpt')


def plot_comp(prediction,i,X_source):
    fig = plt.figure(figsize=(8, 6))
    grid=plt.GridSpec(8,6,wspace=1.3,hspace=1.0)
    mianplot=plt.subplot(grid[0:8,0:4])
    y1=np.linspace(X_source-10,X_source+10,24)
    #print(theta.shape,fai.shape,prediction[i,:,:,0].shape)
    dat1=plt.pcolor(theta,fai,submap,clim=[0,1.0], cmap='plasma') 
    plt.xlabel(r'$\theta$(°)')
    plt.ylabel(r'$\phi$(°)')
    plt.xlim(-160,160)

    subplot=plt.subplot(grid[0:8,4:6])
    dat2=plt.pcolor(y1,x1,prediction[i,:,:,1].transpose(),clim=[0,1.0], cmap='plasma') 
    #dat1=ax[2].pcolor(theta,fai,prediction[i,:,:,1],clim=[0,1.0], cmap='plasma') 
    #cb = plt.colorbar(dat1,orientation="horizontal")
    #cb.set_label('Probability')
    
    plt.xlabel(r'$X (m)$')
    #plt.ylabel(r'$Y (m)$',fontsize=20)
    #ax[1].tick_params(labelsize=15)
    
    plt.subplots_adjust(top=0.95,bottom=0.18,left=0.13,right=0.95)
    plt.savefig('predict/'+str(i)+'.jpg',dpi=300)



Np=20

dir1='data'
filename=[]
def read_file(dir1):
    data1=[]
    data2=[]
    files= os.listdir(dir1)
    
    for i in range(Np):
        file='Inpt_'+str(i)
        filename.append(file)
        data0=np.load(dir1+'/'+file+'.npy')
        data1.append(data0)
        filelbale='label_pdf_'+str(i)+'.npy'
        data0=np.load(dir1+'/'+filelbale)
        data2.append(data0)
    return np.array(data1),np.array(data2)


data_traing,data_traing_label=read_file(dir1)
data_traing_input_tf=data_traing.transpose(0,2,3,1)
data_traing_label_tf=data_traing_label.transpose(0,2,3,1)
#data_traing_input_tf[:,:,3:,:]=0
#data_traing_label_tf=data_traing_label
print(data_traing_label_tf.shape)

X=np.linspace(-20,30,20)


#print(filename)
prediction = model.predict(data_traing_input_tf)
np.save('prediction.npy',prediction)

plt.rcParams['font.size'] = 20
theta=np.linspace(atan(0.5)-np.pi, np.pi-atan(0.5), 32)*180.0/np.pi   #-150~150
fai=np.linspace(-85/180.0*np.pi, 85/180.0*np.pi, 24)*180.0/np.pi          #0~150

x1=np.linspace(-30,30,32)
y1=np.linspace(-10,10,24)

print(prediction.shape,data_traing_label_tf.shape)
submap=np.mean(prediction[:,:,:,0],axis=0)
#print(submap.shape)
for i in range(Np):
    #print(prediction)
    plot_comp(prediction,i,X[i])
    '''
    fig, ax = plt.subplots(2,2, figsize = (12, 10))

    y1=np.linspace(X[i]-10,X[i]+10,24)
    dat0=ax[0][0].pcolor(theta,fai,data_traing_label_tf[i,:,:,0],clim=[0,1.0], cmap='plasma')
    dat0=ax[0][1].pcolor(x1,y1,data_traing_label_tf[i,:,:,1],clim=[0,1.0], cmap='plasma')
    #cb = plt.colorbar(dat0,orientation="vertical",ax = ax[0])
    #ax[0].set_xlabel(r'$\theta$(°)',fontsize=23)
    #ax[0].set_ylabel(r'$\phi$(°)',fontsize=23)
    ax[0][0].set_xlim(-160,160)
    #ax[0].tick_params(labelsize=15)



    dat1=ax[1][0].pcolor(theta,fai,prediction[i,:,:,0],clim=[0,1.0], cmap='plasma') 
    dat1=ax[1][1].pcolor(x1,y1,prediction[i,:,:,1],clim=[0,1.0], cmap='plasma') 
    #dat1=ax[2].pcolor(theta,fai,prediction[i,:,:,1],clim=[0,1.0], cmap='plasma') 
    #cb = plt.colorbar(dat1,orientation="horizontal")
    #cb.set_label('Probability')

    ax[1][0].set_xlabel(r'$\theta$(°)',fontsize=23)
    ax[1][0].set_ylabel(r'$\phi$(°)',fontsize=23)
    #ax[1].tick_params(labelsize=15)
    ax[1][0].set_xlim(-160,160)
    plt.subplots_adjust(top=0.95,bottom=0.18,left=0.1,right=0.95)
    plt.savefig('predict_pic/'+str(i)+'.png',dpi=300)
    plt.close()
    '''



    
#ax.set_title(r'$f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$')
