from django.db import models


TIMESLOTS = (
	(1, '12:00 am'),
	(2, '12:30 am'),
	(3, '01:00 am'),
	(4, '01:30 am'),
	(5, '02:00 am'),
	(6, '02:30 am'),
	(7, '03:00 am'),
	(8, '03:30 am'),
	(9, '04:00 am'),
	(10, '04:30 am'),
	(11, '05:00 am'),
	(12, '05:30 am'),
	(13, '06:00 am'),
	(14, '06:30 am'),
	(15, '07:00 am'),
	(16, '07:30 am'),
	(17, '08:00 am'),
	(18, '08:30 am'),
	(19, '09:00 am'),
	(20, '09:30 am'),
	(21, '10:00 am'),
	(22, '10:30 am'),
	(23, '11:00 am'),
	(24, '11:30 am'),
	(25, '12:00 pm'),
	(26, '12:30 pm'),
	(27, '01:00 pm'),
	(28, '01:30 pm'),
	(29, '02:00 pm'),
	(30, '02:30 pm'),
	(31, '03:00 pm'),
	(32, '03:30 pm'),
	(33, '04:00 pm'),
	(34, '04:30 pm'),
	(35, '05:00 pm'),
	(36, '05:30 pm'),
	(37, '06:00 pm'),
	(38, '06:30 pm'),
	(39, '07:00 pm'),
	(40, '07:30 pm'),
	(41, '08:00 pm'),
	(42, '08:30 pm'),
	(43, '09:00 pm'),
	(44, '09:30 pm'),
	(45, '10:00 pm'),
	(46, '10:30 pm'),
	(47, '11:00 pm'),
	(48, '11:30 pm'),
)


class Table(models.Model):
	number = models.IntegerField()
	column = models.IntegerField()
	row = models.IntegerField()


class Reservation(models.Model):
	year = models.IntegerField()
	month = models.IntegerField()
	day = models.IntegerField()
	hour = models.IntegerField()
	table = models.IntegerField()
	last = models.CharField(max_length=20)
	first = models.CharField(max_length=20)
	email = models.EmailField()
	phone = models.IntegerField()
'''
	def __str__(self):
		return str(self.year)+'-'+str(self.month)+'-'+str(self.day)+'-'+str(self.hour)+'-'+str(self.table)

	class Admin:
		pass
'''

class Day(models.Model):
	year = models.IntegerField()
	month = models.IntegerField()
	day = models.IntegerField()
	weekday = models.IntegerField() # 0 = monday
	opens = models.IntegerField(choices=TIMESLOTS) # hh:mm am (or pm)
	closes = models.IntegerField(choices=TIMESLOTS)
'''
	def __str__(self):
		return str(self.year)+'-'+str(self.month)+'-'+str(day)

	class Admin:
		pass
'''

class TypicalDay(models.Model):
	opens = models.IntegerField(choices=TIMESLOTS)
	closes = models.IntegerField(choices=TIMESLOTS)
'''
	def __str__(self):
		return str(self.opens)+'-'+str(self.closes)

	class Admin:
		pass
'''

class TypicalWeek(models.Model):
	sun_opens = models.IntegerField(choices=TIMESLOTS)
	sun_closes = models.IntegerField(choices=TIMESLOTS)
	mon_opens = models.IntegerField(choices=TIMESLOTS)
	mon_closes = models.IntegerField(choices=TIMESLOTS)
	tue_opens = models.IntegerField(choices=TIMESLOTS)
	tue_closes = models.IntegerField(choices=TIMESLOTS)
	wed_opens = models.IntegerField(choices=TIMESLOTS)
	wed_closes = models.IntegerField(choices=TIMESLOTS)
	thu_opens = models.IntegerField(choices=TIMESLOTS)
	thu_closes = models.IntegerField(choices=TIMESLOTS)
	fri_opens = models.IntegerField(choices=TIMESLOTS)
	fri_closes = models.IntegerField(choices=TIMESLOTS)
	sat_opens = models.IntegerField(choices=TIMESLOTS)
	sat_closes = models.IntegerField(choices=TIMESLOTS)
'''
	class Admin:
		pass
'''

