from django.urls import path

from hierarchy.apps import HierarchyConfig

from hierarchy.views import (ContactsCreateAPIView,
                             ContactsListAPIView,
                             ContactsUpdateAPIView,
                             ContactsDestroyAPIView,
                             ContactsRetrieveAPIView,
                             ProductsCreateAPIView,
                             ProductsListAPIView,
                             ProductsUpdateAPIView,
                             ProductsDestroyAPIView,
                             ProductsRetrieveAPIView,
                             FactoryCreateAPIView,
                             FactoryListAPIView,
                             FactoryUpdateAPIView,
                             FactoryDestroyAPIView,
                             FactoryRetrieveAPIView,
                             RetailCreateAPIView,
                             RetailListAPIView,
                             RetailUpdateAPIView,
                             RetailDestroyAPIView,
                             RetailRetrieveAPIView,
                             EntrepreneurCreateAPIView,
                             EntrepreneurListAPIView,
                             EntrepreneurUpdateAPIView,
                             EntrepreneurDestroyAPIView,
                             EntrepreneurRetrieveAPIView
                             )

app_name = HierarchyConfig.name

urlpatterns = [
    # контакты
    path('contacts/create/', ContactsCreateAPIView.as_view(), name='contacts_create'),
    path('contacts/list/', ContactsListAPIView.as_view(), name='contacts_list'),
    path('contacts/update/<int:pk>/', ContactsUpdateAPIView.as_view(), name='contacts_update'),
    path('contacts/delete/<int:pk>/', ContactsDestroyAPIView.as_view(), name='contacts_delete'),
    path('contacts/<int:pk>/', ContactsRetrieveAPIView.as_view(), name='contacts_get'),

    # продукты
    path('products/create/', ProductsCreateAPIView.as_view(), name='products_create'),
    path('products/list/', ProductsListAPIView.as_view(), name='products_list'),
    path('products/update/<int:pk>/', ProductsUpdateAPIView.as_view(), name='products_update'),
    path('products/delete/<int:pk>/', ProductsDestroyAPIView.as_view(), name='products_delete'),
    path('products/<int:pk>/', ProductsRetrieveAPIView.as_view(), name='products_get'),

    # заводы
    path('factory/create/', FactoryCreateAPIView.as_view(), name='factory_create'),
    path('factory/list/', FactoryListAPIView.as_view(), name='factory_list'),
    path('factory/update/<int:pk>/', FactoryUpdateAPIView.as_view(), name='factory_update'),
    path('factory/delete/<int:pk>/', FactoryDestroyAPIView.as_view(), name='factory_delete'),
    path('factory/<int:pk>/', FactoryRetrieveAPIView.as_view(), name='factory_get'),

    # розничные сети
    path('retail/create/', RetailCreateAPIView.as_view(), name='retail_create'),
    path('retail/list/', RetailListAPIView.as_view(), name='retail_list'),
    path('retail/update/<int:pk>/', RetailUpdateAPIView.as_view(), name='retail_update'),
    path('retail/delete/<int:pk>/', RetailDestroyAPIView.as_view(), name='retail_delete'),
    path('retail/<int:pk>/', RetailRetrieveAPIView.as_view(), name='retail_get'),

    # индивидуальные предприниматели
    path('entrepreneur/create/', EntrepreneurCreateAPIView.as_view(), name='entrepreneur_create'),
    path('entrepreneur/list/', EntrepreneurListAPIView.as_view(), name='entrepreneur_list'),
    path('entrepreneur/update/<int:pk>/', EntrepreneurUpdateAPIView.as_view(), name='entrepreneur_update'),
    path('entrepreneur/delete/<int:pk>/', EntrepreneurDestroyAPIView.as_view(), name='entrepreneur_delete'),
    path('entrepreneur/<int:pk>/', EntrepreneurRetrieveAPIView.as_view(), name='entrepreneur_get'),
              ]
