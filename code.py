import subprocess
import json

def today():
    from datetime import date
    return str(date.today())

def created():
    secret_key = "rathinrsk:db104947e684ff4149f8bed89230ef726987496f"
    base_url = 'https://api.github.com/repos/flutter/flutter'
    output = subprocess.Popen(["curl",secret_key, base_url],shell=True, stdout=subprocess.PIPE)
    jsonS,_ = output.communicate()
    data = json.loads(jsonS)
    created_date = data['created_at'].split('T')[0]
    return created_date


def find(page_number):
    secret_key = "rathinrsk:db104947e684ff4149f8bed89230ef726987496f"
    base_url = 'https://api.github.com/repos/flutter/flutter/commits?page=' + str(page_number) + '&since=' + start_date + '&until=' + end_date
    output = subprocess.Popen(["curl",secret_key, base_url],shell=True, stdout=subprocess.PIPE)
    jsonS,_ = output.communicate()
    data = json.loads(jsonS)
    for i in data:
        try:
            geeks.append([i['commit']['author']['name'],i['commit']['author']['date']])
        except:
            flag = True
            return

start_date = input('Enter start date inMM-DD-YYYY format')
end_date = input('Enter end date inMM-DD-YYYY format')
url = 'https://github.com/flutter/flutter'
if start_date=='':
    start_date = created()
if end_date=='':
    end_date = today()

geeks = []
flag = False
i = 1
while not flag:
    find(i)
    i+=1
    if i>=4:
        break

d = {}

for i in geeks:
    if i[0] not in d:
        d[i[0]] = [1,i[0],i[1]]
    else:
        d[i[0]][0] += 1



max_commits = 0
name = ''
date = ''
for i in d:
    if d[i][0] > max_commits:
        max_commits = d[i][0]
        name = d[i][1]
        date = d[i][2]

print(name,max_commits,date)

