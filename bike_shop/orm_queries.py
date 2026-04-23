# orm_queries.py
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_shop.settings')
django.setup()

from products.models import Product, Category, Manufacturer
from django.db.models import Q, Count, Avg, Max, Min, Sum

print("=" * 70)
print("LAB WORK #17 - DJANGO ORM QUERIES")
print("=" * 70)

# QUERY 1: Filtering
print("\n【1】FILTERING")
print("-" * 50)

print("\n▶ Query 1.1: Products more expensive than 500 rubles")
expensive = Product.objects.filter(price__gt=500)
print(f"   Result: found {expensive.count()} products")
for p in expensive[:5]:
    print(f"   - {p.name}: {p.price} rub.")

print("\n▶ Query 1.2: Products in specific category (Bicycles)")
category_products = Product.objects.filter(category__name='Bicycles')
print(f"   Result: found {category_products.count()} products")
for p in category_products[:5]:
    print(f"   - {p.name}")

print("\n▶ Query 1.3: Products with stock less than 50")
low_stock = Product.objects.filter(stock_quantity__lt=50)
print(f"   Result: found {low_stock.count()} products")
for p in low_stock[:5]:
    print(f"   - {p.name}: {p.stock_quantity} pcs")

# QUERY 2: Sorting
print("\n【2】SORTING")
print("-" * 50)

print("\n▶ Query 2.1: Products by price (ascending)")
cheapest = Product.objects.order_by('price')[:5]
for p in cheapest:
    print(f"   - {p.name}: {p.price} rub.")

print("\n▶ Query 2.2: Products by stock (descending)")
most_stock = Product.objects.order_by('-stock_quantity')[:5]
for p in most_stock:
    print(f"   - {p.name}: {p.stock_quantity} pcs")

print("\n▶ Query 2.3: Products by name (alphabetical)")
alphabetical = Product.objects.order_by('name')[:5]
for p in alphabetical:
    print(f"   - {p.name}")

# QUERY 3: Search
print("\n【3】SEARCH")
print("-" * 50)

print("\n▶ Query 3.1: Products containing 'Bike Accessory 1' in name")
search1 = Product.objects.filter(name__contains='Bike Accessory 1')
print(f"   Result: found {search1.count()} products")
for p in search1:
    print(f"   - {p.name}")

print("\n▶ Query 3.2: Complex search (price < 300 OR stock > 50)")
complex_search = Product.objects.filter(Q(price__lt=300) | Q(stock_quantity__gt=50))
print(f"   Result: found {complex_search.count()} products")
for p in complex_search[:5]:
    print(f"   - {p.name}: price={p.price} rub., stock={p.stock_quantity} pcs")

# QUERY 4: Aggregation
print("\n【4】AGGREGATION")
print("-" * 50)

total_products = Product.objects.count()
print(f"\n▶ Total products: {total_products}")

avg_price = Product.objects.aggregate(Avg('price'))
print(f"▶ Average price: {avg_price['price__avg']:.2f} rub.")

price_stats = Product.objects.aggregate(Max('price'), Min('price'))
print(f"▶ Max price: {price_stats['price__max']} rub.")
print(f"▶ Min price: {price_stats['price__min']} rub.")

total_stock = Product.objects.aggregate(Sum('stock_quantity'))
print(f"▶ Total stock quantity: {total_stock['stock_quantity__sum']} pcs")

# QUERY 5: Grouping and annotation
print("\n【5】GROUPING AND ANNOTATION")
print("-" * 50)

print("\n▶ Products count by category:")
category_stats = Category.objects.annotate(product_count=Count('products'))
for cat in category_stats:
    if cat.product_count > 0:
        print(f"   - {cat.name}: {cat.product_count} products")

print("\n▶ Products count by manufacturer:")
manufacturer_stats = Manufacturer.objects.annotate(product_count=Count('products'))
for man in manufacturer_stats:
    if man.product_count > 0:
        print(f"   - {man.name} ({man.country}): {man.product_count} products")

print("\n▶ Average price by category:")
category_avg = Category.objects.annotate(avg_price=Avg('products__price'))
for cat in category_avg:
    if cat.avg_price:
        print(f"   - {cat.name}: {cat.avg_price:.2f} rub. average")

print("\n" + "=" * 70)
print("✅ ALL QUERIES SUCCESSFULLY EXECUTED!")
print("=" * 70)