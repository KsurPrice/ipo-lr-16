# fill_database.py
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_shop.settings')
django.setup()

from products.models import Category, Manufacturer, Product
from django.contrib.auth.models import User
from cart.models import Cart, CartItem

print("=" * 60)
print("DATABASE FILLING")
print("=" * 60)

# 1. Create 5 manufacturers
print("\n1. Creating manufacturers (5 pcs):")
manufacturers_data = [
    {'name': 'Shimano', 'country': 'Japan', 'description': 'Leading bicycle components manufacturer'},
    {'name': 'Giant', 'country': 'Taiwan', 'description': 'Largest bicycle manufacturer'},
    {'name': 'Trek', 'country': 'USA', 'description': 'American premium bicycle brand'},
    {'name': 'Cateye', 'country': 'Japan', 'description': 'Bike computers and lights manufacturer'},
    {'name': 'Abus', 'country': 'Germany', 'description': 'German locks and security systems'},
]

for m in manufacturers_data:
    obj, created = Manufacturer.objects.get_or_create(
        name=m['name'],
        defaults={'country': m['country'], 'description': m['description']}
    )
    print(f"   - {obj.name} ({obj.country}) - {'created' if created else 'exists'}")
print(f"   Total: {Manufacturer.objects.count()} manufacturers")

# 2. Create 10 categories
print("\n2. Creating categories (10 pcs):")
categories_data = [
    'Bicycles', 'Helmets', 'Lights', 'Locks', 'Bags',
    'Tools', 'Clothing', 'Shoes', 'Accessories', 'Spare parts'
]

for cat in categories_data:
    obj, created = Category.objects.get_or_create(
        name=cat,
        defaults={'description': f'Category: {cat}'}
    )
    print(f"   - {obj.name} - {'created' if created else 'exists'}")
print(f"   Total: {Category.objects.count()} categories")

# 3. Create 34 products
print("\n3. Creating products (34 pcs):")
products_count = 0
categories = list(Category.objects.all())
manufacturers = list(Manufacturer.objects.all())

for i in range(1, 35):
    product_data = {
        'name': f'Bike Accessory {i}',
        'description': f'High quality bike accessory #{i}. Perfect for cyclists of any level.',
        'price': i * 50 + 100,
        'stock_quantity': i * 3 + 10,
        'category': categories[(i - 1) % len(categories)],
        'manufacturer': manufacturers[(i - 1) % len(manufacturers)],
    }
    obj, created = Product.objects.get_or_create(
        name=product_data['name'],
        defaults=product_data
    )
    if created:
        products_count += 1
        print(f"   - Created: {obj.name} (price: {obj.price} rub., stock: {obj.stock_quantity} pcs)")
print(f"   Total created: {products_count} products")
print(f"   Total products in DB: {Product.objects.count()}")

# 4. Create 5 users and carts with items
print("\n4. Creating users and carts (5 pcs):")
products_list = list(Product.objects.all())

for i in range(1, 6):
    user, created = User.objects.get_or_create(
        username=f'user{i}',
        defaults={'email': f'user{i}@example.com'}
    )
    if created:
        user.set_password(f'password{i}')
        user.save()
        print(f"   - Created user: {user.username} (password: password{i})")
    else:
        print(f"   - User already exists: {user.username}")
    
    # Create cart for user
    cart, cart_created = Cart.objects.get_or_create(user=user)
    if cart_created:
        print(f"     * Created cart for {user.username}")
    
    # Add 2-3 items to cart
    items_added = 0
    for j in range(1, (i % 3) + 2):
        product = products_list[(i + j) % len(products_list)]
        quantity = (i * j) % 3 + 1
        
        cart_item, item_created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity}
        )
        if item_created:
            items_added += 1
            print(f"     * Added: {product.name} - {quantity} pcs")
    
    if items_added > 0:
        print(f"     * Added {items_added} items to cart")

print("\n" + "=" * 60)
print("FINAL STATISTICS:")
print(f"   Manufacturers: {Manufacturer.objects.count()} pcs (required: 5)")
print(f"   Categories: {Category.objects.count()} pcs (required: 10)")
print(f"   Products: {Product.objects.count()} pcs (required: 34)")
print(f"   Users: {User.objects.count()} pcs (required: 5)")
print(f"   Carts: {Cart.objects.count()} pcs")
print("=" * 60)
print("✅ DATABASE SUCCESSFULLY FILLED!")