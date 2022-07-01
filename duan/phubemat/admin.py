from django.contrib import admin
from .models import (
    CayDocLap,
    RanhGioiPhuBeMat,
    BeMatCongTrinh,
    BeMatKhuDanCu,
    DatTrong,
    NuocMat,
    ThucVatDayBien
)
from nendialy.admin import CustomGeoAdmin


# Register
admin.site.register(CayDocLap, CustomGeoAdmin)
admin.site.register(RanhGioiPhuBeMat, CustomGeoAdmin)
admin.site.register(BeMatCongTrinh, CustomGeoAdmin)
admin.site.register(BeMatKhuDanCu, CustomGeoAdmin)
admin.site.register(DatTrong, CustomGeoAdmin)
admin.site.register(NuocMat, CustomGeoAdmin)
admin.site.register(ThucVatDayBien, CustomGeoAdmin)