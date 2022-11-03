# """mysite URL Configuration
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

# mysite/urls.py
from django.contrib import admin
from django.urls import path
from .views import get_cars, get_customer, get_employee, get_orders, save_car, save_customer, save_employee,\
    update_car, update_customer, update_employee, delete_car, delete_customer, delete_employee, order_car,\
    cancel_order, rent_car, return_car

# save_order,
urlpatterns = [
    # path("", admin.site.urls),
    path("admin/", admin.site.urls),
    path("cars/", get_cars),
    path("customers/", get_customer),
    path("employees/", get_employee),
    path("orders/", get_orders),
    path("save_car/", save_car),
    path("order_car/<int:customer_id>/<int:car_id>/", order_car),
    path("delete_car/<int:id>/", delete_car),
    path("update_car/<int:id>/", update_car),
    path("update_customer/<int:id>/", update_customer),
    path("delete_customer/<int:id>/", delete_customer),
    path("save_customer/", save_customer),
    path("update_employee/<int:id>/", update_employee),
    path("save_employee/", save_employee),
    path("delete_employee/<int:id>/", delete_employee),
    path("cancel_order/<int:order_id>/<int:customer_id>/<int:car_id>/", cancel_order),
    path("rent_car/<int:order_id>/<int:customer_id>/<int:car_id>/", rent_car),
    path("return_car/<int:order_id>/<int:customer_id>/<int:car_id>/<int:damaged>/", return_car),
]
