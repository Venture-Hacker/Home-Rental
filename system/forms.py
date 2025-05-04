from django import forms
from crispy_forms.helper import FormHelper
from .models import House, Order, PrivateMsg

class HouseForm(forms.ModelForm):

    helper = FormHelper()
    helper.form_show_labels = False
    class Meta:
        model = House
        fields = [
            "image",
            "city",
            "house_owner",
            "house_number",
            "cost_per_day",
            "content",
        ]
class OrderForm(forms.ModelForm):

    # added  
    helper = FormHelper()
    helper.form_show_labels = True
    class Meta:
        model = Order
        fields = [
            "city",
            "tenant_name",
            "cell_no",
            "address",
            "from_date",
            "to",
        ]
class MessageForm(forms.ModelForm):
    class Meta:
        model = PrivateMsg
        fields = [
            "name",
            "email",
            "message",
        ]
