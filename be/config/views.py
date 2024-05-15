from django.http import JsonResponse


def health_check(request):
    return JsonResponse({"health": True}, status=200)
