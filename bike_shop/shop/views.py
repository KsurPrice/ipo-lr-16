# shop/views.py
from django.http import HttpResponse

def home(request):
    """Главная страница с ссылками"""
    html_content = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>BikeShop - Аксессуары для велосипедов</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }
            
            .container {
                background: white;
                border-radius: 20px;
                padding: 50px;
                max-width: 800px;
                width: 100%;
                text-align: center;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                animation: fadeIn 0.8s ease-in;
            }
            
            @keyframes fadeIn {
                from {
                    opacity: 0;
                    transform: translateY(-30px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            
            h1 {
                color: #333;
                font-size: 2.5em;
                margin-bottom: 20px;
            }
            
            .bike-icon {
                font-size: 80px;
                margin-bottom: 20px;
            }
            
            .description {
                color: #666;
                font-size: 1.2em;
                margin-bottom: 40px;
                line-height: 1.6;
            }
            
            .links {
                display: flex;
                gap: 20px;
                justify-content: center;
                flex-wrap: wrap;
            }
            
            .btn {
                display: inline-block;
                padding: 15px 35px;
                font-size: 1.1em;
                font-weight: 600;
                text-decoration: none;
                border-radius: 50px;
                transition: all 0.3s ease;
                cursor: pointer;
            }
            
            .btn-primary {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
            }
            
            .btn-primary:hover {
                transform: translateY(-3px);
                box-shadow: 0 8px 25px rgba(102, 126, 234, 0.5);
            }
            
            .btn-secondary {
                background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                color: white;
                box-shadow: 0 4px 15px rgba(245, 87, 108, 0.4);
            }
            
            .btn-secondary:hover {
                transform: translateY(-3px);
                box-shadow: 0 8px 25px rgba(245, 87, 108, 0.5);
            }
            
            @media (max-width: 600px) {
                .container {
                    padding: 30px 20px;
                }
                h1 {
                    font-size: 1.8em;
                }
                .btn {
                    padding: 12px 25px;
                    font-size: 1em;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="bike-icon">🚲</div>
            <h1>BikeShop</h1>
            <p class="description">Лучшие аксессуары для вашего велосипеда!<br>Фонари, замки, сумки и многое другое.</p>
            <div class="links">
                <a href="/about/" class="btn btn-primary">📖 Об авторе</a>
                <a href="/store-info/" class="btn btn-secondary">🏪 О магазине</a>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)

def about(request):
    """Страница об авторе - Карась Илья, 88ТП"""
    html_content = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Об авторе - BikeShop</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }
            
            .container {
                background: white;
                border-radius: 20px;
                padding: 50px;
                max-width: 700px;
                width: 100%;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                animation: slideIn 0.6s ease-out;
            }
            
            @keyframes slideIn {
                from {
                    opacity: 0;
                    transform: translateX(-30px);
                }
                to {
                    opacity: 1;
                    transform: translateX(0);
                }
            }
            
            .back-btn {
                display: inline-block;
                margin-bottom: 30px;
                color: #667eea;
                text-decoration: none;
                font-weight: 600;
                transition: transform 0.3s;
            }
            
            .back-btn:hover {
                transform: translateX(-5px);
            }
            
            h1 {
                color: #333;
                font-size: 2.2em;
                margin-bottom: 30px;
                border-left: 5px solid #667eea;
                padding-left: 20px;
            }
            
            .info-card {
                background: #f8f9fa;
                border-radius: 15px;
                padding: 25px;
                margin-bottom: 20px;
            }
            
            .info-row {
                display: flex;
                padding: 12px 0;
                border-bottom: 1px solid #e0e0e0;
            }
            
            .info-label {
                font-weight: 700;
                width: 130px;
                color: #555;
            }
            
            .info-value {
                color: #333;
                flex: 1;
            }
            
            .avatar {
                text-align: center;
                margin-bottom: 30px;
            }
            
            .avatar-icon {
                font-size: 80px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                width: 120px;
                height: 120px;
                border-radius: 50%;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            }
            
            .back-link {
                text-align: center;
                margin-top: 30px;
            }
            
            .btn-back {
                display: inline-block;
                padding: 12px 30px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                text-decoration: none;
                border-radius: 50px;
                transition: all 0.3s;
                font-weight: 600;
            }
            
            .btn-back:hover {
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <a href="/" class="back-btn">← На главную</a>
            
            <div class="avatar">
                <div class="avatar-icon">👨‍💻</div>
            </div>
            
            <h1>Об авторе</h1>
            
            <div class="info-card">
                <div class="info-row">
                    <div class="info-label">ФИО:</div>
                    <div class="info-value">Карась Илья</div>
                </div>
                <div class="info-row">
                    <div class="info-label">Группа:</div>
                    <div class="info-value">88ТП</div>
                </div>
                <div class="info-row">
                    <div class="info-label">Курс:</div>
                    <div class="info-value">2 курс</div>
                </div>
                <div class="info-row">
                    <div class="info-label">Специальность:</div>
                    <div class="info-value">Техник-программист</div>
                </div>
                <div class="info-row">
                    <div class="info-label">Email:</div>
                    <div class="info-value">ilyakaras.off@gmail.com</div>
                </div>
                <div class="info-row">
                    <div class="info-label">Дата выполнения:</div>
                    <div class="info-value">22 апреля 2026 г.</div>
                </div>
            </div>
            
            <div class="info-card">
                <div class="info-row">
                    <div class="info-label">О себе:</div>
                    <div class="info-value">Увлекаюсь волейболом, программированием и созданием веб-приложений на Django.</div>
                </div>
                <div class="info-row">
                    <div class="info-label">Хобби:</div>
                    <div class="info-value">Волейбол</div>
                </div>
            </div>
            
            <div class="back-link">
                <a href="/" class="btn-back">Вернуться на главную</a>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)

def store_info(request):
    """Страница о магазине - велоаксессуары"""
    html_content = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>О магазине - BikeShop</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }
            
            .container {
                background: white;
                border-radius: 20px;
                padding: 50px;
                max-width: 800px;
                width: 100%;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                animation: slideIn 0.6s ease-out;
            }
            
            @keyframes slideIn {
                from {
                    opacity: 0;
                    transform: translateX(30px);
                }
                to {
                    opacity: 1;
                    transform: translateX(0);
                }
            }
            
            .back-btn {
                display: inline-block;
                margin-bottom: 30px;
                color: #667eea;
                text-decoration: none;
                font-weight: 600;
                transition: transform 0.3s;
            }
            
            .back-btn:hover {
                transform: translateX(-5px);
            }
            
            h1 {
                color: #333;
                font-size: 2.2em;
                margin-bottom: 20px;
                border-left: 5px solid #f5576c;
                padding-left: 20px;
            }
            
            .theme-badge {
                background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                color: white;
                padding: 10px 20px;
                border-radius: 50px;
                display: inline-block;
                margin-bottom: 30px;
                font-weight: 600;
            }
            
            .products-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
                margin: 30px 0;
            }
            
            .product-card {
                background: #f8f9fa;
                border-radius: 15px;
                padding: 20px;
                text-align: center;
                transition: transform 0.3s;
            }
            
            .product-card:hover {
                transform: translateY(-5px);
            }
            
            .product-icon {
                font-size: 50px;
                margin-bottom: 10px;
            }
            
            .product-name {
                font-weight: 700;
                color: #333;
                margin-bottom: 5px;
            }
            
            .product-desc {
                font-size: 0.85em;
                color: #666;
            }
            
            .info-section {
                background: #f8f9fa;
                border-radius: 15px;
                padding: 25px;
                margin: 20px 0;
            }
            
            .info-section h3 {
                color: #667eea;
                margin-bottom: 15px;
            }
            
            .info-section p {
                color: #555;
                line-height: 1.6;
            }
            
            .source-link {
                color: #667eea;
                text-decoration: none;
                font-weight: 600;
            }
            
            .source-link:hover {
                text-decoration: underline;
            }
            
            .btn-back {
                display: inline-block;
                padding: 12px 30px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                text-decoration: none;
                border-radius: 50px;
                transition: all 0.3s;
                font-weight: 600;
                margin-top: 20px;
            }
            
            .btn-back:hover {
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <a href="/" class="back-btn">← На главную</a>
            
            <div style="text-align: center;">
                <div class="theme-badge">BikeShop</div>
            </div>
            
            <h1>О магазине BikeShop</h1>
            
            <div class="products-grid">
                <div class="product-card">
                    <div class="product-icon">🔦</div>
                    <div class="product-name">Велофары</div>
                    <div class="product-desc">LED фары до 1000 люмен</div>
                </div>
                <div class="product-card">
                    <div class="product-icon">🔒</div>
                    <div class="product-name">Замки</div>
                    <div class="product-desc">Тросовые и U-образные</div>
                </div>
                <div class="product-card">
                    <div class="product-icon">🎒</div>
                    <div class="product-name">Сумки</div>
                    <div class="product-desc">На раму, руль и багажник</div>
                </div>
                <div class="product-card">
                    <div class="product-icon">🪖</div>
                    <div class="product-name">Шлемы</div>
                    <div class="product-desc">Защита для головы</div>
                </div>
                <div class="product-card">
                    <div class="product-icon">🔧</div>
                    <div class="product-name">Инструменты</div>
                    <div class="product-desc">Насосы, ключи, ремкомплекты</div>
                </div>
                <div class="product-card">
                    <div class="product-icon">💡</div>
                    <div class="product-name">Аксессуары</div>
                    <div class="product-desc">Зеркала, звонки, фляги</div>
                </div>
            </div>            
            <div class="info-section">
                <h3>✨ Наши преимущества</h3>
                <p>✓ Только оригинальные аксессуары от проверенных брендов</p>
                <p>✓ Быстрая доставка по всей стране</p>
                <p>✓ Гарантия качества на все товары</p>
                <p>✓ Консультации опытных велосипедистов</p>
            </div>
            <div style="text-align: center;">
                <a href="/" class="btn-back">Вернуться на главную</a>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)