#!/usr/bin/env python3
import os.path
import uuid
import random
from flask import Flask, request, render_template, \
    json, jsonify, redirect, url_for
app = Flask(__name__)

@app.route('/question', methods=['GET', 'POST', 'PUT', 'DELETE'])
def question():
    data = request.get_json(silent=True)
    print("------------------------ question ------------------------")
    print(data)
    print("------------------------ question ------------------------")
    question = "Test1 question"
    answers = ["resp1", "resp2", "resp3", "resp4"]
    nq = 1 
    name = uuid.uuid4()# data.name
    score = 0# data.score
    level = 1# data.level
    #if ("nq" in data) {
        #nq = data.nq 
        #name = data.name
        #score = data.score
        #level = data.level
    #}
    # if os.path.exists('app/data/test1.json'):
    with open('app/data/test1.json') as jsonfile:
        json_struct=json.load(jsonfile)
        len_t0t = len(json_struct["level"][1]["topics"])
        len_t0q = len(json_struct["level"][1]["topics"][0]['questions'])
        len_t1q = len(json_struct["level"][1]["topics"][1]['questions'])
        c1 = int(len_t0t * random.random())
        len_t1qx = len(json_struct["level"][1]["topics"][c1]['questions'])
        c2 = int(len_t1qx * random.random())
        question = json_struct["level"][1]["topics"][c1]['questions'][c2]["q"]
        answers = json_struct["level"][1]["topics"][c1]['questions'][c2]["o"]
        ca = json_struct["level"][1]["topics"][c1]['questions'][c2]["ca"]

        print(int(len_t0t * random.random()))
        print(int(len_t1qx * random.random()))
        print(int(len_t0q * random.random()))
        print(int(len_t1q * random.random()))
        # print json_struct["level"][0]["topics"][0]['questions'].len()
        # print dbjson.level[0].topics[1].questions.len()
	# nq is number question
    return render_template('question.html', name=name, nq = nq, score=score, level=level, question=question, answers=answers, ca = ca)
    # return "question..."

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def index():
    data = request.get_json(silent=True)
    css = ""
    js = ""
    fn = "base"
    name = "Guest"
    if data is not None:
        for k, v in data.items():
            if k == "fn":
                fn = data.get("fn")
    print("------------------------ index ------------------------")
    print(data)
    print("------------------------ index ------------------------")
    if fn == "base":
        data = {"fn":fn, "cache_id":uuid.uuid4(), "nq":0, "name": name,"score":0,"level":1,"leveltotal":3}
    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

# curl -H "Content-Type: application/json" -d '{"fn":"auth","name":"Fesus"}' 0:5000
# curl -H "Content-Type: application/json" -d '{"fn":"question","name":"Fesus"}' 0:5000
