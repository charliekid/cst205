# CST 205
# Charlie Nguyen
# 11/17/20

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import random                           # used to choose random images to display
from Homework4.image_info import image_info       # Used to hold our image information


# Creates an instance of the Flask class
app = Flask(__name__)

bootstrap = Bootstrap(app)

# Choose three random images
random1 = random.choice(image_info)
random2 = random.choice(image_info)
random3 = random.choice(image_info)
print(random1["id"])

# Home route
@app.route('/')
def home():

    return render_template('template.html')




# @app.route('/hello')
# def hello():
#     my_string = "<p>Here are interesting facts...</p><br>Samuel - is taking 205 for fun to be a full time student <br> Justin - has a 9 year old cat<br>Michael- has 2 white poodles <br>alicia - is an only child "
#     return my_string
#

# # Runs by template
# @app.route('/charlie')
# def t_test():
#     return render_template('template.html')