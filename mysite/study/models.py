from django.db import models

#Sets
#take all sets that has more than 5 cards in them
class CanUseManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(card_amount__gt=5)
        )
    
class Set(models.Model):
    card_amount = models.IntegerField()
    name = models.CharField(max_length=100)
    objects = models.Manager()
    can_use = CanUseManager()


    class Meta:
        ordering = ['name']

#Cards
class Card(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=255)
    set = models.ForeignKey(
        Set,
        on_delete = models.CASCADE,
        related_name = 'cards'
    )
    objects = models.Manager()
    
    def __str__(self):
        return f"Question: {self.question} | Answer: {self.answer}"


