import re

from captcha.fields import CaptchaField, CaptchaTextInput
from django import forms
from django.core.exceptions import ValidationError

from .models import *


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'category', 'preview_content', 'content', 'photo', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'preview_content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'name': 'upload'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        else:
            return title


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['news', 'author', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.HiddenInput(),
            'news': forms.HiddenInput(),
        }


class ContactEmailForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class': 'form-control text-center'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control text-center'}))
    captcha = CaptchaField(label='', widget=CaptchaTextInput(attrs={'class': 'form-control text-center mt-2'}))
