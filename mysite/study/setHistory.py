from django.conf import settings
from .models import Set

class History:
    def __init__(self, request):
        self.session = request.session
        
        history = self.session.get(settings.HISTORY_SESSION_ID)
        if not history:
            history = self.session[settings.HISTORY_SESSION_ID] = {}
        self.history = history

    def SaveHistory(self, set):
        set_id = str(set.id)
        if set_id not in self.history:
            self.history[set_id] = {
                'name': set.name,
                'card_amount': set.card_amount
            }
        self.save()

    def __iter__(self):
        for set_id, data in self.history.items():
            yield {
                'set_id': set_id,
                'name': data['name'],
                'card_amount': data['card_amount'],
            }

    def save(self):
        self.session.modified = True