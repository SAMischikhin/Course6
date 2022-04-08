from rest_framework import pagination, viewsets

from ads.models import Ad, Comment
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer
from ads.permissions import IsAdmin, IsOwner
from rest_framework.generics import ListAPIView

from rest_framework.permissions import AllowAny


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = pagination.PageNumberPagination

    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user.pk)

    def get_permissions(self):
        if self.action in ['retrieve', 'update', 'partial_update', 'destroy', 'create']:
            self.permission_classes = [IsAdmin | IsOwner]
        elif self.action in ['list']:
            self.permission_classes = [AllowAny, ]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action in ['list', 'destroy']:
            return AdSerializer
        elif self.action in ['retrieve', 'partial_update', 'update', 'create']:
            return AdDetailSerializer


class MyAdViewList(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = pagination.PageNumberPagination

    def get_queryset(self):
        self.queryset = self.queryset.filter(author_id=self.request.user.pk)
        return self.queryset


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user.pk,
                        ad_id=self.kwargs.get("ad_id"))

    def get_permissions(self):
        if self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdmin | IsOwner]
        elif self.action in ['list']:
            self.permission_classes = [AllowAny, ]
        return super().get_permissions()
