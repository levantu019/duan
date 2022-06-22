from django.contrib.gis.db import models
from nendialy.models import NenDiaLy2N5N10N
from nendialy.choices import GiaoThong as gt


# -------------------- 5. Giao thông --------------------
# Abstract


# Feature: 1. Đường bộ
class DuongBo(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=gt.DB_CHOICES)
    loaiDuongBo = models.IntegerField(choices=gt.DB_LOAI_CHOICES)
    capKyThuat = models.IntegerField(choices=gt.DB_CKT_CHOICES)
    loaiChatLieuTraiMat = models.IntegerField(choices=gt.DB_LOAICLTM_CHOICES)
    loaiHienTrangSuDung = models.IntegerField(choices=gt.DB_LOAIHTSD_CHOICES)
    chieuXeChay = models.IntegerField(choices=gt.DB_CHIEUXECHAY_CHOICES)
    viTri = models.IntegerField(choices=gt.DB_VITRI_CHOICES)
    soLanDuong = models.IntegerField()
    chieuRong = models.FloatField()
    ten = models.CharField(max_length=255)
    lienKetGiaoThong = models.IntegerField(choices=gt.DB_LKGT_CHOICES)
    tenTuyenGiaoThongXuyenQuocGia = models.CharField(max_length=255)
    tenQuocLo = models.CharField(max_length=255)
    tenDuongTinh = models.CharField(max_length=255)
    tenDuongHuyen = models.CharField(max_length=255)
    tenDuongXa = models.CharField(max_length=255)
    tenDuongDoThi = models.CharField(max_length=255)
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)


# Feature: 2. Cống giao thông
class CongGiaoThong(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=gt.CGT_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)


# Feature: 3. Đường băng
class DuongBang(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=gt.DBANG_CHOICES)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)


# Feature: 4. Bãi đáp trực thăng
class BaiDapTrucThang(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=gt.BDTT_CHOICES)
    viTriBaiDap = models.IntegerField(choices=gt.BDTT_VTBD_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)


# Feature: 5. Báo hiệu hàng hải AIS
class BaoHieuHangHaiAIS(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=gt.BHHHAIS_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)


# Feature: 6. Bến cảng
class BenCang(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=gt.BC_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)


# Feature: 7. Cầu tàu
class CauTau(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=gt.CT_CHOICES)
    loaiCauTau = models.IntegerField(choices=gt.CT_LOAI_CHOICES)
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)


# Feature: 8. Báo hiệu dẫn luồng hàng hải đường thuỷ
class BaoHieuDanLuongHangHaiDuongThuy(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=gt.BHDLHHDT_CHOICES)
    coDen = models.BooleanField(default=True)
    huongBaoHieu = models.IntegerField(choices=gt.BHDLHHDT_HUONGBH_CHOICES)
    hinhDang = models.IntegerField(choices=gt.BHDLHHDT_HINHDANG_CHOICES)
    mauSac = models.IntegerField(choices=gt.BHDLHHDT_MAUSAC_CHOICES)
    phoiHopMauSac = models.IntegerField(choices=gt.BHDLHHDT_PHMS_CHOICES)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)


# Feature: 9. Các đối tượng hàng hải hải văn
class CacDoiTuongHangHaiHaiVan(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=gt.CDTHHHV_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)


# Feature: 10. Nhóm Âu tàu
class NhomAuTau(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=gt.NAT_CHOICES)
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

