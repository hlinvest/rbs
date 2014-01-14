from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from rr.r.models import Table, Reservation, Day, TypicalDay, TypicalWeek
import calendar, time


COLUMNS = 10
ROWS = 5

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


def index(request):
	message = 'Please select an option.'
	return render_to_response('index.html', {'message': message})


def admin_typical_day(request):
	tds = TypicalDay.objects.all()
	opens = []
	for timeslot in TIMESLOTS:
		if tds and timeslot[0] == tds[0].opens: opens.append({'sel':1, 'ndx':timeslot[0], 'str':timeslot[1]})
		else: opens.append({'sel':None, 'ndx':timeslot[0], 'str':timeslot[1]})
	closes = []
	for timeslot in TIMESLOTS:
		if tds and timeslot[0] == tds[0].closes: closes.append({'sel':1, 'ndx':timeslot[0], 'str':timeslot[1]})
		else: closes.append({'sel':None, 'ndx':timeslot[0], 'str':timeslot[1]})
	message = 'Select opening and closing times, then click the Submit button.'
	return render_to_response('admin/typical_day.html', {
		'message': message,
		'opens': opens,
		'closes': closes,
	})


def admin_typical_day_result(request):
	tds = TypicalDay.objects.all()
	if tds:
		for td in tds: td.delete()
	opens = request.POST['opens']
	closes = request.POST['closes']
	if opens >= closes:
		message = 'ERROR: Closes must be greater than Opens.'
		return render_to_response('index.html', {
			'message': message,
		})
	td = TypicalDay(
		opens = request.POST['opens'],
		closes = request.POST['closes'],
	)
	td.save()
	message = 'TypicalDay record created.'
	return render_to_response('admin/index.html', {'message': message})


