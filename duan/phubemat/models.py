from django.contrib.gis.db import models
from nendialy.models import NenDiaLy2N5N10N
from nendialy.choices import PhuBeMat as pbm


# -------------------- 6. Phủ bề mặt --------------------
# Abstract
class PhuBeMat(NenDiaLy2N5N10N):
    class Meta:
        abstract = True

    # Fiedls
    GM_Surface = models.PolygonField(null=True, blank=True)


# Feature: 1. Cây độc lập
class CayDocLap(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=pbm.CDL_CHOICES)
    tenCay = models.CharField(max_length=255)
    chieuCao = models.FloatField()
    GM_Point = models.PointField(null=True, blank=True)


# Feature: 2. Ranh giới phủ bề mặt
class RanhGioiPhuBeMat(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=pbm.RGPBM_CHOICES)
    loaiRanhGioiPhuBeMat = models.IntegerField(choices=pbm.RGPBM_LOAI_CHOICES)
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)


# Feature: 3. Bề mặt công trình
class BeMatCongTrinh(PhuBeMat):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=pbm.BMCT_CHOICES)
    thucVat = models.IntegerField(choices=pbm.BMCT_TV_CHOICES)


# Feature: 4. Bề mặt khu dân cư
class BeMatKhuDanCu(PhuBeMat):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=pbm.BMKDC_CHOICES)
    thucVat = models.IntegerField(choices=pbm.BMKDC_TV_CHOICES)


# Feature: 5. Đất trống
class DatTrong(PhuBeMat):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=pbm.DT_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)


# Feature: 6. Nước mặt 
class NuocMat(PhuBeMat):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=pbm.NM_CHOICES)


# Feature: 7. Thực vật đáy biển
class ThucVatDayBien(PhuBeMat):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=pbm.TVDB_CHOICES)