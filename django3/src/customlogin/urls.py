from django.urls.conf import path
from customlogin.views import *
app_name='cl'   #customlogin
urlpatterns=[
    path('signup/',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('signout/',signout,name='signout')
    
    ]