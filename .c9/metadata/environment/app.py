{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":14,"position":14,"stack":[[{"start":{"row":241,"column":21},"end":{"row":241,"column":22},"action":"remove","lines":["s"],"id":2}],[{"start":{"row":241,"column":21},"end":{"row":241,"column":22},"action":"remove","lines":["e"],"id":3},{"start":{"row":241,"column":20},"end":{"row":241,"column":21},"action":"remove","lines":["l"]},{"start":{"row":241,"column":19},"end":{"row":241,"column":20},"action":"remove","lines":["a"]},{"start":{"row":241,"column":18},"end":{"row":241,"column":19},"action":"remove","lines":["F"]}],[{"start":{"row":241,"column":18},"end":{"row":241,"column":19},"action":"insert","lines":["T"],"id":4},{"start":{"row":241,"column":19},"end":{"row":241,"column":20},"action":"insert","lines":["r"]},{"start":{"row":241,"column":20},"end":{"row":241,"column":21},"action":"insert","lines":["i"]},{"start":{"row":241,"column":21},"end":{"row":241,"column":22},"action":"insert","lines":["e"]}],[{"start":{"row":241,"column":21},"end":{"row":241,"column":22},"action":"remove","lines":["e"],"id":5},{"start":{"row":241,"column":20},"end":{"row":241,"column":21},"action":"remove","lines":["i"]}],[{"start":{"row":241,"column":20},"end":{"row":241,"column":21},"action":"insert","lines":["u"],"id":6},{"start":{"row":241,"column":21},"end":{"row":241,"column":22},"action":"insert","lines":["e"]}],[{"start":{"row":241,"column":21},"end":{"row":241,"column":22},"action":"remove","lines":["e"],"id":7},{"start":{"row":241,"column":20},"end":{"row":241,"column":21},"action":"remove","lines":["u"]},{"start":{"row":241,"column":19},"end":{"row":241,"column":20},"action":"remove","lines":["r"]},{"start":{"row":241,"column":18},"end":{"row":241,"column":19},"action":"remove","lines":["T"]}],[{"start":{"row":241,"column":18},"end":{"row":241,"column":19},"action":"insert","lines":["F"],"id":8},{"start":{"row":241,"column":19},"end":{"row":241,"column":20},"action":"insert","lines":["a"]},{"start":{"row":241,"column":20},"end":{"row":241,"column":21},"action":"insert","lines":["l"]},{"start":{"row":241,"column":21},"end":{"row":241,"column":22},"action":"insert","lines":["s"]},{"start":{"row":241,"column":22},"end":{"row":241,"column":23},"action":"insert","lines":["e"]}],[{"start":{"row":36,"column":8},"end":{"row":37,"column":9},"action":"remove","lines":["return render_template('login.html')","    else:"],"id":9},{"start":{"row":36,"column":4},"end":{"row":36,"column":8},"action":"remove","lines":["    "]},{"start":{"row":36,"column":0},"end":{"row":36,"column":4},"action":"remove","lines":["    "]},{"start":{"row":35,"column":32},"end":{"row":36,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":239,"column":22},"end":{"row":239,"column":23},"action":"remove","lines":["e"],"id":10},{"start":{"row":239,"column":21},"end":{"row":239,"column":22},"action":"remove","lines":["s"]},{"start":{"row":239,"column":20},"end":{"row":239,"column":21},"action":"remove","lines":["l"]},{"start":{"row":239,"column":19},"end":{"row":239,"column":20},"action":"remove","lines":["a"]},{"start":{"row":239,"column":18},"end":{"row":239,"column":19},"action":"remove","lines":["F"]}],[{"start":{"row":239,"column":18},"end":{"row":239,"column":19},"action":"insert","lines":["T"],"id":11},{"start":{"row":239,"column":19},"end":{"row":239,"column":20},"action":"insert","lines":["r"]},{"start":{"row":239,"column":20},"end":{"row":239,"column":21},"action":"insert","lines":["u"]},{"start":{"row":239,"column":21},"end":{"row":239,"column":22},"action":"insert","lines":["e"]}],[{"start":{"row":239,"column":21},"end":{"row":239,"column":22},"action":"remove","lines":["e"],"id":12},{"start":{"row":239,"column":20},"end":{"row":239,"column":21},"action":"remove","lines":["u"]},{"start":{"row":239,"column":19},"end":{"row":239,"column":20},"action":"remove","lines":["r"]},{"start":{"row":239,"column":18},"end":{"row":239,"column":19},"action":"remove","lines":["T"]}],[{"start":{"row":239,"column":18},"end":{"row":239,"column":19},"action":"insert","lines":["F"],"id":13},{"start":{"row":239,"column":19},"end":{"row":239,"column":20},"action":"insert","lines":["a"]},{"start":{"row":239,"column":20},"end":{"row":239,"column":21},"action":"insert","lines":[";"]},{"start":{"row":239,"column":21},"end":{"row":239,"column":22},"action":"insert","lines":["s"]}],[{"start":{"row":239,"column":21},"end":{"row":239,"column":22},"action":"remove","lines":["s"],"id":14},{"start":{"row":239,"column":20},"end":{"row":239,"column":21},"action":"remove","lines":[";"]}],[{"start":{"row":239,"column":20},"end":{"row":239,"column":21},"action":"insert","lines":["l"],"id":15},{"start":{"row":239,"column":21},"end":{"row":239,"column":22},"action":"insert","lines":["s"]},{"start":{"row":239,"column":22},"end":{"row":239,"column":23},"action":"insert","lines":["e"]}],[{"start":{"row":32,"column":0},"end":{"row":47,"column":57},"action":"remove","lines":["#LOGIN FUNCTION   ","@app.route('/login', methods=['POST', 'GET'])","def login():","    if request.method == 'GET': ","        user = mongo.db.user","        login_user = user.find_one({","        'email': request.form.get('email'), ","        'password':request.form.get('password'","        )})","        ","        if login_user:","            session['email'] = login_user['email']","            session['name'] = login_user['name']","            return redirect(url_for('user'))","       ","        return 'Invalid username or password combination'"],"id":17},{"start":{"row":32,"column":0},"end":{"row":48,"column":57},"action":"insert","lines":["@app.route('/login', methods=['POST', 'GET'])","def login():","    if request.method == 'GET': ","        return render_template('login.html')","    else:","        user = mongo.db.user","        login_user = user.find_one({","        'email': request.form.get('email'), ","        'password':request.form.get('password'","        )})","        ","        if login_user:","            session['email'] = login_user['email']","            session['name'] = login_user['name']","            return redirect(url_for('user'))","       ","        return 'Invalid username or password combination'"]}]]},"ace":{"folds":[],"scrolltop":312,"scrollleft":0,"selection":{"start":{"row":48,"column":57},"end":{"row":48,"column":57},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":32,"state":"start","mode":"ace/mode/python"}},"timestamp":1569371420333,"hash":"8a203ebdd7f966695b6ebd1109a818428984e918"}