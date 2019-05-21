from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from . import views

router = routers.DefaultRouter()
router.register('User', views.UserViewSet)
router.register('Group', views.GroupViewSet)
router.register('Post', views.PostViewSet)
router.register('Profile', views.ProfileViewSet)
router.register('Verify', views.VerifyViewSet)
router.register('Payment', views.PaymentViewSet)
router.register('Transition', views.TransitionViewSet)
router.register('CashInOrOut', views.CashInOrOutViewSet)
router.register('Cycle', views.CycleViewSet)
router.register('Pickcycle', views.PickcycleViewSet)
router.register('Dropcycle', views.DropcycleViewSet)
router.register('Location', views.LocationViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]