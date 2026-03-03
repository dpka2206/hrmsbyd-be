from accounts.models import User
from accounts.storages.user_storage_interface import UserStorageInterface


class UserStorage(UserStorageInterface):
    def get_user_by_id(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
