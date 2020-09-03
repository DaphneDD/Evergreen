from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Candidate
from .serializers import CandidateSerializer
from django.views.decorators.csrf import csrf_exempt

def test_list(request):
    if request.method == 'GET':
        data = request.GET
    else:
        data = {"message": "This route only handles get request"}
    return JsonResponse(data)


@api_view(['GET', 'POST'])
def candidate_list(request):
    if request.method == 'GET':
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def candidate_detail(request, pk):
    try:
        candidate = Candidate.objects.get(pk=pk)
    except Candidate.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CandidateSerializer(candidate)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CandidateSerializer(candidate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        candidate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
