from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Certificate
from .blockchain_utils import save_hash_to_blockchain

@receiver(post_save, sender=Certificate)
def write_hash_to_blockchain(sender, instance, created, **kwargs):
    if created:
        tx_hash = save_hash_to_blockchain(
            instance.hash,
            from_address='0x...',       # ETH wallet manzili
            private_key='PRIVATE_KEY'   # ETH wallet private key
        )
        # Istasangiz, tx_hash ni modelga yoki logga yozing
