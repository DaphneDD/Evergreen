from django.shortcuts import render

from django.http import JsonResponse

def test_list(request):
    if request.method == 'GET':
        data = request.GET
    else:
        data = {"message": "This route only handles get request"}
    return JsonResponse(data)
