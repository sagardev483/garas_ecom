from django.urls import path, include

from products import views

urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view(), name='latest-products'),
    path('categories/', views.CategoryList.as_view(), name='categories'),


]
