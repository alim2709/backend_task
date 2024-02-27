from rest_framework import routers

from topics.views import TopicViewSet

router = routers.DefaultRouter()

router.register("", TopicViewSet)

urlpatterns = router.urls

app_name = "topics"
