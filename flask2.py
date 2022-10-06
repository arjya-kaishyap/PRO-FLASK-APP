from asyncio import tasks
from flask import Flask,jsonify,request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'buy groceries',
        'description':u'milk,cheese,pizza,fruit,tylenol',
        'done': False
    },
    {
        'id':2,
        'title': u'learn python',
        'description': u'need to find a good python tutorial on the web',
        'done': False
    }
]

@app.route("/add-data",methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "messge":"Please Provide the Data!"
        },400)
    task = {
        'id':tasks[-1]['id']+1,
        'Name':request.json['Name'],
        'Contact':request.json.get('Contact'," "),
        'done':False
    }    
    tasks.append(task)
    return jsonify({
        'status':"Success",
        'message': 'Task Added Successfully'
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        'data': tasks
    })

if(__name__ == "__main__"):
    app.run(debug = True)