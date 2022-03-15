from tkinter import Widget
from django.forms import ModelForm, Textarea

from .models import Chat

class ChatForm(ModelForm):
    class Meta:
        model = Chat
        fields = "__all__"
        exclude = ('author',)
        Widget = { 'body': Textarea(),
        }