from django.contrib.gis.db import models
from nendialy.models import NenDiaLy2N5N10N
from nendialy.choices import DiaHinh as dh


# -------------------- 4. Địa hình --------------------
# Abstract
class MoHinhSoDoCao(NenDiaLy2N5N10N):
    class Meta:
        abstract = True

class MoHinhSoDoCaoGoc(MoHinhSoDoCao):
    class Meta:
        abstract = True

class DiaChat(NenDiaLy2N5N10N):
    class Meta:
        abstract = True


# Feature: 1. Điểm độ cao
class DiemDoCao(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.DDC_CHOICES)
    doCao = models.FloatField()
    GM_Point = models.PointField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 2. Đường bình độ
class DuongBinhDo(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.DBD_CHOICES)
    loaiDuongBinhDo = models.IntegerField(choices=dh.DBD_LOAI_CHOICES)
    loaiKhoangCaoDeu = models.IntegerField(choices=dh.DBD_LOAIKCD_CHOICES)
    doCao = models.FloatField()
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 3. Chất đáy
class ChatDay(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.CD_CHOICES)
    loaiChatDay = models.IntegerField(choices=dh.CD_LOAI_CHOICES)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 4. Điểm độ sâu
class DiemDoSau(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.DDS_CHOICES)
    doSau = models.FloatField()
    GM_Point = models.PointField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 5. Đường bình độ sâu
class DuongBinhDoSau(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.DBDS_CHOICES)
    loaiDuongBinhDo = models.IntegerField(choices=dh.DBDS_LOAI_CHOICES)
    loaiKhoangCaoDeu = models.IntegerField(choices=dh.DBDS_LOAIKCD_CHOICES)
    doSau = models.FloatField()
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 6. Địa hình đặc biệt đáy biển
class DiaHinhDacBietDayBien(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.DHDBDB_CHOICES)
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 7. Địa mạo
class DiaMao(NenDiaLy2N5N10N):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDiaMao = models.CharField(max_length=50)
    tenDiaMao = models.CharField(max_length=255)
    dongLucDiaMao = models.CharField(max_length=255)
    motaDiaMao = models.CharField(max_length=255, null=True, blank=True)
    tyleDiaMao = models.FloatField()
    ghichuDiaMao = models.CharField(max_length=500, null=True, blank=True)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 8. Mô hình số độ cao gốc lớp điểm
class MoHinhSoDoCaoGocLopDiem(MoHinhSoDoCaoGoc):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.DEMGLP_CHOICES)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 9. Mô hình số độ cao gốc lớp đường
class MoHinhSoDoCaoGocLopDuong(MoHinhSoDoCaoGoc):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.DEMGLL_CHOICES)
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 10. Mô hình số độ cao gốc lớp vùng
class MoHinhSoDoCaoGocLopVung(MoHinhSoDoCaoGoc):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.DEMGLA_CHOICES)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 11. Mô hình số độ cao gốc lớp vùng biển tập
class MoHinhSoDoCaoGocLopVungBienTap(MoHinhSoDoCaoGoc):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDoiTuong = models.CharField(max_length=50, choices=dh.DEMGLVBT_CHOICES)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)

    # 
    def __str__(self):
        return self.maDoiTuong + '-' + self.get_maDoiTuong_display()


# Feature: 12. Lớp lưới tam giác bất quy tắc (TIN)
class LopLuoiTamGiacBatQuyTac(MoHinhSoDoCao):
    class Meta:
        ordering = ['id']
        
    # Fields
    doChinhXac = models.FloatField()
    # rst = 


# Feature: 13. Lớp Raster
class LopRaster(MoHinhSoDoCao):
    class Meta:
        ordering = ['id']
        
    # Fields
    maDEMRaster = models.CharField(max_length=50)
    duongDanDEMRaster = models.CharField(max_length=255)
    moTaDEM = models.CharField(max_length=500, null=True, blank=True)
    # rst


# Feature: 14. Hố khoan địa chất
class HoKhoanDiaChat(DiaChat):
    class Meta:
        ordering = ['id']
        
    # Fields
    maHoKhoanDiaChat = models.CharField(max_length=50)
    tenHoKhoanDiaChat = models.CharField(max_length=255)
    motaHoKhoanDiaChat = models.CharField(max_length=500, null=True, blank=True)
    dosauHoKhoanDiaChat = models.FloatField()
    hinhanhHoKhoanDiaChat = models.ImageField(upload_to='images/', null=True, blank=True)
    ghichuHoKhoanDiaChat = models.CharField(max_length=500, null=True, blank=True)
    GM_Point = models.PointField(null=True, blank=True, srid=4756)


