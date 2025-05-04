from django import forms
# from .models import Customer, CUSTOMER_TYPE
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

)
User = get_user_model()

class UserLoginForm(forms.Form):

   #  #added
    # CUSTOMER_TYPE = (
    #     ('ownner', 'Owner'),
    #     ('tenant', 'Tenant')
    # )

   # #Added
   #  Who_are_you = forms.ChoiceField(choices=WHO_ARE_YOU,
   #      widget=forms.RadioSelect())

    # customer_type = forms.CharField(max_length=100, choices=CUSTOMER_TYPE, null=True)
    email = forms.EmailField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This User doesnot Exist or Incorrect Password.")
            if not user.is_active:
                raise forms.ValidationError("This user is no longer active.")
        return super(UserLoginForm,self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
    CUSTOMER_TYPE = (
        ('ownner', 'Owner'),
        ('tenant', 'Tenant')
        )

    customer_type = forms.ChoiceField(choices=CUSTOMER_TYPE,
          widget=forms.RadioSelect())
    # customer_type = forms.CharField(max_length=100, choices=CUSTOMER_TYPE, null=True, widget=forms.RadioSelect(), initial='tenant')
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    # #added



    # #Added
    # Who_are_you = forms.ChoiceField(choices=WHO_ARE_YOU,
    #     widget=forms.RadioSelect())
    
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
        ] 