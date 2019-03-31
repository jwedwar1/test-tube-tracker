from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signup/$', views.SignUp, name='signup'),
    path('create_sample/', views.CreateSampleView.as_view(), name = 'create_sample'),
    path('sample_add/', views.AddSample, name = 'sample_add'),
    #path('samples/', views.SampleListView.as_view(), name='sample_list'),
    path('sample/<int:pk>', views.SampleDetailView.as_view(), name='sample-detail'),
    path('sample/<int:pk>/update/', views.SampleUpdate.as_view(), name='sample_update'),
    path('sample/<int:pk>/delete/', views.SampleDelete.as_view(), name='sample_delete'),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    path('newlist/', views.TableView.as_view(), name='new_sample_list'),
    url(r'^table/', views.sampledef)
    
]
