from django.shortcuts import get_object_or_404, render
from .models import Set
from .forms import MakeCardForm, MakeSetForm
from django.views.decorators.http import require_POST
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from taggit.models import Tag


# Display all sets you own
def view_sets(request, tag_slug=None):
    view_sets = Set.can_use.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        view_sets = view_sets.filter(tags__in=[tag])

    # Pagination
    paginator = Paginator(view_sets, 12)
    page_number = request.GET.get('page', 1)
    try:
        sets = paginator.page(page_number)
    except PageNotAnInteger:
        sets = paginator.page(1)
    except EmptyPage:
        sets = paginator.page(paginator.num_pages)
    return render(
        request,
        'study/collection/collection.html',
        {
            'sets': sets,
            'tag': tag
        }
   )


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

def make_set(request):
 
    if request.method == 'POST':
        form = MakeSetForm(data=request.POST)
        if form.is_valid():
            # unsaved comment
            set = form.save(commit=False)
            #save the comment
            set.save()    
    else:
        form = MakeSetForm()
    return render(
        request,
        'study/collection/makeSet.html',
        {
            'form': form
        },
    )

