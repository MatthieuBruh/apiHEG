from django.template.context_processors import request
from rest_framework import filters, generics

from django_filters.rest_framework import DjangoFilterBackend as Searcher
from rest_framework import viewsets
from rest_framework import permissions
from url_filter.integrations.drf import DjangoFilterBackend
from .models import Etudiant, Filiere, Module, EtudiantParticipeModule
from .serializers import EtudiantSerializer, FiliereSerializer, ModuleSerializer, EtudiantParticipeModuleSerializer


# Create your views here.
class FiliereViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Filiere.objects.all()
    serializer_class = FiliereSerializer
    permission_classes = [permissions.IsAuthenticated]


class EtudiantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [DjangoFilterBackend, Searcher, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = '__all__'
    filterset_fields = '__all__'
    search_fields = ['nom', 'argent', 'prenom']
    ordering_fields = '__all__'


class ModuleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAuthenticated]


class EtudiantParticipeModuleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = EtudiantParticipeModule.objects.all()
    serializer_class = EtudiantParticipeModuleSerializer
    permission_classes = [permissions.IsAuthenticated]


# Tri par défaut
    # ordering = ['prénom']

    # Exemples :
    # Étudiants dont les id sont > à 3 ==> http://127.0.0.1:8000/etudiants/?id__gte=3
    # Étudiants qui ont plus de 300 CHF ==> http://127.0.0.1:8000/etudiants/?argent__gte=300
    # Étudiants qui sont dans la filière 8 ==> http://127.0.0.1:8000/etudiants/?filiere=8
    # Étudiants qui sont dans la filière 6,8 ==> http://127.0.0.1:8000/etudiants/?filiere__in=6,8
    # Étudiants qui ont un champ contenant par Cé ==> http://127.0.0.1:8000/etudiants/?search=C%C3%A9
    # Étudiants qui ont plus de 300 CHF et par ordre d'argent ==> http://127.0.0.1:8000/etudiants/?argent__gte=300&ordering=argent
    # Étudiants qui ont plus de 300 CHF et par ordre de prénom et de nom ==> http://127.0.0.1:8000/etudiants/?argent__gte=300&ordering=prenom,argent
    """
    Texte : 
    __icontains, __iexact
    __startswith, __endswith

    Nombres: 
    __lt(less than), __gt(greather than)
    __lte, __gte, __exact, != (not)
    __range (between ",")
    __startswith, __endswith
    """
