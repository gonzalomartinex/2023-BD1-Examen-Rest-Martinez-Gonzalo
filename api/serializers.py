from api.models import *
from rest_framework import serializers

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'

class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = '__all__'
        
class ProductsSerializer(serializers.ModelSerializer):
    supplierid = SuppliersSerializer(many=False)
    categoryid = CategoriesSerializer(many=False)
    class Meta:
        model = Products
        fields = '__all__'

class OrdersSerializer(serializers.ModelSerializer):
    customerid = CustomersSerializer(many=False)
    employeeid = EmployeesSerializer(many=False)
    class Meta:
        model = Orders
        fields = '__all__'

class OrderdetailsSerializer(serializers.ModelSerializer):
    productid = ProductsSerializer(many=False)
    class Meta:
        model = Orderdetails
        fields = '__all__'

class prueba1Serialzer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


