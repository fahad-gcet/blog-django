from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^new/$', views.CreateView.as_view(), name='create'),
	url(r'^login/$', auth_views.login, {'template_name': 'core/login.html'}, name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
	url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
]