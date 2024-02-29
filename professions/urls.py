from rest_framework import routers

from professions.views import ProfessionViewSet

router = routers.DefaultRouter()

router.register("", ProfessionViewSet)

urlpatterns = router.urls

app_name = "professions"
