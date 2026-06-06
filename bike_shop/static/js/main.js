// static/js/main.js

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

async function addToCart(productId, quantity = 1) {
    try {
        const token = localStorage.getItem('access_token');
        const headers = {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        };
        if (token) {
            headers['Authorization'] = `Bearer ${token}`;
        }
        const response = await fetch('/api/cart/add_item/', {
            method: 'POST',
            headers: headers,
            body: JSON.stringify({ product_id: productId, quantity: quantity })
        });
        if (response.ok) {
            showNotification('Товар добавлен в корзину!', 'success');
            updateCartCounter();
        } else if (response.status === 401) {
            showNotification('Войдите, чтобы добавить товар в корзину', 'error');
            setTimeout(() => { window.location.href = '/login/'; }, 1500);
        } else {
            const error = await response.json();
            showNotification(error.error || 'Ошибка при добавлении', 'error');
        }
    } catch (error) {
        console.error('Ошибка:', error);
        showNotification('Ошибка соединения с сервером', 'error');
    }
}

async function updateCartCounter() {
    try {
        const token = localStorage.getItem('access_token');
        const headers = {};
        if (token) {
            headers['Authorization'] = `Bearer ${token}`;
        }
        const response = await fetch('/api/cart/', { headers: headers });
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

function showNotification(message, type = 'success') {
    const bgColor = type === 'success' ? '#28a745' : '#dc3545';
    const icon = type === 'success' ? '✓' : '✗';
    const toast = document.createElement('div');
    toast.className = 'toast-notification';
    toast.innerHTML = `<div style="background: ${bgColor}; color: white; padding: 12px 20px; border-radius: 8px;"><strong>${icon} ${message}</strong></div>`;
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 3000);
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.add-to-cart-btn').forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const productId = this.dataset.productId;
            if (productId) addToCart(productId);
        });
    });
    updateCartCounter();
});

window.addToCart = addToCart;
window.showNotification = showNotification;