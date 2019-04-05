from django.conf.urls import include, url
from . import views  

urlpatterns = [
    # post views
    url(r'', views.user_login, name='login'),
    # url(r'^social-auth/', include('social.apps.django_app.urls', namespace='social')),
]


