import requests
import random
import selenium
import acmicpc_request

url = "https://solved.ac/api/v3/search/problem"
headers = {"Accept": "application/json"}

used_problem = []
problem_list_real = [[], [], [], [], []]
problem_list = [[], [], [], [], []]
query_list = ["#math", "#dp", "#dp", "#greedy", "#backtracking"]

for j in range(0, 5):
    last_problem_id = 1000
    while True:
        print(f"Debug - {last_problem_id + 1}")
        querystring = {"query":f"*b2..g %ko {query_list[j]} s#125.. id:{last_problem_id + 1}..", "sort":"id", "page":"1"}
        response = requests.get(url, headers=headers, params=querystring)
        #print(response.json()['count'])
        if int(response.json()['count']) == 0:
            break
        try:
            for i in range(0, 100):
                problem_list[j].append(str(response.json()['items'][i]['problemId']))
                last_problem_id = int(response.json()['items'][i]['problemId'])

        except:
            pass

    random.shuffle(problem_list[j])

for i in range(0, 5):
    j = 0
    k = 99
    while len(problem_list_real[i]) <= k:
        if not problem_list[i][j] in used_problem:
            problem_list_real[i].append(problem_list[i][j])
            used_problem.append(problem_list[i][j]) 
        j = j + 1