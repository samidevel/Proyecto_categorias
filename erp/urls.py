from django.urls import path
from erp.views.category.views import category_list

app_name = 'erp'

urlpatterns = [

    path('category/list/', category_list, name='category_list'),
    
]