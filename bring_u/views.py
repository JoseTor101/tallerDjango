from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse
from .models import Restaurants,Menu
# Create your views here.


def restaurants(request):
    searchRestaurant= request.GET.get('searchRestaurant')
    if searchRestaurant:
        movies = Movie.objects.filter(title__icontains = searchRestaurant)
    else:
        movies = Movie.objects.all()
    return render(request, 'restaurants.html', {'searchRestaurant': searchRestaurant, 'movies': movies})

def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurants, pk=restaurant_id)
    menu_items = restaurant.menu_set.all()  # Obtener todos los platos asociados al restaurante
    return render(request, 'restaurant_detail.html', {'restaurant': restaurant, 'menu_items': menu_items})