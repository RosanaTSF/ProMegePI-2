from django.urls import path, include

from .views import DeleteView, SupplierCreateView, SupplierListView, SupplierDetailView, PhoneSupplierCreateView

urlpatterns = [
    path("", SupplierListView.as_view(), name="supplier-index"),
    path("Detail/<int:pk>/", SupplierDetailView.as_view(), name="supplier-detail"),
    path("new", SupplierCreateView.as_view(), name="supplier-new"),    
    # path("detail", IndexView.as_view(), name="supplier-index"),
    path("delete/", DeleteView.as_view(), name="supplier-delete"),
    # phone_supplier
    path("NewPhoneNumber/<int:int>/", PhoneSupplierCreateView.as_view(), name="supplier-createphone")
]