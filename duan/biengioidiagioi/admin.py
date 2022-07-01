from django.contrib.gis import admin
from .models import (
    VungBien,
    DiaPhanHanhChinhTrenBien,
    DuongRanhGioiHanhChinhTrenBien
)
from nendialy.admin import CustomGeoAdmin


# Register
admin.site.register(VungBien, CustomGeoAdmin)
admin.site.register(DiaPhanHanhChinhTrenBien, CustomGeoAdmin)
admin.site.register(DuongRanhGioiHanhChinhTrenBien, CustomGeoAdmin)