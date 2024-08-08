from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Branch, Product
from .forms import ProductRegistrationForm

# Create your views here.

def dashboard(request):
    branch = get_list_or_404(Branch)
    context = {
        "branch": branch,
    }
    return render(request, 'dashboard/dashboard.html', context)

def products(request):
    products = get_list_or_404(Product)
    if request.method == "POST":
        form = ProductRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-products')
    form = ProductRegistrationForm()
    context = {
        "products": products,
        "form": form,
    }
    return render(request, 'dashboard/products.html', context)