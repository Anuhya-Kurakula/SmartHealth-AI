from django.http import JsonResponse

def survey_test(request):
    return JsonResponse({
        "message": "Survey API Working"
    })