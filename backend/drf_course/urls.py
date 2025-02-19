from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from core import views as core_views
from ecommerce import views as ecommerce_views


router = routers.DefaultRouter()
router.register(r'item', ecommerce_views.ItemViewSet, basename='item') # Those are regex urls
router.register(r'order', ecommerce_views.OrderViewSet, basename='order') # Those are regex urls

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('contact/', core_views.ContactAPIView.as_view()),
    path(
        'api-token-auth/',
        obtain_auth_token
    ), # gives us access to token auth
]
