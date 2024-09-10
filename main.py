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
def update_data(Dataa):
    check = next((newdata for newdata in Data[id]==Dataa.id),None)
    if check!=None:
        Data.append(Dataa)
        return flask.jsonify(Data)
    return None

@app.route("/books",methods=["delete"])
def delete_data(data_id):
    data_to_delete= ([data for data in Data if Data[id]==data_id],None)
    if data_to_delete!=None:
        Data.remove(data_to_delete)
app.run(debug=True,port=2248)
