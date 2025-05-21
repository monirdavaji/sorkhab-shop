from django import forms
from django.core import validators
from django.core.validators import MaxLengthValidator


class ContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفا نام و نام خانوادگی خود را وارد کنید' ,'class':'form-control'}),
        label='نام و نام خانوادگی',
        help_text='حداکثر ۱۵۰ کاراکتر' ,
        validators=[
            MaxLengthValidator(150,'نام و نام خانوادگی شما نمی تواند بیشتر از ۱۵۰ کاراکتر باشد')
        ]

    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder':'لطفا ایمیل خود را وارد نمایید' ,'class':'form-control'}),
        label='ایمیل',
        validators=[
            MaxLengthValidator(100,'ایمیل شما نمی تواند بیشتر از ۱۰۰ کاراکتر باشد')
        ]

    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفا موضوع پیام خود را وارد نمایید' ,'class':'form-control'}),
        label='موضوع پیام',
        validators=[
            MaxLengthValidator(200,'موضوع پیام شما نمی تواند بیشتر از ۲۰۰ کاراکتر باشد')
        ]
    )

    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder':'لطفا متن پیام خود را وارد نمایید' ,'class':'form-control' ,'rows':'8'}),
        label='متن پیام'

    )

