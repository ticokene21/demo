from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),

    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<question_id>[0-9]+)/delete/$', views.delete_question, name='delete'),
    url(r'^(?P<question_id>[0-9]+)/edit/$', views.edit_question, name='edit'),
  
    url(r'^insertQ/$', views.insert_question, name='vote'),
    #url(r'^/delete/$', views.delete, name='vote'),
    #url(r'^(?P<question_id>[0-9]+)/edit/$', views.vote, name='vote'),
]