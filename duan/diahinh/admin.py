from django.contrib import admin
from .models import (
    DiemDoCao,
    DuongBinhDo,
    ChatDay,
    DiemDoSau,
    DuongBinhDoSau,
    DiaHinhDacBietDayBien,
    DiaMao,
    MoHinhSoDoCaoGocLopDiem,
    MoHinhSoDoCaoGocLopDuong,
    MoHinhSoDoCaoGocLopVung,
    MoHinhSoDoCaoGocLopVungBienTap,
    LopLuoiTamGiacBatQuyTac,
    LopRaster,
    HoKhoanDiaChat,
    SoLieuHKDC,
    MatCatDienHinh,
    LoaiDiaChat
)
from nendialy.admin import CustomGeoAdmin


# Register
admin.site.register(DiemDoCao, CustomGeoAdmin)
admin.site.register(DuongBinhDo, CustomGeoAdmin)
admin.site.register(ChatDay, CustomGeoAdmin)
admin.site.register(DiemDoSau, CustomGeoAdmin)
admin.site.register(DuongBinhDoSau, CustomGeoAdmin)
admin.site.register(DiaHinhDacBietDayBien, CustomGeoAdmin)
admin.site.register(DiaMao, CustomGeoAdmin)
admin.site.register(MoHinhSoDoCaoGocLopDiem, CustomGeoAdmin)
admin.site.register(MoHinhSoDoCaoGocLopDuong, CustomGeoAdmin)
admin.site.register(MoHinhSoDoCaoGocLopVung, CustomGeoAdmin)
admin.site.register(MoHinhSoDoCaoGocLopVungBienTap, CustomGeoAdmin)
admin.site.register(LopLuoiTamGiacBatQuyTac, CustomGeoAdmin)
admin.site.register(LopRaster, CustomGeoAdmin)
admin.site.register(HoKhoanDiaChat, CustomGeoAdmin)
admin.site.register(SoLieuHKDC, CustomGeoAdmin)
admin.site.register(MatCatDienHinh, CustomGeoAdmin)
admin.site.register(LoaiDiaChat, CustomGeoAdmin)