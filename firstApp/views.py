from django.shortcuts import render
from django.http import JsonResponse
from firstApp.models import Employee

# Create your views here.
def employeeView(request):
    '''emp = {
    'id': 123,
    'name': 'Robert',
    'salary': 10000
    }'''

    # Get all Employees from db
    data = Employee.objects.all()
    # convert result QuerySet to a Dictionary usable by JsonResponse
    response = {'employees': list(data.values('name', 'salary'))}

    #JsonResponse will serialize the dict into JSON
    return JsonResponse(response)
























#
