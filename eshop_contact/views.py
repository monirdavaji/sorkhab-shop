from django.shortcuts import render
from django.contrib import messages
from eshop_contact.forms import ContactForm
from .models import ContactUs
from django.core.mail import send_mail
from django.conf import settings
from eshop_settings.models import SiteSetting



def send_confirmation_email(user_email,user_full_name):
    subject = "نظر شما دریافت شد"
    message = f'{user_full_name} عزیز '
    message += '\n نظر شما با موفقیت ثبت شد و در اسرع وقت پیگیری خواهد شد'
    from_email = settings.DEFAULT_FROM_EMAIL  # همون ایمیل فرستنده که در settings مشخص کردیم
    recipient_list = [user_email]  # ایمیل کاربر
    from_name = 'سرخاب شاپ'
    full_from_email = f"{from_name} <{from_email}>"

    print(send_mail(
        subject=subject,
        message=message,
        from_email=full_from_email,
        recipient_list=recipient_list,
        fail_silently=False,  # اگر مشکلی پیش بیاد، ارور نمایش داده می‌شه
    ))




def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        full_name = contact_form.cleaned_data['full_name']
        email = contact_form.cleaned_data['email']
        subject = contact_form.cleaned_data['subject']
        text = contact_form.cleaned_data['text']
        ContactUs.objects.create(full_name=full_name, email=email, subject=subject, text=text, is_read=False)
        messages.success(request,'پیام شما با موفقیت ارسال شد')
        send_confirmation_email(email,full_name)
        contact_form = ContactForm()

    setting = SiteSetting.objects.first()



    context = {
        'contact_form': contact_form,
        'setting': setting
    }
    return render(request,'contact_us/contact_us_page.html',context)

