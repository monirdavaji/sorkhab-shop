from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render,redirect
from .forms import LoginForm, RegisterForm, EditProfileForm
from django.contrib.auth import login,get_user_model,authenticate,logout
from django.contrib import messages

# todo: you can set it in settings.py and get import it from there
User = get_user_model()

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request,username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            login_form.add_error('username','کاربری با این مشخصات یافت نشد')
    context = {'login_form': login_form}
    return render(request,'account/login.html',context)



def register_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        user_name = register_form.cleaned_data.get('username')
        password = register_form.cleaned_data.get('password')
        email = register_form.cleaned_data.get('email')
        User.objects.create_user(username=user_name, password=password, email=email)
        messages.success(request,'ثبت نام با موفقیت انجام شد حالا وارد شوید')
        return redirect('login')

    context = {'register_form': register_form}
    return render(request,'account/register.html',context)


def logout_user(request):
    logout(request)
    messages.success(request, "با موفقیت خارج شدید.")
    return redirect('login')

@login_required(login_url='/login')
def user_profile_view(request):
    context = {}
    return render(request,'account/profile_user.html',context)

@login_required(login_url='/login')
def edit_profile(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    if user is None:
        raise Http404()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'اطلاعات با موفقیت تغییر یافت')
            return redirect('my_profile')
    else:
        form = EditProfileForm(instance=request.user)

    context = {'form':form}
    return render(request,'account/edit_profile.html',context)

# باید دستی همه ی اطلاعات رو بگیرم .این برای وقتیه که بخوایم از فرم عادی بجای مدل فرم استفاده کنیم
# @login_required(login_url='/login')
# def edit_profile(request):
#     user = request.user
#
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST)
#         if form.is_valid():
#             # دستی اطلاعات رو روی کاربر ذخیره می‌کنیم
#             user.first_name = form.cleaned_data['first_name']
#             user.last_name = form.cleaned_data['last_name']
#             user.email = form.cleaned_data['email']
#             user.save()
#             messages.success(request, 'اطلاعات با موفقیت ذخیره شد')
#             return redirect('my_profile')
#     else:
#         # فرم رو با اطلاعات فعلی کاربر پر می‌کنیم
#         form = EditProfileForm(initial={
#             'first_name': user.first_name,
#             'last_name': user.last_name,
#             'email': user.email,
#         })
#
#     return render(request, 'account/edit_profile.html', {'form': form})
