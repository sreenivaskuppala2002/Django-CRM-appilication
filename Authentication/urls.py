from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register,name='register'),
    path('createcustomer/',views.createcustomer,name='createcustomer'),
    path('update/<int:pk>',views.update,name='update'),
    path('select/<int:id>',views.select,name='select'),
    path('delete/<int:pk>',views.delete,name='delete')
]

