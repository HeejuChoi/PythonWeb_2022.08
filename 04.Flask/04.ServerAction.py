from flask import Flask, render_template, request, current_app
import os #디렉토리와 파일에 관련된 작업을 하겠다. 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('01.index.html')

@app.route('/menu', methods=['GET','POST'])
def menu():
    if request.method == 'GET': 
        languages = [
            {'disp': '영어', 'val':'en'},
            {'disp': '일어', 'val':'jp'},
            {'disp': '중국어', 'val':'cn'},
            {'disp': '프랑스어', 'val':'fr'},
            {'disp': '스페인어', 'val':'es'}
        ]
        return render_template('02.Menu.html', options = languages) # 서버에서 클라이언트로 정보 전달
    else: 
        # 사용자가 입력한 정보를 서버가 읽음
        index = request.form['index']
        lang = request.form['lang']
        lyrics = request.form['lyrics']
        print(lang, '\n' , index, '\n', lyrics, sep='')  
        # 사용자가 입력한 파일을 읽어서 upload 디렉토리에 저장
        f_image = request.files['image']
        print(f_image.filename)          # 사용자가 입력한 파일 이름 
        filename = os.path.join(current_app.root_path, 'static/upload/') + f_image.filename
        print(filename)   
        f_image.save(filename)  #upload폴더에 사진이 저장됨 (클라이언트가 올린 사진을 서버가 저장함)
        # 모델 실행 후 결과를 돌려줌
        result = '독수리 (73.52%)'
        return render_template('03.Menu_res.html', result=result, fname=f_image.filename)

if __name__ == '__main__':
    app.run(debug=True)