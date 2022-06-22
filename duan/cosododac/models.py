from django.contrib.gis.db import models
from nendialy.models import NenDiaLy2N5N10N
from nendialy.choices import CoSoDoDac as csdd


# -------------------- 2. Cơ sở đo đạc --------------------
# Abstract
class CoSoDoDac(NenDiaLy2N5N10N):
    class Meta:
        abstract = True
        
    # Fields
    soHieuDiem = models.CharField(max_length=50)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)


# Feature: 1. Điểm gốc đo đạc quốc gia
class DiemGocDoDacQuocGia(CoSoDoDac):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=csdd.DGDDQG_CHOICES)
    doCao = models.FloatField()

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 2. Điểm đo đạc quốc gia
class DiemDoDacQuocGia(CoSoDoDac):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=csdd.DDDQG_CHOICES)
    doCao = models.FloatField()
    loaiMoc = models.IntegerField(choices=csdd.DDDQG_LOAIMOC_CHOICES)
    loaiCapHang = models.IntegerField(choices=csdd.DDDQG_LOAICAPHANG_CHOICES)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 3. Trạm định vị vệ tinh quốc gia
class TramDinhViVeTinhQuocGia(CoSoDoDac):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=csdd.TDVVTQG_CHOICES)
    ten = models.CharField(max_length=255)
    loaiTramDinhViVeTinh = models.IntegerField(choices=csdd.TDVVTQG_LOAI_CHOICES)
    
    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()
