from django.shortcuts import render

from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import (
    CayDocLap,
    RanhGioiPhuBeMat,
    BeMatCongTrinh,
    BeMatKhuDanCu,
    DatTrong,
    NuocMat,
    ThucVatDayBien
)
from .serializers import (
    CDLSerializer,
    RGPBMSerializer,
    BMCTSerializer,
    BMKDCSerializer,
    DTSerializer,
    NMSerializer,
    TVDBSerializer
)


# 1. Cây độc lập
class CDLViewSet(viewsets.ModelViewSet):
    queryset = CayDocLap.objects.all()
    serializer_class = CDLSerializer

    @action(method=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = CayDocLap.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 2. Ranh giới phủ bề mặt
class CDLViewSet(viewsets.ModelViewSet):
    queryset = RanhGioiPhuBeMat.objects.all()
    serializer_class = RGPBMSerializer

    @action(method=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = RanhGioiPhuBeMat.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(method=['get'], detail=False, url_path='loairgpbm')
    def choices_loaiRanhGioiPhuBeMat(self, request):
        try:
            choices = RanhGioiPhuBeMat.loaiRanhGioiPhuBeMat.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 3. Bề mặt công trình
class CDLViewSet(viewsets.ModelViewSet):
    queryset = BeMatCongTrinh.objects.all()
    serializer_class = BMCTSerializer

    @action(method=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = BeMatCongTrinh.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 4. Bề mặt khu dân cư
class CDLViewSet(viewsets.ModelViewSet):
    queryset = BeMatKhuDanCu.objects.all()
    serializer_class = BMKDCSerializer

    @action(method=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = BeMatKhuDanCu.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(method=['get'], detail=False, url_path='thucvat')
    def choices_thucVat(self, request):
        try:
            choices = BeMatKhuDanCu.thucVat.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 5. Đất trống
class CDLViewSet(viewsets.ModelViewSet):
    queryset = DatTrong.objects.all()
    serializer_class = DTSerializer

    @action(method=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = DatTrong.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 6. Nước mặt 
class CDLViewSet(viewsets.ModelViewSet):
    queryset = NuocMat.objects.all()
    serializer_class = NMSerializer

    @action(method=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = NuocMat.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 7. Thực vật đáy biển
class CDLViewSet(viewsets.ModelViewSet):
    queryset = ThucVatDayBien.objects.all()
    serializer_class = TVDBSerializer

    @action(method=['get'], detail=False, url_path='madoituong')
    def choices_maDoiTuong(self, request):
        try:
            choices = ThucVatDayBien.maDoiTuong.field.choices
            return Response(data=choices, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)