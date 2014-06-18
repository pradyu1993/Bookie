
import mock
import pickle
import transaction

from bookie.tests import factory
from bookie.tests import TestViewBase
from bookie.lib.social_utils import (
    create_twitter_userapi,
    create_twitter_OAuthHandler)


class TestSocialOAuth(TestViewBase):

    def test_search_content(self):
        """Test if correct urls are rendered if OAuthHandler
        is edited"""
        create_twitter_OAuthHandler = mock.Mock(
            return_value="https://twitter_url/")
        self._login_admin()
        res = self.app.get('/oauth/twitter_connect')
        self.assertTrue(
            "https://twitter_url/" in res.body,
            msg="OAuth should render url returned by\
             OAuthHandler when no params")

    def test_credentials_duplicate(self):
        """Test if oauth duplicate credentials are allowed """
        message = """Another user (Admin) has already connected\
             with those Twitter credentials."""
        factory.make_twitter_connection()
        transaction.commit()
        twitter_user = pickle.load(
            open("bookie/tests/test_lib/save.p", "rb"))
        create_twitter_userapi = mock.Mock(return_value=twitter_user)
        self._login_admin()
        res = self.app.get('/oauth/twitter_connect',
                           status=200)
        self.assertTrue(
            message in res.body,
            "when same credentials are used backend should show message")