def admin_typical_week(request):
	tws = TypicalWeek.objects.all()
	if tws:
		sun_opens = []
		for timeslot in TIMESLOTS:
			if tws and timeslot[0] == tws[0].sun_opens: sun_opens.append({'sel':1, 'ndx':timeslot[0], 'str':timeslot[1]})
			else: sun_opens.append({'sel':None, 'ndx':timeslot[0], 'str':timeslot[1]})
		sun_closes = []
		for timeslot in TIMESLOTS:
			if tws and timeslot[0] == tws[0].sun_closes: sun_closes.append({'sel':1, 'ndx':timeslot[0], 'str':timeslot[1]})
			else: sun_closes.append({'sel':None, 'ndx':timeslot[0], 'str':timeslot[1]})
		mon_opens = []
		for timeslot in TIMESLOTS:
			if tws and timeslot[0] == tws[0].mon_opens: mon_opens.append({'sel':1, 'ndx':timeslot[0], 'str':timeslot[1]})
			else: mon_opens.append({'sel':None, 'ndx':timeslot[0], 'str':timeslot[1]})
		mon_closes = []
		for timeslot in TIMESLOTS:
			if tws and timeslot[0] == tws[0].mon_closes: mon_closes.append({'sel':1, 'ndx':timeslot[0], 'str':timeslot[1]})
			else: mon_closes.append({'sel':None, 'ndx':timeslot[0], 'str':timeslot[1]})
		tue_opens = []
		for timeslot in TIMESLOTS:
			if tws and timeslot[0] == tws[0].tue_opens: tue_opens.append({'sel':1, 'ndx':timeslot[0], 'str':timeslot[1]})
			else: tue_opens.append({'sel':None, 'ndx':timeslot[0], 'str':timeslot[1]})
		tue_closes = []
		for timeslot in TIMESLOTS:
			if tws and timeslot[0] == tws[0].tue_closes: tue_closes.append({'sel':1, 'ndx':timeslot[0], 'str':timeslot[1]})
			else: tue_closes.append({'sel':None, 'ndx':timeslot[0], 'str':timeslot[1]})
		wed_opens = []
		for timeslot in TIMESLOTS:
			if tws and timeslot[0] == tws[0].wed_opens: wed_opens.append({'sel':1, 'ndx':timeslot[0], 'str':timeslot[1]})
			else: wed_opens.append({'sel':None, 'ndx':timeslot[0], 'str':timeslot[1]})
		wed_closes = []
		for timeslot in TIMESLOTS:
			if tws and timeslot[0] == tws[0].wed_closes: wed_closes.append({'sel':1, 'ndx':timeslot[0], 'str':timeslot[1]})
			else: wed_closes.append({'sel':None, 'ndx':timeslot[0], 'str':timeslot[1]})
		thu_opens = []
		for timeslot in TIMESLOTS:
			if tws and timeslot[0] == tws[0].thu_opens: thu_opens.append({'sel':1, 'ndx':timeslot[0], 'str':timeslot[1]})
			else: thu_opens.append({'sel':None, 'ndx':timeslot[0], 'str':timeslot[1]})
		thu_closes = []
		for timeslot in TIMESLOTS:
			if tws and timeslot[0] == tws[0].thu_closes: thu_closes.append({'sel':1, 'ndx':timeslot[0], 'str':timeslot[1]})
			else: thu_closes.append({'sel':None, 'ndx':timeslot[0], 'str':timeslot[1]})
		fri_opens = []
		for timeslot in TIMESLOTS:
			if tws and timeslot[0] == tws[0].fri_opens: fri_opens.append({'sel':1, 'ndx':timeslot[0], 'str':timeslot[1]})
			else: fri_opens.append({'sel':None, 'ndx':timeslot[0], 'str':timeslot[1]})
		fri_closes = []
		for timeslot in TIMESLOTS:
			if tws and timeslot[0] == tws[0].fri_closes: fri_closes.append({'sel':1, 'ndx':timeslot[0], 'str':timeslot[1]})
			else: fri_closes.append({'sel':None, 'ndx':timeslot[0], 'str':timeslot[1]})
		sat_opens = []
		for timeslot in TIMESLOTS:
			if tws and timeslot[0] == tws[0].sat_opens: sat_opens.append({'sel':1, 'ndx':timeslot[0], 'str':timeslot[1]})
			else: sat_opens.append({'sel':None, 'ndx':timeslot[0], 'str':timeslot[1]})
		sat_closes = []
		for timeslot in TIMESLOTS:
			if tws and timeslot[0] == tws[0].sat_closes: sat_closes.append({'sel':1, 'ndx':timeslot[0], 'str':timeslot[1]})
			else: sat_closes.append({'sel':None, 'ndx':timeslot[0], 'str':timeslot[1]})
		message = 'Select opening and closing times, then click the Submit button.'
		return render_to_response('admin/typical_week.html', {
			'message': message,
			'sun_opens': sun_opens,
			'sun_closes': sun_closes,
			'mon_opens': mon_opens,
			'mon_closes': mon_closes,
			'tue_opens': tue_opens,
			'tue_closes': tue_closes,
			'wed_opens': wed_opens,
			'wed_closes': wed_closes,
			'thu_opens': thu_opens,
			'thu_closes': thu_closes,
			'fri_opens': fri_opens,
			'fri_closes': fri_closes,
			'sat_opens': sat_opens,
			'sat_closes': sat_closes,
		})
	else:
		tds = TypicalDay.objects.all()
		if not tds:
			message = 'ERROR: A typical day record must be entered first.'
			return render_to_response('index.html', {
				'message': message,
			})
		opens = []
		for timeslot in TIMESLOTS:
			if tds and timeslot[0] == tds[0].opens: opens.append({'sel':1, 'ndx':timeslot[0], 'str':timeslot[1]})
			else: opens.append({'sel':None, 'ndx':timeslot[0], 'str':timeslot[1]})
		closes = []
		for timeslot in TIMESLOTS:
			if tds and timeslot[0] == tds[0].closes: closes.append({'sel':1, 'ndx':timeslot[0], 'str':timeslot[1]})
			else: closes.append({'sel':None, 'ndx':timeslot[0], 'str':timeslot[1]})
		message = 'Select opening and closing times, then click the Submit button.'
		return render_to_response('admin/typical_week.html', {
			'message': message,
			'sun_opens': opens,
			'sun_closes': closes,
			'mon_opens': opens,
			'mon_closes': closes,
			'tue_opens': opens,
			'tue_closes': closes,
			'wed_opens': opens,
			'wed_closes': closes,
			'thu_opens': opens,
			'thu_closes': closes,
			'fri_opens': opens,
			'fri_closes': closes,
			'sat_opens': opens,
			'sat_closes': closes,
		})


