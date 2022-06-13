from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings


def upload_avator_path(instance, filename):
    ext = filename.split('.')[-1]
    return '/'.join(['avatars', str(instance.userProfile.id)+str(instance.nickName)+str(".")+str(ext)])


class UserManager(BaseUserManager):
    # ユーザーの作成
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('email is must')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    # スーパーユーザーの作成
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


class Profile(models.Model):
    nickName = models.CharField(max_length=20)
    userProfile = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name="userProfile",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(blank=True, null=True,
                            upload_to=upload_avator_path)

    def __str__(self):
        return self.nickName


class Target(models.Model):
    main = models.CharField(max_length=100)
    sub1 = models.CharField(blank=True, null=True, max_length=100)
    sub2 = models.CharField(blank=True, null=True, max_length=100)
    sub3 = models.CharField(blank=True, null=True, max_length=100)
    sub4 = models.CharField(blank=True, null=True, max_length=100)
    sub6 = models.CharField(blank=True, null=True, max_length=100)
    sub7 = models.CharField(blank=True, null=True, max_length=100)
    sub8 = models.CharField(blank=True, null=True, max_length=100)
    sub9 = models.CharField(blank=True, null=True, max_length=100)
    userTarget = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='userTarget',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='liked',
        blank=True
    )

    todo1_1 = models.CharField(blank=True, null=True, max_length=50)
    todo1_2 = models.CharField(blank=True, null=True, max_length=50)
    todo1_3 = models.CharField(blank=True, null=True, max_length=50)
    todo1_4 = models.CharField(blank=True, null=True, max_length=50)
    todo1_6 = models.CharField(blank=True, null=True, max_length=50)
    todo1_7 = models.CharField(blank=True, null=True, max_length=50)
    todo1_8 = models.CharField(blank=True, null=True, max_length=50)
    todo1_9 = models.CharField(blank=True, null=True, max_length=50)

    todo2_1 = models.CharField(blank=True, null=True, max_length=50)
    todo2_2 = models.CharField(blank=True, null=True, max_length=50)
    todo2_3 = models.CharField(blank=True, null=True, max_length=50)
    todo2_4 = models.CharField(blank=True, null=True, max_length=50)
    todo2_6 = models.CharField(blank=True, null=True, max_length=50)
    todo2_7 = models.CharField(blank=True, null=True, max_length=50)
    todo2_8 = models.CharField(blank=True, null=True, max_length=50)
    todo2_9 = models.CharField(blank=True, null=True, max_length=50)

    todo3_1 = models.CharField(blank=True, null=True, max_length=50)
    todo3_2 = models.CharField(blank=True, null=True, max_length=50)
    todo3_3 = models.CharField(blank=True, null=True, max_length=50)
    todo3_4 = models.CharField(blank=True, null=True, max_length=50)
    todo3_6 = models.CharField(blank=True, null=True, max_length=50)
    todo3_7 = models.CharField(blank=True, null=True, max_length=50)
    todo3_8 = models.CharField(blank=True, null=True, max_length=50)
    todo3_9 = models.CharField(blank=True, null=True, max_length=50)

    todo4_1 = models.CharField(blank=True, null=True, max_length=50)
    todo4_2 = models.CharField(blank=True, null=True, max_length=50)
    todo4_3 = models.CharField(blank=True, null=True, max_length=50)
    todo4_4 = models.CharField(blank=True, null=True, max_length=50)
    todo4_6 = models.CharField(blank=True, null=True, max_length=50)
    todo4_7 = models.CharField(blank=True, null=True, max_length=50)
    todo4_8 = models.CharField(blank=True, null=True, max_length=50)
    todo4_9 = models.CharField(blank=True, null=True, max_length=50)

    todo6_1 = models.CharField(blank=True, null=True, max_length=50)
    todo6_2 = models.CharField(blank=True, null=True, max_length=50)
    todo6_3 = models.CharField(blank=True, null=True, max_length=50)
    todo6_4 = models.CharField(blank=True, null=True, max_length=50)
    todo6_6 = models.CharField(blank=True, null=True, max_length=50)
    todo6_7 = models.CharField(blank=True, null=True, max_length=50)
    todo6_8 = models.CharField(blank=True, null=True, max_length=50)
    todo6_9 = models.CharField(blank=True, null=True, max_length=50)

    todo7_1 = models.CharField(blank=True, null=True, max_length=50)
    todo7_2 = models.CharField(blank=True, null=True, max_length=50)
    todo7_3 = models.CharField(blank=True, null=True, max_length=50)
    todo7_4 = models.CharField(blank=True, null=True, max_length=50)
    todo7_6 = models.CharField(blank=True, null=True, max_length=50)
    todo7_7 = models.CharField(blank=True, null=True, max_length=50)
    todo7_8 = models.CharField(blank=True, null=True, max_length=50)
    todo7_9 = models.CharField(blank=True, null=True, max_length=50)

    todo8_1 = models.CharField(blank=True, null=True, max_length=50)
    todo8_2 = models.CharField(blank=True, null=True, max_length=50)
    todo8_3 = models.CharField(blank=True, null=True, max_length=50)
    todo8_4 = models.CharField(blank=True, null=True, max_length=50)
    todo8_6 = models.CharField(blank=True, null=True, max_length=50)
    todo8_7 = models.CharField(blank=True, null=True, max_length=50)
    todo8_8 = models.CharField(blank=True, null=True, max_length=50)
    todo8_9 = models.CharField(blank=True, null=True, max_length=50)

    todo9_1 = models.CharField(blank=True, null=True, max_length=50)
    todo9_2 = models.CharField(blank=True, null=True, max_length=50)
    todo9_3 = models.CharField(blank=True, null=True, max_length=50)
    todo9_4 = models.CharField(blank=True, null=True, max_length=50)
    todo9_6 = models.CharField(blank=True, null=True, max_length=50)
    todo9_7 = models.CharField(blank=True, null=True, max_length=50)
    todo9_8 = models.CharField(blank=True, null=True, max_length=50)
    todo9_9 = models.CharField(blank=True, null=True, max_length=50)

    def __str__(self):
        return self.main


class Comment(models.Model):
    text = models.CharField(max_length=20)
    userComment = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="userComment",
        on_delete=models.CASCADE
    )
    target = models.ForeignKey(Target, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
