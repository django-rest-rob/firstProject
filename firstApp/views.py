from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def employeeView(request):
    emp = {
    'id': 123,
    'name': 'Robert',
    'salary': 10000
    }

    #JsonResponse will serialize the emp dict into JSON
    return JsonResponse(emp)
