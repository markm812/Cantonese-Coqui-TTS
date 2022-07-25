import soundfile as sf

data, samplerate = sf.read('zh-HK\clips\common_voice_zh-HK_24364491.wav')
print(data)
print(samplerate)
