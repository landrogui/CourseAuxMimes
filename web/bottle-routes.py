import os
from app.main import *
from bottle import route, run
from bottle import static_file

# This is to set the root directory of the web server

os.chdir("C:/Users/Guillaume/Dev/CourseAuxMimes")

# print(str(os.listdir()))
# print(os.curdir)
# print(os.getcwd())


@route('/')
def main_html():
    return static_file('main.html', root='web/')


@route('/vue-test')
def vue_test():
    return static_file('index.html', root='web-vuetify/')


@route('/css/<filename:path>')
def send_css(filename):
    return static_file(filename, root='css/')


@route('/fonts/<filename:path>')
def send_fonts(filename):
    return static_file(filename, root='fonts/')


@route('/img/<filename:path>')
def send_img(filename):
    return static_file(filename, root='img/')


@route('/get-word-list')
def ajax_hello():
    return getListWords("Francais")


@route('/hello')
def hello():
    return "Hello World!"


run(host='localhost', port=8080, debug=True)