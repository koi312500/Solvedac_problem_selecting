import requests
import random
import selenium
import acmicpc_request

url = "https://solved.ac/api/v3/search/problem"
headers = {"Accept": "application/json"}

used_problem = []
problem_list_real = []
problem_list = []
query_list = []
tag_cnt = 0

while True:
    a = str(input("Input solvedac's tag(Enter `end` to finsh) : "))
    if a == "end":
        break
    problem_list_real.append([])
    problem_list.append([])
    query_list.append(f"#{a}")
    tag_cnt = tag_cnt + 1

for j in range(0, tag_cnt):
    last_problem_id = 1000
    while True:
        querystring = {"query":f"*b2..g %ko {query_list[j]} s#125.. id:{last_problem_id + 1}..", "sort":"id", "page":"1"}
        response = requests.get(url, headers=headers, params=querystring)
        if int(response.json()['count']) == 0:
            break
        try:
            for i in range(0, 100):
                problem_list[j].append(str(response.json()['items'][i]['problemId']))
                last_problem_id = int(response.json()['items'][i]['problemId'])

        except:
            pass

    random.shuffle(problem_list[j])
    print(f"Tag : {query_list[j]}({j+1}/{tag_cnt}) Finshed.")

for i in range(0, tag_cnt):
    j = 0
    while len(problem_list_real[i]) <= 99:
        if not problem_list[i][j] in used_problem:
            problem_list_real[i].append(problem_list[i][j])
            used_problem.append(problem_list[i][j]) 
        j = j + 1

crawler = acmicpc_request.BOJBot("https://www.acmicpc.net/")
crawler.login()
for i in range(0, tag_cnt):
    crawler.self_add_problem(problem_list_real[i])