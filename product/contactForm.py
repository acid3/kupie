from django import forms
from product.models import ProductBase
from privmsg.models import prvMsg

class msgForm(forms.ModelForm):
    class Meta():
        model = prvMsg
        # fields = [ 'msg', 'sender_id', 'reciver_id']
        fields = [ 'msg']
