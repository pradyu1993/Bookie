
import transaction

from bookie.models.social import SocialMgr
from bookie.tests import factory
from bookie.tests import TestDBBase


class TestSocialMgr(TestDBBase):

	def testConnectionsReturn(self):
		factory.make_twitter_connection()
		factory.make_twitter_connection(username='bookie')
		transaction.commit()

		connections = SocialMgr.get_twitter_connections()
		self.assertEqual(2, len(connections))

		connection = SocialMgr.get_twitter_connections('bookie')
		self.assertEqual(1, len(connection))

	def testTweetIdUpdate(self):
		factory.make_twitter_connection()
		transaction.commit()

		connection = SocialMgr.get_twitter_connections('admin')
		SocialMgr.update_lasttweet_data(connection, '123456')

		new_connection = SocialMgr.get_twitter_connections('admin')
		self.assertEqual(new_connection.last_tweet_id, '123456')
