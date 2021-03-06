from django.conf.urls import url
from golem_tournament import views

urlpatterns = [
    url(r'^sign_up/$', views.SignUp.as_view(), name="sign_up"),
    url(r'^golems/$', views.GolemList.as_view()),
    url(r'^golems/create/$', views.GolemCreator.as_view()),
    url(r'^golems/(?P<pk>[0-9]+)/$', views.GolemDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<username>[A-Za-z0-9_-]+)/$', views.UserDetail.as_view()),
]
