from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def sensor(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # print(data)
        return JsonResponse(data)



def chart(request):
    return render(request, 'application/chart.html')
