import os

from trainer import Trainer, TrainerArgs

from TTS.config.shared_configs import BaseAudioConfig
from TTS.tts.configs.shared_configs import BaseDatasetConfig, CapacitronVAEConfig
from TTS.tts.configs.tacotron2_config import Tacotron2Config
from TTS.tts.datasets import load_tts_samples, common_voice
from TTS.tts.models.tacotron2 import Tacotron2
from TTS.tts.utils.text.tokenizer import TTSTokenizer
from TTS.tts.utils.speakers import SpeakerManager
from TTS.utils.audio import AudioProcessor

output_path = os.path.dirname(os.path.abspath(__file__))

data_path = "zh-HK/"

# Using LJSpeech like dataset processing for the blizzard dataset
dataset_config = BaseDatasetConfig(
    name="zh-HK",
    meta_file_train="train.tsv",
    path=data_path,
)

# Audio files settings
audio_config = BaseAudioConfig(
    sample_rate=22050,
    do_trim_silence=True,
    trim_db=60.0,
    signal_norm=False,
    mel_fmin=0.0,
    mel_fmax=11025,
    spec_gain=1.0,
    log_func="np.log",
    ref_level_db=20,
    preemphasis=0.0,
)

# Using the standard Capacitron config
capacitron_config = CapacitronVAEConfig(capacitron_VAE_loss_alpha=1.0, capacitron_capacity=50)

# Suggested Tacotron2 config
config = Tacotron2Config(
    run_name="Capacitron-Tacotron2",
    audio=audio_config,
    capacitron_vae=capacitron_config,
    use_capacitron_vae=True,
    batch_size=128,  # Tune this to your gpu
    max_audio_len=8 * 22050,  # Tune this to your gpu
    min_audio_len=1 * 22050,
    eval_batch_size=16,
    num_loader_workers=8,
    num_eval_loader_workers=8,
    precompute_num_workers=24,
    run_eval=True,
    test_delay_epochs=25,
    ga_alpha=0.0,
    r=2,
    optimizer="CapacitronOptimizer",
    optimizer_params={"RAdam": {"betas": [0.9, 0.998], "weight_decay": 1e-6}, "SGD": {"lr": 1e-5, "momentum": 0.9}},
    attention_type="dynamic_convolution",
    grad_clip=0.0,  # Important! We overwrite the standard grad_clip with capacitron_grad_clip
    double_decoder_consistency=False,
    epochs=1000,
    text_cleaner="phoneme_cleaners",
    use_phonemes=True,
    phoneme_language="yue", # Specify language to be yue aka cantonese
    phonemizer="espeak", # We use espeak as it supports zh-yue phoneme
    phoneme_cache_path=os.path.join(data_path, "phoneme_cache"),
    stopnet_pos_weight=15,
    print_step=25,
    print_eval=True,
    mixed_precision=False,
    sort_by_audio_len=True,
    seq_len_norm=True,
    output_path=output_path,
    datasets=[dataset_config],
    lr=1e-3,
    lr_scheduler="StepwiseGradualLR",
    lr_scheduler_params={
        "gradual_learning_rates": [
            [0, 1e-3],
            [2e4, 5e-4],
            [4e5, 3e-4],
            [6e4, 1e-4],
            [8e4, 5e-5],
        ]
    },
    scheduler_after_epoch=False,  # scheduler doesn't work without this flag
    # Need to experiment with these below for capacitron
    loss_masking=False,
    decoder_loss_alpha=1.0,
    postnet_loss_alpha=1.0,
    postnet_diff_spec_alpha=0.0,
    decoder_diff_spec_alpha=0.0,
    decoder_ssim_alpha=0.0,
    postnet_ssim_alpha=0.0,
)

# Audio processor
ap = AudioProcessor(**config.audio.to_dict())

# Tokenizer with config settings
tokenizer, config = TTSTokenizer.init_from_config(config)

# Split dataset for training and evaluation
# Dataset formatter is specified here as we are using CommonVoice dataset
train_samples, eval_samples = load_tts_samples(dataset_config, eval_split=True, formatter = common_voice)

# Speak Manager for multi speaker training
# Referencing different speaker with their ID
# Useful in synthesizing speeches with targetted speaker's voice
speaker_manager = SpeakerManager()
speaker_manager.set_ids_from_data(train_samples + eval_samples, parse_key="speaker_name")
config.num_speakers = speaker_manager.num_speakers

# Define model, using Tacotron2 framework
model = Tacotron2(config, ap, tokenizer, speaker_manager=speaker_manager)

# Obtain Trainer
trainer = Trainer(
    TrainerArgs(),
    config,
    output_path,
    model=model,
    train_samples=train_samples,
    eval_samples=eval_samples,
    training_assets={"audio_processor": ap},
)

# Start training
trainer.fit()
