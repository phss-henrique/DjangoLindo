from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario, Imovel, Contrato, Pagamento
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated


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
"""
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
    """




    #  ///////////// APIView

"""class UsuarioView(APIView):
    def get(self, request):
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UsuarioDetailView(APIView):
    def get_object(self,pk):
        return Usuario.objects.get(pk=pk)
    def get(self, pk):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)
    
    def put(self, request, pk):
        usuario = self.get_object(pk=pk)
        serializer = UsuarioSerializer(usuario, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


class ImovelView(APIView):
    def get(self, request):
        imovel = Imovel.objects.all()
        serializer = ImovelSerializer(imovel, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ImovelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ImovelDetailView(APIView):
    def get_object(self,pk):
        return Imovel.objects.get(pk=pk)
    def get(self, pk):
        imovel = self.get_object(pk)
        serializer = ImovelSerializer(imovel)
        return Response(serializer.data)
    
    def put(self, request, pk):
        imovel = self.get_object(pk=pk)
        serializer = ImovelSerializer(imovel, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        

        
class ContratoView(APIView):
    def get(self, request):
        contrato = Contrato.objects.all()
        serializer = ContratoSerializer(contrato, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ContratoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ContratoDetailView(APIView):
    def get_object(self,pk):
        return Contrato.objects.get(pk=pk)
    def get(self, pk):
        contrato = self.get_object(pk)
        serializer = ContratoSerializer(contrato)
        return Response(serializer.data)
    
    def put(self, request, pk):
        contrato = self.get_object(pk=pk)
        serializer = ContratoSerializer(contrato, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
class PagamentoView(APIView):
    def get(self, request):
        pagamento = Pagamento.objects.all()
        serializer = PagamentoSerializer(pagamento, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PagamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PagamentoDetailView(APIView):
    def get_object(self,pk):
        return Pagamento.objects.get(pk=pk)
    def get(self, pk):
        pagamento = self.get_object(pk)
        serializer = ContratoSerializer(pagamento)
        return Response(serializer.data)
    
    def put(self, request, pk):
        pagamento = self.get_object(pk=pk)
        serializer = PagamentoSerializer(pagamento, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)"""

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]  
        return [IsAuthenticated()] 

class ImovelViewSet(ModelViewSet):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

class ContratoViewSet(ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

class PagamentoViewSet(ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer

             