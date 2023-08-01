from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('ragistration/', views.registration),
    path('table/', views.table),
    path('update_view/<int:uid>/',views.update_view),
    path('update/',views.Update_form_data),
    path('delete/<int:pk>/',views.Delete_form_data, name="delete_user"),
    path('login/',views.User_Login),
    path('userlogin',views.Login)
]
