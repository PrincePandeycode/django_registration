from django.urls import path,include
from .views import home,signIn,signout,signup

urlpatterns = [
    path('', home,name='home'),
    path('signIn', signIn,name = 'signIn'),
    path('signup' ,signup,name = 'signup'),
    path('signout', signout, name = 'signout'),
]