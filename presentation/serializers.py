from rest_framework import serializers

from presentation.models import Presentation
from user.models import User


class UserSerializerOnPresentation(serializers.ModelSerializer):

    """ User serializer on Presentation """

    class Meta:
        model = User
        fields = ('name', 'last_name',)


class PresentationSerializer(serializers.ModelSerializer):

    owner = UserSerializerOnPresentation(read_only=True)

    class Meta:
        model = Presentation
        fields = ('title', 'presentation',  'description', 'owner',)
