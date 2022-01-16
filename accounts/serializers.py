from django.db.models import Q # for queries
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import users , Comment
from django.core.exceptions import ValidationError
from uuid import uuid4
from rest_framework.serializers import SerializerMethodField


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=users.objects.all())]
        )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=users.objects.all())]
        )
    password = serializers.CharField(max_length=8)

    phonenumber = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=users.objects.all())]
    )

    class Meta:
        model = users
        fields = (
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'phonenumber',
            
        )


class UserLoginSerializer(serializers.ModelSerializer):
    # to accept either username or email
    user_id = serializers.CharField()
    password = serializers.CharField()
    token = serializers.CharField(required=False, read_only=True)

    def validate(self, data):
        # user,email,password validator
        user_id = data.get("user_id", None)
        password = data.get("password", None)
        if not user_id and not password:
            raise ValidationError("Details not entered.")
        user = None
        # if the email has been passed
        if '@' in user_id:
            user = users.objects.filter(
                Q(email=user_id) &
                Q(password=password)
                ).distinct()
            if not user.exists():
                raise ValidationError("User credentials are not correct.")
            user = users.objects.get(email=user_id)
        else:
            user = users.objects.filter(
                Q(username=user_id) &
                Q(password=password)
            ).distinct()
            if not user.exists():
                raise ValidationError("User credentials are not correct.")
            user = users.objects.get(username=user_id)
        if user.ifLogged:
            raise ValidationError("User already logged in.")
        user.ifLogged = True
        data['token'] = uuid4()
        user.token = data['token']
        user.save()
        return data

    class Meta:
        model = users
        fields = (
            'user_id',
            'password',
            'token',
        )

        read_only_fields = (
            'token',
        )


class UserLogoutSerializer(serializers.ModelSerializer):
    token = serializers.CharField()
    status = serializers.CharField(required=False, read_only=True)

    def validate(self, data):
        token = data.get("token", None)
        print(token)
        user = None
        try:
            user = users.objects.get(token=token)
            if not user.ifLogged:
                raise ValidationError("User is not logged in.")
        except Exception as e:
            raise ValidationError(str(e))
        user.ifLogged = False
        user.token = ""
        user.save()
        data['status'] = "User is logged out."
        return data

    class Meta:
        model = users
        fields = (
            'token',
            'status',
        )


class CommentSerializer(serializers.ModelSerializer):
    reply_count = SerializerMethodField()
    author = SerializerMethodField()
    class Meta:
        model = Comment
        fields = ('content', 'parent', 'author', 'reply_count', 'product')

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0

    def get_author(self, obj):
        return obj.author.username




# UserModel = get_user_model()


# class UserSerializer(serializers.ModelSerializer):

#     password = serializers.CharField(write_only=True)

#     def create(self, validated_data):

#         user = UserModel.objects.create_user(
#             username=validated_data['username'],
#             password=validated_data['password'],
#         )
#         return user

#     class Meta:
#         model = UserModel
#         # Tuple of serialized model fields (see link [2])
#         fields = ( "id", "username", "password", )



# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.CustomUser
#         fields = ('email', 'username', )

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         password = validated_data.pop('password')
#         user = User(**validated_data)
#         user.set_password(password)
#         user.save()
#         return user
        
