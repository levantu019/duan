from django.contrib import admin
from .models import (
    DiemGocDoDacQuocGia,
    DiemDoDacQuocGia,
    TramDinhViVeTinhQuocGia
)
from nendialy.admin import CustomGeoAdmin

# Register
admin.site.register(DiemGocDoDacQuocGia, CustomGeoAdmin)
admin.site.register(DiemDoDacQuocGia, CustomGeoAdmin)
admin.site.register(TramDinhViVeTinhQuocGia, CustomGeoAdmin)