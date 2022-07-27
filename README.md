# Cantonese-Coqui-TTS

Original Repo:
https://github.com/coqui-ai/TTS

## Install requirements
### Using Python3.8
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
