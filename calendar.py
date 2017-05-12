import uuid
from src.common.database import database
from src.common.utils import Utils

class Calendar(object):
	"""Create a class calendar:
	Attributes: create_calendar
			  :  read_calendar
	    return: new calendar details
			  : read_calendar events"""

	def __init__(self, date, user_id,id_db):
		"""Initialize the inputs"""
		self.date = date
		self.user_id = user_id
		self.id_db = id_db
		self.name = name


	def create_calendar(self):
		"""return calendar name and date for new calendar"""
		date = self.date
		cal_name = self.name
		event_name = event_name
		return date, cal_name, event_name


	def read_calendar(self):
		"""Return Event name, venue, Time """
		#import from class Event, method fetch
		#return event name, venue and time
		
		event = Event()
		event.fetch()
		#print the if



		