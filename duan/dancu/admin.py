from django.contrib import admin
from .models import (
    KhuDanCu,
    Nha,
    CongTrinhPhuTro,
    KhoiNha,
    DiaDanhDanCu,
    HaTangKyThuatKhac,
    TramKhiTuongThuyVanQuocGia,
    TramQuanTracMoiTruong,
    TramQuanTracTaiNguyenNuoc,
    DuongDayTaiDien,
    CotDien,
    DuongOngDan,
    RanhGioi,
    CongTrinhYTe,
    CongTrinhGiaoDuc,
    CongTrinhTheThao,
    CongTrinhVanHoa,
    CongTrinhThuongMaiDichVu,
    CongTrinhTonGiaoTinNguong,
    TruSoCoQuanNhaNuoc,
    CongTrinhCongNghiep,
    CoSoSanXuatNongLamNghiep,
    KhuChucNangDacThu,
    CongTrinhXuLyChatThai,
    CongTrinhAnNinh,
    CongTrinhQuocPhong
)
from nendialy.admin import CustomGeoAdmin

# Register
admin.site.register(KhuDanCu, CustomGeoAdmin)
admin.site.register(Nha, CustomGeoAdmin)
admin.site.register(CongTrinhPhuTro, CustomGeoAdmin)
admin.site.register(KhoiNha, CustomGeoAdmin)
admin.site.register(DiaDanhDanCu, CustomGeoAdmin)
admin.site.register(HaTangKyThuatKhac, CustomGeoAdmin)
admin.site.register(TramKhiTuongThuyVanQuocGia, CustomGeoAdmin)
admin.site.register(TramQuanTracMoiTruong, CustomGeoAdmin)
admin.site.register(TramQuanTracTaiNguyenNuoc, CustomGeoAdmin)
admin.site.register(DuongDayTaiDien, CustomGeoAdmin)
admin.site.register(CotDien, CustomGeoAdmin)
admin.site.register(DuongOngDan, CustomGeoAdmin)
admin.site.register(RanhGioi, CustomGeoAdmin)
admin.site.register(CongTrinhYTe, CustomGeoAdmin)
admin.site.register(CongTrinhGiaoDuc, CustomGeoAdmin)
admin.site.register(CongTrinhTheThao, CustomGeoAdmin)
admin.site.register(CongTrinhVanHoa, CustomGeoAdmin)
admin.site.register(CongTrinhThuongMaiDichVu, CustomGeoAdmin)
admin.site.register(CongTrinhTonGiaoTinNguong, CustomGeoAdmin)
admin.site.register(TruSoCoQuanNhaNuoc, CustomGeoAdmin)
admin.site.register(CongTrinhCongNghiep, CustomGeoAdmin)
admin.site.register(CoSoSanXuatNongLamNghiep, CustomGeoAdmin)
admin.site.register(KhuChucNangDacThu, CustomGeoAdmin)
admin.site.register(CongTrinhXuLyChatThai, CustomGeoAdmin)
admin.site.register(CongTrinhAnNinh, CustomGeoAdmin)
admin.site.register(CongTrinhQuocPhong, CustomGeoAdmin)