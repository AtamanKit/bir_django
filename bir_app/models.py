from django.db import models

class AL(models.Model):
    OF_CHOICES = [
        ('UN', 'Ungheni'),
        ('FL', 'Falesti'),
        ('GL', 'Glodeni'),
        ('RS', 'Riscani'),
    ]

    oficiul = models.CharField(max_length=10, choices=OF_CHOICES, default="Oficiul")
    nr_ds = models.CharField(max_length=10, blank=True)
    nr_al = models.CharField(max_length=10, blank=True)
    instalatia = models.CharField(max_length=256, default="Instalatia")
    pt = models.CharField(max_length=256, blank=True)
    localitatea = models.CharField(max_length=256, blank=True)
    fid_nr = models.CharField(max_length=256, blank=True)
    lucrarile = models.CharField(max_length=256, default="Lucrarile")
    sef = models.CharField(max_length=36, default="Sef")
    mem_ech = models.CharField(max_length=256, blank=True)
    emitent = models.CharField(max_length=36, default="Emitent")
    cu_dec = models.CharField(max_length=36, blank=True)
    mas_teh = models.CharField(max_length=256, blank=True)
    semnatura = models.CharField(max_length=36, default="Semnatura")
    starea = models.CharField(max_length=256, default="Starea")
    pregatire = models.CharField(max_length=256, default="Pregatire")
    admitere = models.CharField(max_length=256, default="Admitere")
    terminare = models.CharField(max_length=256, default="Terminare")
    link = models.CharField(max_length=256, blank=True)