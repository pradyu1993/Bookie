
import tweepy

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import UnicodeText

from bookie.models import Base


class TwitterConnection(Base):
    """ Table to store User Twitter information"""
    __tablename__ = "TwitterConnection"

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    # User Twitter Data
    twitter_uid = Column(UnicodeText())
    twitter_access_key = Column(UnicodeText())
    twitter_access_secret = Column(UnicodeText())
    twitter_username = Column(UnicodeText())
    twitter_refresh_date = Column(DateTime)

    def twitter_api(self):
        twitter_consumer_key = settings.TWITTER_CONSUMER_KEY
        twitter_consumer_secret = settings.TWITTER_CONSUMER_SECRET
        auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
        auth.set_access_token(self.twitter_access_key, self.twitter_access_secret)
        api = tweepy.API(auth)
        return api

    def sync_twitter_data(self):
		# function to sync all the data from twitter
    	return