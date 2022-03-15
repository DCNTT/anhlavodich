
from django.forms import ModelForm, Textarea

from .models import Chat

class ChatForm(ModelForm):
    class Meta:
        model = Chat
        fields = "__all__"
        exclude = ('author',)
        Widgets = { 'body': Textarea(),
        }