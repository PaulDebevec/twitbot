# app/models/botpost_model.py

from app import db
from datetime import datetime

class BotPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.JSON, nullable=False)
    posted = db.Column(db.Boolean, default=False)
    date_posted = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now(), nullable=False)

    def __init__(self, body, posted=False):
        self.body = body
        self.posted = posted

    @staticmethod
    def create(botpost_data):
        """
        Create a single BotPost.

        :param botpost_data: A dictionary representing BotPost data.
        """
        new_botpost = BotPost(
            body=botpost_data['body'],
            posted=botpost_data.get('posted', False),
            date_posted=botpost_data.get('date_posted', None),
        )

        db.session.add(new_botpost)
        db.session.commit()

    @staticmethod
    def bulk_create(botposts_data):
        """
        Bulk create BotPosts from a list of dictionaries.

        :param botposts_data: A list of dictionaries representing BotPost data.
        """
        botpost_objects = [
            BotPost(
                body=botpost_data['body'],
                posted=botpost_data.get('posted', False),
                date_posted=botpost_data.get('date_posted', None),
            )
            for botpost_data in botposts_data
        ]

        db.session.bulk_save_objects(botpost_objects)
        db.session.commit()
