from django.urls import path
from income.views import (
    HomePageView, 
    FormPageView, 
    ResultPageView, 
    AdultCreate, 
    AdultDelete, 
    AdultUpdate, 
    AdultList, 
    AdultDetail, 
    ApiRoot,
    )

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('form',FormPageView.as_view(),name=FormPageView.name),
    path('result',ResultPageView.as_view(),name=ResultPageView.name),
    path('api-root/',ApiRoot.as_view(),name=ApiRoot.name),
    path('adults/',AdultList.as_view(),name=AdultList.name),
    path('adults/add/', AdultCreate.as_view(), name='adult-add'),
    path('adults/<int:pk>/',AdultDetail.as_view(),name=AdultDetail.name),
    path('adults/<int:pk>/edit/', AdultUpdate.as_view(), name='adult-edit'),
    path('adults/<int:pk>/delete/', AdultDelete.as_view(), name='adult-delete'),
]
