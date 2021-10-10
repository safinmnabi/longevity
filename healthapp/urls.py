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
    path('cpack/', views.createpack, name='createpack'),
    path('pack/', views.fetch_subpack, name='getpack'),
    path('del/<id>', views.delete, name='del'),
    path('subpack/<id>', views.buysubscription, name='updatepack'),
    path('reward/', views.rewards, name='rewards'),
    path('pay/', views.payments, name='payments'),
    path('gre/', views.fetch_reward, name='gre'),
    path('gpay/', views.fetch_pay, name='pay'),
    path('upload/', views.filepost, name='filepost'),
    path('flist/', views.filelist, name='filelist'),
    path('gc/', views.getcsv, name='getcsv'),
    path('dismod/<did>', views.dismod, name='dismod'),
    path('getmod/<did>/<uid>', views.getdismod, name='getdismod'),
    path('cmp/<did>', views.postpathology, name='postpathology'),
    path('getp/<did>/<uid>', views.getpathology, name='getpathology'),
    path('dp/<id>', views.deletep, name='deletep'),


]