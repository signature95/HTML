from flask import Flask, render_template, url_for
import pymysql


app = Flask(__name__)

# export FLASK_APP=main
# (base) jeong-giho@jeong-gihoui-MacBookPro HTML_test % flask run

# 미리 url을 짜놓고 들어가기도 함. (몇번 페이지를 만들것이고 어떤 기능을 형성할 것인지 문서화하고 개발을 시도함)
# 로컬 호스트에 들어갈 때, index.html을 보여주겠다.
@app.route('/')
def index():
    labels = []
    cost = []
    tax = []
    #접속이 안되는 경우를 고려 (connect 생성)
    try:
        sample_db = pymysql.connect(
            user='root', 
            password='jjms7794',
            host='localhost',
            database='web_test'
        )
        # 커서 입력
        cursor = sample_db.cursor()
        # sql 명령문 실행
        sql = "select * from chart"
        # data 출력
        cursor.execute(sql)
        result = cursor.fetchall()
        # 각 리스트에 데이터를 append 시켜준다.
        for list in result:
            labels.append(list[0])
            cost.append(list[1])
            tax.append(list[2])
        print(result)        
    finally:
        # 접속 종료
        sample_db.close()
    
    # 뽑은 data를 리턴해줘야 index.html에서 인식할 수 있게 된다. 
    return render_template('index.html', result = result, label = labels, data1 = cost, data2 = tax)



@app.route('/dy')
def dy():
    return render_template('dygraph.html')


@app.route('/chart')
def chart():
    labels = []
    cost = []
    tax = []
    #접속이 안되는 경우를 고려 (connect 생성)
    try:
        sample_db = pymysql.connect(
            user='root', 
            password='jjms7794',
            host='localhost',
            database='web_test'
        )
        # 커서 입력
        cursor = sample_db.cursor()
        # sql 명령문 실행
        sql = "select * from chart"
        # data 출력
        cursor.execute(sql)
        result = cursor.fetchall()
        # 각 리스트에 데이터를 append 시켜준다.
        for list in result:
            labels.append(list[0])
            cost.append(list[1])
            tax.append(list[2])
        print(result)        
    finally:
        # 접속 종료
        sample_db.close()
    
    # 뽑은 data를 리턴해줘야 index.html에서 인식할 수 있게 된다. 
    return render_template('dashboard.html', result = result, label = labels, data1 = cost, data2 = tax)

@app.route('/paging')
def paging():
    labels = []
    cost = []
    tax = []
    #접속이 안되는 경우를 고려 (connect 생성)
    try:
        sample_db = pymysql.connect(
            user='root', 
            password='jjms7794',
            host='localhost',
            database='web_test'
        )
        # 커서 입력
        cursor = sample_db.cursor()
        # sql 명령문 실행
        sql = "select * from chart"
        # data 출력
        cursor.execute(sql)
        result = cursor.fetchall()
        # 각 리스트에 데이터를 append 시켜준다.
        for list in result:
            labels.append(list[0])
            cost.append(list[1])
            tax.append(list[2])
        print(result)        
    finally:
        # 접속 종료
        sample_db.close()
    return render_template('ppage.html', result = result, label = labels, data1 = cost, data2 = tax)

app.run

