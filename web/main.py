from flask import *
from adapter.intend import adapterIntend
from adapter.greeting import adapterGreeting
from adapter.ner import adapterNer
from app import chatbot
from app import apixuChatBot as api
# import adapter.crf_ner_no_accent.ner_crf_no_accent as ner_crf_no_accent
import datetime
import pprint
app = Flask(__name__, static_url_path="/static")
pp = pprint.PrettyPrinter(indent=2)
adapterIntend = adapterIntend.AdapterIntend()
adapterNer = adapterNer.AdapterNer()
adapterGreeting = adapterGreeting.AdapterGreeting()


@app.route('/')
def index():
    session['loc'] = []
    session['time'] = []
    session['weather'] = []
    session['bot_state'] = 1
    session['bot_msg'] = ""

    return render_template('index.html')
@app.route('/m', methods=['POST'])
def response_message():
    m = request.form['m']
    results = response(m)
    # if ner_crf_no_accent.check_accent(m) == True:
    #     results = response(m)
    # else:
    #     results = response_no_accent(m)
    if m == ":)" or m ==":(" or m==":D" or m == ":;" or m == "<3" or m == ":*":
                return json.dumps({
                'message': ":D"
                 })
    if m == ":P" or m ==":j" or m=="-_-" or m == ":/" or m ==":o":
                return json.dumps({
                'message': ":j"
                 })                          
    intend = results['intend']
    if intend == 1:
        return json.dumps({
            'message': results['msg']
        })
    elif intend == 2 :
        msg = ""
        pp.pprint(results)
        if results['loc'] == None or len(results['loc']) == 0:
            return json.dumps({
            'message': results['msg']
        })
        if results['time'] == None or len(results['time']) == 0 :
            return json.dumps({
            'message': results['msg']
        })
        if len(results['msg']['error']) != 0:
            for i in range(len(results['msg']['error'])):
                msg += results['msg']['error'][i] + ' <br/> '

        for i in range(len(results['msg']['data'])):
            msg += " <strong> Tại "+ str(results['msg']['data'][i]['địa điểm']).title() +" "+ str(results['msg']['data'][i]['thời gian']) +' :</strong> <br/>'
            for k,v in results['msg']['data'][i]['thời tiết'].items():
                if isinstance(v, dict):
                    msg += str(k)+ ": <br/>"
                    for i,j in v.items():
                        msg += "&nbsp; &nbsp;{} : {} <br/>".format(i,j)
                else:
                    msg += str(k) + " : " + str(v) +' <br/> '
        msg += " :D <br/> "      
        return json.dumps({
            'message': msg
        })

    elif intend == 3:
        msg = ""
        pp.pprint(results)
        if results['loc'] == None or len(results['loc']) == 0:
            return json.dumps({
            'message': results['msg']
        })
        if  results['time'] == None or len(results['time']) == 0 :
            return json.dumps({
            'message': results['msg']
        })
        if len(results['msg']['error']) != 0:
            for i in range(len(results['msg']['error'])):
                msg += results['msg']['error'][i] + ' <br/> '

        for i in range(len(results['msg']['data'])):
            msg += " <strong> Tại "+ str(results['msg']['data'][i]['địa điểm']).title() +" "+ str(results['msg']['data'][i]['thời gian']) +' :</strong> <br/>'
            for k,v in results['msg']['data'][i]['thời tiết'].items():
                if isinstance(v, dict):
                    msg += str(k)+ ": <br/>"
                    for i,j in v.items():
                        msg += " &nbsp;&nbsp;   {} : {} <br/>".format(i,j)
                else:
                    msg += str(k) + " : " + str(v) +' <br/> '
        msg += " :D <br/> "      
        return json.dumps({
            'message': msg
        })
    else :
        msg = ""
        pp.pprint(results)
        if   results['loc'] == None or len(results['loc']) == 0:
            return json.dumps({
            'message': results['msg']
        })
        if results['time'] == None or len(results['time']) == 0 :
            return json.dumps({
            'message': results['msg']
        })
        if len(results['msg']['error']) != 0:
            for i in range(len(results['msg']['error'])):
                msg += results['msg']['error'][i] + ' <br/>'

        for i in range(len(results['msg']['data'])):
            msg += " <strong> Tại "+ str(results['msg']['data'][i]['địa điểm']).title() +" "+ str(results['msg']['data'][i]['thời gian']) +':</strong> <br/> '
            for k,v in results['msg']['data'][i]['thời tiết'].items():
                if isinstance(v, dict):
                    msg += str(k)+ ": <br/> "
                    for i,j in v.items():
                        msg += " &nbsp; &nbsp;   {} : {} <br/>".format(i,j)
                else:
                    msg += str(k) + " : " + str(v) +' <br/> '
        msg += " :D <br/>"            
        return json.dumps({
            'message': msg
        })


