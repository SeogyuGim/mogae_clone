from django.urls import include, path
from .views import MoimListView

urlpatterns = [
    path('api/moim/', MoimListView.as_view(), name='moim'),
    # url(r'^moim/$', MoimListView.as_view(), name='moim'),
]