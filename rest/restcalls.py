import requests,json

url = 'http://localhost:8080/todo/api/v1.0/tasks'
    

task= {'title': 'varshu1'}
'''response = requests.post(url,json=task)
print(response.text)'''

def get_task(task_id):
    url1=url+'/'+str(task_id)
    response = requests.get(url1)
    print(response.text)

def create_task(task):
    response=requests.post(url,json=task)
    print(response.text)
    
def update_task(task_id):
    url1=url+'/'+str(task_id)
    task1={'title':'foo', 'done': True}
    response=requests.put(url1,json=task1)
    print(response.text)
    
create_task(task)
#get_task(2)
update_task(3)
#get_task(2)
