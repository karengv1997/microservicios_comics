from django.http.response import JsonResponse
from . import services

def get_comics_results(**kwargs):
    results = services.get_comics()
    comics_list = [
        {
        'id': comic['id'],
        'title': comic['title'],
        'image': comic['thumbnail']['path'],
        'onSaleDate': comic['dates'][0]['date'],
        }
        for comic in results['data']['results']
    ]
    if kwargs:
        lookup = {comic['title']: comic for comic in comics_list}
        return lookup[kwargs['title']]

    return sorted(comics_list, key=lambda x: x['title'])

def get_personajes_results(**kwargs):
    results = services.get_personajes()
    personajes_list = [
        {
        'id': personaje['id'],
        'name': personaje['name'],
        'image': personaje['thumbnail']['path'],
        'appearences': personaje['comics']['available'],
        }
        for personaje in results['data']['results']
    ]
    if kwargs:
        lookup = {personaje['name']: personaje for personaje in personajes_list}
        return lookup[kwargs['name']]

    return sorted(personajes_list, key=lambda x: x['name'])

def comics(request, *args, **kwargs):
    return JsonResponse({'results': get_comics_results(**kwargs)})

def personajes(request, *args, **kwargs):
    return JsonResponse({'results': get_personajes_results(**kwargs)})

def results(request):
    comics = get_comics_results()
    personajes = get_personajes_results()
    results = [f"{comic}{personaje}" for comic, personaje in zip(comics, personajes)]
    return JsonResponse({'results': comics + personajes})