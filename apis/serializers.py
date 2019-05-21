from rest_framework import serializers
from cycles.models import Cycle, Pickcycle, Dropcycle, Location
from payments.models import Payment, Transition, CashInOrOut
from django.contrib.auth.models import User, Group
from users.models import Profile, Verify
from posts.models import Post


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('url', 'id', 'title', 'author', 'date', 'body', 'image')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('url', 'id', 'user', 'full_name', 'date_of_birth', 'profile_picture', 'phone_number',  'address', 'is_email_verified')


class VerifySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Verify
        fields = ('url', 'id', 'user', 'nid', 'nid_front', 'nid_back', 'nid_selfie', 'utility', 'is_verified', 'is_verify_submit')


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = ('url', 'id', 'owner', 'balance', 'earned', 'due')


class TransitionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transition
        fields = ('url', 'id', 'sender', 'receiver', 'amount', 'date')


class CashInOrOutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CashInOrOut
        fields = ('url', 'id', 'client', 'cash_in', 'cash_out', 'date')


class CycleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cycle
        fields = ('url', 'id', 'owner', 'name', 'model', 'image', 'rent', 'is_picked', 'rating', 'picked_times', 'pick_id')


class PickcycleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pickcycle
        fields = ('url', 'id', 'cycle_id', 'picked_by', 'pick_date')


class DropcycleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dropcycle
        fields = ('url', 'id', 'pick_id', 'drop_date')


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('url', 'id', 'area', 'near_by', 'near_by_t', 'gps_lat', 'gps_lon', 'cycle_id')
