from django.conf.urls import url

from .work import WorkView
from .routers import HybridRouter

api_router = HybridRouter()

api_router.add_api_view(
    'work',
    url(r'^work/$', WorkView.as_view(), name='work')
)
