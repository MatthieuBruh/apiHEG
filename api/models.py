from django.db import models
from django.db.models import constraints


# Create your models here.
from django.template.defaultfilters import upper


class Filiere (models.Model):
    fil_id = models.CharField(max_length=3)
    fil_name = models.CharField(max_length=50)

    def __str__(self):
        return self.fil_name


class Module(models.Model):
    mod_numero = models.IntegerField(primary_key=True)
    mod_nom = models.CharField(max_length=60)

    def __str__(self):
        return "(" + str(self.mod_numero) + ") " + self.mod_nom


class Etudiant (models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    filiere = models.ForeignKey(Filiere, related_name='etudiants', on_delete=models.CASCADE)
    argent = models.IntegerField()
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True)

    def __str__(self):
        return self.nom.upper() + " " + self.prenom


class EtudiantParticipeModule(models.Model):
    par_etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    par_module = models.ForeignKey(Module, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('par_etudiant', 'par_module'),)


"""
insert into api_etudiant (id, nom, prenom, argent, date, filiere_id) values (1, 'Goldby', 'Tabbi', 214, '1995-11-26', 1);
insert into api_etudiant (id, nom, prenom, argent, date, filiere_id) values (2, 'Bellino', 'Cello', 572, '2003-12-06', 1);
insert into api_etudiant (id, nom, prenom, argent, date, filiere_id) values (3, 'Churms', 'Erminia', 425, '1996-12-04', 1);
insert into api_etudiant (id, nom, prenom, argent, date, filiere_id) values (4, 'Langthorne', 'Saul', 343, '1993-12-08', 1);
insert into api_etudiant (id, nom, prenom, argent, date, filiere_id) values (5, 'Dolman', 'Eilis', 943, '2003-08-26', 4);
insert into api_etudiant (id, nom, prenom, argent, date, filiere_id) values (6, 'Cowmeadow', 'Kamillah', 815, '2000-10-20', 4);
insert into api_etudiant (id, nom, prenom, argent, date, filiere_id) values (7, 'Achrameev', 'Nadya', 601, '1999-12-03', 4);
insert into api_etudiant (id, nom, prenom, argent, date, filiere_id) values (8, 'Huntington', 'Jamie', 992, '2002-11-23', 4);
insert into api_etudiant (id, nom, prenom, argent, date, filiere_id) values (9, 'Melville', 'Poul', 650, '1992-12-17', 2);
insert into api_etudiant (id, nom, prenom, argent, date, filiere_id) values (10, 'Woolvett', 'Juliann', 190, '1994-08-25', 2);
insert into api_etudiant (id, nom, prenom, argent, date, filiere_id) values (11, 'Pittwood', 'Biddie', 339, '2001-08-09', 2);
insert into api_etudiant (id, nom, prenom, argent, date, filiere_id) values (12, 'Alben', 'Saxe', 489, '1992-06-11', 2);
insert into api_etudiant (id, nom, prenom, argent, date, filiere_id) values (13, 'Glentz', 'Kevon', 915, '1998-01-20', 2);
insert into api_etudiant (id, nom, prenom, argent, date, filiere_id) values (14, 'Roskilly', 'Greer', 401, '1993-11-17', 3);
insert into api_etudiant (id, nom, prenom, argent, date, filiere_id) values (15, 'Mellor', 'Aurthur', 755, '1994-08-01', 3);
insert into api_etudiant (id, nom, prenom, argent, date, filiere_id) values (16, 'Jepps', 'Rocky', 329, '2004-02-11', 3);
insert into api_etudiant (id, nom, prenom, argent, date, filiere_id) values (17, 'Heazel', 'Marylin', 874, '1998-07-10', 3);
insert into api_etudiant (id, nom, prenom, argent, date, filiere_id) values (18, 'Andre', 'Miquela', 853, '1990-10-14', 1);
insert into api_etudiant (id, nom, prenom, argent, date, filiere_id) values (19, 'ODee', 'Willis', 557, '1997-04-17', 1);
insert into api_etudiant (id, nom, prenom, argent, date, filiere_id) values (20, 'Stockey', 'Lynnette', 658, '1993-09-07', 4);
"""
