from django.contrib import admin
from .models import (
    DuongBo,
    CongGiaoThong,
    DuongBang,
    BaiDapTrucThang,
    BaoHieuHangHaiAIS,
    BenCang,
    CauTau,
    BaoHieuDanLuongHangHaiDuongThuy,
    CacDoiTuongHangHaiHaiVan,
    NhomAuTau
)
from nendialy.admin import CustomGeoAdmin


# Register
admin.site.register(DuongBo, CustomGeoAdmin)
admin.site.register(CongGiaoThong, CustomGeoAdmin)
admin.site.register(DuongBang, CustomGeoAdmin)
admin.site.register(BaiDapTrucThang, CustomGeoAdmin)
admin.site.register(BaoHieuHangHaiAIS, CustomGeoAdmin)
admin.site.register(BenCang, CustomGeoAdmin)
admin.site.register(CauTau, CustomGeoAdmin)
admin.site.register(BaoHieuDanLuongHangHaiDuongThuy, CustomGeoAdmin)
admin.site.register(CacDoiTuongHangHaiHaiVan, CustomGeoAdmin)
admin.site.register(NhomAuTau, CustomGeoAdmin)