from django import forms
from home.models import *


class CreateHomeForm(forms.ModelForm):

    class Meta:
        model = HomeModel
        fields = ['title', "body", 'image']


class UpdateHomeForm(forms.ModelForm):

    class Meta:
        model = HomeModel
        fields = ['title', "body", 'image']


class DeleteHomeFrom(forms.ModelForm):

    class Meta:
        model = HomeModel
        fields = ['title', "body", 'image']
