from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Manufacturer

def product_list(request):
    """Отображение списка товаров"""
    products = Product.objects.all().select_related('category', 'manufacturer')
    
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
    
    categories = Category.objects.all()
    manufacturers = Manufacturer.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
        'manufacturers': manufacturers,
        'total_count': products.count(),
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request, product_id):
    """Отображение детальной информации о товаре"""
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})