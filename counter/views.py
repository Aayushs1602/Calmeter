from django.shortcuts import render
import requests
import json

# +cvFmARzAxzIBYPBbcrFHw==t1rqyyvNViQ5TeKa
# Create your views here.
def home(request):

    if request.method == 'POST':
        query = request.POST['query']
        print(query)
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query, headers={'X-Api-Key':'+cvFmARzAxzIBYPBbcrFHw==t1rqyyvNViQ5TeKa'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = 'There was an error'
            print(e)
        return render(request, 'home.html', {'api': api})  
    else:  
        return render(request, 'home.html', {'query': 'Entry a valid query'})
