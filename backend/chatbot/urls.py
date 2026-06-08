from django.urls import path
from .views import chat

urlpatterns = [
    path("chat/", chat),
]
from .views import chat, dashboard_stats

urlpatterns = [

    path("chat/", chat),

    path("dashboard/", dashboard_stats)

]