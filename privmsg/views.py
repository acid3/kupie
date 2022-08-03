from re import template
from django.shortcuts import render, redirect
# from numpy import product
from product import contactForm
from django.db.models import Q
from product.models import ProductBase
from .models import prvMsg
from .msg_form import UserForm
from product.contactForm import msgForm
# Create your views here.


# def RecivedPM(request):
#     msg_rcv = prvMsg.objects.filter(
#         reciver_id=request.user).order_by('-sendDate')
#     template = "privmsg/odebrane.html"
#     context = {'msgrcv': msg_rcv,
#                }

#     return render(request, template, context)


# zmiana dla testu pusha dla branchu 'message'
def test_dla_testu():
    pass


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
                return redirect('/msg/odebrane')

        else:
            user_form = msgForm()

    context = {'user_form': user_form}
    template = "privmsg/napisz.html"

    return render(request, template, context)


def readMsg(request, msgSlug):
    template = "privmsg/wiadomosc.html"
    message = prvMsg.objects.get(slug=msgSlug)

    logged_user_msg = prvMsg.objects.filter(
        Q(reciver_id=request.user) | (Q(sender_id=request.user)))
    sender_msg = logged_user_msg.filter(
        Q(sender_id=message.sender_id) | Q(reciver_id=message.sender_id))
    actual_msg = sender_msg.filter(Q(title=message.title))
    czat = actual_msg.order_by('sendDate')

    prvMsg.objects.filter(slug=msgSlug).update(is_open=True)
    context = {'message': message,
               'czat': czat,
               }

    return render(request, template, context)
