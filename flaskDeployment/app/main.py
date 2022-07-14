# import requirements needed
from flask import Flask, render_template
from utils import get_base_url

# setup the webserver
# port may need to be changed if there are multiple flask servers running on same server
port = 12344
base_url = get_base_url(port)

# if the base url is not empty, then the server is running in development, and we need to specify the static folder so that the static files are served
if base_url == '/':
    app = Flask(__name__)
else:
    app = Flask(__name__, static_url_path=base_url+'static')

# set up the routes and logic for the webserver
@app.route(f'{base_url}') # when the URL reaches this point
def home():
    return render_template('index.html')

@app.route(f'{base_url}/index')
def home_2():
    return render_template('index.html')

@app.route(f'{base_url}/charts')
def chart():
    return render_template('charts.html')

@app.route(f'{base_url}/machineLearning')
def ml():
    return render_template('machineLearning.html')

@app.route(f'{base_url}/About-us')
def aboutUs():
    return render_template('About-us.html')

# define additional routes here
# for example:
# @app.route(f'{base_url}/team_members')
# def team_members():
#     return render_template('team_members.html') # would need to actually make this page

if __name__ == '__main__':
    # IMPORTANT: change url to the site where you are editing this file.
    website_url = 'cocalc21.ai-camp.dev'
    
    print(f'Try to open\n\n    https://{website_url}' + base_url + '\n\n')
    app.run(host = '0.0.0.0', port=port, debug=True)
