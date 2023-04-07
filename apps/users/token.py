from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.users.models import User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Add other user model fields to jwt payload, in this case, 'role'
    """

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["role"] = User.UserType.labels[user.role]

        return token
