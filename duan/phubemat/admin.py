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


# Register
admin.site.register(CayDocLap)
admin.site.register(RanhGioiPhuBeMat)
admin.site.register(BeMatCongTrinh)
admin.site.register(BeMatKhuDanCu)
admin.site.register(DatTrong)
admin.site.register(NuocMat)
admin.site.register(ThucVatDayBien)