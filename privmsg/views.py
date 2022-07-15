from re import template
from django.shortcuts import render, redirect
# from numpy import product
from product import contactForm

from product.models import ProductBase
from .models import prvMsg
from .msg_form import UserForm
from product.contactForm import msgForm
# Create your views here.


def RecivedPM(request):
    msg_rcv = prvMsg.objects.filter(
        reciver_id=request.user).order_by('-sendDate')
    template = "privmsg/odebrane.html"
    context = {'msgrcv': msg_rcv,
               }

    return render(request, template, context)


def writeMsg(request, msgSlug):

    if not msgSlug:
        if request.method == 'POST':
            user_form = UserForm(data=request.POST)
            if user_form.is_valid():
                # pobiera i automatycznie wpisuje do modelu user_id
                user_form.instance.sender_id = request.user
                user_form.save()
                return redirect('/msg/odebrane')

        else:
            user_form = UserForm()

    else:
        if request.method == 'POST':
            detail = prvMsg.objects.get(slug=msgSlug)
            user_form = msgForm(data=request.POST)
            if user_form.is_valid():
                user_form.instance.sender_id = request.user
                user_form.instance.reciver_id = detail.sender_id
                user_form.instance.is_open = False
                user_form.instance.title = detail.title
                user_form.save()

        else:
            user_form = msgForm()

    context = {'user_form': user_form}
    template = "privmsg/napisz.html"

    return render(request, template, context)


def readMsg(request, msgSlug):
    template = "privmsg/wiadomosc.html"
    message = prvMsg.objects.get(slug=msgSlug)
    prvMsg.objects.filter(slug=msgSlug).update(is_open=True)
    context = {'message': message,
               }

    return render(request, template, context)
