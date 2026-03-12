from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Card

def update_card_amount(card_instance):
    related_set = card_instance.set
    related_set.card_amount = related_set.cards.count()
    related_set.save()

# +1 to the relative set card amount when creating a new card
@receiver(post_save, sender=Card)
def card_created(sender, instance, **kwargs):
    update_card_amount(instance)

# -1 to relative set card amount when deleting a new card(future feature)
@receiver(post_delete, sender=Card)
def card_deleted(sender, instance, **kwargs):
    update_card_amount(instance)