def admin_typical_week_result(request):
	tws = TypicalWeek.objects.all()
	if tws:
		for tw in tws: tw.delete()
	tw = TypicalWeek(
		sun_opens = request.POST['sun_opens'],
		sun_closes = request.POST['sun_closes'],
		mon_opens = request.POST['mon_opens'],
		mon_closes = request.POST['mon_closes'],
		tue_opens = request.POST['tue_opens'],
		tue_closes = request.POST['tue_closes'],
		wed_opens = request.POST['wed_opens'],
		wed_closes = request.POST['wed_closes'],
		thu_opens = request.POST['thu_opens'],
		thu_closes = request.POST['thu_closes'],
		fri_opens = request.POST['fri_opens'],
		fri_closes = request.POST['fri_closes'],
		sat_opens = request.POST['sat_opens'],
		sat_closes = request.POST['sat_closes'],
	)
	tw.save()
	message = 'TypicalWeek record created.'
	return render_to_response('admin/index.html', {'message': message})


def admin_table_map(request):
	tables = []
	for row in range(ROWS):
		dicts = []
		for column in range(COLUMNS):
			try:
				t = Table.objects.get(
					row__exact = row+1,
					column__exact = column+1,
				)
			except: dicts.append({'row': row+1, 'column': column+1})
			else: dicts.append({'row': row+1, 'column': column+1, 'number': t.number})
		tables.append(dicts)
	message = 'Enter the number of each table in the restaurant, then click the Submit button.'
	return render_to_response('admin/table_map.html', {
		'message': message,
		'tables': tables,
	})


def admin_table_map_result(request):
	ts = Table.objects.all()
	if ts:
		for t in ts: t.delete()
	tables = []
	for row in range(ROWS):
		for column in range(COLUMNS):
			table = '%d %d' % (row+1, column+1)
			try: number = int(request.POST[table])
			except: continue
			entry = table+' '+str(number)
			tables.append(entry)
	for table in tables:
		a = table.split(' ')
		row = int(a[0])
		column = int(a[1])
		number = int(a[2])
		t = Table(
			number = number,
			column = column,
			row = row,
		)
		t.save()
	message = 'Created table records.'
	return render_to_response('index.html', {
		'message': message,
	})


def reservation_day(request):
	ts = Table.objects.all()
	if not ts:
		message = 'ERROR: A table map has not yet been set up.'
		return render_to_response('index.html', {
			'message': message,
		})
	months = [
		'January', 'February', 'March', 'April', 'May', 'June', 
		'July', 'August', 'September', 'October', 'November', 'December',
	]
	calendar.setfirstweekday(calendar.SUNDAY)
	this_year = int(time.strftime('%Y', time.localtime()))
	next_year = this_year
	this_month = int(time.strftime('%m', time.localtime()))
	next_month = this_month + 1
	if next_month == 13:
		next_year = next_year + 1
		next_month = 1
	this_month_cal = calendar.monthcalendar(this_year, this_month)
	next_month_cal = calendar.monthcalendar(next_year, next_month)
	this_month_year = '%s %d' % (months[this_month-1], this_year)
	next_month_year = '%s %d' % (months[next_month-1], next_year)
	message = 'Select the day when you would like to reserve a table.'
	return render_to_response('reservation_day.html', {
		'message': message,
		'this_month_cal': this_month_cal,
		'next_month_cal': next_month_cal,
		'this_month_year': this_month_year,
		'next_month_year': next_month_year,
	})


