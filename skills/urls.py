from rest_framework import routers

from skills.views import SkillViewSet

router = routers.DefaultRouter()

router.register("", SkillViewSet)

urlpatterns = router.urls

app_name = "skills"
