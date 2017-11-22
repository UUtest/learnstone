# -*- coding: utf-8 -*-
import re

re_telephone = re.compile(r'^[a-z]+\.?[a-z]+\@[a-z\.]+\.com$')

def is_valid_email(addr):
    return re_telephone.match(addr)

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')