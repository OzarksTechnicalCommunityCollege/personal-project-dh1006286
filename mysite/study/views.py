from django.shortcuts import get_object_or_404, render
from .models import Set, Card
from .forms import MakeCardForm
from django.views.decorators.http import require_POST
from django.views.generic import ListView

# Display all sets you own
class StudyListView(ListView):
    queryset =  Set.can_use.all()
    context_object_name = 'sets'
    # will change later
    paginate_by = 12
    template_name = 'study/collection/collection.html'

# review the flashcards
def view_cards(request, slug):
    selected_set = get_object_or_404(Set, slug=slug)
    cards = selected_set.cards.all()
    
    return render(
        request,
        'study/collection/viewCards.html',
        {
            'set': selected_set,
            'cards': cards,
        }
    )

# Make a new Card
def make_card(request, set_id):
    set = get_object_or_404(
        Set,
        id=set_id,
    )

    card = None

    if request.method == 'POST':
        form = MakeCardForm(data=request.POST)
        if form.is_valid():
            # unsaved comment
            card = form.save(commit=False)
            #assing set to the comment
            card.set = set
            #save the comment
            card.save()    
    else:
        form = MakeCardForm()
    return render(
        request,
        'study/collection/makeCard.html',
        {
            'set': set,
            'form': form
        },
    )