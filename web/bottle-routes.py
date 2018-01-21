import main
import os
from bottle import route, run
from bottle import static_file

# This is to set the root directory of the web server
os.chdir("C:/DEV/GitHub/GitRepo/CourseAuxMimes")

# print(str(os.listdir()))
# print(os.curdir)
# print(os.getcwd())

@route('/')
def main_html():
    return static_file('main.html', root='web/')

@route('/vue-test')
def vue_test():
    return static_file('index.html', root='web-vuetify/')

@route('/get-word-list')
def ajax_hello():
    return main.getList()

@route('/hello')
def hello():
    return "Hello World!"

run(host='localhost', port=8080, debug=True)