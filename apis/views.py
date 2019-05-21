from rest_framework import viewsets, permissions
from cycles.models import Cycle, Pickcycle, Dropcycle, Location
from payments.models import Payment, Transition, CashInOrOut
from django.contrib.auth.models import User, Group
from users.models import Profile, Verify
from posts.models import Post
from .serializers import UserSerializer, GroupSerializer, PostSerializer, ProfileSerializer, VerifySerializer, PaymentSerializer, TransitionSerializer, CashInOrOutSerializer, CycleSerializer, PickcycleSerializer, DropcycleSerializer, LocationSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class VerifyViewSet(viewsets.ModelViewSet):
    queryset = Verify.objects.all()
    serializer_class = VerifySerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class TransitionViewSet(viewsets.ModelViewSet):
    queryset = Transition.objects.all()
    serializer_class = TransitionSerializer


class CashInOrOutViewSet(viewsets.ModelViewSet):
    queryset = CashInOrOut.objects.all()
    serializer_class = CashInOrOutSerializer


class CycleViewSet(viewsets.ModelViewSet):
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer


class PickcycleViewSet(viewsets.ModelViewSet):
    queryset = Pickcycle.objects.all()
    serializer_class = PickcycleSerializer


class DropcycleViewSet(viewsets.ModelViewSet):
    queryset = Dropcycle.objects.all()
    serializer_class = DropcycleSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
