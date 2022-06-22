from django.contrib import admin
from .models import (
    VungBien,
    DiaPhanHanhChinhTrenBien,
    DuongRanhGioiHanhChinhTrenBien
)


# Register
admin.site.register(VungBien)
admin.site.register(DiaPhanHanhChinhTrenBien)
admin.site.register(DuongRanhGioiHanhChinhTrenBien)