# -*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
#输出18:
#L1 = ['Hello', 'World', 18, 'Apple', None]
#L2 = [s.lower() if isinstance(s, str) else s for s in L1]
