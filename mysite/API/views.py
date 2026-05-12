from django.shortcuts import render
import requests

# THIS APP IS TO PURELY SHOW THAT I'M ABLE 
# TO DEMONSTRATE MY COMPETENCY IN 
# CONNECTING TO AN API 

def fetch_osrs_data(request):

    response = requests.get(
        'https://secure.runescape.com/m=itemdb_oldschool/api/catalogue/items.json?category=1&alpha=c&page=2',
        params = {

        }
        )
    result = response.json().get('items', [])
    return render(
        request,
        'API/api.html',
        {
            'data': result 
        }
    )