

Суть: зробити сторінку, (на Django) на якій буде 3 випадаючих списки із збереженням вибраних значень в URL
Swagger: https://onboarding.art-code.team/swagger-ui/index.html

1. Реалізуйте 3 випадаючих списка, значення яких завантажуються з API і не кешуються
- Послуги - api/test/v1/search/terms
- Бренди - api/test/v1/search/brands_terms
- Стилі - api/test/v1/search/styles

2. При виборі значення зі списку оновлюйте URL сторінки, зберігаючи вибрані значення
/s-{service_slug}/ - для послуг
/b-{brand_slug}/ - для брендів
/st-{style_slug}/ - для стилів

Приклад URL, коли вибрані всі 3 значення у випадаючих списках http://localhost:8000/s-zamina-zcheplennia/b-daihatsu/st-modern

3. При оновленні сторінки відображення вибраних значень випадаючих списків не повиині пропадати
- отримання значень для випадаючих списків - api/test/v1/search/parse_link
