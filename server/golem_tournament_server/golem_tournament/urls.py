from django.conf.urls import url
from golem_tournament import views

urlpatterns = [
    url(r'^golems/$', views.GolemList.as_view()),
    url(r'^golems/create/$', views.GolemCreator.as_view()),
    url(r'^golems/(?P<pk>[0-9]+)/$', views.GolemDetail.as_view()),
]
