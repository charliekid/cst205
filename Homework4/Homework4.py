# CST 205
# Charlie Nguyen
# 11/2/20
# Homework 4: This project allows me to show 3 random images that the user can choose and
# see more information on the image. This project uses flask.

from PIL import Image
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import random                           # used to choose random images to display
from image_info import image_info       # Used to hold our image information

# Creates an instance of the Flask class
app = Flask(__name__)

bootstrap = Bootstrap(app)

# Home route
@app.route('/')
def home():
    # Choose three random images
    random1 = random.choice(image_info)
    random2 = random.choice(image_info)
    random3 = random.choice(image_info)
    return render_template('home.html',
                           id1=random1["id"], title1=random1["title"],
                           id2=random2["id"], title2=random2["title"],
                           id3=random3["id"], title3=random3["title"]
                           )

# Image page
@app.route('/picture/<id>')
def image_page(id):
    # look for the images info
    for anImage in image_info:
        if anImage["id"] == id:
            title = anImage["title"]
            author = anImage["flickr_user"]
            path = "Homework4/static/images/" + id + ".jpg"
            im = Image.open(path)
            w = im.width
            h = im.height
            mode = im.mode
            format = im.format

    return  render_template('imagePage.html', id=id, title=title, author=author, w=w, h=h, mode=mode, format=format)
