from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from .models import CustomUser
from .serializers import AdminSerializer


def index(request):
    return render(request,"index.html")

class adminUser(APIView):
    def post(self,request,*args,**kwargs):
        serializer=AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def get(self,request,*args,**kwargs):
        qs=CustomUser.objects.all()
        data1=AdminSerializer(qs,many=True)
        return Response(data1.data)
    def delete(self, request, pk):
        try:
            instance = CustomUser.objects.get(id=pk)
        except CustomUser.DoesNotExist:
            return Response({"error": "Object does not exist"})
        
        instance.delete()
        return Response({"msg": "Deleted"})
    
    def patch(self, request, pk):
        try:
            instance = CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return Response({"error": "Object does not exist"})

        serializer = AdminSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
