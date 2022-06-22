from django.contrib.gis.db import models
from nendialy.models import NenDiaLy2N5N10N
from nendialy.choices import DanCu as dc


# -------------------- 3. Dân cư --------------------
# Abstract


# Feature: 1. Khu dân cư
class KhuDanCu(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.KDC_CHOICES)
    loaiKhuDanCu = models.IntegerField(choices=dc.KDC_LOAI_CHOICES)
    soDan = models.IntegerField(null=True, blank=True)
    ten = models.CharField(max_length=255, null=True, blank=True)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 2. Nhà
class Nha(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.NHA_CHOICES)
    loaiNha = models.IntegerField(choices=dc.NHA_LOAI_CHOICES)
    mucDoKienCo = models.IntegerField(choices=dc.NHA_MUCDOKIENCO_CHOICES)
    chieuCao = models.FloatField()
    soTang = models.IntegerField()
    ten = models.CharField(max_length=255, null=True, blank=True)
    diaChi = models.CharField(max_length=255, null=True, blank=True)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 3. Công trình phụ trợ
class CongTrinhPhuTro(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.CTPT_CHOICES)
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 4. Khối nhà
class KhoiNha(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.KN_CHOICES)
    nhomSoTang = models.IntegerField(choices=dc.KN_NHOMSOTANG_CHOICES)
    nhomChieuCao = models.IntegerField(choices=dc.KN_NHOMCHIEUCAO_CHOICES)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 5. Địa danh dân cư
class DiaDanhDanCu(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.DD_CHOICES)
    danhTuChung = models.IntegerField(choices=dc.DD_DANHTUCHUNG_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 6. Hạ tầng kỹ thuật khác
class HaTangKyThuatKhac(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.HTKTK_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)
    chieuCao = models.FloatField(null=True, blank=True)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 7. Trạm khí tượng thuỷ văn quốc gia
class TramKhiTuongThuyVanQuocGia(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.TKTTVQG_CHOICES)
    loaiTramKhiTuongThuyVan = models.IntegerField(choices=dc.TKTTVQG_LOAI_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 8. Trạm quan trắc môi trường
class TramQuanTracMoiTruong(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.TQTMT_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 9. Trạm quan trắc tài nguyên nước
class TramQuanTracTaiNguyenNuoc(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.TQTTNN_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 10. Đường dây tải điện
class DuongDayTaiDien(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.DDTD_CHOICES)
    dienAp = models.FloatField()
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 11. Cột điện
class CotDien(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.CD_CHOICES)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 12. Đường ống dẫn
class DuongOngDan(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.DOD_CHOICES)
    loaiOngDan = models.IntegerField(choices=dc.DOD_LOAI_CHOICES)
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 13. Ranh giới
class RanhGioi(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']

    # Fields
    maDoiTuong = models.CharField(max_length=50)
    loaiRanhGioi = models.IntegerField(choices=dc.RG_LOAI_CHOICES)
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 14. Công trình y tế
class CongTrinhYTe(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.CTYT_CHOICES)
    capYTe = models.IntegerField(choices=dc.CTYT_CAPYTE_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 15. Công trình giáo dục
class CongTrinhGiaoDuc(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.CTGD_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 16. Công trình thể thao
class CongTrinhTheThao(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.CTTT_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 17. Công trình văn hoá
class CongTrinhVanHoa(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.CTVH_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)
    xepHangDiTich = models.IntegerField(choices=dc.CTVH_XEPHANG_CHOICES)
    chieuCao = models.FloatField(null=True, blank=True)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 18. Công trình thương mại dịch vụ
class CongTrinhThuongMaiDichVu(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.CTTMDV_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 19. Công trình tôn giáo tín ngưỡng
class CongTrinhTonGiaoTinNguong(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.CTTGTN_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)
    xepHangDiTich = models.IntegerField(choices=dc.CTTGTN_XEPHANG_CHOICES)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 20. Trụ sở cơ quan nhà nước
class TruSoCoQuanNhaNuoc(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.TSCQNN_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 21. Công trình công nghiệp
class CongTrinhCongNghiep(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.CTCN_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)
    loaiCongTrinhCongNghiep = models.IntegerField(choices=dc.CTCN_LOAI_CHOICES)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 22. Cơ sở sản xuất nông lâm nghiệp
class CoSoSanXuatNongLamNghiep(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.CSSXNLN_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 23. Khu chức năng đặc thù
class KhuChucNangDacThu(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.KCNDT_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 24. Công trình xử lý chát thải
class CongTrinhXuLyChatThai(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.CTXLCT_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 25. Công trình an ninh
class CongTrinhAnNinh(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.CTAN_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)
    
    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()

    # @property
    def set_GM_Point(self, data):
        self.GM_Point = data


# Feature: 26. Công trình quốc phòng
class CongTrinhQuocPhong(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']

    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dc.CTQP_CHOICES)
    ten = models.CharField(max_length=255, null=True, blank=True)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()

