from django.shortcuts import get_object_or_404, render
from .models import Set, Card

# look at all set you own
def set_collection(request):
    
    sets = Set.can_use.all()

    return render(
        request,
        'study/collection/collection.html',
        {'sets': sets}
    )

# review the flashcards
def view_cards(request, id):
    selected_set = get_object_or_404(Set, id=id)
    cards = selected_set.cards.all()
    
    return render(
        request,
        'study/collection/viewCards.html',
        {'cards': cards}
    )
