# Buvayda Ixtisoslashtirilgan Maktabi — Rasmiy Veb-Sayt

Django + PostgreSQL + ko'p tilli (UZ/RU/EN) rasmiy maktab veb-sayti.

---

## 📁 Loyiha tuzilmasi

```
buvayda_school/
├── buvayda_school/       # Asosiy Django konfiguratsiya
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                 # Bosh sahifa, Maktab haqida
├── news/                 # Yangiliklar
├── staff/                # Rahbarlar va O'qituvchilar
├── gallery/              # Fotogalereya
├── achievements/         # O'quvchi yutuqlari
├── contact/              # Aloqa va murojaat formi
├── templates/            # HTML shablonlar
├── static/               # CSS, JS
├── media/                # Yuklangan fayllar (avtomatik yaratiladi)
└── requirements.txt
```

---

## ⚙️ O'rnatish

### 1. Virtual muhit yaratish

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 2. Kutubxonalarni o'rnatish

```bash
pip install -r requirements.txt
```

### 3. PostgreSQL ma'lumotlar bazasini yaratish

```sql
CREATE DATABASE buvayda_school_db;
CREATE USER postgres WITH PASSWORD 'postgres';
GRANT ALL PRIVILEGES ON DATABASE buvayda_school_db TO postgres;
```

Yoki `.env` fayl orqali sozlash (quyida ko'ring).

### 4. Muhit o'zgaruvchilari (ixtiyoriy, lekin tavsiya etiladi)

`.env` fayl yarating:
```
DB_NAME=buvayda_school_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your-very-secret-key-here
```

### 5. Migratsiyalarni bajarish

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Tarjima fayllarini yaratish

```bash
python manage.py makemessages -l uz
python manage.py makemessages -l ru
python manage.py makemessages -l en
python manage.py compilemessages
```

### 7. Superuser yaratish (admin uchun)

```bash
python manage.py createsuperuser
```

### 8. Static fayllarni yig'ish

```bash
python manage.py collectstatic
```

### 9. Serverni ishga tushirish

```bash
python manage.py runserver
```

Sayt: http://127.0.0.1:8000
Admin: http://127.0.0.1:8000/admin

---

## 🌐 Ko'p tillilik (i18n)

Sayt **3 tilda** ishlaydi:
- 🇺🇿 O'zbekcha (standart)
- 🇷🇺 Русский
- 🇬🇧 English

Til almashtirish: Sayt yuqori qismidagi **UZ / RU / EN** tugmalar orqali.

---

## 🛠 Admin Panel

`/admin` URL orqali kiring va quyidagilarni boshqaring:

| Bo'lim | Nima qilish mumkin |
|--------|-------------------|
| **Maktab haqida** | Nom, tavsif, statistika, rasm, xarita URL |
| **Yangiliklar** | Maqolalar qo'shish, kategoriya, rasm |
| **Rahbarlar** | Direktor va boshqa rahbarlar |
| **O'qituvchilar** | Fan bo'yicha o'qituvchilar |
| **Galereya** | Albomlar va rasmlar |
| **Yutuqlar** | Olimpiada, sport, fan natijalari |
| **Murojaatlar** | Foydalanuvchilardan kelgan xabarlar |

Barcha ma'lumotlar **3 tilda** kiritiladi (UZ, RU, EN).

---

## 🚀 Production uchun

1. `settings.py` da `DEBUG = False` qiling
2. `ALLOWED_HOSTS` ga domeningizni qo'shing
3. `SECRET_KEY` ni xavfsiz kalit bilan almashtiring
4. Gunicorn bilan ishga tushiring:
   ```bash
   gunicorn qoqon_im.wsgi:application --bind 0.0.0.0:8000
   ```
5. Nginx orqali yo'naltiring va SSL sertifikat o'rnating

---

## 📦 Asosiy kutubxonalar

- `Django` — asosiy freymvork
- `psycopg2-binary` — PostgreSQL ulanishi
- `django-modeltranslation` — ko'p tillilik
- `Pillow` — rasm ishlash
- `gunicorn` — production server
- `whitenoise` — static fayllar



