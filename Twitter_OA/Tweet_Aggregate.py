import collections
class Solution(object):
	def aggregate(self, time_interval, lines):
		d = collections.defaultdict(dict)
		for line in lines:
			date, category, num = line.strip().split(", ")
			year, month, day = date.split('-')
			y_m = year + "-" + month
			if category in d[y_m]:
				d[y_m][category] += int(num)
			else:
				d[y_m][category] = int(num)
		time_series = self.get_time_series(time_interval)
		print time_series
		for time in time_series:
			if time in d:
				s = time
				for c in sorted(d[time]):
					pair = c + ", " + str(d[time][c])
					s += ", " + pair
				print s

	def get_time_series(self, time_interval):
		s, e = time_interval.split(',')
		res = []
		s_y, s_m = s.split("-")
		e_y, e_m = e.split("-")
		s_y, s_m, e_y, e_m = int(s_y), int(s_m), int(e_y), int(e_m)
		while not(s_y == e_y and s_m == e_m):
			str_s_m = str(s_m) if s_m >= 10 else "0" + str(s_m)
			str_s_y = str(s_y)
			new_date = str_s_y + "-" + str_s_m
			res.append(new_date)
			if s_m + 1 <= 12:
				s_m += 1
			else:
				s_m = 1
				s_y += 1
		res.append(e)
		return res[::-1]

test = Solution()
time_interval = "2015-08,2016-04"
lines = ["2015-08-15, clicks, 635", "2016-03-24, app_installs, 683", "2015-04-05, favorites, 763", "2015-12-26, clicks, 525", "2016-06-03, re_tweets, 101", "2015-12-02, app_installs, 982", "2016-09-17, app_installs, 770"]
print time_interval
print lines
test.aggregate(time_interval, lines)
