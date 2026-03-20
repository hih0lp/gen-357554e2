from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product
from .forms import OrderForm

def index(request):
    products = Product.objects.filter(is_available=True)
    form = OrderForm()
    context = {
        'products': products,
        'form': form,
    }
    return render(request, 'core/index.html', context)

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваш заказ успешно оформлен! Мы свяжемся с вами в ближайшее время.')
            return redirect('index')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    return redirect('index')