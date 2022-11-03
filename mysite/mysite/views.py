# mysite/views.py
from .models import Car, Customer, Employee, Order
from rest_framework.response import Response
from .serializers import CarSerializer, CustomerSerializer, EmployeeSerializer, OrderSerializer
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view
# @api_view(['GET'])
#
# def get_cars(request):
#     cars = Car.objects.all()
#     serializer = CarSerializer(cars, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
# def get_customers(request):
#     customer = Customer.objects.all()
#     serializer = CustomerSerializer(customer, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
# def get_employees(request):
#     employee = Employee.objects.all()
#     serializer = EmployeeSerializer(employee, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
# def get_orders(request):
#     order = Order.objects.all()
#     serializer = OrderSerializer(order, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
# @api_view(['POST'])
# def save_car(request):
#     serializer = CarSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
# @api_view(['PUT'])
# def update_car(request, car_id):
#     try:
#         theCar = Car.objects.get(pk=car_id)
#     except Car.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     serializer = CarSerializer(theCar, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(status=status.HTTP_400_BAD_REQUEST)

# Cars
@api_view(['GET'])
def get_cars(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def save_car(request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def update_car(request, id):
    try:
        theCar = Car.object.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CarSerializer(theCar, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAB_REQUEST)

@api_view(['DELETE'])
def delete_car(request, id):
    try:
        theCar = Car.object.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    theCar.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Customers
@api_view(['GET'])
def get_customer(request):
    customer = Customer.objects.all()
    serializer = CustomerSerializer(customer, many=True)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def save_customer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def update_customer(request, id):
    try:
        theCustomer = Customer.object.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CustomerSerializer(theCustomer, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAB_REQUEST)

@api_view(['DELETE'])
def delete_customer(request, id):
    try:
        theCustomer = Customer.object.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    theCustomer.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Employees
@api_view(['GET'])
def get_employee(request):
    employee = Employee.objects.all()
    serializer = EmployeeSerializer(employee, many=True)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def save_employee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def update_employee(request, id):
    try:
        theEmployee = Employee.object.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = EmployeeSerializer(theEmployee, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAB_REQUEST)

@api_view(['DELETE'])
def delete_employee(request, id):
    try:
        theEmployee = Employee.object.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    theEmployee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Orders
@api_view(['GET'])
def get_orders(request):
    order = Order.objects.all()
    serializer = OrderSerializer(order, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def order_car(request, customer_id, car_id):
    try:
        car = Car.objects.get(pk=car_id)
        customer = Customer.objects.get(pk=customer_id)
    except Car.DoesNotExist or Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if car.status == "booked":
        return Response(status=status.HTTP_400_BAD_REQUEST)

    car.status = "booked"
    car.save(update_fields=["status"])

    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def cancel_order(request, order_id, customer_id, car_id):
    try:
        car = Car.objects.get(pk=car_id)
        customer = Customer.objects.get(pk=customer_id)
        order = Order.objects.get(pk=order_id) # ???
    except Car.DoesNotExist or Customer.DoesNotExist or Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if car.status != "booked":
        return Response(status=status.HTTP_400_BAD_REQUEST)

    car.status = "available"

    car.save(update_fields=["status"])

    order.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def rent_car(request, order_id, customer_id, car_id):
    try:
        car = Car.objects.get(pk=car_id)
        customer = Customer.objects.get(pk=customer_id)
        order = Order.objects.get(pk=order_id)
    except Car.DoesNotExist or Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if car.status != "booked" or customer.has_car == "y":
        return Response(status=status.HTTP_400_BAD_REQUEST)

    car.status = "rented"
    customer.has_car = "y"

    car.save(update_fields=["status"])
    customer.save(update_fields=["has_car"])

    serializer = OrderSerializer(order, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAB_REQUEST)

@api_view(['PUT'])
def return_car(request, order_id, customer_id, car_id, damaged):
    try:
        car = Car.objects.get(pk=car_id)
        customer = Customer.objects.get(pk=customer_id)
        order = Order.objects.get(pk=order_id)
    except Car.DoesNotExist or Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if car.status != "rented" or customer.has_car == "n":
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if damaged:
        car.status = "damaged"
    else:
        car.status = "available"
    customer.has_car = "n"

    car.save(update_fields=["status"])
    customer.save(update_fields=["has_car"])

    serializer = OrderSerializer(order, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAB_REQUEST)