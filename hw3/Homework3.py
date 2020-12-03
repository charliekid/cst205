# CST 205
# Charlie Nguyen
# 10/21/20
# Homework 3 - NOTE I was unable to get grayscale and thumbnail to work correctly

from PySide2.QtWidgets import (QApplication, QLabel, QWidget,
                                QPushButton, QLineEdit, QVBoxLayout, QComboBox)
from PySide2.QtCore import Slot
from Homework4.image_info import image_info
from PIL import Image


# this holds all of our tags
new_dict = {}
# this holds what the search hits
max_list = []
max_val = 0

# get tags into a dictionary so we can search easier
def preprocess(my_image_info):
    for i in my_image_info:
        new_dict[i['id']] = [tag.lower() for tag in i['tags']]

        # We are adding it to an existing tag list and removes the commas
        for j in i['title'].split():
            new_dict[i['id']].append(j.rstrip(',').lower())

        # adds a zero and a tie breaker for the second item
        new_dict[i['id']].insert(0, 0)
        new_dict[i['id']].insert(1,i['title'][0].lower())

    return new_dict


# loops through the dictionary and checks against the search string.
def get_count_from_search(dictionary, search):
    for key, value in dictionary.items():
        for counter, term in enumerate(value):
            if counter >1:
                if term in search: # if the term is in the search the increment that first value
                    value[0] +=1    
    return dictionary

def find_max_occurrence(list, val):
    for key, value in new_dict.items():
        for counter, term in enumerate(value):
            if counter == 0:
                if term >= val:
                    if term > val and len(list) > 0:
                        del max_list[:len(list)]
                    val = term
                    if val > 0:
                        list.append((value[1], key))
    return list

# Sephia filter function
def sepia(pixel):
  if pixel[0] < 63:
    r,g,b = int(pixel[0]*1.1), pixel[1], int(pixel[2]*.9)
  elif pixel[0]>62 and pixel[0]<192:
    r,g,b = int(pixel[0]*1.15), pixel[1], int(pixel[2]*.85)
  else:
    r = int(pixel[0]*1.08)
    if r>255: r=255
    g,b = pixel[1], pixel[2]//2
  return r,g,b

# Creates the window we want with a Line Edit
# Includes a submit button as well
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        vbox = QVBoxLayout()
        self.setGeometry(100, 100, 600, 400)

        # Sets up the line edit and search
        self.search_line_edit = QLineEdit("Search")
        self.search_line_edit.setMinimumWidth(250)
        self.search_line_edit.selectAll()
        self.submit_btn = QPushButton("Submit")
        self.my_lbl = QLabel('')
        self.instruction_label = QLabel("Search")
        self.submit_btn.clicked.connect(self.on_submit)
        self.search_line_edit.returnPressed.connect(self.on_submit)

        # sets up the combo box and choices
        self.img_manipulation_list = ["Pick a filter", "Sepia", "Negative", "Grayscale", "Thumbnail", "None"]
        self.my_combo_box = QComboBox()
        self.my_combo_box.addItems(self.img_manipulation_list)
        self.user_manipulation_label = QLabel("")

        # adds line edit and search to the window
        vbox.addWidget(self.instruction_label)
        vbox.addWidget(self.search_line_edit)


        # adds combo box to the window
        vbox.addWidget(self.my_combo_box)
        vbox.addWidget(self.user_manipulation_label)

        vbox.addWidget(self.submit_btn)
        vbox.addWidget(self.my_lbl)

        self.setLayout(vbox)
        # self.my_combo_box.currentIndexChanged.connect(self.update_ui)

    @Slot()
    def on_submit(self):
        user_input = self.search_line_edit.text()
        get_count_from_search(new_dict, user_input)
        find_max_occurrence(max_list, max_val)
        max_list.sort()

        # check for whats in the combo box and apply
        my_text = self.my_combo_box.currentText()
        my_index = self.my_combo_box.currentIndex()

        # opens the image
        im = Image.open(f'images/{max_list[0][1]}.jpg')

        # Checks to see what is in the combo box to apply filter
        if my_text == "Sepia":
            sepia_list = map(sepia, im.getdata())
            im.putdata(list(sepia_list))
        if my_text == "Negative":
            negative_list = [(255 - p[0], 255 - p[1], 255 - p[2])
                             for p in im.getdata()]
            im.putdata(negative_list)
        if my_text == "GrayScale":
            grayscale_list = [ ( (a[0]+a[1]+a[2])//3, ) * 3
                  for a in im.getdata() ]
            im.putdata(grayscale_list)
        if my_text == "Thumbnail":
            w,h = im.width, im.height
            target = Image.new('RGB', (w, h), 'red')
            target_x = 0
            for source_x in range(0, im.width, 2):
                target_y = 0
                for source_y in range(0, im.height, 2):
                    pixel = im.getpixel((im, im))
                    target.putpixel((target_x, target_y), pixel)
                    target_y += 1
                target_x += 1
            target.show()



        im.show()
        #self.my_lbl.setText(f'You typed in {user_input}')
        print(user_input)

    ## we want to update the photo to the newly selected filter
    @Slot()
    def update_ui(self):
        my_text = self.my_combo_box.currentText()
        my_index = self.my_combo_box.currentIndex()

# WHERE THE PROGRAM BEGANS
preprocess(image_info)

# open the window for the search here
app = QApplication([])
my_win = MyWindow()
my_win.show()
app.exec_()

