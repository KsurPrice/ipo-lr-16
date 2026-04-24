from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .models import Product, Category, Manufacturer
from cart.models import Cart, CartItem

def product_list(request):
    """Список товаров с фильтрацией и поиском"""
    products = Product.objects.all().select_related('category', 'manufacturer')
    
    # Поиск по названию и описанию
    search_query = request.GET.get('search', '')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    # Фильтрация по категории
    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)
    
    # Фильтрация по производителю
    manufacturer_id = request.GET.get('manufacturer')
    if manufacturer_id:
        products = products.filter(manufacturer_id=manufacturer_id)
    
    # Сортировка
    sort_by = request.GET.get('sort')
    if sort_by == 'price_asc':
        products = products.order_by('price')
    elif sort_by == 'price_desc':
        products = products.order_by('-price')
    elif sort_by == 'name_asc':
        products = products.order_by('name')
    
    context = {
        'products': products,
        'categories': Category.objects.all(),
        'manufacturers': Manufacturer.objects.all(),
        'total_count': products.count(),
        'search_query': search_query,
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request, pk):
    """Детальная информация о товаре"""
    product = get_object_or_404(Product, id=pk)
    return render(request, 'products/product_detail.html', {'product': product})

@login_required
def add_to_cart(request, product_id):
    """Добавление товара в корзину"""
    product = get_object_or_404(Product, id=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': 1}
    )
    
    if not created:
        if cart_item.quantity + 1 <= product.stock_quantity:
            cart_item.quantity += 1
            cart_item.save()
            messages.success(request, f'Товар "{product.name}" добавлен в корзину (+1)')
        else:
            messages.error(request, f'Недостаточно товара. Доступно: {product.stock_quantity} шт.')
    else:
        messages.success(request, f'Товар "{product.name}" добавлен в корзину')
    
    return redirect('products:cart_view')

@login_required
def update_cart_item(request, item_id):
    """Обновление количества товара в корзине"""
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    
    if request.method == 'POST':
        new_quantity = int(request.POST.get('quantity', 1))
        product = cart_item.product
        
        if new_quantity <= product.stock_quantity:
            if new_quantity > 0:
                cart_item.quantity = new_quantity
                cart_item.save()
                messages.success(request, f'Количество обновлено до {new_quantity} шт.')
            else:
                cart_item.delete()
                messages.success(request, f'Товар удален из корзины')
        else:
            messages.error(request, f'Недостаточно товара. Доступно: {product.stock_quantity} шт.')
    
    return redirect('products:cart_view')

@login_required
def remove_from_cart(request, item_id):
    """Удаление товара из корзины"""
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    messages.success(request, f'Товар удален из корзины')
    return redirect('products:cart_view')

@login_required
def cart_view(request):
    """Просмотр корзины"""
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all().select_related('product')
    
    return render(request, 'products/cart.html', {
        'cart_items': cart_items,
        'total_price': cart.get_total_price(),
    })