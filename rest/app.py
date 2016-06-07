#!flask/bin/python
from flask import Flask, jsonify, request, abort, make_response

app = Flask(__name__)
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False,
        'data':'foo'
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
    
]

@app.route('/')
def index():
    return "Hello, varshu!"

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id']== task_id]
    if len(task)== 0:
        abort(404)
    return jsonify({'task':task[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'not found'}), 404)

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        return make_response(jsonify({'error':'no json data'}), 400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description',""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/todo/api/v1.0/tasks/<int:task_id>',methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id']== task_id]
    if len(task)==0:
        abort(404)
    if not request.json:
        abort(404)
    if 'title' in request.json and type(request.json['title'])!= str:
        abort(404)
    if 'description' in request.json and type(request.json['description']) is not str:
         return make_response(jsonify({'error':'description bad'}), 400)
    if 'done' in request.json and type(request.json['done']) is not bool:
         return make_response(jsonify({'error':'done value is bad'}), 404)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/tasks/<int:task_id>',methods=['DELETE'])
def delete_task(task_id):
    task=[task for task in tasks if task['id']==task_id]
    if len(task)==0:
        abort(400)
    tasks.remove(task[0])
    return jsonify({'result':True})

if __name__ == '__main__':
    app.run(debug=True,port=int("8080"),host='0.0.0.0')
