from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import * 
from django.contrib.auth.backends import UserModel
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CreateUserForm
from django.contrib import messages


def store(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'store/store.html', context)



def cart(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		#Create empty cart for now for non-logged in user
		items = []

	context = {'items':items,'order' : order}
	return render(request, 'store/cart.html', context)



def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0}

	context = {'items':items, 'order':order}
	return render(request, 'store/checkout.html', context)



def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print(action)
    print(productId)
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order,created = Order.objects.get_or_create(customer=customer,complete = False)
    orderItem,created = Order.objects.get_or_create(order = order,product = product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action=='remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()
    if orderItem.quantity<=0:
        orderItem.delete()
    return JsonResponse('ITEM IS ADDED',safe=False)


def registerPage(request):
    if request.user.is_authenticated:
        if UserModel.is_superuser or UserModel.is_staff:
            return redirect('/admin/')
        else:
            return redirect('store')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(
                    request, 'Account created successfully for '+user)
                return redirect('Login')
        context = {'form': form}
        return render(request, 'store/register.html', context)



def loginPage(request):
    if request.user.is_authenticated:
        if UserModel.is_superuser or UserModel.is_staff:
            return redirect('/admin/')
        else:
            return redirect('store')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_superuser or user.is_staff:
                    login(request, user)
                    return redirect('/admin/')
                else:
                    login(request, user)
                    return redirect('store')
            else:
                messages.info(request, 'Username or Password is incorrect')
        context = {}
        return render(request, 'store/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('Logout')


def contact(request):
    if request.method == 'POST':
        Cname = request.POST['Cname']
        Cemail = request.POST['Cemail']
        ins = MailID(Cname=Cname, Cemail=Cemail)
        ins.save()
        return redirect('ContactSuccess')
    return render(request, 'store/mail.html')



def contactSuccessPage(request):
    return render(request, 'store/contactSuccess.html')