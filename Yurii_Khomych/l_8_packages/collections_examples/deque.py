from collections import deque
q = deque()

q.append('eat')
q.append('sleep')
q.append('code')

q
# deque(['eat', 'sleep', 'code'])

q.pop()
# 'code'
q.pop()
# 'sleep'
q.pop()
# 'eat'

q.pop()