def response(user_msg):
    intend = adapterIntend.get_intend(user_msg)
    # return intend
    if session['bot_state'] == 1:
        if intend == 1 :
            data = adapterGreeting.make_response(user_msg)
        elif intend == 2 :
            data = adapterNer.detect_entity(user_msg)
        elif intend == 3 :
            data = adapterNer.detect_entity(user_msg)
        else:
            data = None
        return make_msg(data,intend)
    elif session['bot_state'] == 2:
        if intend == 1 :
            data = adapterGreeting.make_response(user_msg)
        elif intend == 2 :
            data = adapterNer.detect_entity(user_msg)
        elif intend == 3 :
            data = adapterNer.detect_entity(user_msg)
        else:
            data = adapterNer.detect_entity(user_msg)
        return make_msg(data,intend)
    elif session['bot_state'] == 3 :
        data = adapterNer.detect_entity(user_msg)
        if adapterNer.detect_question_again(user_msg):
            data = adapterNer.detect_entity(user_msg)
            return make_msg(data,intend)
        # elif data['LOC'] != [] or data['TIME'] != [] or data['WEATHER'] != []:
        #     return make_msg(data, intend)
        else :
            session['bot_state'] = 1
            session['time'] = None
            session['loc'] = None
            if intend == 1:
                data = adapterGreeting.make_response(user_msg)
            elif intend == 2:
                data = adapterNer.detect_entity(user_msg)
            elif intend == 3:
                data = adapterNer.detect_entity(user_msg)
            else:
                data = None
            return make_msg(data, intend)

def response_no_accent(user_msg):
    data = ner_crf_no_accent.ner_crf(user_msg)
    return data



def make_msg(data=None,intend=4):
    data_msg = {}
    if session['bot_state'] == 3:
        if data['LOC'] == [] and data['TIME'] == [] and data['WEATHER'] == [] :
            session['loc'] = []
            session['time'] = []
            session['weather'] = ["thời tiết"]
            session['bot_msg'] = "mình không hiểu ý bạn :("
            session['bot_state'] = 1
        else :
            if data['LOC'] != [] :
                session['loc'] = data['LOC']
            if data['TIME'] != [] :
                session['time'] = data['TIME']
            if len(data["WEATHER"]) == 0:
                session['weather'] = session['weather']
            else:
                session['weather'] = data["WEATHER"]
                session['bot_state'] = 3
            session['bot_msg'] = query_api({"loc": session['loc'], "time": session['time'], "weather": session['weather']})
    
    else :
        if intend == 1:
            session['loc'] = None
            session['time'] = None
            session['bot_msg'] = data
            session['weather'] = ["thời tiết"]
            session['bot_state'] = 1
        elif intend == 2:
            # session['loc'] = data["LOC"]
            # session['time'] = data["TIME"]
            if data['LOC'] != [] :
                session['loc'] = data['LOC']
            if data['TIME'] != [] :
                session['time'] = data['TIME']
            if len(data["WEATHER"]) == 0 and session['weather'] == []:
                session['weather'] = ["thời tiết"]
            elif len(data['WEATHER']) == 0:
                session['weather'] = session['weather']
            else:
                session['weather'] = data["WEATHER"]

            if session['loc'] == None or session['loc'] == []:
                session['bot_msg'] = "bạn cho xin địa điểm :D"
                session['bot_state'] = 2
            elif session['time'] == None or session['time'] == []:
                session['bot_msg'] = "bạn cho xin thời gian :D"
                session['bot_state'] = 2
            else:
                session['bot_msg'] = query_api({"loc": session['loc'], "time": session['time'], "weather": session['weather']})
                session['bot_state'] = 3
        elif intend == 3:
            # session['loc'] = data["LOC"]
            # session['time'] = data["TIME"]
            if data['LOC'] != [] :
                session['loc'] = data['LOC']
            if data['TIME'] != [] :
                session['time'] = data['TIME']
            if len(data["WEATHER"]) == 0 and session['weather'] == []:
                session['weather'] = ["thời tiết"]
            elif len(data['WEATHER']) == 0:
                session['weather'] = session['weather']
            else:
                session['weather'] = data["WEATHER"]

            if session['loc'] == None or session['loc'] == []:
                session['bot_msg'] = "bạn cho xin địa điểm :D"
                session['bot_state'] = 2
            elif session['time'] == None or session['time'] == []:
                session['bot_msg'] = "bạn cho xin thời gian :D"
                session['bot_state'] = 2
            else:
                session['bot_msg'] = query_api({"loc": session['loc'], "time": session['time'], "weather": session['weather']})
                session['bot_state'] = 3
        elif intend == 4 and session['bot_state'] == 1:
            session['loc'] = None
            session['time'] = None
            session['bot_msg'] = "mình không hiểu ý bạn :("
            session['weather'] = ["thời tiết"]
            session['bot_state'] = 1
        elif intend == 4 and session['bot_state'] == 2:
            if data["LOC"] != []:
                session['loc'] = data["LOC"]
            if data["TIME"] != []:
                session['time'] = data["TIME"]
            if len(data["WEATHER"]) == 0:
                session['weather'] = session['weather']
            else:
                session['weather'] = data["WEATHER"]

            if session['loc'] == None or session['loc'] == []:
                session['bot_msg'] = "bạn cho xin địa điểm :D"
                session['bot_state'] = 2
            elif session['time'] == None or session['time'] == []:
                session['bot_msg'] = "bạn cho xin thời gian :D"
                session['bot_state'] = 2
            else:
                session['bot_msg'] = query_api({"loc":session['loc'],"time":session['time'],"weather":session['weather']})
                session['bot_state'] = 3
    data_msg["intend"] = intend
    data_msg["loc"] = session['loc']
    data_msg["time"] = session['time']
    data_msg["weather"] = session['weather']
    data_msg["msg"] = session['bot_msg']
    data_msg["state"] = session['bot_state']
    return data_msg