# Feature: 15. Số liệu hố khoan địa chất
class SoLieuHKDC(models.Model):
    class Meta:
        ordering = ['id']
        
    # Fields
    maSolieuHoKhoanDC = models.CharField(max_length=50)
    dosauBDLaymauHKDC = models.FloatField()
    dosauKTLaymauHKDC = models.FloatField()
    soHieuMau = models.CharField(max_length=500)
    sohieuTNghiemHKDC = models.CharField(max_length=500)
    lopHKDC = models.CharField(max_length=500)
    P10 = models.FloatField(null=True, blank=True)
    P5 = models.FloatField(null=True, blank=True)
    P2 = models.FloatField(null=True, blank=True)
    P1 = models.FloatField(null=True, blank=True)
    P0_5 = models.FloatField(null=True, blank=True)
    P0_25 = models.FloatField(null=True, blank=True)
    P0_1 = models.FloatField(null=True, blank=True)
    P0_05 = models.FloatField(null=True, blank=True)
    P0_01 = models.FloatField(null=True, blank=True)
    P0_005 = models.FloatField(null=True, blank=True)
    DoAmTuNhien = models.FloatField(null=True, blank=True)
    KLTheTichTuNhien = models.FloatField(null=True, blank=True)
    KLTheTichKho = models.FloatField(null=True, blank=True)
    KLRieng = models.FloatField(null=True, blank=True)
    HeSoRong = models.FloatField(null=True, blank=True)
    DoLoRong = models.FloatField(null=True, blank=True)
    DoBaoHoa = models.FloatField(null=True, blank=True)
    GocNghiKho = models.FloatField(null=True, blank=True)
    GocNghiUot = models.FloatField(null=True, blank=True)
    HSRongLonNhat = models.FloatField(null=True, blank=True)
    HSRongNhoNhat = models.FloatField(null=True, blank=True)
    DungTrongMaxCat = models.FloatField(null=True, blank=True)
    DungTrongMinCat = models.FloatField(null=True, blank=True)
    CDKNKho = models.FloatField(null=True, blank=True)
    CDKNBaoHoa = models.FloatField(null=True, blank=True)
    CDKNHeSoMem = models.FloatField(null=True, blank=True)
    TinhCoLyDa_KLTTTN = models.FloatField(null=True, blank=True)
    TinhCoLyDa_DoRong = models.FloatField(null=True, blank=True)
    TinhCoLyDa_TyLeKheHo = models.FloatField(null=True, blank=True)
    TinhCoLyDa_DoKheHo = models.FloatField(null=True, blank=True)
    TinhCoLyDa_KLRieng = models.FloatField(null=True, blank=True)
    TNNenDa_Kho = models.FloatField(null=True, blank=True)
    TNNenDa_BaoHoa = models.FloatField(null=True, blank=True)
    TNNenDa_HeSoHM = models.FloatField(null=True, blank=True)
    R0 = models.FloatField(null=True, blank=True)
    E0 = models.FloatField(null=True, blank=True)
    Phanloaidat_HKDC = models.FloatField(null=True, blank=True)
    HKDC = models.ForeignKey(HoKhoanDiaChat, on_delete=models.CASCADE)


# Feature: 16. Mặt cắt điển hình địa chất
class MatCatDienHinh(DiaChat):
    class Meta:
        ordering = ['id']
        
    # Fields
    maMCDienHinh = models.CharField(max_length=50)
    ten = models.CharField(max_length=255, null=True, blank=True)
    hinhAnh = models.ImageField(upload_to='images/')
    moTa = models.CharField(max_length=500)
    tyLeDung = models.FloatField()
    tyLeNgang = models.FloatField()
    ghiChu = models.CharField(max_length=500, null=True, blank=True)
    GM_Curve = models.LineStringField(null=True, blank=True, srid=4756)


# Feature: 17. Loại Địa chất
class LoaiDiaChat(DiaChat):
    class Meta:
        ordering = ['id']
        
    # Fields
    maLoaiDC = models.CharField(max_length=50)
    phanHeThachHoc = models.CharField(max_length=255)
    kieuThachHoc = models.CharField(max_length=255)
    kieuDiaChatCongTrinh = models.CharField(max_length=255)
    tuoiDiaChatCongTrinh = models.FloatField()
    kyHieu = models.CharField(max_length=50, null=True, blank=True)
    moTa = models.CharField(max_length=500, null=True, blank=True)
    GM_Surface = models.PolygonField(null=True, blank=True, srid=4756)