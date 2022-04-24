from django import forms
from blog.models import BlogModel


class CreateBlogForm(forms.ModelForm):

    class Meta:
        model = BlogModel
        fields = ['title', 'body', 'image']


class UpdateBlogForm(forms.ModelForm):

    class Meta:
        model = BlogModel
        fields = ['title', 'body', 'image']


class DeleteBlogFrom(forms.ModelForm):

    class Meta:
        model = BlogModel
        fields = ['title', 'body', 'image']
