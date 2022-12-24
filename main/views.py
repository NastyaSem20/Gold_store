from django.contrib.sites import requests
from django.shortcuts import render
from django.views.decorators.http import require_POST
from .forms import UserForm, OpenForm
from datetime import datetime
from .models import Models, Users, DonationPerMonth


def index(request):
    models = Models.objects.all()
    print(models)
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'models': models})


def about(request):
    return render(request, 'main/about.html')


def cart(request):
    users = Users.objects.all()
    # выбираем нужного пользователия через авторизацию
    user = Users.objects.get(id=request.session['user_id'])
    models_in_cart = user.cart[2:]
    models_in_cart = models_in_cart.split()

    summ = 0
    for m in models_in_cart:
        model_cost = Models.objects.get(id=int(m)).cost
        summ += model_cost
    request.session['summ'] = summ
    models = []
    print(models_in_cart)
    for i in models_in_cart:
        models.append(Models.objects.get(id=int(i)))
    return render(request, 'main/cart.html', {'models': models, 'summ': summ})


def add_basket(request):
    # выбираем нужного пользователия через авторизацию
    models = Models.objects.all()
    print(Users.objects.all())
    user = Users.objects.get(id=request.session['user_id'])
    cart = user.cart
    cart = cart + str(request.GET.get('product_id')) + ' '
    user.cart = cart
    user.save()
    return render(request, 'main/index.html',  {'title': 'Главная страница сайта', 'models': models})


def registration(request):
    if request.method == 'GET':
        userform = UserForm()
        return render(request, 'main/registration.html', {"form": userform})
    else:
        models = Models.objects.all()
        user = Users()
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user.ID = Users.objects.all()[0].id + 1
        request.session['user_id'] = user.ID
        user.cart = "''"
        user.name = name
        user.password = password
        user.email = email
        user.save()
        return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'models': models})


def sign_in(request):
    if request.method == 'GET':
        userform = OpenForm()
        return render(request, 'main/sign_in.html', {"form": userform})
    else:
        userform = OpenForm()
        models = Models.objects.all()
        name = request.POST.get('name')
        password = request.POST.get('password')
        users = Users.objects.all()
        print(users)
        if name in list(map(lambda x: x.name, users)):
            for i in users:
                if password == i.password:
                    request.session['user_id'] = i.ID
                    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'models': models})
            return render(request, 'main/sign_in.html', {'error': 'Wrong password', "form": userform})
        else:
            return render(request, 'main/sign_in.html', {'error': 'Who are you?', "form": userform})

def buy(request):
    summ = request.session['summ']
    user_id = Users.objects.get(id=request.session['user_id'])
    date = str(datetime.now().month)
    if str(DonationPerMonth.objects.all()[0]) < date:
        new_month = DonationPerMonth()
        new_month.id_donators = str(user_id)
        new_month.summ = (summ * 0.05)
        new_month.number = date
        new_month.save()
    else:
        current_month = DonationPerMonth.objects.get(number=date)
        current_month.id_donators = current_month.id_donators + ' ' + str(user_id)
        current_month.summ += (summ * 0.05)
        current_month.save()
    months = DonationPerMonth.objects.all()
    summ = sum([i.summ for i in months])

    return render(request, 'main/donations.html', {'months': months, 'all_summ': summ})


