from django.http import JsonResponse
from .models import FoodCategory, Product, Nutrition


def food_category(request):
    categories = FoodCategory.objects.all().values()

    return JsonResponse({"categories": list(categories)})


def product(request):
    food_category = request.GET.get("food-category")
    products = list(Product.objects.filter(food_category=food_category).values())

    return JsonResponse({"products": products})


def nutrition(request):
    product_ids = request.GET.getlist("product")
    nutritions = list(Nutrition.objects.filter(product__in=product_ids).values())

    return JsonResponse({"nutritions": nutritions})
