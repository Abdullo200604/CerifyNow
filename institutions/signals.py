from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Certificate
from .utils import generate_qr
from .blockchain_utils import save_hash_to_blockchain

@receiver(post_save, sender=Certificate)
def certificate_post_save(sender, instance, created, **kwargs):
    # Faqat yangi Certificate yaratilganda ishlaydi
    if created:
        # 1. Blockchain'ga hash yozish (hash_value string)
        tx_hash = save_hash_to_blockchain(instance.hash)
        # 2. QR-code generatsiya qilish (hash asosida)
        qr_file = generate_qr(instance.hash)
        # QR-code'ni fayl sifatida saqlash
        instance.qr_code.save(f"{instance.pk}_qr.png", qr_file, save=False)
        # O'zgarishlarni saqlash (loopdan qochish uchun save=False yuqorida)
        instance.save()
