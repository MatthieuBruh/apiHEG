from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Etudiant, Filiere, Module, EtudiantParticipeModule


class FiliereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filiere
        fields = '__all__'


class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = '__all__'  # ['nom', 'prenom', 'argent', 'filiere']
        # depth = 1


class ModuleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'


class EtudiantParticipeModuleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EtudiantParticipeModule
        fields = '__all__'
