from django import forms
from django.core.validators import *
from django.contrib.auth import get_user_model

User = get_user_model()


# اینم فرم عادی بجای پایینی اینو هم میشه نوشت
# class EditProfileForm(forms.Form):
#     first_name = forms.CharField(
#         max_length=150,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
#     last_name = forms.CharField(
#         max_length=150,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
#     email = forms.EmailField(
#         widget=forms.EmailInput(attrs={'class': 'form-control'})
#     )


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد کنید'}),
        label='نام کاربری')
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا رمز عبو خود را وارد کنید '}),
        label='رمز عبور')


# todo: bets practice for fields validations is to use regex
class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفا نام کاربری خود را وارد نمایید '}),
        label='نام کاربری ' ,
        validators=[
            MinLengthValidator(4,message='نام کاربری حداقل میتواند ۴ کاراکتر باشد'),
            MaxLengthValidator(20,message='نام کاربری حداکثر می تواند ۲۰ کاراکتر باشد')
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد کنید'}),
        label= 'ایمیل' ,
        validators=[
            MaxLengthValidator(40)
        ]
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'لطفا پسورد خود را وارد نمایید '}),
        label= 'کلمه عبور' ,
        validators=[
            MinLengthValidator(8,message='کلمه عبور باید حداقل ۸ کاراکتر باشد ') ,
            MaxLengthValidator(30,message='کلمه عبور حداکثر باید ۳۰ کاراکتر باشد')
        ]
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'لطفا کلمه عبور را دوباره وارد کنید'}),
        label='تکرار کلمه عبور'

    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        is_exists = User.objects.filter(username=username).exists()
        if is_exists:
            raise forms.ValidationError('این کاربر قبلا ثبت نام کرده است')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists = User.objects.filter(email=email).exists()
        if is_exists:
            raise forms.ValidationError('ایمیل وجود دارد ایمیل دیگری وارد نمایید')
        return email


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password and password != re_password:
            self.add_error('re_password', 'کلمه‌های عبور با هم مطابقت ندارند')

