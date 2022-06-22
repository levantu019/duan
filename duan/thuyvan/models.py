from django.contrib.gis.db import models
from nendialy.models import NenDiaLy2N5N10N
from nendialy.choices import ThuyVan as tv


# -------------------- 7. Thuỷ văn --------------------
# Abstract
class RanhGioiNuocMat(NenDiaLy2N5N10N):
    class Meta:
        abstract = True

    # Fields
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)


# Feature: 1. Biển đảo
class BienDao(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=tv.BD_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)


# Feature: 2. Đảo
class Dao(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50)
    ten = models.CharField(max_length=255)
    loaiTrangThaiXuatLo = models.IntegerField(choices=tv.DAO_LOAITTXL_CHOICES)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)


# Feature: 3. Bãi bồi
class BaiBoi(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=tv.BB_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)
    loaiBaiBoi = models.IntegerField(choices=tv.BB_LOAI_CHOICES)
    trangThaiXuatLo = models.IntegerField(choices=tv.BB_TTXL_CHOICES)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)


# Feature: 4. Bãi đá dưới nước
class BaiDaDuoiNuoc(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=tv.BDDN_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)
    trangThaiXuatLo = models.IntegerField(choices=tv.BDDN_TTXL_CHOICES)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)


# Feature: 5. Nguồn nước
class NguonNuoc(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=tv.NN_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)
    loaiNguonNuoc = models.IntegerField(choices=tv.NN_LOAI_CHOICES)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)


# Feature: 6. Điểm độ cao mực nước
class DiemDoCaoMucNuoc(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=tv.DDCMN_CHOICES)
    doCao = models.FloatField()
    GM_Point = models.PointField(null=True, blank=True, srid=4756)

# Feature: 7. Đường bờ nước
class DuongBoNuoc(RanhGioiNuocMat):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=tv.DBN_CHOICES)
    loaiTrangThaiDuongBoNuoc = models.IntegerField(choices=tv.DBN_LOAITT_CHOICES)
    loaiDuongBoNuoc = models.IntegerField(choices=tv.DBN_LOAI_CHOICES)


# Feature: 8. Đường mép nước
class DuongMepNuoc(RanhGioiNuocMat):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=tv.DMN_CHOICES)
    loaiDuongMepNuoc = models.IntegerField(choices=tv.DMN_LOAI_CHOICES)


# Feature: 9. Ranh giới nước mặt quy ước
class RanhGioiNuocMatQuyUoc(RanhGioiNuocMat):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=tv.RGNMQU_CHOICES)
    loaiRanhGioiNuocMatQuyUoc = models.IntegerField(choices=tv.RGNMQU_LOAI_CHOICES)


# Feature: 10. Bờ kè bờ cạp
class BoKeBoCap(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=tv.BKBC_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)
    loaiChatLieu = models.IntegerField(choices=tv.BKBC_LOAICL_CHOICES)
    loaiThanhPhan = models.IntegerField(choices=tv.BKBC_LOAITP_CHOICES)
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)


# Feature: 11. Kênh mương
class KenhMuong(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=tv.KM_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)
    loaiHienTrangSuDung = models.IntegerField(choices=tv.KM_LOAIHTSD_CHOICES)
    chieuRong = models.FloatField()
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)


# Feature: 12. Trạm thu thập TTTV
class TramThuThapKTTV(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        
    # Fields
    maTramKTTV = models.CharField(max_length=50, choices=tv.TTTKTTV_CHOICES)
    tenTram = models.CharField(max_length=255)
    loaiTramThuThapKTTV = models.IntegerField(choices=tv.TTTKTTV_LOAI_CHOICES)
    kieuThuThapKTTV = models.IntegerField(choices=tv.TTTKTTV_KTT_CHOICES)
    Mota_TramKTTV = models.CharField(max_length=500, null=True, blank=True)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)


