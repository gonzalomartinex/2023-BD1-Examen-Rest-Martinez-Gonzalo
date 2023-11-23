from django.shortcuts import render
from api.models import *
from api.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])

def categories(request):
        if request.method == 'GET':
            categories = Categories.objects.all()
            serializer = CategoriesSerializer(categories, many = True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = CategoriesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])

def categoriesid(request, id):
        try:
            categories = Categories.objects.get(categoryid=id)
        except categories.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = CategoriesSerializer(categories, many = False)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            serializer = CategoriesSerializer(categories, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            categories.delete()
            return Response(status=status.HTTP_200_OK)
             

@api_view(['GET','POST'])

def customers(request):
        if request.method == 'GET':
            customers = Customers.objects.all()
            serializer = CustomersSerializer(customers, many = True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = CustomersSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])

def customersid(request, id):
        try:
            customers = Customers.objects.get(customerid=id)
        except customers.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = CustomersSerializer(customers, many = False)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            serializer = CustomersSerializer(customers, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            customers.delete()
            return Response(status=status.HTTP_200_OK)        
            
@api_view(['GET','POST'])

def suppliers(request):
        if request.method == 'GET':
            suppliers = Suppliers.objects.all()
            serializer = SuppliersSerializer(suppliers, many = True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = SuppliersSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])

def suppliersid(request, id):
        try:
            suppliers = Suppliers.objects.get(supplierid=id)
        except Suppliers.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


        if request.method == 'GET':
            serializer = SuppliersSerializer(suppliers, many = False)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            serializer = SuppliersSerializer(suppliers, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            suppliers.delete()
            return Response(status=status.HTTP_200_OK)  

@api_view(['GET', 'POST'])
def products(request):
    if request.method == 'GET':
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def productsid(request, id):
    try:
        products = Products.objects.get(productid=id)
    except products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET': 
        serializer = ProductsSerializer(products, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductsSerializer(products, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        products.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])

def orders(request):
        if request.method == 'GET':
            orders = Orders.objects.all()
            serializer = OrdersSerializer(orders, many = True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = OrdersSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])

def ordersid(request, id):
        try:
            orders = Orders.objects.get(orderid=id)
        except orders.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = OrdersSerializer(orders, many = False)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            serializer = OrdersSerializer(orders, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            orders.delete()
            return Response(status=status.HTTP_200_OK)
        
@api_view(['GET', 'POST'])

def orderdetails(request):
        if request.method == 'GET':
            orderdetails = Orderdetails.objects.all()
            serializer = OrderdetailsSerializer(orderdetails, many = True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = OrderdetailsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])

def orderdetailsid(request, id):
        try:
            orderdetails = Orderdetails.objects.get(orderid=id)
        except orderdetails.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = OrderdetailsSerializer(orderdetails, many = False)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            serializer = OrderdetailsSerializer(orderdetails, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            orderdetails.delete()
            return Response(status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])

def employees(request):
        if request.method == 'GET':
            employees = Employees.objects.all()
            serializer = EmployeesSerializer(employees, many = True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = EmployeesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            employees.delete()
            return Response(status=status.HTTP_200_OK)
        
        
@api_view(['GET', 'PUT', 'DELETE'])

def employeesid(request, id):
        try:
            employees = Employees.objects.get(employeeid=id)
        except employees.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = EmployeesSerializer(employees, many = False)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            serializer = EmployeesSerializer(employees, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            employees.delete()
            return Response(status=status.HTTP_200_OK)

@api_view(['GET'])

def endpoint1(request):
        if request.method == 'GET':
            categories = Categories.objects.filter(categoryid = 6)
            serializer = prueba1Serialzer(categories, many = True)
            return Response(serializer.data)