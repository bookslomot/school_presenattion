from rest_framework import serializers

from presentation.models import Presentation
from user.models import User


class UserSerializerOnPresentation(serializers.ModelSerializer):

    """ User serializer on Presentation """

    class Meta:
        model = User
        fields = ('id', 'name', 'last_name',)


class PresentationSerializerList(serializers.ModelSerializer):

    owner = UserSerializerOnPresentation(read_only=True)

    class Meta:
        model = Presentation
        fields = ('id', 'title', 'presentation',  'description', 'owner',)


class PresentationSerializerDetail(serializers.ModelSerializer):

    owner = UserSerializerOnPresentation(read_only=True)

    class Meta:
        model = Presentation
        fields = ('title', 'presentation',  'description', 'owner',)
