# CST 205
# Charlie Nguyen
# 10/14/20

# sys module needed for optional command line arguments
from PySide2.QtWidgets import (QApplication, QLabel, QWidget,
                               QPushButton, QLineEdit, QVBoxLayout)
from PySide2.QtCore import Slot
from PIL import Image
from Homework4.image_info import image_info
from pprint import pprint

# this holds all of our tags
new_dict = {}

# Makes searching images a bit easier
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

# something to store those images
# find the max occurence(s) and associated id(s)
# max val stores the max
max_list = []
max_val = 0

def find_max_occurrence(max_list, max_val):
    print("inside of the find_max_occurance")
    for key, value in new_dict.items():
        for counter, term in enumerate(value):
            if counter == 0:
                if term >= max_val:
                    if term > max_val and len(max_list) > 0:
                        del max_list[:len(max_list)]
                    max_val = term
                    if max_val > 0:
                        max_list.append((value[1], key))
    return list

def open_image(list):
    print("insdie of open image")
    max_list.sort()
    im = Image.open(f'images/{list[0][1]}.jpg')
    im.show()

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

        # # sets up the combo box and choices
        # self.img_manipulation_list = ["Pick a filter", "Sepia", "Negative", "Grayscale", "Thumbnail", "None"]
        # self.my_combo_box = QComboBox()
        # self.my_combo_box.addItems(self.img_manipulation_list)
        # self.user_manipulation_label = QLabel("")

        # adds line edit and search to the window
        vbox.addWidget(self.instruction_label)
        vbox.addWidget(self.search_line_edit)
        vbox.addWidget(self.submit_btn)
        vbox.addWidget(self.my_lbl)

        # # adds combo box to the window
        # vbox.addWidget(self.my_combo_box)
        # vbox.addWidget(self.user_manipulation_label)

        self.setLayout(vbox)
        # self.my_combo_box.currentIndexChanged.connect(self.update_ui)

    @Slot()
    def on_submit(self):
        user_input = self.search_line_edit.text()
        get_count_from_search(new_dict, user_input)
        find_max_occurrence(max_list, max_val)
        open_image(max_list)
        #self.my_lbl.setText(f'You typed in {user_input}')
        print(user_input)

    # ComboBox update stuff
    # @Slot()
    # def update_ui(self):
    #     my_text = self.my_combo_box.currentText()
    #     my_index = self.my_combo_box.currentIndex()
    #     self.user_manipulation_label.setText(f'You chose {self.img_manipulation_list[my_index]}.')


# image prepping
pprint(preprocess(image_info))

# Instantiates and shows windows
app = QApplication([])
my_win = MyWindow()
my_win.show()
app.exec_()