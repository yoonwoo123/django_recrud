from django.contrib import admin
from django.urls import path
from . import views

app_name = 'boards'
# boards:index
urlpatterns = [
    path('', views.index, name='index'), # boards/  , name으로 지정해서 쓰면 url에서 통째로 관리하기 유용하다.
    path('new/', views.new, name='new'), # boards/new/
    # path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    # path('<int:pk>/update/', views.update, name='update'),
]