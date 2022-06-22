from django.contrib import admin
from .models import (
    DiemGocDoDacQuocGia,
    DiemDoDacQuocGia,
    TramDinhViVeTinhQuocGia
)


# Register
admin.site.register(DiemGocDoDacQuocGia)
admin.site.register(DiemDoDacQuocGia)
admin.site.register(TramDinhViVeTinhQuocGia)