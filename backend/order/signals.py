from django.db.models.signals import post_save, pre_delete, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .tasks import send_order_item_approval
from .models import Order, OrderItem
from profiles.models import Telegram


@receiver(post_save, sender=OrderItem)
def create_order_items(sender, instance, created, **kwargs):
    # print(instance.product.seller.pk, instance.product.seller.pk)
    seller = Telegram.objects.get(user__id=instance.product.seller_id)
    buyer = Telegram.objects.get(user__id=instance.order.buyer_id)
    send_order_item_approval.delay(seller_id=seller.telegram_id,
                                   # building=seller.user.building,
                                   # room=seller.user.room,
                                   product_name=instance.product.name,
                                   product_id=instance.product.id,
                                   quantity=instance.quantity,
                                   buyer_id=buyer.telegram_id,
                                   price=instance.product.price)