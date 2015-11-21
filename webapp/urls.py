from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^contacts/$', views.contact_index),
	url(r'^contact/(?P<contact_id>[0-9]+)/$', views.contact_view, name='contact_view'),
]