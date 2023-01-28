from django.urls import path, include
from . import views
from .views import view_chemical_class
urlpatterns = [
    path(r'login', view_chemical_class.as_view({"post":"UserReg"})),
    path(r'post_values', view_chemical_class.as_view({"post":"post_API_chemical_values"})),
    path(r'get_values', view_chemical_class.as_view({"post":"get_API_chemical_values"})),
    path(r'update_values', view_chemical_class.as_view({"post":"update_values"})),
    path(r'delete_values_by_id', view_chemical_class.as_view({"post":"delate_values_by_id"})),
    path(r'delete_values', view_chemical_class.as_view({"delete":"deleteData"}))
]



