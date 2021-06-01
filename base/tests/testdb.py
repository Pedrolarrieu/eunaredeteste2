import pytest

pytestmark = pytest.mark.django_db

@pytest.mark.django_db
class TestUsers:
    pytestmark = pytest.mark.django_db
    def test_my_user(self):
        me = TestUsers.objects.get(username='me')
        assert me.is_superuser