import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grupos.settings')

django.setup()

from appgrupos.models import Meys, Organizacion1, Documento, Dependencia
from groups_manager.models import Member, MemberMixin
from django.db.models.signals import post_save, post_delete
from groups_manager.models import group_save, group_delete, Group, GroupType




post_save.connect(group_save, sender=Organizacion1)
post_delete.connect(group_delete, sender=Organizacion1)
post_save.connect(group_save, sender=Dependencia)
post_delete.connect(group_delete, sender=Dependencia)


def crear():
      
    
    Organizacion1.objects.all().delete()
    Dependencia.objects.all().delete()
    Member.objects.all().delete()
    
    jemco = Organizacion1(name='JEMCO')
    jemco.save()
    subjemco = Organizacion1(name='SUBJEMCO', parent=jemco)
    subjemco.save()
    coffa = Organizacion1(name='COFFA', parent=subjemco)
    coffa.save()
    meyscoffa = Dependencia(name='Meys COFFA', parent=coffa)
    meyscoffa.save()
    dependencia = Dependencia(name='Departamento Materiales', parent=coffa)
    dependencia.save()
    # Creacion de miembros y asignacion a grupos
    raul = Member.objects.create(first_name='Raul', last_name='Olmos')
    meyscoffa.add_member(raul)
    documento = Documento.objects.create(documento='3TU1-1234/5')
    #raul.assign_object(meyscoffa, documento, custom_permissions=custom_permissions)
    raul.assign_object(meyscoffa, documento)
    g = Group.objects.all()
    print(g)
    
        

if __name__ == '__main__':
    crear()
    print("Listo")
