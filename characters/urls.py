from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CharacterViewSet

router = DefaultRouter()
router.register(r'characters', CharacterViewSet, basename="character")



def home(request):
    return JsonResponse({"message": "Welcome to the Harry Potter Character API!", "api_docs": "/api/"})

urlpatterns = [
    path('', home),  
    path('admin/', admin.site.urls),
    path('api/', include('characters.urls')),
    path('', include(router.urls)),
]



from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CharacterViewSet

router = DefaultRouter()
router.register(r'characters', CharacterViewSet, basename="character")

urlpatterns = router.urls
