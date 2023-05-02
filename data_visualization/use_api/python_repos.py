import requests
from plotly.graph_objs import Bar
from plotly import offline
#执行API调用并存储响应
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
headers={'Accept':'application/vnd.github.v3+json'}
r=requests.get(url,headers=headers)
print(f"status code:{r.status_code}")
#将api响应付给一个变量
response_dict=r.json()

#处理结果
# print(response_dict.keys())
# print(response_dict['total_count'])
#搜索有关仓库的信息
repo_dicts=response_dict['items']
repo_names,stars=[],[]
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#可视化
data=[{
    'type':'bar',
    'x':repo_names,
    'y':stars,
    'marker':{
        'color':'rgb(60,100,150)',
        'line':{
            'width':1.5,
            'color':'rgb(25,25,25)',
        }
    },
    'opacity':0.6,
}]
my_layout={
    'title':'Github上最受欢迎的python项目',
    'titlefont':{'size':28},
    'xaxis':{
        'title':'Repository',
        'titlefont':{'size':24},
        'tickfont':{'size':14},
    },
    'yaxis':{
        'title':'Stars',
        'titlefont':{'size':24},
        'tickfont':{'size':14},
    },
}
fig={'data':data,'layout':my_layout}
offline.plot(fig,filename='python_repos.html')
