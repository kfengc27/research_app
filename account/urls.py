from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import logout_then_login

from . import views  

urlpatterns = [
    # post views
    # url(r'', views.user_login, name='login'),
    # url(r'^social-auth/', include('social.apps.django_app.urls', namespace='social')),
    # url(r'^login/$', views.user_login, name = "login"),
    #login / logou urls 
    url(r'^login/$',
        LoginView.as_view(),
        name='login'),
    url(r'^logout/$',
        LogoutView.as_view(),
        name='logout'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
    url(r'^$', views.dashboard, name='dashboard'),

    # url(r'^logout-then-login/$',
    #     logout_then_login.views(),
    #     name='logout_then_login'),

    # url(r'^logout/$', 'django.contrib.auth.views.logout', name ='logout'),
    # url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
    
]


