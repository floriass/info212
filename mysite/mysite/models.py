from django.db import models

class Car(models.Model):
    make = models.CharField(max_length = 50)
    carmodel = models.CharField(max_length = 50)
    year = models.CharField(max_length = 4)
    location = models.CharField(max_length = 50)
    status = models.CharField(max_length = 50)

    def __str__(self):
        return self.make + ' '+ self.carmodel + ' '+ self.year + ' '+ self.location + ' '+ self.status

class Customer(models.Model):
    name = models.CharField(max_length = 50)
    age = models.CharField(max_length = 3)
    address = models.CharField(max_length = 50)
    has_car = models.CharField(max_length = 1)

    def __str__(self):
        return self.name + ' ' + self.age + ' ' + self.address + ' ' + self.has_car

class Employee(models.Model):
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 50)
    branch = models.CharField(max_length = 50)

    def __str__(self):
        return self.name + ' ' + self.address + ' ' + self.branch

class Order(models.Model):
    car = models.CharField(max_length = 50)
    customer = models.CharField(max_length = 50)

    def __str__(self):
        return self.car + ' ' + self.customer

