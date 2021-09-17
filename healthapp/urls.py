from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('create/', views.createbiodata, name='createbiodata'),
    path('risksindex/', views.risksindex, name='risksindex'),
    path('createrisk/', views.createrisk, name='createrisk'),
    path('recommindex/', views.recommindex, name='recommindex'),
    path('createrecomm/', views.createrecomm, name='createrecomm'),
    path('update/<id>', views.updatebiodata, name='updatebiodata'),

]