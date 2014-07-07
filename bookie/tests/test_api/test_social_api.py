
import json
import transaction
from mock import patch

from bookie.tests import factory
from bookie.tests import TestViewBase


class TestSocialConnectionsApi(TestViewBase):
    """Check if SocialConnections API returns all the added accounts"""

    def testBaseApi(self):
        factory.make_twitter_connection()
        transaction.commit()

        params = {
            'api_key': self.api_key
        }
        res = self.app.get('/api/v1/admin/social_connections',
                           params=params,
                           status=200)
        connections = json.loads(res.body)
        self.assertEqual('admin',
                         connections['social_connections'][0]['username'],
                         'Username should be admin')
        params = {
            'api_key': self.api_key
        }

    def testSocialAuthentication(self):
        """Test to check that user login is required to do this api call"""

        res = self.app.get('/api/v1/admin/social_connections',
                           status=403)
        self.assertEqual(
            res.status, "403 Forbidden",
            "status should be 403")

    @patch('bookie.bcelery.tasks.refresh_twitter_fetch')
    def testTwitterRefresh(self, mock_refresh):

        """Test if refresh_twitter_fetch is called if admin tries to refresh 
        using api """

        factory.make_twitter_connection()
        transaction.commit()

        params = {
            'api_key': self.api_key
        }
        self.app.get("/api/v1/a/social/twitter_refresh/admin",
                     params=params,
                     status=200)

        self.assertTrue(mock_refresh.called)
