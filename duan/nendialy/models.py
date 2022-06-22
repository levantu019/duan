from django.contrib.gis.db import models

# Models

# -------------------- Nền địa lý 2000, 5000, 1000 --------------------
# Abstract
class NenDiaLy2N5N10N(models.Model):
    class Meta:
        abstract = True

    # Fields
    maNhanDang = models.CharField(max_length=50)
    phienBan = models.IntegerField()
    ngayPhienBan = models.DateTimeField()
    giaTriDoChinhXacMatPhang = models.FloatField(null=True, blank=True)
    nguyenNhanThayDoi = models.CharField(max_length=250, null=True, blank=True)