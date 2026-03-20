from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_email', 'customer_phone', 'product', 'comment']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванов Иван Иванович'}),
            'customer_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@mail.ru'}),
            'customer_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 (999) 123-45-67'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Особые пожелания к заказу...'}),
        }
        labels = {
            'customer_name': 'ФИО',
            'customer_email': 'Email',
            'customer_phone': 'Телефон',
            'product': 'Выберите букет',
            'comment': 'Комментарий',
        }