from decimal import Decimal

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView

from .models import User
from DiDiStore import settings
from .forms import RegistrationForm, LoginForm
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Book, Category
from .cart import Cart


# Create your views here.
def index(request):
    forms = RegistrationForm(request.POST or None)
    if forms.is_valid():
        forms.save()
        return redirect('home')

    books = Book.objects.all()
    maincats = Category.objects.all()
    cats = Category.objects.all()

    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
                print(message)
                redirect("cab")
            else:
                message = 'Login failed!'

    context = {
        "books": books,
        "cats": cats,
        "mncats": maincats,
        "forms": forms,
        "form": form,
        "msg": message,
    }

    return render(request, "DiDiStoreApp/index.html", context)


def show_book(request, bookid):
    bookss = get_object_or_404(Book, id=bookid)
    context = {
        "bookss": bookss,
    }
    return render(request, "DiDiStoreApp/det.html", context)

def show_category(request, id):
    forms = RegistrationForm(request.POST or None)
    if forms.is_valid():
        forms.save()
        return redirect('home')

    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
                print(message)
                redirect("cab")
            else:
                message = 'Login failed!'

    books = Book.objects.filter(category_id=id)
    cats = Category.objects.all()
    context = {
        "books": books,
        "cats": cats,
        "forms": forms,
        "form":form,
    }
    return render(request, "DiDiStoreApp/index.html", context)



def signout(request):
    logout(request)
    return redirect('home')


def cart_add(request, bookid):
    cart = Cart(request)
    book = get_object_or_404(Book, id=bookid)
    cart.add(book=book)

    return redirect('cart_details')


def cart_update(request, bookid, quantity):
    cart = Cart(request)
    book = get_object_or_404(Book, id=bookid)
    cart.update(book=book, quantity=quantity)
    price = (book.price * quantity)

    return render(request, 'cart/price.html', {"price": price})


def cart_remove(request, bookid):
    cart = Cart(request)
    book = get_object_or_404(Book, id=bookid)
    cart.remove(book)
    return redirect('cart_details')


# def summmary(request):
#     cart = Cart(request)
#     cart.get_total_price(cart)
#     return redirect('home')

def cart_details(request):
    cart = Cart(request)
    context = {
        "cart": cart,
    }
    return render(request, 'DiDiStoreApp/desired.html', context)



def my_cab(request):
    return render(request, "DiDiStoreApp/account.html")


def LogoutUser(request):
    logout(request)
    redirect("home")