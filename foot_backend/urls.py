from kek.views import Test,Registr,geT
from django.conf.urls import url
from rest_framework.routers import SimpleRouter
route = SimpleRouter
urlpatterns = [
    url(r'image',Test),
    url(r'users/create',Registr.as_view(),),
    url(r'users/reg',geT,)
]
# urlpatterns=route.urls