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
from nendialy.admin import CustomGeoAdmin


# Register
admin.site.register(BienDao, CustomGeoAdmin)
admin.site.register(Dao, CustomGeoAdmin)
admin.site.register(BaiBoi, CustomGeoAdmin)
admin.site.register(BaiDaDuoiNuoc, CustomGeoAdmin)
admin.site.register(NguonNuoc, CustomGeoAdmin)
admin.site.register(DiemDoCaoMucNuoc, CustomGeoAdmin)
admin.site.register(DuongBoNuoc, CustomGeoAdmin)
admin.site.register(DuongMepNuoc, CustomGeoAdmin)
admin.site.register(RanhGioiNuocMatQuyUoc, CustomGeoAdmin)
admin.site.register(BoKeBoCap, CustomGeoAdmin)
admin.site.register(KenhMuong, CustomGeoAdmin)
admin.site.register(TramThuThapKTTV, CustomGeoAdmin)
admin.site.register(ThamSoKTTV, CustomGeoAdmin)
admin.site.register(SongGioDongChay, CustomGeoAdmin)
admin.site.register(ThamSoNuoc, CustomGeoAdmin)
