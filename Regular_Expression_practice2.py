# -*- coding: utf-8 -*-
import re

re_pick_up = re.compile(r'^\<?([a-zA-Z\s]+)?\>?\s?([a-zA-Z\.]*)@[a-z]+\.[a-zA-Z]{3}$')#这里不太明白为何第二个分组改成([a-zA-Z\.]+)+就不行了

def name_of_email(addr):
    return re_pick_up.match(addr).group(1)

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
assert name_of_email('bill.gates@microsoft.com')
assert name_of_email('bill.gates@microsoft.com')
print('ok')