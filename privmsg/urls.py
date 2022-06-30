from django.urls import path
from . views import RecivedPM, writeMsg


app_name = 'accounts'

urlpatterns = [
    path('odebrane/' , RecivedPM , name='recived') , 
    path('napisz/', writeMsg, name='write'),
    # path('wyslane/', AdminLogin.as_view(), name="login"),

]
