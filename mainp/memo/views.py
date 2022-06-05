from django.shortcuts import render, redirect
from django.contrib import messages
from memo.forms import ChatForm
from .models import Chat

# Create your views here.
def memo(request):
    chats = Chat.objects.all().order_by('-postime')
    return render(request, 'memo.html', {'chats':chats})


def new(request):
    if request.method == "POST":
        form  = ChatForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Chat created!')
            return redirect('memo')
    else:
        form = ChatForm()
    return render(request , 'input.html', {"form":form})