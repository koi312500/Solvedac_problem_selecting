import requests

url = "https://solved.ac/api/v3/search/problem"
headers = {"Accept": "application/json"}

problem_list = []

last_problem_id = 1000
while True:
    print(f"Debug - {last_problem_id + 1}")
    querystring = {"query":f"*b2..g %ko #math s#125.. id:{last_problem_id + 1}..", "sort":"id", "page":"1"}
    response = requests.get(url, headers=headers, params=querystring)
    if int(response.json()['count']) == 0:
        break
    try:
        for i in range(0, 100):
            problem_list.append(str(response.json()['items'][i]['problemId']))
            last_problem_id = int(response.json()['items'][i]['problemId'])

    except:
        pass

print(problem_list)
