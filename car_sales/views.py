from django.shortcuts import render
from car.models import Car
from brand.models import Brand

def home(request, brand_slug=None):
    data = Car.objects.all()
    brands = Brand.objects.all()

    if brand_slug:
        brand = Brand.objects.get(slug=brand_slug)
        data = Car.objects.filter(brand=brand)

    return render(request, 'home.html', {'data': data, 'brand': brands})
