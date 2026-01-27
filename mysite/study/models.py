from django.db import models
from django.urls import reverse

#Sets
#take all sets that has more than 5 cards in them
class CanUseManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(card_amount__gt=5)
        )
    
class Set(models.Model):
    name = models.CharField(max_length=100)
    card_amount = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique_for_date='created')

    # Managers
    objects = models.Manager()
    # custum managers
    # only sets with more than 5 cards
    can_use = CanUseManager()
    
    class Meta:
        ordering = ['name']
   
    # 
    def get_absolute_url(self):
        return reverse(
            'study:view_cards', 
            args=[
                self.slug
                ]) 
    
    def __str__(self):
        return f"Name: {self.name} Amount of Cards: {self.card_amount}"

#Cards
class Card(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    false_answer_1 = models.CharField(max_length=500)
    false_answer_2 = models.CharField(max_length=500)
    false_answer_3 = models.CharField(max_length=500)
    set = models.ForeignKey(
        Set,
        on_delete = models.CASCADE,
        related_name = 'cards'
    )

    # managers
    objects = models.Manager()
    
    def __str__(self):
        return f"Question: {self.question} | Answer: {self.answer}"


