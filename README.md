# Cantonese-Coqui-TTS

Original Repo:
https://github.com/coqui-ai/TTS
## Important: 
### This application only works in Linux environment
### Use WSL/VM if you are on WindowsOS
## Install requirements
### Setup CUDA 10.1 (update 2) before installing requirements
Follow the documentation by Nvidia: https://docs.nvidia.com/cuda/archive/10.1/
For WSL:
```
wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin
sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/11.7.0/local_installers/cuda-repo-wsl-ubuntu-11-7-local_11.7.0-1_amd64.deb
sudo dpkg -i cuda-repo-wsl-ubuntu-11-7-local_11.7.0-1_amd64.deb
sudo cp /var/cuda-repo-wsl-ubuntu-11-7-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cuda
```
For Ubuntu 18.04:
```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pin
sudo mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/11.7.0/local_installers/cuda-repo-ubuntu1804-11-7-local_11.7.0-515.43.04-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1804-11-7-local_11.7.0-515.43.04-1_amd64.deb
sudo cp /var/cuda-repo-ubuntu1804-11-7-local/cuda-*-keyring.gpg /usr/share/keyrings/
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
## Run training (Capacitron_Tacotron2)

### With dataset from CommonVoice zh-HK
```
python train_capacitron_t2.py
```

### You can find more useful template inside recipes/, or refer to the original repo by CoquiAI
### More dataset formatter can be found in Cantonese-Coqui-TTS/TTS/tts/datasets/formatters.py 
### You may also define your own dataset formatter according to https://tts.readthedocs.io/en/latest/formatting_your_dataset.html
