# Cantonese-Coqui-TTS

Original Repo:
https://github.com/coqui-ai/TTS
## Important: 
### This application only works in Linux environment
### Use WSL/VM if you are on WindowsOS
## Install requirements
### Setup CUDA 10.1 (update 2) before installing requirements
Follow the documentation by Nvidia: https://docs.nvidia.com/cuda/archive/10.1/  
#### For WSL:
```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pin
sudo mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/ /"
sudo apt-get update
sudo apt-get -y install cuda
```
#### For Ubuntu 18.04:
```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pin
sudo mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/10.1/Prod/local_installers/cuda-repo-ubuntu1804-10-1-local-10.1.243-418.87.00_1.0-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1804-10-1-local-10.1.243-418.87.00_1.0-1_amd64.deb
sudo apt-key add /var/cuda-repo-10-1-local-10.1.243-418.87.00/7fa2af80.pub
sudo apt-get update
sudo apt-get -y install cuda
```
## Installation Error
If you are encountering any installation errors related to `repo not signed/public key error`:  
Please remove the outdated key and install the demanded one.  
For more details please refer to: https://forums.developer.nvidia.com/t/notice-cuda-linux-repository-key-rotation/212771
### Suggest using Python3.8
```
pip install -e .[all]
```
### If you have problem related to `espeak not found` or `language yue not supported by espeak`, please do:
```
sudo apt-get install espeak-ng
```
## Run training (Capacitron_Tacotron2)

### With dataset from CommonVoice zh-HK
```
python train_capacitron_t2.py
```
#### If you have problem regarding `assert sample rate`, please take care of following:
```
Use librosa/pudub to resample your dataset to the same sample rate; same as your defined sameple rate in `audio_config` in your `train.py`
```
### You can find more useful template inside recipes/, or refer to the original repo by CoquiAI
### More dataset formatter can be found in Cantonese-Coqui-TTS/TTS/tts/datasets/formatters.py 
### You may also define your own dataset formatter according to https://tts.readthedocs.io/en/latest/formatting_your_dataset.html
