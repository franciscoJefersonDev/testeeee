import os
from datetime import date, datetime

gitAccessToken = ''
time = datetime.now().strftime("%H:%M")
date = date.today()
commit = '{time}-{date}'.format(time=time, date=date)

# print(commit)
# with open('/home/francisco/Área de Trabalho/git-access-token.txt') as f:
#     gitAccessToken = f.readlines()[0]
#     print(gitAccessToken)

os.system('git add .')
os.system('git commit -m {commit}'.format(commit=commit))
os.system('git push')
