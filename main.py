import flask
app = flask.Flask("me")

Data = [
    {"id": 1, "data": "aaa"},
    {"id": 2, "data": "bbb"}
]

@app.route("/books", methods=['GET'])
def get_all_datas():
    return flask.jsonify(Data)

@app.route("/books",methods=["post"])
def add_datas(datatxt):
    NewData=flask.request.json
    NewData["id"]=len(Data)+1
    NewData["data"]=datatxt
    Data.append(NewData)
    return flask.jsonify(NewData+" added"),200

@app.route("/books",methods=["put"])
def update_data(Data):
    check = next((newdata for newdata in Data[id]==Data.id),None)
    if check!=None:

app.run(debug=True,port=2248)