def reservation_day_result(request):
	months = [
		'January', 'February', 'March', 'April', 'May', 'June', 
		'July', 'August', 'September', 'October', 'November', 'December',
	]
	selection = request.POST['selection']
	a = selection.split(' ')
	year = int(a[1])
	mon = a[0]
	for i in range(len(months)):
		if mon == months[i]:
			month = i + 1
			break
	day = int(a[2])
	try:
		d = Day.objects.get(
			year__exact = year,
			month__exact = month,
			day__exact = day
		)
		opens = d.opens
		closes = d.closes
	except:
		calendar.setfirstweekday(calendar.SUNDAY)
		weekday = calendar.weekday(year, month, day)
		tws = TypicalWeek.objects.all()
		if not tws:
			message = 'ERROR: A typical week record must be entered first.'
			return render_to_response('index.html', {
				'message': message,
			})
		if weekday == 0:
			opens = tws[0].mon_opens
			closes = tws[0].mon_closes
		elif weekday == 1:
			opens = tws[0].tue_opens
			closes = tws[0].tue_closes
		elif weekday == 2:
			opens = tws[0].wed_opens
			closes = tws[0].wed_closes
		elif weekday == 3:
			opens = tws[0].thu_opens
			closes = tws[0].thu_closes
		elif weekday == 4:
			opens = tws[0].fri_opens
			closes = tws[0].fri_closes
		elif weekday == 5:
			opens = tws[0].sat_opens
			closes = tws[0].sat_closes
		elif weekday == 6:
			opens = tws[0].sun_opens
			closes = tws[0].sun_closes
		d = Day(
			year = year,
			month = month,
			day = day,
			weekday = weekday,
			opens = opens,
			closes = closes,
		)
		d.save()
	hours = []
	for hour in range(opens, closes, 2):
		for timeslot in TIMESLOTS:
			if timeslot[0] == hour:
				hour_str = timeslot[1]
				break
		hours.append({'hour': hour, 'hour_str': hour_str})
	if hours == []:
		message = 'We\'re sorry, but we don\'t have any hours available on that day.'
		return render_to_response('index.html', {
			'message': message,
		})
	month_str = months[month-1]
	message = 'Select the hour you would like to reserve.'
	return render_to_response('reservation_hour.html', {
		'message': message,
		'year': year,
		'month': month,
		'day': day,
		'hours': hours,
		'month_str': month_str,
	})


def reservation_hour_result(request):
	months = [
		'January', 'February', 'March', 'April', 'May', 'June', 
		'July', 'August', 'September', 'October', 'November', 'December',
	]
	slot = request.POST['slot']
	a = slot.split(' ')
	year = int(a[0])
	month = int(a[1])
	day = int(a[2])
	hour = int(a[3])
	month_str = months[month-1]
	hour_str = ''
	for timeslot in TIMESLOTS:
		if timeslot[0] == hour:
			hour_str = timeslot[1]
			break
	'''
	rows = []
	for i in range(ROWS): rows.append(i+1)
	columns = []
	for i in range(COLUMNS): columns.append(i+1)
	'''
	tables = [] # table number for [row][column]
	for row in range(ROWS):
		dicts = []
		for column in range(COLUMNS):
			try: t = Table.objects.get(
				column__exact = column+1,
				row__exact = row+1,
			)
			except:
				dicts.append({'number': None})
			else:
				try: r = Reservation.objects.get(
					year__exact = year,
					month__exact = month,
					day__exact = day,
					hour__exact = hour,
					table__exact = t.number,
				)
				except: dicts.append({'number': str(t.number)})
				else: dicts.append({'number': str(t.number), 'checked': True})
		tables.append(dicts)
	if tables == []:
		message = 'We\'re sorry, but we don\'t have any tables available at that time.'
		return render_to_response('index.html', {
			'message': message,
		})
	message = 'Select the table (or tables) you would like to reserve, then click the Submit button.'
	return render_to_response('reservation_table.html', {
		'message': message,
		'year': year,
		'month': month,
		'day': day,
		'hour': hour,
		'tables': tables,
		'month_str': month_str,
		'hour_str': hour_str,
	})


def reservation_table_result(request):
	reservations = ''
	for row in range(ROWS):
		for column in range(COLUMNS):
			table = '%d %d' % (row+1, column+1)
			try: reservation = request.POST[table]
			except: continue
			else:
				t = Table.objects.get(
					row = row+1,
					column = column+1,
				)
				reservations += reservation+'|'
	message = 'Enter your name, email address, and phone number.'
	return render_to_response('reservation_customer.html', {
		'message': message,
		'reservations': reservations,
	})


def reservation_customer_result(request):
	last = request.POST['last']
	first = request.POST['first']
	email = request.POST['email']
	phone = request.POST['phone']
	reservations = request.POST['reservations']
	a1 = reservations.rstrip('|').split('|')
	for reservation in a1:
		a2 = reservation.split(' ')
		year = int(a2[0])
		month = int(a2[1])
		day = int(a2[2])
		hour = int(a2[3])
		table = int(a2[4])
		try:
			r = Reservation.objects.get(
				year__exact = year,
				month__exact = month,
				day__exact = day,
				hour__exact = hour,
				table__exact = table,
			)
		except:
			r = Reservation(
				year = year,
				month = month,
				day = day,
				hour = hour,
				table = table,
				last = last,
				first = first,
				email = email,
				phone = phone,
			)
			r.save()
	message = 'Your reservation has been made.'
	return render_to_response('index.html', {
		'message': message,
	})

