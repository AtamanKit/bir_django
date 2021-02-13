from django.db import models

class AL(models.Model):
    OF_CHOICES = [
        ('UN', 'Ungheni'),
        ('FL', 'Falesti'),
        ('GL', 'Glodeni'),
        ('RS', 'Riscani'),
    ]

    oficiul = models.CharField(max_length=10, choices=OF_CHOICES)
    nr_ds = models.CharField(max_length=10, blank=True)
    nr_al = models.CharField(max_length=10, blank=True)
    instalatia = models.CharField(max_length=256)
    pt = models.CharField(max_length=256, blank=True)
    localitatea = models.CharField(max_length=256, blank=True)
    fid_nr = models.CharField(max_length=256, blank=True)
    lucrarile = models.CharField(max_length=256)
    sef = models.CharField(max_length=36)
    mem_ech = models.CharField(max_length=256, blank=True)
    emitent = models.CharField(max_length=36)
    cu_dec = models.CharField(max_length=36, blank=True)
    mas_teh = models.CharField(max_length=256, blank=True)
    semnatura = models.CharField(max_length=36)
    starea = models.CharField(max_length=256)
    pregatire = models.CharField(max_length=256)
    admitere = models.CharField(max_length=256)
    terminare = models.CharField(max_length=256)
    link = models.CharField(max_length=256, blank=True)