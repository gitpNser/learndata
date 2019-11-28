import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
	t = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
	tz_zone = int(re.match(r'UTC([\+\-\d]+)\:(\d+)', tz_str).group(1))
	tz_zone = timezone(timedelta(hours=tz_zone))
	# print(tz_zone)
	t = t.replace(tzinfo=tz_zone)
	return t.timestamp()

#test
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')