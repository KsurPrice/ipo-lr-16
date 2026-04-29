// static/js/main.js

// Функция для показа уведомлений
function showNotification(message, type = 'success') {
    const bgColor = type === 'success' ? '#28a745' : '#dc3545';
    const icon = type === 'success' ? '✓' : '✗';
    
    const toast = document.createElement('div');
    toast.className = 'toast-notification';
    toast.innerHTML = `
        <div style="background: ${bgColor}; color: white; padding: 12px 20px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
            <strong>${icon} ${message}</strong>
        </div>
    `;
    
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.remove();
    }, 3000);
}

// Функция для получения CSRF токена
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Функция добавления товара в корзину через API
async function addToCart(productId, quantity = 1) {
    try {
        const response = await fetch('/api/cart/add_item/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
                product_id: productId,
                quantity: quantity
            })
        });
        
        if (response.ok) {
            const data = await response.json();
            showNotification(`Товар добавлен в корзину!`, 'success');
            updateCartCounter();
            return data;
        } else {
            const error = await response.json();
            showNotification(error.error || 'Ошибка при добавлении', 'error');
            return null;
        }
    } catch (error) {
        console.error('Ошибка:', error);
        showNotification('Ошибка соединения с сервером', 'error');
        return null;
    }
}

// Функция обновления счетчика корзины
async function updateCartCounter() {
    try {
        const response = await fetch('/api/cart/');
        if (response.ok) {
            const data = await response.json();
            const cartBadge = document.querySelector('.cart-badge');
            if (cartBadge && data.items_count > 0) {
                cartBadge.textContent = data.items_count;
                cartBadge.style.display = 'inline';
            } else if (cartBadge) {
                cartBadge.style.display = 'none';
            }
        }
    } catch (error) {
        console.error('Ошибка обновления корзины:', error);
    }
}

// Функция загрузки товаров через API (для динамической загрузки)
async function loadProductsViaAPI(filters = {}) {
    showSpinner();
    try {
        let url = '/api/products/';
        const params = new URLSearchParams();
        if (filters.category) params.append('category', filters.category);
        if (filters.search) params.append('search', filters.search);
        if (params.toString()) url += '?' + params.toString();
        
        const response = await fetch(url);
        if (response.ok) {
            const products = await response.json();
            renderProducts(products);
        } else {
            showNotification('Ошибка загрузки товаров', 'error');
        }
    } catch (error) {
        console.error('Ошибка:', error);
        showNotification('Ошибка соединения с сервером', 'error');
    } finally {
        hideSpinner();
    }
}

// Показать спиннер
function showSpinner() {
    let spinner = document.querySelector('.spinner-overlay');
    if (!spinner) {
        spinner = document.createElement('div');
        spinner.className = 'spinner-overlay';
        spinner.innerHTML = `
            <div class="spinner-border text-light" role="status" style="width: 3rem; height: 3rem;">
                <span class="visually-hidden">Загрузка...</span>
            </div>
        `;
        document.body.appendChild(spinner);
    }
    spinner.style.display = 'flex';
}

// Скрыть спиннер
function hideSpinner() {
    const spinner = document.querySelector('.spinner-overlay');
    if (spinner) {
        spinner.style.display = 'none';
    }
}

// Инициализация при загрузке страницы
document.addEventListener('DOMContentLoaded', function() {
    // Обработчики для кнопок "В корзину"
    document.querySelectorAll('.add-to-cart-btn').forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const productId = this.dataset.productId;
            if (productId) {
                addToCart(productId);
            }
        });
    });
    
    // Обновляем счетчик корзины при загрузке
    updateCartCounter();
});

// Экспорт функций для использования в других файлах
window.addToCart = addToCart;
window.showNotification = showNotification;