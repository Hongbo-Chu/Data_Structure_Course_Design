from flask import Flask, render_template,jsonify,request
import sys
sys.path.append('../back/')
from huffman_final import huffman
from search import searcher
app = Flask(__name__)

@app.route('/homepage')
def hello():
    # return "212"
    return render_template('homepage.html')
# #显示中文文本
# @app.route('/jsondemo', methods = ['post'])
# def jsondemo():
#     print('haha')
#     info = request.json.get('name')
#     print(info)

#     path = "D:/vscodePythonSpace/Data_Structure_Course_Design/cs_data/"
#     path += str(info)
#     with open(path, "r") as f:
#         data = f.read()
#     return data

#显示搜索结果
@app.route('/jsondemo', methods = ['post'])
def jsondemo():
    print('haha')
    info = request.json.get('name')
    print(info)
    ans = searcher(info)
    return ans



@app.route('/encode', methods = ['post'])
def encode():
    print('encode')
    ii = request.json.get('name')
    path1 = "cs_data/"
    print(path1)
    path1 += str(ii)
    a = huffman(path1)
    a.get_code()
    return a.encodingFile(path1)



@app.route('/doc')
def doc():
    return render_template('doc.html')

if __name__ == '__main__':
    app.run(port=8080, debug=True)
    
    

