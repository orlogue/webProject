from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_order_item_approval
from .models import OrderItem
from profiles.models import Telegram


@receiver(post_save, sender=OrderItem)
def create_order_items(sender, instance, created, **kwargs):
    seller = Telegram.objects.get(user__id=instance.product.seller_id)
    buyer = Telegram.objects.get(user__id=instance.order.buyer_id)
    send_order_item_approval.delay(seller_id=seller.telegram_id,
                                   product_name=instance.product.name,
                                   product_id=instance.product.id,
                                   quantity=instance.quantity,
                                   buyer_id=buyer.telegram_id,
                                   price=instance.product.price)
