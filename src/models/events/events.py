import uuid
from src.common.database import Database
from src.common.utils import Utils


class Events(object):
    """Creates class event"""
    def __init__(self, event_date, calender_id, event_name, event_venue, _id=None):
        """
        Initialize class event.
        :param _id:
        :param event_date:
        :param calender_id:
        :param event_name:
        :param event_venue:
        """
        self._id = uuid.uuid4().hex if None else _id
        self.event_date = event_date
        self.calendar_id = calender_id
        self.event_name = event_name
        self.event_venue = event_venue

    def save_to_db(self):
        """Adds event to database
        """
        Database.insert('events', self.json())






