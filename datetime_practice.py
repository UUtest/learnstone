# -*- coding:utf-8 -*-
import re
from datetime import datetime, timezone, timedelta

re_pick_up =  re.compile(r'^UTC([\+\-]+[0-9]+)\:0{2}')

def to_timestamp(dt_str, tz_str):
    Hours=re_pick_up.match(tz_str).group(1)
    dt_str1=datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    dt = dt_str1.replace(tzinfo=timezone(timedelta(hours=int(Hours))))
    dt1 =dt.astimezone(timezone.utc)
    return dt1.timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')