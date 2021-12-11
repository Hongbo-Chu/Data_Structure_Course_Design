from flask import Flask, render_template,jsonify,request
import sys
sys.path.append('../back/')
from huffman_final import huffman
from search import searcher
from TOP30 import TOP
app = Flask(__name__)


#渲染页面
@app.route('/homepage')
def homepage():
    # return "212"
    return render_template('homepage.html')

@app.route('/doc')
def doc():
    return render_template('doc.html')

@app.route('/exdoc')
def exdoc():
    return render_template('exdoc.html')

@app.route('/encode')
def encode():
    return render_template('encode.html')
@app.route('/statistic')
def statistic():
    return render_template('statistic.html')
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




# @app.route('/encode', methods = ['post'])
# def encode():
#     print('encode')
#     ii = request.json.get('name')
#     path1 = "cs_data/"
#     print(path1)
#     path1 += str(ii)
#     a = huffman(path1)
#     a.get_code()
#     return a.encodingFile(path1)

#新建文件
@app.route('/newdoc', methods = ['post'])
def newdoc():
    f = request.json.get('name')
    cont = request.json.get('cont')
    f = str(f)
    cont = str(cont)
    fname = 'D:\\vscodePythonSpace\Data_Structure_Course_Design\cs_data\\'+f
    file = open(fname,'w')
    file.write(cont)
    return cont

#编辑已有的文件
@app.route('/exdoc/edit', methods = ['post'])
def edit_exdoc():
    f = request.json.get('name')
    fname = 'D:\\vscodePythonSpace\Data_Structure_Course_Design\cs_data\\'+f
    with open(fname, "r") as f:
        data = f.read()
    return data

@app.route('/exdoc/save', methods = ['post'])
def edit_exdoc_save():
    f = request.json.get('name')
    cont = request.json.get('cont')
    f = str(f)
    cont = str(cont)
    fname = 'D:\\vscodePythonSpace\Data_Structure_Course_Design\cs_data\\'+f
    file = open(fname,'w')
    file.write(cont)
    return cont

@app.route('/encode/search', methods = ['post'])
def encode_search():
    f = request.json.get('name')
    f = str(f)
    fname = 'D:\\vscodePythonSpace\Data_Structure_Course_Design\cs_data\\'+f
    with open(fname, "r") as f:
        data = f.read()
    return data

@app.route('/encode/encoding', methods = ['post'])
def encode_encoding():
    ii = request.json.get('name')
    path1 = "D:\\vscodePythonSpace\Data_Structure_Course_Design\cs_data\\"
    print(path1)
    path1 += str(ii)
    a = huffman(path1)
    a.get_code()
    # print(a.encodingFile(path1))
    return a.encodingFile(path1)


@app.route('/encode/save', methods = ['post'])
def encode_save():
    f = request.json.get('name')
    cont = request.json.get('cont')
    f = str(f)
    cont = str(cont)
    fname = 'D:\\vscodePythonSpace\Data_Structure_Course_Design\huffman_code\\'+f
    file = open(fname,'w')
    file.write(cont)
    return cont

@app.route('/encode/decode', methods = ['post'])
def encode_decode():
    ii = request.json.get('name')
    path1 = "D:\\vscodePythonSpace\Data_Structure_Course_Design\cs_data\\"
    print(path1)
    path1 += str(ii)
    a = huffman(path1)
    a.get_code()
    # print(a.encodingFile(path1))
    return a.decoding(a.encodingFile(path1))

@app.route('/statistic/show', methods = ['post'])
def statistic_show():
    ii = request.json.get('name')
    T = TOP(ii)
    return T.sorrt()
    
    # return a.decoding(a.encodingFile(path1))
    # 开始对选定文件进行词频统计

if __name__ == '__main__':
    app.run(port=8080, debug=True)
    
    

