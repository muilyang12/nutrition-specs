import json
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from .models import FoodCategory, Product, Nutrition


@csrf_exempt
def food_category(request):
    if request.method == "GET":
        try:
            categories = FoodCategory.objects.all().values()

            return JsonResponse({"categories": list(categories)})

        except:
            return HttpResponse(status=500, content="Server Error")

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            category_name = data.get("categoryName")

            if not category_name:
                return HttpResponseBadRequest("Invalid Data")

            category = FoodCategory(category_name=category_name)
            category.save()

            return HttpResponse(status=201)

        except IntegrityError:
            return HttpResponseBadRequest("Duplicated Data")

        except:
            return HttpResponse(status=500, content="Server Error")


@csrf_exempt
def product(request):
    if request.method == "GET":
        try:
            food_category = request.GET.get("food-category")
            products = Product.objects.filter(food_category=food_category).values()

            return JsonResponse({"products": list(products)})

        except:
            return HttpResponse(status=500, content="Server Error")

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            category_id = data.get("categoryId")
            brand_name = data.get("brandName")
            product_name = data.get("productName")

            if not category_id or not brand_name or not product_name:
                return HttpResponseBadRequest("Invalid Data")

            food_category = None
            try:
                food_category = FoodCategory.objects.get(id=category_id)
            except FoodCategory.DoesNotExist:
                return HttpResponseBadRequest("Invalid Data")

            product = Product(
                food_category=food_category,
                brand_name=brand_name,
                product_name=product_name,
            )
            product.save()

            return HttpResponse(status=201)

        except:
            return HttpResponse(status=500, content="Server Error")


@csrf_exempt
def nutrition(request):
    if request.method == "GET":
        try:
            product_ids = request.GET.getlist("product")
            nutritions = Nutrition.objects.filter(product__in=product_ids).values()

            return JsonResponse({"nutritions": list(nutritions)})

        except:
            return HttpResponse(status=500, content="Server Error")

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            product_id = data.get("productId")
            serving_size = data.get("servingSize")
            calory = data.get("calory")
            carbohydrate = data.get("carbohydrate")
            protein = data.get("protein")
            fat = data.get("fat")

            if (
                not product_id
                or not serving_size
                or not calory
                or not carbohydrate
                or not protein
                or not fat
            ):
                return HttpResponseBadRequest("Invalid Data")

            product = None
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return HttpResponseBadRequest("Invalid Data")

            nutrition = Nutrition(
                product=product,
                serving_size=serving_size,
                calory=calory,
                carbohydrate=carbohydrate,
                protein=protein,
                fat=fat,
            )
            nutrition.save()

            return HttpResponse(status=201)

        except:
            return HttpResponse(status=500, content="Server Error")
