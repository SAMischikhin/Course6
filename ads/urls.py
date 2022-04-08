from django.conf.urls import url
from django.urls import include, path

from rest_framework.routers import SimpleRouter

from ads.views import AdViewSet, MyAdViewList, CommentViewSet
ad_router = SimpleRouter()
comment_router = SimpleRouter()

comment_router.register("comments", CommentViewSet)
ad_router.register("ads", AdViewSet, basename="ads")


urlpatterns = [
    path("ads/me/", MyAdViewList.as_view()),
    path("ads/<int:ad_id>/", include(comment_router.urls)),
]

urlpatterns += ad_router.urls
urlpatterns += comment_router.urls
