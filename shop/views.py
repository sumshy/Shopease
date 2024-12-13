from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Product
from .forms import ProductForm

# Your existing index view
def index(request):
    """
    View for the homepage.
    """
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

# Product list view (to see the products)
@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

# Product detail view (to see a single product)
@login_required
def product_detail(request, pk):
    """
    View for displaying details of a single product.
    """
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

# View for creating a new product (restricted to Product Managers)
@login_required
@permission_required('shop.add_product', raise_exception=True)  # Only Product Manager can access this
def product_create(request):
    """
    View for creating a new product.
    """
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

# View for updating an existing product (restricted to Product Managers)
@login_required
@permission_required('shop.change_product', raise_exception=True)
def product_update(request, pk):
    """
    View for updating an existing product.
    """
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})

# View for deleting a product (restricted to Product Managers)
@login_required
@permission_required('shop.delete_product', raise_exception=True)
def product_delete(request, pk):

    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect('index')
    return render(request, 'product_confirm_delete.html', {'product': product})

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout view
@login_required
def logout_view(request):
    logout(request)
    return redirect('index')

def about(request):

    return render(request, 'about.html')

def services(request):

    return render(request, 'services.html')