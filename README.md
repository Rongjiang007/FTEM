## Introduction
We design a tunnel electromagnetic joint scan observation system and present a deep learning-based parametric inversion for improved tunnel electromagnetic imaging, designed specifically for tunnel prediction of water filled structures. It utilizes a configuration wherein transmitters scan along the surface while receivers are positioned within the tunnel, employing time-domain and frequency-domain transmitters and a multi-component receiver. The DL model for the first time provides parametric imaging of two different view, forming a self-checking mechanism, which can help constrain the predictions and reduce the non-uniqueness of the inversion. Trained by synthetic data, our system shows impressive adaptability to predict the 3D spatial position of water-filled anomalies and strong robustness in the tunnel environment
with metal interference.

## Dependencies
Ubuntu 22.04.1 LTS
Python 3.10.6
SimPEG 0.18.1
scipy  1.10.0
numpy 1.23.5
tensorflow 2.10.0

## Install
pip install -r requirement.txt
conda install SimPEG --channel conda-forge
For SimPEG, you may refer to more detail at  https://docs.simpeg.xyz/latest/content/getting_started/installing.html


## To achieve prediction, run:

Before prediction, you need to download the pre-trained weight model from https://zenodo.org/records/14745131, which contain UNet_model/FTEM.ckpt.data-00000-of-00001, UNet_model/FTEM.ckpt.index, UNet_model/FTEM.h5. Then place the directory containing the weight model in the same directory as the prediction code.
Then run: python predi.py

The program will read data from directory 3. The data is obtained through scanning observations, allowing for the prediction of the three-dimensional spatial location of the underground water-filled structures.

FTEM_batch_train.ipynb is used to train a new model. The traindata can be download from https://zenodo.org/records/11407019

The Topo directory provides specific examples for terrain-based prediction, gdata.ipynb is used to generate electromagnetic field observation data with terrain, and predi.py is used to predict the data and results will be saved in creted dir by gdata. The prediction results are saved in the "predict" folder.





## License

This project is licensed under the MIT License.