def query_api(data):
    res = []
    current_time = datetime.datetime.now()
    current_day = current_time.day
    current_month = current_time.month
    current_year = current_time.year
    locs = data['loc']
    times = data['time']
    weather = data['weather']
    for loc in locs :
        for time in times :
            args = {"q":"{},{}".format(loc['lat'],loc['lng']),"dt":"{}-{}-{}".format(time['year'],time['month'],time['day'])}
            if datetime.date(current_year,current_month,current_day) < datetime.date(int(time['year']),int(time['month']),int(time['day'])) :
                res.append(api.get_forecast_weather(args))
            elif datetime.date(current_year,current_month,current_day) == datetime.date(int(time['year']),int(time['month']),int(time['day'])):
                res.append(api.get_data_current_weather(args))
            else :
                res.append(api.get_history_weather(args))
    return filter_msg(res,weather,locs,times)


def filter_msg( data, weather, locs, times):
    w = ['nắng', 'mưa', 'nhiệt độ', 'mây', 'độ ẩm', 'gió', 'tầm nhìn', 'áp suất khí quyển', 'uv', 'lượng mưa',
         'hướng gió', 'nóng', 'lạnh', 'rét', 'thời tiết']
    er = []
    enable_data = []
    res = {}
    for i in weather:
        if i not in w:
            er.append("không có dữ liệu về {} :(".format(i))
        else:
            enable_data.append(i)
    res['error'] = er
    filter_data = []
    sat = []
    for loc in locs:
        for time in times:
            sat.append((time, loc))
    # for tup in sat:
    for id, i in enumerate(data):
        d = {}
        d["thời tiết"] = {}
        for k in enable_data:
            if k in ["thời tiết"]:
                d["thời tiết"] = i
                break
            elif k in ["nắng"]:
                for z in i:
                    if "nhiệt độ" in z or "mây" in z or "lượng mưa" in z or "điều kiện thời tiết" in z:
                        d["thời tiết"][z] = i[z]
            elif k in ["nhiệt độ", "nóng", "lạnh", "rét"]:
                for z in i:
                    if "nhiệt độ" in z or "mây" in z or "điều kiện thời tiết" in z:
                        d["thời tiết"][z] = i[z]
            elif k in ["mưa", "lượng mưa"]:
                for z in i:
                    if "lượng mưa" in z or "điều kiện thời tiết" in z:
                        print(z)
                        d["thời tiết"][z] = i[z]
            elif k in ["mây"]:
                for z in i:
                    if "mây" in z or "điều kiện thời tiết" in z:
                        d["thời tiết"][z] = i[z]
            elif k in ["tầm nhìn"]:
                for z in i:
                    if "tầm nhìn" in z:
                        d["thời tiết"][z] = i[z]
            elif k in ["uv"]:
                for z in i:
                    if "uv" in z:
                        d["thời tiết"][z] = i[z]
            elif k in ["hướng gió", "gió"]:
                for z in i:
                    if "gió" in z:
                        d["thời tiết"][z] = i[z]
            elif k in ["áp suất khí quyển"]:
                for z in i:
                    if "áp suất" in z:
                        d["thời tiết"][z] = i[z]
            elif k in ["độ ẩm"]:
                for z in i:
                    if "độ ẩm" in z or "lượng mưa" in z:
                        d["thời tiết"][z] = i[z]
        time = sat[id][0]
        loc = sat[id][1]
        d['thời gian'] = "{}/{}/{}".format(time['day'], time['month'], time['year'])
        d['địa điểm'] = loc['name']
        filter_data.append(d)
    res['data'] = filter_data
    return res

#====================================================
def main():
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run()
