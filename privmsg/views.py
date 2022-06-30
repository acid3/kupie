from re import template
from django.shortcuts import render, redirect
from .models import prvMsg
from .msg_form import UserForm
# Create your views here.


def RecivedPM(request):
    msg_rcv = prvMsg.objects.filter(reciver_id=request.user)

    template = "privmsg/odebrane.html"

    # context = "chuj"
    context = {'msgrcv': msg_rcv,
               }

    return render(request, template, context)


def writeMsg(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            # pobiera i automatycznie wpisuje do modelu user_id
            user_form.instance.sender_id = request.user
            user_form.save()
            return redirect('/msg/odebrane')

    else:
        user_form = UserForm()

    context = {'user_form': user_form}
    template = "privmsg/napisz.html"

    return render(request, template, context)

