from django.shortcuts import render, redirect
from .models import Pizza
from .forms import ToppingForm, OrderForm

def index(request):
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/index.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()

    if request.method != 'POST':
        form = ToppingForm()
    else:
        form = ToppingForm(data=request.POST)
        if form.is_valid():
            new_topping = form.save(commit=False)
            new_topping.pizza = pizza
            new_topping.save()
            return redirect('pizzas:pizza', pizza_id=pizza_id)

    context = {'pizza': pizza, 'toppings': toppings, 'form': form}
    return render(request, 'pizzas/pizza.html', context)

def order(request):
    if request.method != 'POST':
        form = OrderForm()
    else:
        form = OrderForm(data=request.POST)
        if form.is_valid():
            selected_toppings = form.cleaned_data['toppings']
            
            total_price = 10.00
            
            for topping in selected_toppings:
                total_price += topping.price

            context = {
                'form': form,
                'selected_toppings': selected_toppings,
                'total_price': total_price,
            }
            
            return render(request, 'pizzas/order.html', context)
    
    context = {'form': form}
    return render(request, 'pizzas/order.html', context)