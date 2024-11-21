from django.shortcuts import render
from .forms import UserRegister
from django.http import HttpResponse
from .models import *


# Create your views here.
def index(request):
    return render(request, 'fourth_task/index.html')


def shop(request):
    items = Game.objects.all()
    return render(request, 'fourth_task/shop.html', {'items': items})


def cart(request):
    return render(request, 'fourth_task/cart.html')







# Create your views here.
def sign_up_by_django(request):
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            users = Buyer.objects.filter(name = username)
            print(users)
            if password == repeat_password and age >= 18 and not users.exists():
                info['message'] = f'Приветствуем, {username}!'
                Buyer.objects.create(name=username,balance=1000,age=age)

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'

            if age < 18:
                info['error'] = 'Вы должны быть старше 18'

            if users.exists():
                info['error'] = f'Пользователь {username} уже существует'
        else:
            info['error'] = 'Некорректные данные в форме'
    else:
        form = UserRegister()
    info['form'] = form
    return render(request,'fifth_task/form_example.html',{'info':info})


def sign_up_by_html(request):
    users = {'Petrov':'hgffkjgyuyd', 'Ivanov':'jhgfrgsedtyguh', 'Sidorov':'gfdrtyuhtyuikj', 'Fedorov':'hfjfjdhdhry', 'Tuchkin':'fdhfhjdf'}
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        print(type(age))
        if password == repeat_password and age >= 18 and username not in users:
            return HttpResponse(f'Приветствуем, {username}!')
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'

        if age < 18:
            info['error'] = 'Вы должны быть старше 18'

        if username in users:
            info['error'] = f'Пользователь {username} уже существует'
    return render(request,'fifth_task/registration_page.html',{'info':info})

# from django.views.generic import TemplateView
# from django.shortcuts import render
# from .forms import UserRegister
# from .models import *
# from django.http import HttpResponse
#
#
# class Platform(TemplateView):
#     template_name = 'menu.html'
#
#
# class Cart(TemplateView):
#     template_name = 'cart.html'
#
#
# def menu(request):
#     mydict = Game.objects.all()
#     context = {
#         'mydict': mydict,
#     }
#     return render(request, 'games.html', context)
#
# def sign_up_by_django(request):
#     users = Buyer.objects.all()
#     usernames = [i.name for i in users]
#     i = 0
#     info = {'error': []}
#     if request.method == "POST":
#         form = UserRegister(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             repeat_password = form.cleaned_data['repeat_password']
#             age = form.cleaned_data['age']
#             if username not in usernames and password == repeat_password and int(age) >= 18:
#                 Buyer.objects.create(name=username, balance=0, age=age)
#                 context = {'username': username}
#                 return render(request, 'registration_complete.html', context)
#             elif username in usernames:
#                 i += 1
#                 info[f'error {i}'] = HttpResponse('Пользователь уже существует', status=400, reason='repeated login')
#                 print(info[f'error {i}'])
#                 return HttpResponse('Пользователь уже существует', status=400, reason='repeated login')
#             elif password != repeat_password:
#                 i += 1
#                 info[f'error {i}'] = HttpResponse('Пользователь уже существует', status=400, reason='repeated login')
#                 print(info[f'error {i}'])
#                 return HttpResponse('Пароли не совпадают', status=400, reason='non-identical passwords')
#             elif int(age) < 18:
#                 i += 1
#                 info[f'error {i}'] = HttpResponse(
#                     f'Вы должны быть старше 18', status=400, reason='insufficient age')
#
#                 return HttpResponse(
#                     f'Вы должны быть старше 18', status=400, reason='insufficient age')
#     else:
#
#         form = UserRegister()
#         context = {'info': info, 'form': form}
#         return render(request, 'registration_page.html', context)