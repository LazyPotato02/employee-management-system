from django.urls import path

from employee_management_sys.materials.views import MaterialAddView, MaterialListView, MaterialEditView, \
    MaterialDeleteView

urlpatterns = [
    path('add', MaterialAddView.as_view(), name='material add'),
    path('list', MaterialListView.as_view(), name='material list'),
    path('edit/<int:pk>', MaterialEditView.as_view(), name='material edit'),
    path('delete/<int:pk>', MaterialDeleteView.as_view(), name='material delete'),
]
