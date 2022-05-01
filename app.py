from flask import Flask, render_template, request, redirect, send_file
from exporter import save_to_file
from scrapper import get_jobs

# 플라스크 인스턴스 생성
app = Flask("1") 

# 검색결과를 담을 임시 Dictionary 생성
db={}

# HTTP 요청에 따른 라우팅 설정
# 요청 경로가 없는 경우
@app.route('/')
def home():
    return render_template("home.html") #home.html 를 렌더링하여 보여줌

# /report 경로로 요청했을 경우
@app.route('/report')
def report():
    keyword = request.args.get('keyword') # 요청에서 keyword 아규먼트를 가져옴
    if keyword: # keyword 존재할 경우
        keyword = keyword.lower() # keyword 를 소문자로 변환
        fromDB = db.get(keyword) # db 에서 keyword 값을 가져옴 
        if fromDB: # db 에 keyword 값이 존재했을 경우
            jobs = fromDB
            result_number = len(jobs) # 검색된 값의 갯수를 가져옴
        else: # db 에 keyword 값이 존재하지 않을 경우
            jobs = get_jobs(keyword) # 사이트에서 검색된 값을 가져옴
            db[keyword] = jobs # db에 keyword와 검색된 값을 저장 
            result_number = len(jobs)
    else: # keyword  존재하지 않을 경우
        return redirect("/") # 기본 경로로 리다이렉트
        # keyword, 검색결과의 갯수, 검색결과를 report.html 로 전달하고 렌더링함
    return render_template("report.html", keyword=keyword, result_number=result_number, jobs=jobs) 

# /export 경로로 요청했을 경우
@app.route('/export')
def export():
    try:
        keyword = request.args.get('keyword') # 요청에서 keyword 아규먼트를 가져옴
        if not keyword: # keyword 가 존재하지 않을 경우
            raise Exception() # 예외발생
        keyword = keyword.lower() # keyword 를 소문자로 변환
        jobs = db.get(keyword) # db 에서 keyword 의 값을 가져옴
        if not jobs: # keyword 의 값이 없을 경우
            raise Exception() # 예외발생
        save_to_file(jobs) # jobs 를 csv 파일로 저장
        return send_file("jobs.csv")
    except:
        return redirect("/") # 예외가 발생했으면 기본 경로로 리다이렉트

# 그 외의 경로로 요청했을 경우
@app.route('/<random_string>')
def kimchi(random_string):
    return redirect("/") # 기본 경로로 리다이렉트

app.run(host="0.0.0.0") # Flask 호스트 IP와 포트를 설정