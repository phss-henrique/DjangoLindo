from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario, Imovel, Contrato, Pagamento
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView


@api_view(['GET','POST','PUT','DELETE'])
def listUsers(request):
    if request.method == 'GET':
        queryset = Usuario.objects.all()
        serializers = UsuarioSerializer(queryset, many=True)
        return Response(serializers.data) 
    
    elif request.method == 'POST':
        serializers = UsuarioSerializer(data = request.data, many=False)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        
    elif request.method == 'PUT':
        serializers = UsuarioSerializer(data = request.data, many=False)
        if serializers.is_valid():
            serializers.update()
            return Response(serializers.data,status=status.HTTP_202_ACCEPTED)
        
    else:
        return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','PUT','DELETE'])
def listImoveis(request):
    if request.method == 'GET':
        queryset = Imovel.objects.all()
        serializers = ImovelSerializer(queryset, many=True)
        return Response(serializers.data) 
    
    elif request.method == 'POST':
        serializers = ImovelSerializer(data = request.data, many=False)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        
    elif request.method == 'PUT':
        serializers = ImovelSerializer(data = request.data, many=False)
        if serializers.is_valid():
            serializers.update()
            return Response(serializers.data,status=status.HTTP_202_ACCEPTED)
        
    else:
        return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','POST','PUT','DELETE'])
def listContratos(request):
    if request.method == 'GET':
        queryset = Contrato.objects.all()
        serializers = ImovelSerializer(queryset, many=True)
        return Response(serializers.data) 
    
    elif request.method == 'POST':
        serializers = ContratoSerializer(data = request.data, many=False)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        
    elif request.method == 'PUT':
        serializers = ContratoSerializer(data = request.data, many=False)
        if serializers.is_valid():
            serializers.update()
            return Response(serializers.data,status=status.HTTP_202_ACCEPTED)
        
    else:
        return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)    
    
@api_view(['GET','POST','PUT','DELETE'])
def listPagamentos(request):
    if request.method == 'GET':
        queryset = Pagamento.objects.all()
        serializers = PagamentoSerializer(queryset, many=True)
        return Response(serializers.data) 
    
    elif request.method == 'POST':
        serializers = PagamentoSerializer(data = request.data, many=False)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        
    elif request.method == 'PUT':
        serializers = PagamentoSerializer(data = request.data, many=False)
        if serializers.is_valid():
            serializers.update()
            return Response(serializers.data,status=status.HTTP_202_ACCEPTED)
        
    else:
        return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)  
    


class UsuarioView(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetailView(RetrieveDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class ImovelView(ListCreateAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

class ImovelDetailView(RetrieveDestroyAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer


class ContratoView(ListCreateAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

class ContratoDetailView(RetrieveDestroyAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

    
class PagamentoView(ListCreateAPIView):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer

class PagamentoDetailView(RetrieveDestroyAPIView):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer