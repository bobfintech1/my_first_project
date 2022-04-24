from django import forms
from contact.models import ContactModel


class CreateContactForm(forms.ModelForm):

    class Meta:
        model = ContactModel
        fields = ['title', 'body', 'image']


class UpdateContactForm(forms.ModelForm):

    class Meta:
        model = ContactModel
        fields = ['title', 'body', 'image']


class DeleteContactFrom(forms.ModelForm):

    class Meta:
        model = ContactModel
        fields = ['title', 'body', 'image']
