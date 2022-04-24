from django import forms
from post.models import PostModel


class CreatePostForm(forms.ModelForm):

    class Meta:
        model = PostModel
        fields = ['title', 'body', 'image']


class UpdatePostForm(forms.ModelForm):

    class Meta:
        model = PostModel
        fields = ['title', 'body', 'image']


class DeletePostFrom(forms.ModelForm):

    class Meta:
        model = PostModel
        fields = ['title', 'body', 'image']