# Feature: 13. Tham số KTTV
class ThamSoKTTV(models.Model):
    class Meta:
        ordering = ['id']
        
    # Fields
    maThamSoKTTV = models.CharField(max_length=50, choices=tv.TSKTTV_CHOICES)
    thoigianThuThap = models.DateTimeField(null=True, blank=True)
    giatriThang1 = models.FloatField(null=True, blank=True)
    giatriThang2 = models.FloatField(null=True, blank=True)
    giatriThang3 = models.FloatField(null=True, blank=True)
    giatriThang4 = models.FloatField(null=True, blank=True)
    giatriThang5 = models.FloatField(null=True, blank=True)
    giatriThang6 = models.FloatField(null=True, blank=True)
    giatriThang7 = models.FloatField(null=True, blank=True)
    giatriThang8 = models.FloatField(null=True, blank=True)
    giatriThang9 = models.FloatField(null=True, blank=True)
    giatriThang10 = models.FloatField(null=True, blank=True)
    giatriThang11 = models.FloatField(null=True, blank=True)
    giatriThang12 = models.FloatField(null=True, blank=True)
    thamSo = models.IntegerField(choices=tv.TSKTTV_TS_CHOICES)
    tramKTTV = models.ForeignKey(TramThuThapKTTV, on_delete=models.CASCADE)


# Feature: 14. Số liệu sóng, gió, dòng chảy
class SongGioDongChay(models.Model):
    class Meta:
        ordering = ['id']
        
    # Fields
    maSongGioDongChay = models.CharField(max_length=50, choices=tv.SGDC_CHOICES)
    thoigianThuThap = models.DateTimeField(null=True, blank=True)
    huongThang1 = models.CharField(max_length=50, choices=tv.SGDC_HUONG_CHOICES)
    giaTriThang1 = models.FloatField()
    huongThang2 = models.CharField(max_length=50, choices=tv.SGDC_HUONG_CHOICES)
    giaTriThang2 = models.FloatField()
    huongThang3 = models.CharField(max_length=50, choices=tv.SGDC_HUONG_CHOICES)
    giaTriThang3 = models.FloatField()
    huongThang4 = models.CharField(max_length=50, choices=tv.SGDC_HUONG_CHOICES)
    giaTriThang4 = models.FloatField()
    huongThang5 = models.CharField(max_length=50, choices=tv.SGDC_HUONG_CHOICES)
    giaTriThang5 = models.FloatField()
    huongThang6 = models.CharField(max_length=50, choices=tv.SGDC_HUONG_CHOICES)
    giaTriThang6 = models.FloatField()
    huongThang7 = models.CharField(max_length=50, choices=tv.SGDC_HUONG_CHOICES)
    giaTriThang7 = models.FloatField()
    huongThang8 = models.CharField(max_length=50, choices=tv.SGDC_HUONG_CHOICES)
    giaTriThang8 = models.FloatField()
    huongThang9 = models.CharField(max_length=50, choices=tv.SGDC_HUONG_CHOICES)
    giaTriThang9 = models.FloatField()
    huongThang10 = models.CharField(max_length=50, choices=tv.SGDC_HUONG_CHOICES)
    giaTriThang10 = models.FloatField()
    huongThang11 = models.CharField(max_length=50, choices=tv.SGDC_HUONG_CHOICES)
    giaTriThang11 = models.FloatField()
    huongThang12 = models.CharField(max_length=50, choices=tv.SGDC_HUONG_CHOICES)
    giaTriThang12 = models.FloatField()
    thamSo = models.IntegerField(choices=tv.SGDC_TS_CHOICES)
    tramKTTV = models.ForeignKey(TramThuThapKTTV, on_delete=models.CASCADE)


# Feature: 15. Tham số nước
class ThamSoNuoc(models.Model):
    class Meta:
        ordering = ['id']
        
    # Fields
    maThamSoNuoc = models.CharField(max_length=50, choices=tv.TSN_CHOICES)
    thoigianThuThap = models.DateTimeField(null=True, blank=True)
    giatriThang1 = models.FloatField(null=True, blank=True)
    giatriThang2 = models.FloatField(null=True, blank=True)
    giatriThang3 = models.FloatField(null=True, blank=True)
    giatriThang4 = models.FloatField(null=True, blank=True)
    giatriThang5 = models.FloatField(null=True, blank=True)
    giatriThang6 = models.FloatField(null=True, blank=True)
    giatriThang7 = models.FloatField(null=True, blank=True)
    giatriThang8 = models.FloatField(null=True, blank=True)
    giatriThang9 = models.FloatField(null=True, blank=True)
    giatriThang10 = models.FloatField(null=True, blank=True)
    giatriThang11 = models.FloatField(null=True, blank=True)
    giatriThang12 = models.FloatField(null=True, blank=True)
    tangDoSau = models.IntegerField(choices=tv.TSN_TDS_CHOICES)
    thamSo = models.IntegerField(choices=tv.TSN_TS_CHOICES)
    tramKTTV = models.ForeignKey(TramThuThapKTTV, on_delete=models.CASCADE)



