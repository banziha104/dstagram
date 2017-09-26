from django.conf.urls import url,include


urlpatterns = [
    url(r'^login/$',include('django.contrib.auth.urls')),
    url(r'^logout')
]