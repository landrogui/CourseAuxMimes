from flask import Flask

# EB looks for an 'application' callable by default.
application = Flask(__name__)

application.static_folder = ''
application.template_folder = ''


@application.route('/')
def hello_world_route():
    return application.send_static_file('index_test.html')


@application.route('/<filename>')
def route_static_file(filename):
    return application.send_static_file(filename)


@application.route('/subfolder/<path:filepath>')
def route_dynamic_static_file(filepath):
    return application.send_static_file('subfolder/' + filepath)


@application.route('/css/<path:filename>')
def send_css(filename):
    return application.send_static_file('css/' + filename)


@application.route('/fonts/<path:filename>')
def send_fonts(filename):
    return application.send_static_file('fonts/' + filename)


@application.route('/img/<path:filename>')
def send_img(filename):
    return application.send_static_file('img/' + filename)


# Route to find npm installed component
@application.route('/node_modules/<path:filename>')
def send_npm(filename):
    return application.send_static_file('node_modules/' + filename)


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
