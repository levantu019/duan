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


# Register
admin.site.register(DuongBo)
admin.site.register(CongGiaoThong)
admin.site.register(DuongBang)
admin.site.register(BaiDapTrucThang)
admin.site.register(BaoHieuHangHaiAIS)
admin.site.register(BenCang)
admin.site.register(CauTau)
admin.site.register(BaoHieuDanLuongHangHaiDuongThuy)
admin.site.register(CacDoiTuongHangHaiHaiVan)
admin.site.register(NhomAuTau)