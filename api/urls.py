from django.urls import include, path
from rest_framework import routers
from .views import EtudiantViewSet, FiliereViewSet, ModuleViewSet, EtudiantParticipeModuleViewSet


router = routers.DefaultRouter()
router.register(r'etudiants', EtudiantViewSet)
# router.register(r'Ici', ViewEtudiantFiliereViewSet, basename="etudiant")
router.register(r'filieres', FiliereViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'participe', EtudiantParticipeModuleViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
