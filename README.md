# CerifyNow

CerifyNow is a modern platform for **verifying and certifying educational documents** (diplomas, certificates, honorary awards) issued by educational institutions, using the Ethereum blockchain. This ensures documents are **tamper-proof, publicly auditable, and easily verified** using QR codes.

---

## 🚀 Features

- **Institution registration** and approval workflow (admin panel)
- **Document hash generation and storage** on Ethereum blockchain
- **QR code generation** for each document hash (for easy verification)
- **REST API** for integration with web and mobile applications
- **Blockchain verification**: instantly check document authenticity by hash or QR
- **Secure, scalable, and future-proof** architecture

---

## ⚙️ Technologies Used

- **Backend**: Django, Django REST Framework, python-dotenv, Web3.py
- **Blockchain**: Solidity smart contract (Ethereum Sepolia or Mainnet), Infura
- **Database**: SQLite (for development, can switch to PostgreSQL)
- **Others**: qrcode, Pillow (for QR code), dotenv
- **Frontend**: (Optional) React/Vue/Next.js (not included in this repo)

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Abdullo200604/CerifyNow.git
cd CerifyNow/root
2. Install requirements
bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate    # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
3. Prepare your environment
Create a .env file (see .env.example for the template):

env
Copy
Edit
INFURA_URL=https://sepolia.infura.io/v3/YOUR_INFURA_PROJECT_ID
WALLET_ADDRESS=0xYourWalletAddress
PRIVATE_KEY=your_private_key
CONTRACT_ADDRESS=0xYourContractAddress
Never commit your actual .env file!

4. Run migrations
bash
Copy
Edit
python manage.py migrate
5. Create superuser
bash
Copy
Edit
python manage.py createsuperuser
6. Run development server
bash
Copy
Edit
python manage.py runserver
7. (Optional) Test blockchain integration
See institutions/blockchain_utils.py for functions like save_hash_to_blockchain.

📦 Project Structure
bash
Copy
Edit
CerifyNow/
 └── root/
     ├── institutions/
     │    ├── models.py
     │    ├── blockchain_utils.py
     │    ├── signals.py
     │    ├── ...
     ├── users/
     ├── manage.py
     ├── .env.example
     ├── requirements.txt
     ├── README.md
     └── ...
🔐 Security
DO NOT COMMIT your actual .env file or private keys.

Smart contract ABI is public and can be stored in code.

All sensitive keys should be kept private and rotated periodically.

📄 License
This project is open-source under the MIT License.

🤝 Contributing
Pull requests are welcome! Please fork the repository and submit a PR.

📬 Contact
For questions or partnership requests, please open an issue or contact the maintainer.

yaml
Copy
Edit

---

## **O‘ZBEKCHA QISQA VARIANT (LOZIM BO‘LSA)**

```markdown
# CerifyNow

CerifyNow — bu ta’lim muassasalari tomonidan berilgan diplom, sertifikat, faxriy yorliqlarni **blokcheyn orqali ishonchli tasdiqlash va tekshirish** platformasi.

---

## Asosiy imkoniyatlar

- Hujjat (PDF yoki boshqa) hashini blokcheynga yozish
- Har bir hujjat uchun QR kod yaratish
- Django va DRF asosida REST API
- Foydalanuvchi ro‘yxatidan o‘tishi va admin tasdiqlash
- Tez, himoyalangan va zamonaviy arxitektura

---

## O‘rnatish

1. **Repository’ni klon qiling**  
2. **`requirements.txt` bo‘yicha o‘rnatish**  
3. **`.env.example` asosida `.env` fayl yarating**  
4. **Migrate va createsuperuser**  
5. **`runserver` bilan loyihani ishga tushiring**

---

## Muhim: `.env` faylingizni hech qachon GitHub’ga joylamang!  
Maxfiy ma’lumotlar xavfsizligini ta’minlang.

---

## Hamkorlik va savollar uchun issue yoki pull request yuboring.

---
