from django.urls import path
from . views import RecivedPM, writeMsg, readMsg


app_name = 'accounts'

urlpatterns = [
    path('odebrane/' , RecivedPM , name='recived') , 
    path('napisz/', writeMsg, name='write'),
    path('odebrane/<slug:msgSlug>', readMsg, name='readmsg' ),
    path('napisz/<slug:msgSlug>', writeMsg, name='replay'),

    # path('wyslane/', AdminLogin.as_view(), name="login"),
]
