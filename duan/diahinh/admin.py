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


# Register
admin.site.register(DiemDoCao)
admin.site.register(DuongBinhDo)
admin.site.register(ChatDay)
admin.site.register(DiemDoSau)
admin.site.register(DuongBinhDoSau)
admin.site.register(DiaHinhDacBietDayBien)
admin.site.register(DiaMao)
admin.site.register(MoHinhSoDoCaoGocLopDiem)
admin.site.register(MoHinhSoDoCaoGocLopDuong)
admin.site.register(MoHinhSoDoCaoGocLopVung)
admin.site.register(MoHinhSoDoCaoGocLopVungBienTap)
admin.site.register(LopLuoiTamGiacBatQuyTac)
admin.site.register(LopRaster)
admin.site.register(HoKhoanDiaChat)
admin.site.register(SoLieuHKDC)
admin.site.register(MatCatDienHinh)
admin.site.register(LoaiDiaChat)