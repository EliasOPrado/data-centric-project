{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":100,"column":4},"end":{"row":100,"column":8},"action":"remove","lines":["    "],"id":23478}],[{"start":{"row":101,"column":4},"end":{"row":101,"column":8},"action":"remove","lines":["    "],"id":23479}],[{"start":{"row":97,"column":0},"end":{"row":97,"column":4},"action":"insert","lines":["    "],"id":23480},{"start":{"row":98,"column":0},"end":{"row":98,"column":4},"action":"insert","lines":["    "]},{"start":{"row":99,"column":0},"end":{"row":99,"column":4},"action":"insert","lines":["    "]},{"start":{"row":100,"column":0},"end":{"row":100,"column":4},"action":"insert","lines":["    "]},{"start":{"row":101,"column":0},"end":{"row":101,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":81,"column":16},"end":{"row":81,"column":31},"action":"insert","lines":["page=1, limit=8"],"id":23481}],[{"start":{"row":81,"column":33},"end":{"row":82,"column":0},"action":"insert","lines":["",""],"id":23482},{"start":{"row":82,"column":0},"end":{"row":82,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":82,"column":4},"end":{"row":87,"column":118},"action":"insert","lines":[" limit = int(limit)","    page = int(page)","    #print(page, limit)","    skip = page * limit - limit","    maximum = math.ceil( (mongo.db.products.count_documents({})) / limit)","    product_pagination = list(mongo.db.products.find().sort(\"$natural\", pymongo.DESCENDING).skip(skip).limit( limit ))"],"id":23483}],[{"start":{"row":90,"column":27},"end":{"row":90,"column":28},"action":"insert","lines":[","],"id":23484}],[{"start":{"row":90,"column":28},"end":{"row":91,"column":0},"action":"insert","lines":["",""],"id":23485},{"start":{"row":91,"column":0},"end":{"row":91,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":90,"column":28},"end":{"row":91,"column":0},"action":"insert","lines":["",""],"id":23487},{"start":{"row":91,"column":0},"end":{"row":91,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":91,"column":4},"end":{"row":94,"column":36},"action":"insert","lines":[" product_pagination=product_pagination,","        page=page,","        pages=range(1, maximum + 1),","        maximum=maximum, limit=limit"],"id":23488}],[{"start":{"row":91,"column":4},"end":{"row":91,"column":5},"action":"remove","lines":[" "],"id":23489}],[{"start":{"row":90,"column":0},"end":{"row":90,"column":4},"action":"insert","lines":["    "],"id":23490},{"start":{"row":91,"column":0},"end":{"row":91,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":107,"column":27},"end":{"row":108,"column":0},"action":"insert","lines":["",""],"id":23491},{"start":{"row":108,"column":0},"end":{"row":108,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":89,"column":27},"end":{"row":90,"column":0},"action":"insert","lines":["",""],"id":23492},{"start":{"row":90,"column":0},"end":{"row":90,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":80,"column":24},"end":{"row":80,"column":25},"action":"remove","lines":["s"],"id":23493}],[{"start":{"row":82,"column":4},"end":{"row":82,"column":5},"action":"remove","lines":[" "],"id":23494}],[{"start":{"row":129,"column":27},"end":{"row":129,"column":28},"action":"insert","lines":[" "],"id":23495}],[{"start":{"row":129,"column":26},"end":{"row":129,"column":27},"action":"insert","lines":[" "],"id":23496}],[{"start":{"row":106,"column":53},"end":{"row":106,"column":62},"action":"insert","lines":["homeGarde"],"id":23497}],[{"start":{"row":106,"column":62},"end":{"row":106,"column":63},"action":"insert","lines":["n"],"id":23498}],[{"start":{"row":124,"column":53},"end":{"row":124,"column":54},"action":"insert","lines":["m"],"id":23499},{"start":{"row":124,"column":54},"end":{"row":124,"column":55},"action":"insert","lines":["o"]},{"start":{"row":124,"column":55},"end":{"row":124,"column":56},"action":"insert","lines":["t"]},{"start":{"row":124,"column":56},"end":{"row":124,"column":57},"action":"insert","lines":["o"]},{"start":{"row":124,"column":57},"end":{"row":124,"column":58},"action":"insert","lines":["r"]},{"start":{"row":124,"column":58},"end":{"row":124,"column":59},"action":"insert","lines":["s"]}],[{"start":{"row":87,"column":53},"end":{"row":87,"column":64},"action":"insert","lines":["electronics"],"id":23500}],[{"start":{"row":128,"column":21},"end":{"row":128,"column":22},"action":"insert","lines":[","],"id":23501}],[{"start":{"row":144,"column":0},"end":{"row":144,"column":2},"action":"insert","lines":["# "],"id":23502},{"start":{"row":145,"column":0},"end":{"row":145,"column":2},"action":"insert","lines":["# "]},{"start":{"row":146,"column":0},"end":{"row":146,"column":2},"action":"insert","lines":["# "]},{"start":{"row":147,"column":0},"end":{"row":147,"column":2},"action":"insert","lines":["# "]},{"start":{"row":148,"column":0},"end":{"row":148,"column":2},"action":"insert","lines":["# "]},{"start":{"row":149,"column":0},"end":{"row":149,"column":2},"action":"insert","lines":["# "]},{"start":{"row":152,"column":0},"end":{"row":152,"column":2},"action":"insert","lines":["# "]},{"start":{"row":154,"column":0},"end":{"row":154,"column":2},"action":"insert","lines":["# "]},{"start":{"row":155,"column":0},"end":{"row":155,"column":2},"action":"insert","lines":["# "]},{"start":{"row":156,"column":0},"end":{"row":156,"column":2},"action":"insert","lines":["# "]},{"start":{"row":157,"column":0},"end":{"row":157,"column":2},"action":"insert","lines":["# "]},{"start":{"row":159,"column":0},"end":{"row":159,"column":2},"action":"insert","lines":["# "]},{"start":{"row":160,"column":0},"end":{"row":160,"column":2},"action":"insert","lines":["# "]},{"start":{"row":161,"column":0},"end":{"row":161,"column":2},"action":"insert","lines":["# "]},{"start":{"row":162,"column":0},"end":{"row":162,"column":2},"action":"insert","lines":["# "]},{"start":{"row":163,"column":0},"end":{"row":163,"column":2},"action":"insert","lines":["# "]},{"start":{"row":164,"column":0},"end":{"row":164,"column":2},"action":"insert","lines":["# "]},{"start":{"row":165,"column":0},"end":{"row":165,"column":2},"action":"insert","lines":["# "]},{"start":{"row":166,"column":0},"end":{"row":166,"column":2},"action":"insert","lines":["# "]},{"start":{"row":167,"column":0},"end":{"row":167,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":82,"column":4},"end":{"row":83,"column":20},"action":"remove","lines":["limit = int(limit)","    page = int(page)"],"id":23505}],[{"start":{"row":79,"column":22},"end":{"row":80,"column":0},"action":"insert","lines":["",""],"id":23506},{"start":{"row":80,"column":0},"end":{"row":80,"column":1},"action":"insert","lines":["@"]}],[{"start":{"row":80,"column":1},"end":{"row":80,"column":2},"action":"insert","lines":["a"],"id":23507},{"start":{"row":80,"column":2},"end":{"row":80,"column":3},"action":"insert","lines":["p"]},{"start":{"row":80,"column":3},"end":{"row":80,"column":4},"action":"insert","lines":["p"]},{"start":{"row":80,"column":4},"end":{"row":80,"column":5},"action":"insert","lines":["."]},{"start":{"row":80,"column":5},"end":{"row":80,"column":6},"action":"insert","lines":["r"]},{"start":{"row":80,"column":6},"end":{"row":80,"column":7},"action":"insert","lines":["p"]}],[{"start":{"row":80,"column":6},"end":{"row":80,"column":7},"action":"remove","lines":["p"],"id":23508}],[{"start":{"row":80,"column":6},"end":{"row":80,"column":7},"action":"insert","lines":["o"],"id":23509},{"start":{"row":80,"column":7},"end":{"row":80,"column":8},"action":"insert","lines":["u"]},{"start":{"row":80,"column":8},"end":{"row":80,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":80,"column":9},"end":{"row":80,"column":10},"action":"insert","lines":["e"],"id":23510}],[{"start":{"row":80,"column":10},"end":{"row":80,"column":12},"action":"insert","lines":["()"],"id":23511}],[{"start":{"row":80,"column":11},"end":{"row":80,"column":13},"action":"insert","lines":["''"],"id":23512}],[{"start":{"row":80,"column":12},"end":{"row":80,"column":13},"action":"insert","lines":["/"],"id":23513},{"start":{"row":80,"column":13},"end":{"row":80,"column":14},"action":"insert","lines":["e"]},{"start":{"row":80,"column":14},"end":{"row":80,"column":15},"action":"insert","lines":["l"]},{"start":{"row":80,"column":15},"end":{"row":80,"column":16},"action":"insert","lines":["e"]},{"start":{"row":80,"column":16},"end":{"row":80,"column":17},"action":"insert","lines":["e"]}],[{"start":{"row":80,"column":16},"end":{"row":80,"column":17},"action":"remove","lines":["e"],"id":23514}],[{"start":{"row":80,"column":13},"end":{"row":80,"column":16},"action":"remove","lines":["ele"],"id":23515},{"start":{"row":80,"column":13},"end":{"row":80,"column":24},"action":"insert","lines":["electronics"]}],[{"start":{"row":80,"column":24},"end":{"row":80,"column":25},"action":"insert","lines":["/"],"id":23516}],[{"start":{"row":87,"column":53},"end":{"row":87,"column":64},"action":"remove","lines":["electronics"],"id":23517}],[{"start":{"row":80,"column":26},"end":{"row":80,"column":51},"action":"insert","lines":[", methods=['GET', 'POST']"],"id":23518}],[{"start":{"row":81,"column":40},"end":{"row":81,"column":65},"action":"insert","lines":[", methods=['GET', 'POST']"],"id":23519}],[{"start":{"row":98,"column":26},"end":{"row":99,"column":0},"action":"insert","lines":["",""],"id":23520}],[{"start":{"row":99,"column":0},"end":{"row":99,"column":26},"action":"insert","lines":["@app.route('/home_gardens/"],"id":23521}],[{"start":{"row":99,"column":26},"end":{"row":99,"column":27},"action":"insert","lines":["'"],"id":23522},{"start":{"row":99,"column":27},"end":{"row":99,"column":28},"action":"insert","lines":[")"]}],[{"start":{"row":117,"column":18},"end":{"row":118,"column":0},"action":"insert","lines":["",""],"id":23523}],[{"start":{"row":118,"column":0},"end":{"row":118,"column":20},"action":"insert","lines":["@app.route('/motors/"],"id":23524}],[{"start":{"row":118,"column":20},"end":{"row":118,"column":21},"action":"insert","lines":["'"],"id":23525},{"start":{"row":118,"column":21},"end":{"row":118,"column":22},"action":"insert","lines":[")"]}],[{"start":{"row":99,"column":27},"end":{"row":99,"column":52},"action":"insert","lines":[", methods=['GET', 'POST']"],"id":23526}],[{"start":{"row":100,"column":41},"end":{"row":100,"column":66},"action":"insert","lines":[", methods=['GET', 'POST']"],"id":23527}],[{"start":{"row":83,"column":4},"end":{"row":83,"column":5},"action":"insert","lines":["p"],"id":23528},{"start":{"row":83,"column":5},"end":{"row":83,"column":6},"action":"insert","lines":["a"]},{"start":{"row":83,"column":6},"end":{"row":83,"column":7},"action":"insert","lines":["g"]},{"start":{"row":83,"column":7},"end":{"row":83,"column":8},"action":"insert","lines":["e"]},{"start":{"row":83,"column":8},"end":{"row":83,"column":9},"action":"insert","lines":["="]},{"start":{"row":83,"column":9},"end":{"row":83,"column":10},"action":"insert","lines":["1"]}],[{"start":{"row":83,"column":10},"end":{"row":84,"column":0},"action":"insert","lines":["",""],"id":23529},{"start":{"row":84,"column":0},"end":{"row":84,"column":4},"action":"insert","lines":["    "]},{"start":{"row":84,"column":4},"end":{"row":84,"column":5},"action":"insert","lines":["l"]},{"start":{"row":84,"column":5},"end":{"row":84,"column":6},"action":"insert","lines":["i"]},{"start":{"row":84,"column":6},"end":{"row":84,"column":7},"action":"insert","lines":["m"]},{"start":{"row":84,"column":7},"end":{"row":84,"column":8},"action":"insert","lines":["i"]},{"start":{"row":84,"column":8},"end":{"row":84,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":84,"column":9},"end":{"row":84,"column":10},"action":"insert","lines":["="],"id":23530}],[{"start":{"row":84,"column":10},"end":{"row":84,"column":11},"action":"insert","lines":["6"],"id":23531}],[{"start":{"row":82,"column":30},"end":{"row":82,"column":31},"action":"remove","lines":["8"],"id":23532}],[{"start":{"row":82,"column":30},"end":{"row":82,"column":31},"action":"insert","lines":["6"],"id":23533}],[{"start":{"row":83,"column":9},"end":{"row":83,"column":10},"action":"remove","lines":["1"],"id":23534}],[{"start":{"row":83,"column":9},"end":{"row":83,"column":11},"action":"insert","lines":["[]"],"id":23535}],[{"start":{"row":84,"column":10},"end":{"row":84,"column":11},"action":"remove","lines":["6"],"id":23536}],[{"start":{"row":84,"column":10},"end":{"row":84,"column":12},"action":"insert","lines":["[]"],"id":23537}],[{"start":{"row":83,"column":10},"end":{"row":83,"column":11},"action":"remove","lines":["]"],"id":23538},{"start":{"row":83,"column":9},"end":{"row":83,"column":10},"action":"remove","lines":["["]}],[{"start":{"row":83,"column":9},"end":{"row":83,"column":10},"action":"insert","lines":["i"],"id":23539},{"start":{"row":83,"column":10},"end":{"row":83,"column":11},"action":"insert","lines":["n"]},{"start":{"row":83,"column":11},"end":{"row":83,"column":12},"action":"insert","lines":["t"]}],[{"start":{"row":83,"column":12},"end":{"row":83,"column":14},"action":"insert","lines":["()"],"id":23540}],[{"start":{"row":83,"column":13},"end":{"row":83,"column":14},"action":"insert","lines":["p"],"id":23541},{"start":{"row":83,"column":14},"end":{"row":83,"column":15},"action":"insert","lines":["a"]},{"start":{"row":83,"column":15},"end":{"row":83,"column":16},"action":"insert","lines":["g"]},{"start":{"row":83,"column":16},"end":{"row":83,"column":17},"action":"insert","lines":["e"]}],[{"start":{"row":84,"column":11},"end":{"row":84,"column":12},"action":"remove","lines":["]"],"id":23542},{"start":{"row":84,"column":10},"end":{"row":84,"column":11},"action":"remove","lines":["["]}],[{"start":{"row":84,"column":10},"end":{"row":84,"column":11},"action":"insert","lines":["i"],"id":23543},{"start":{"row":84,"column":11},"end":{"row":84,"column":12},"action":"insert","lines":["n"]},{"start":{"row":84,"column":12},"end":{"row":84,"column":13},"action":"insert","lines":["t"]}],[{"start":{"row":84,"column":13},"end":{"row":84,"column":15},"action":"insert","lines":["()"],"id":23544}],[{"start":{"row":84,"column":14},"end":{"row":84,"column":15},"action":"insert","lines":["l"],"id":23545},{"start":{"row":84,"column":15},"end":{"row":84,"column":16},"action":"insert","lines":["i"]},{"start":{"row":84,"column":16},"end":{"row":84,"column":17},"action":"insert","lines":["m"]},{"start":{"row":84,"column":17},"end":{"row":84,"column":18},"action":"insert","lines":["i"]},{"start":{"row":84,"column":18},"end":{"row":84,"column":19},"action":"insert","lines":["t"]}],[{"start":{"row":84,"column":20},"end":{"row":85,"column":0},"action":"insert","lines":["",""],"id":23546},{"start":{"row":85,"column":0},"end":{"row":85,"column":4},"action":"insert","lines":["    "]},{"start":{"row":85,"column":4},"end":{"row":85,"column":5},"action":"insert","lines":["p"]},{"start":{"row":85,"column":5},"end":{"row":85,"column":6},"action":"insert","lines":["r"]},{"start":{"row":85,"column":6},"end":{"row":85,"column":7},"action":"insert","lines":["i"]},{"start":{"row":85,"column":7},"end":{"row":85,"column":8},"action":"insert","lines":["n"]},{"start":{"row":85,"column":8},"end":{"row":85,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":85,"column":9},"end":{"row":85,"column":10},"action":"insert","lines":[" "],"id":23547}],[{"start":{"row":85,"column":9},"end":{"row":85,"column":10},"action":"remove","lines":[" "],"id":23548}],[{"start":{"row":85,"column":9},"end":{"row":85,"column":11},"action":"insert","lines":["()"],"id":23549}],[{"start":{"row":85,"column":10},"end":{"row":85,"column":11},"action":"insert","lines":["p"],"id":23550},{"start":{"row":85,"column":11},"end":{"row":85,"column":12},"action":"insert","lines":["a"]},{"start":{"row":85,"column":12},"end":{"row":85,"column":13},"action":"insert","lines":["g"]},{"start":{"row":85,"column":13},"end":{"row":85,"column":14},"action":"insert","lines":["e"]}],[{"start":{"row":80,"column":26},"end":{"row":80,"column":51},"action":"remove","lines":[", methods=['GET', 'POST']"],"id":23551}],[{"start":{"row":81,"column":40},"end":{"row":81,"column":65},"action":"remove","lines":[", methods=['GET', 'POST']"],"id":23552}],[{"start":{"row":109,"column":53},"end":{"row":109,"column":63},"action":"remove","lines":["homeGarden"],"id":23553},{"start":{"row":109,"column":53},"end":{"row":109,"column":86},"action":"insert","lines":["{'category_name':\"Home & Garden\"}"]}],[{"start":{"row":89,"column":53},"end":{"row":89,"column":84},"action":"insert","lines":["{'category_name':\"Electronics\"}"],"id":23554}],[{"start":{"row":128,"column":53},"end":{"row":128,"column":59},"action":"remove","lines":["motors"],"id":23555},{"start":{"row":128,"column":53},"end":{"row":128,"column":79},"action":"insert","lines":["{'category_name':\"Motors\"}"]}],[{"start":{"row":128,"column":30},"end":{"row":128,"column":80},"action":"remove","lines":["mongo.db.products.find({'category_name':\"Motors\"})"],"id":23556},{"start":{"row":128,"column":30},"end":{"row":128,"column":31},"action":"insert","lines":["m"]},{"start":{"row":128,"column":31},"end":{"row":128,"column":32},"action":"insert","lines":["o"]},{"start":{"row":128,"column":32},"end":{"row":128,"column":33},"action":"insert","lines":["t"]},{"start":{"row":128,"column":33},"end":{"row":128,"column":34},"action":"insert","lines":["o"]},{"start":{"row":128,"column":34},"end":{"row":128,"column":35},"action":"insert","lines":["r"]},{"start":{"row":128,"column":35},"end":{"row":128,"column":36},"action":"insert","lines":["s"]}],[{"start":{"row":109,"column":30},"end":{"row":109,"column":87},"action":"remove","lines":["mongo.db.products.find({'category_name':\"Home & Garden\"})"],"id":23557},{"start":{"row":109,"column":30},"end":{"row":109,"column":40},"action":"insert","lines":["homeGarden"]}],[{"start":{"row":110,"column":4},"end":{"row":110,"column":72},"action":"remove","lines":["homeGarden=mongo.db.products.find({'category_name':\"Home & Garden\"})"],"id":23558}],[{"start":{"row":108,"column":73},"end":{"row":109,"column":0},"action":"insert","lines":["",""],"id":23559},{"start":{"row":109,"column":0},"end":{"row":109,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":109,"column":4},"end":{"row":109,"column":72},"action":"insert","lines":["homeGarden=mongo.db.products.find({'category_name':\"Home & Garden\"})"],"id":23560}],[{"start":{"row":111,"column":0},"end":{"row":111,"column":4},"action":"remove","lines":["    "],"id":23561},{"start":{"row":110,"column":104},"end":{"row":111,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":129,"column":3},"end":{"row":129,"column":61},"action":"remove","lines":[" motors=mongo.db.products.find({'category_name':\"Motors\"})"],"id":23563}],[{"start":{"row":129,"column":2},"end":{"row":129,"column":3},"action":"remove","lines":[" "],"id":23564},{"start":{"row":129,"column":1},"end":{"row":129,"column":2},"action":"remove","lines":[" "]},{"start":{"row":129,"column":0},"end":{"row":129,"column":1},"action":"remove","lines":[" "]},{"start":{"row":128,"column":100},"end":{"row":129,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":127,"column":73},"end":{"row":128,"column":0},"action":"insert","lines":["",""],"id":23565},{"start":{"row":128,"column":0},"end":{"row":128,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":128,"column":4},"end":{"row":128,"column":62},"action":"insert","lines":[" motors=mongo.db.products.find({'category_name':\"Motors\"})"],"id":23566}],[{"start":{"row":128,"column":4},"end":{"row":128,"column":5},"action":"remove","lines":[" "],"id":23567}],[{"start":{"row":89,"column":4},"end":{"row":89,"column":22},"action":"remove","lines":["product_pagination"],"id":23588},{"start":{"row":89,"column":4},"end":{"row":89,"column":5},"action":"insert","lines":["e"]},{"start":{"row":89,"column":5},"end":{"row":89,"column":6},"action":"insert","lines":["l"]},{"start":{"row":89,"column":6},"end":{"row":89,"column":7},"action":"insert","lines":["e"]},{"start":{"row":89,"column":7},"end":{"row":89,"column":8},"action":"insert","lines":["c"]},{"start":{"row":89,"column":8},"end":{"row":89,"column":9},"action":"insert","lines":["t"]},{"start":{"row":89,"column":9},"end":{"row":89,"column":10},"action":"insert","lines":["r"]},{"start":{"row":89,"column":10},"end":{"row":89,"column":11},"action":"insert","lines":["o"]}],[{"start":{"row":89,"column":11},"end":{"row":89,"column":12},"action":"insert","lines":["n"],"id":23589},{"start":{"row":89,"column":12},"end":{"row":89,"column":13},"action":"insert","lines":["i"]},{"start":{"row":89,"column":13},"end":{"row":89,"column":14},"action":"insert","lines":["c"]},{"start":{"row":89,"column":14},"end":{"row":89,"column":15},"action":"insert","lines":["s"]}],[{"start":{"row":90,"column":4},"end":{"row":90,"column":5},"action":"insert","lines":["#"],"id":23590}],[{"start":{"row":94,"column":8},"end":{"row":94,"column":46},"action":"remove","lines":["product_pagination=product_pagination,"],"id":23591},{"start":{"row":94,"column":8},"end":{"row":94,"column":9},"action":"insert","lines":["\\"]}],[{"start":{"row":94,"column":8},"end":{"row":94,"column":9},"action":"remove","lines":["\\"],"id":23592},{"start":{"row":94,"column":4},"end":{"row":94,"column":8},"action":"remove","lines":["    "]},{"start":{"row":94,"column":0},"end":{"row":94,"column":4},"action":"remove","lines":["    "]},{"start":{"row":93,"column":32},"end":{"row":94,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":109,"column":30},"end":{"row":109,"column":40},"action":"remove","lines":["homeGarden"],"id":23593},{"start":{"row":109,"column":30},"end":{"row":109,"column":87},"action":"insert","lines":["mongo.db.products.find({'category_name':\"Home & Garden\"})"]}],[{"start":{"row":109,"column":4},"end":{"row":109,"column":22},"action":"remove","lines":["product_pagination"],"id":23595},{"start":{"row":109,"column":4},"end":{"row":109,"column":14},"action":"insert","lines":["homeGarden"]}],[{"start":{"row":108,"column":4},"end":{"row":108,"column":6},"action":"insert","lines":["# "],"id":23597}],[{"start":{"row":113,"column":7},"end":{"row":113,"column":46},"action":"remove","lines":[" product_pagination=product_pagination,"],"id":23598}],[{"start":{"row":128,"column":30},"end":{"row":128,"column":36},"action":"remove","lines":["motors"],"id":23599},{"start":{"row":128,"column":30},"end":{"row":128,"column":80},"action":"insert","lines":["mongo.db.products.find({'category_name':\"Motors\"})"]}],[{"start":{"row":128,"column":4},"end":{"row":128,"column":22},"action":"remove","lines":["product_pagination"],"id":23600},{"start":{"row":128,"column":4},"end":{"row":128,"column":9},"action":"insert","lines":["motor"]}],[{"start":{"row":131,"column":21},"end":{"row":132,"column":48},"action":"remove","lines":[",","        product_pagination = product_pagination,"],"id":23602}],[{"start":{"row":131,"column":21},"end":{"row":131,"column":22},"action":"insert","lines":[","],"id":23603}],[{"start":{"row":14,"column":29},"end":{"row":14,"column":49},"action":"remove","lines":["DB_ecommerce_project"],"id":23604}],[{"start":{"row":15,"column":27},"end":{"row":15,"column":128},"action":"remove","lines":["mongodb+srv://elias:kb01210012@myfirstcluster-uyvei.mongodb.net/DB_ecommerce_project?retryWrites=true"],"id":23605}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":15,"column":27},"end":{"row":15,"column":27},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1568143899050,"hash":"95ffe8713a8cf1d5338f9ccc5f229c393c753d42"}