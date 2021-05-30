from rest_framework import routers
from .api import LeadViewSet

# DRF default router
router = routers.DefaultRouter()

# Registering the view to be used in the route
router.register('api/leads', LeadViewSet, 'leads')

# Assigning the urls to urlpatterns
urlpatterns = router.urls
