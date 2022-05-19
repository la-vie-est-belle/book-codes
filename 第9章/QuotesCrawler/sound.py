from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from pathlib import Path


class AudioSource:
    def __init__(self):
        super(AudioSource, self).__init__()
        audio_path = Path('./res/audio')
        audio_names = ['button', 'finish', 'saved']

        self.audio_dict = {}
        for name in audio_names:
            sound_effect = QSoundEffect()
            url = QUrl.fromLocalFile(str(audio_path / (name + '.wav')))
            sound_effect.setSource(url)
            self.audio_dict[name] = sound_effect

    def play_audio(self, name, volume=1):
        """通过音频名称进行播放"""
        audio = self.audio_dict.get(name)

        if not audio:
            QMessageBox.critical(self, '错误', '没有这个音频文件！')
            return

        audio.setVolume(volume)
        audio.play()