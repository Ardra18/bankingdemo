
from django.urls import path
from . import views
app_name='bankapp'

urlpatterns = [

    path('',views.index,name='index'),
    path('',views.allDistCat,name='allDistCat'),
    path('<slug:c_slug/',views.allDistCat,name='districts_by_category')

]