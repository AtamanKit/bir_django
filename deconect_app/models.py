from django.db import models

class Deconect(models.Model):
    oficiul = models.CharField(max_length=10, default="Oficiul")
    nr_ordine = models.CharField(max_length=10, default="Nr. ordine")
    pt = models.CharField(max_length=256, blank=True)
    fid_04kv = models.CharField(max_length=256, blank=True)
    data_dec = models.CharField(max_length=256, blank=True)
    data_conect = models.CharField(max_length=256, blank=True)
    durata = models.CharField(max_length=256, blank=True)
    cons_cas = models.CharField(max_length=10, blank=True)
    cons_ec = models.CharField(max_length=10, blank=True)
    total = models.CharField(max_length=10, blank=True)
    localitate = models.CharField(max_length=10, blank=True)
    cauza = models.CharField(max_length=256, blank=True)
    termen = models.CharField(max_length=64, blank=True)
