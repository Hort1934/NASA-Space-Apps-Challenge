# Ваша forms.py
from django import forms

class VideoForm(forms.Form):
    video_file = forms.FileField(label='Виберіть відеофайл')
