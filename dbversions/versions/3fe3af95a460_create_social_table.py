"""create TwitterConnection table

Revision ID: 3fe3af95a460
Revises: 44dccb7b8b82
Create Date: 2014-05-25 22:36:38.361799

"""

# revision identifiers, used by Alembic.
revision = '3fe3af95a460'
down_revision = '44dccb7b8b82'

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.create_table('TwitterConnection',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('twitter_uid', sa.UnicodeText(), nullable=True),
        sa.Column('twitter_access_key', sa.UnicodeText(), nullable=True),
        sa.Column('twitter_access_secret', sa.UnicodeText, nullable=True),
        sa.Column('twitter_username', sa.UnicodeText, nullable=True),
        sa.Column('twitter_refresh_date', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade():
    op.drop_table('TwitterConnection')

