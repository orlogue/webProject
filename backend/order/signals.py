from django.db.models.signals import post_save, pre_delete, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .tasks import do
from .models import Order, OrderItem
from profiles.models import Telegram

@receiver(post_save, sender=OrderItem)
def create_order_items(sender, instance, created, **kwargs):
    # print(instance.product.seller.pk, instance.product.seller.pk)
    telegram = Telegram.objects.get(user__id=instance.product.seller.pk)
    do.delay(telegram_id=telegram.telegram_id, product=instance.product.name)