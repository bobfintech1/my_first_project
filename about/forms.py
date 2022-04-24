from django import forms
from about.models import *


class CreateAboutForm(forms.ModelForm):

    class Meta:
        model = AboutModel
        fields = ['title', "body", 'image']


class UpdateAboutForm(forms.ModelForm):

    class Meta:
        model = AboutModel
        fields = ['title', "body", 'image']


class DeleteAboutFrom(forms.ModelForm):

    class Meta:
        model = AboutModel
        fields = ['title', "body", 'image']
