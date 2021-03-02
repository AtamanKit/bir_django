from django.db import models

class Deranj(models.Model):
    OF_CHOICES = [
        ('UN', 'Ungheni'),
        ('FL', 'Falesti'),
        ('GL', 'Glodeni'),
        ('RS', 'Riscani'),
    ]

    oficiul = models.CharField(max_length=10, choices=OF_CHOICES, default="Oficiul")
    nr_ordine = models.CharField(max_length=10, default="Nr. ordine")
    transmis = models.CharField(max_length=256, default="Transmis")
    sector = models.CharField(max_length=256, default="Sector")
    instalatia = models.CharField(max_length=256, default="LEA-0,4kv")
    fid_10kv = models.CharField(max_length=256, blank=True)
    pt = models.CharField(max_length=256, blank=True)
    fid_04kv = models.CharField(max_length=256, blank=True)
    continutul = models.CharField(max_length=256, default="Continutuil")
    data = models.DateField(auto_now=True)
    responsabil = models.CharField(max_length=256, default="Responsabil")
    starea = models.CharField(max_length=256, default="Neexecutat")
