from django.contrib import admin
from .models import (
    BienDao,
    Dao,
    BaiBoi,
    BaiDaDuoiNuoc,
    NguonNuoc,
    DiemDoCaoMucNuoc,
    DuongBoNuoc,
    DuongMepNuoc,
    RanhGioiNuocMatQuyUoc,
    BoKeBoCap,
    KenhMuong,
    TramThuThapKTTV,
    ThamSoKTTV,
    SongGioDongChay,
    ThamSoNuoc
)


# Register
admin.site.register(BienDao)
admin.site.register(Dao)
admin.site.register(BaiBoi)
admin.site.register(BaiDaDuoiNuoc)
admin.site.register(NguonNuoc)
admin.site.register(DiemDoCaoMucNuoc)
admin.site.register(DuongBoNuoc)
admin.site.register(DuongMepNuoc)
admin.site.register(RanhGioiNuocMatQuyUoc)
admin.site.register(BoKeBoCap)
admin.site.register(KenhMuong)
admin.site.register(TramThuThapKTTV)
admin.site.register(ThamSoKTTV)
admin.site.register(SongGioDongChay)
admin.site.register(ThamSoNuoc)
