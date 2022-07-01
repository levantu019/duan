from django.contrib import admin
from .models import(
    NVDH,
    DiemNVDH,
    TuyenNVDH,
    VungNVDH,
    DonVi,
    NVBP,
    PhuongAnViTri,
    PhuongAnTuyen,
    PhuongAnVung,
    PheDuyetPhuongAnViTri,
    PheDuyetPhuongAnTuyen,
    PheDuyetPhuongAnVung,
    PheDuyetChungNVBP,
    GanLucLuong,
    PheDuyetPhuongAnGanLucLuong
)
from nendialy.admin import CustomGeoAdmin


admin.site.register(NVDH, CustomGeoAdmin)
admin.site.register(DiemNVDH, CustomGeoAdmin)
admin.site.register(TuyenNVDH, CustomGeoAdmin)
admin.site.register(VungNVDH, CustomGeoAdmin)
admin.site.register(DonVi, CustomGeoAdmin)
admin.site.register(NVBP, CustomGeoAdmin)
admin.site.register(PhuongAnViTri, CustomGeoAdmin)
admin.site.register(PhuongAnTuyen, CustomGeoAdmin)
admin.site.register(PhuongAnVung, CustomGeoAdmin)
admin.site.register(PheDuyetPhuongAnViTri, CustomGeoAdmin)
admin.site.register(PheDuyetPhuongAnTuyen, CustomGeoAdmin)
admin.site.register(PheDuyetPhuongAnVung, CustomGeoAdmin)
admin.site.register(PheDuyetChungNVBP, CustomGeoAdmin)
admin.site.register(GanLucLuong, CustomGeoAdmin)
admin.site.register(PheDuyetPhuongAnGanLucLuong, CustomGeoAdmin)