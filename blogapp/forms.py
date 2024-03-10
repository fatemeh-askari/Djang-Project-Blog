from django.forms import ModelForm, forms
from .models import Comment, ContactUs

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class ContactForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message']