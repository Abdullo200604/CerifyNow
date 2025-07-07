# CerifyNow — Sertifikatlarni blokcheyn asosida boshqarish platformasi

[![Made with Django](https://img.shields.io/badge/Python-Django-green)](https://www.djangoproject.com/)
[![Blockchain](https://img.shields.io/badge/Blockchain-Ethereum-blue)](https://ethereum.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📝 Loyihaning qisqacha tavsifi

CerifyNow — bu tashkilotlar tomonidan berilgan elektron sertifikatlarni blokcheyn asosida yaratish, saqlash va tekshirish imkonini beruvchi platforma. Har bir hujjat (diplom, sertifikat va boshqalar) hash orqali blokcheynga yoziladi va avtomatik QR-kod yaratiladi.

---

## 🔥 Asosiy imkoniyatlar

- Tashkilotlar va foydalanuvchilarni ro‘yxatdan o‘tkazish va boshqarish
- Sertifikatlarni (hujjatlarni) yuklash va saqlash
- Har bir hujjatning SHA256 xashi avtomatik hisoblanadi
- Hash qiymati Ethereum (Sepolia yoki Mainnet) blokcheyniga yoziladi
- QR-kod avtomatik generatsiya qilinadi (hujjat hash uchun)
- REST API va admin panel orqali boshqarish

---

## 🚀 Texnologiyalar

- Backend: Python, Django, Django REST Framework
- Blockchain: Ethereum, Web3.py, Infura/Google Blockchain RPC
- Database: SQLite (develop), PostgreSQL (production uchun moslash mumkin)
- QR-kod: qrcode, Pillow

---

## ⚡️ O‘rnatish va ishga tushirish

1. Repository’ni klon qiling
   
    git clone https://github.com/Abdullo200604/CerifyNow.git
    cd CerifyNow/root
    
2. Virtual environment yarating va faollashtiring
   
    python -m venv .venv
    source .venv/bin/activate   # Linux/Mac
    .venv\Scripts\activate      # Windows
    
3. Kerakli kutubxonalarni o‘rnating
   
    pip install -r requirements.txt
    
4. .env faylini sozlang
    - root/.env.example dan nusxa oling va .env deb nomlang
    - Quyidagilarni to‘ldiring:
     
      INFURA_URL=YOUR_BLOCKCHAIN_RPC_URL
      WALLET_ADDRESS=YOUR_WALLET_ADDRESS
      PRIVATE_KEY=YOUR_PRIVATE_KEY
      CONTRACT_ADDRESS=YOUR_CONTRACT_ADDRESS
      
5. Ma’lumotlar bazasini yaratish va migration
   
    python manage.py makemigrations
    python manage.py migrate
    
6. Superuser yarating
   
    python manage.py createsuperuser
    
7. Serverni ishga tushiring
   
    python manage.py runserver
    
---

## 📦 API endpointlar (namuna)

| Yo‘l                | Metod | Maqsad                   |
|---------------------|-------|--------------------------|
| /api/institutions/ | GET/POST  | Tashkilotlar ro‘yxati/yaratish |
| /api/certificates/ | GET/POST  | Sertifikatlar ro‘yxati/yaratish|
| /api/documents/    | GET/POST  | Hujjatlarni boshqarish        |

---

## ⚙️ Foydalanish bo‘yicha qo‘llanma

1. Admin panel: http://localhost:8000/admin/
2. Institutions, Certificate, Document qo‘shish
3. Har bir yangi hujjat uchun:
    - Hash hisoblanadi
    - Hash blokcheynga yoziladi
    - QR-code generatsiya qilinadi

---

## 🤝 Hissa qo‘shish

- Fork qiling
- O‘zgarish kiriting (yangi branch oching)
- Pull request yuboring

---

## 🛡️ Litsenziya

MIT (ochiq kod)

---

## 👨🏻‍💻 Mualliflar

- Abdulloh Arslonov — [@Abdullo200604](https://github.com/Abdullo200604)
- Jasmina Bobokulova — [@Mis_Jesica](https://github.com/JMJfrds)
- Abdulmajid Mirmakhmudov — [@Mr.Mirmakhmudov](https://github.com/theMirmakhmudov)