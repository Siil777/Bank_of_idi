from tkinter import * 
import tkinter as tk 
from tkinter import ttk 


from tkinter import messagebox as MessageBox

('-----------------------------------------------------------------------------') 
search_list = list()
e = ""
def search_words():
    
    global search_list
    global e
    text_widget_name1.focus_set()
    #text_widget_name2.focus_set()
    
    
    e = entry_widget_name2.get()
   

    if e:
        if search_list == []:
            idx = "1.0"
        else:
            idx = search_list[-1]

        idx = text_widget_name2.search(e, idx, nocase=1, stopindex=END)
        
        lastidx = '%s+%dc' % (idx, len(e))

        try:
            text_widget_name2.tag_remove(SEL, 1.0,lastidx)
            text_widget_name1.tag_remove(SEL, 1.0,lastidx)
        except:
            pass

        try:
            text_widget_name2.tag_add(SEL, idx, lastidx)
            counter_list = []
            counter_list = str(idx).split('.')      
            text_widget_name2.mark_set("insert", "%d.%d" % (float(int(counter_list[0])), float(int(counter_list[1]))))
            text_widget_name2.see(float(int(counter_list[0])))
            search_list.append(lastidx)
            text_widget_name1.tag_add(SEL, idx, lastidx)
            counter_list = []
            counter_list = str(idx).split('.')      
            text_widget_name1.mark_set("insert", "%d.%d" % (float(int(counter_list[0])), float(int(counter_list[1]))))
            text_widget_name1.see(float(int(counter_list[0])))
            search_list.append(lastidx)
            
             
          


        except:
            MessageBox.showinfo("Search complete","in the dictionary out there no matches")
            search_list.clear()
            text_widget_name2.tag_remove(SEL, 1.0,"end-1c")
            

def add_en():
    text_widget_name2.insert(END, entry_widget_name2.get())
    entry_widget_name2.delete(0, END) 


def save_en(): 
    fail=open('eng_file.txt','w', encoding='utf-8-sig')   
    fail.write(text_widget_name2.get('1.0', END)) 
    fail.close
            
def read_eng():
    with open('eng_file.txt', 'r') as file:
        lst = file.readlines()
    for item in lst:
        text_widget_name2.insert(END, item)
root = Tk()
root.geometry("500x600")
root.title('Idi') 

lbl_frame_entry2 = LabelFrame(root, text="Enter the idiom to search", padx=5, pady=5)
lbl_frame_entry2.pack(padx=10, pady=5, fill="both")

entry_widget_name2 = Entry(lbl_frame_entry2, width=50, justify = "left")
entry_widget_name2.pack(fill="both")

lbl_frame_text2 = LabelFrame(root, text="English", padx=5, pady=5, height=100)
lbl_frame_text2.pack(padx=10, pady=5, fill="both", expand=True)

text_widget_name2 = Text(lbl_frame_text2)
text_widget_name2.pack(fill="both", expand=True)


scrollbar = Scrollbar(text_widget_name2, orient="vertical", command=text_widget_name2.yview, cursor="arrow")
scrollbar.pack(fill="y", side="right")
text_widget_name2.config(yscrollcommand=scrollbar.set)


button_name = Button(root, text="Search", command=search_words)
button_name.pack(fill=X)
button_name=Button(root, text='Read', command=read_eng)
button_name.pack(fill=X)
button_name=Button(root, text='add en', command=add_en)
button_name.pack(fill=X) 
button_name=Button(root, text='save en', command=save_en)
button_name.pack(fill=X)


('-------------------------------------------------------------------------------')
('--------------------------------------------------------------------------------') 
search_list = list()
s = ""



def search_word():
    
    global search_list
    global s
    #text_widget_name1.focus_set()
    text_widget_name2.focus_set()
    s = entry_widget_name1.get()

    if s:
        if search_list == []:
            idx = "1.0"
        else:
            idx = search_list[-1]

        idx = text_widget_name1.search(s, idx, nocase=1, stopindex=END)
        lastidx = '%s+%dc' % (idx, len(s))

        try:
            text_widget_name1.tag_remove(SEL, 1.0,lastidx)
        except:
            pass

        try:
            text_widget_name1.tag_add(SEL, idx, lastidx)
            counter_list = []
            counter_list = str(idx).split('.')      
            text_widget_name1.mark_set("insert", "%d.%d" % (float(int(counter_list[0])), float(int(counter_list[1]))))
            text_widget_name1.see(float(int(counter_list[0])))
            search_list.append(lastidx)
            text_widget_name2.tag_add(SEL, idx, lastidx)
            counter_list = []
            counter_list = str(idx).split('.')      
            text_widget_name2.mark_set("insert", "%d.%d" % (float(int(counter_list[0])), float(int(counter_list[1]))))
            text_widget_name2.see(float(int(counter_list[0])))
            search_list.append(lastidx)
        except:
            MessageBox.showinfo("Search complete","in the dictionary out there no matches")
            search_list.clear()
            text_widget_name1.tag_remove(SEL, 1.0,"end-1c")
def add_rus():
    text_widget_name1.insert(END, entry_widget_name1.get())
    entry_widget_name1.delete(0, END)

def save_ru(): 
    f=open('rus_file.txt','w', encoding='utf-8-sig')   
    f.write(text_widget_name1.get('1.0', END)) 
    f.close
    
def read_ru():
    with open('rus_file.txt', 'r', encoding='utf-8-sig') as file:
        lst = file.readlines()
    for item in lst:
        text_widget_name1.insert(END, item)

#def quiz():

## Open the files

#    with open('eng_file.txt') as f:
#        eng = f.readlines()
#        with open('rus_file.txt', encoding='utf-8-sig') as f:
#            russian = f.readlines()

#            # Create the quiz
#            score = 0
            
#            for i in range(5):
                
#            # Get the word
#                word = eng[i].strip()
#                # Ask the question
#                answer = input(f'What is the word "{word}" in Russian?: ')
#                # Check the answer
#                if answer == russian[i].strip():
#                    score += 1
#                    print('Correct!')
#                else:
#                    print('Incorrect!')

#                # Print the result
#                print(f'You scored {score}') 
#score = 0
#i=0
#def quiz():
#    with open('eng_file.txt') as f:
#        eng = f.readlines()
#        with open('rus_file.txt', encoding='utf-8-sig') as f:
#            russian = f.readlines()

#        def check_answer(entry):  
#            global score
#            answer = entry.get()  
#            if  answer == russian[i].strip(): 
#                score += 1
#                print('Correct!')
#            else:
#                print('Incorrect!')
#                entry.destroy()
#            if i < 4:
#                ask_question()
#            else:
#                print(f'You scored {score}')

#        def ask_question():
#            global i
#            i += 1
#            word = eng[i].strip()
#            label = Label(root, text=f'What is the word "{word}" in Russian?: ')
#            label.pack()
#            entry = Entry(root)
#            entry.pack()
#            button = Button(root, text='Submit', command=lambda: check_answer(entry))
#            button.pack()

#    i = -1
#    ask_question()

import random

score = 0
i = 0

def quiz():
    with open('eng_file.txt') as f:
        eng = f.readlines()
        with open('rus_file.txt', encoding='utf-8-sig') as f:
            russian = f.readlines() 
        def check_answer(entry): 
                global score 
                answer = entry.get() 
                if answer == russian[i].strip(): 
                    score += 1 
                    print('Correct!')
                else: 
                    print('Incorrect!') 
                    entry.destroy()
                if i < 4: 
                    ask_question()
                else: 
                    print(f'You scored {score}')

        def ask_question(): 
            global i  
            i += 1  
            word = eng[i].strip()
            label = Label(root, text=f'What is the word "{word}" in Russian?: ')
            label.pack()
            entry = Entry(root)
            entry.pack()
            button = Button(root, text='Submit', command=lambda: check_answer(entry))
            button.pack()



# Generate 5 random idioms
        random_idioms = random.sample(eng, 5)

        for idiom in random_idioms:
            i = eng.index(idiom)
            ask_question()







lbl_frame_entry1 = LabelFrame(root, text="Enter the idiom to search", padx=5, pady=5)
lbl_frame_entry1.pack(padx=10, pady=5, fill="both")

entry_widget_name1 = Entry(lbl_frame_entry1, width=50, justify = "left")
entry_widget_name1.pack(fill="both")

lbl_frame_text1 = LabelFrame(root, text="Russian", padx=5, pady=5, height=50)
lbl_frame_text1.pack(padx=10, pady=5, fill="both", expand=True)

text_widget_name1 = Text(lbl_frame_text1)
text_widget_name1.pack(fill="both", expand=True)

scrollbar = Scrollbar(text_widget_name1, orient="vertical", command=text_widget_name1.yview, cursor="arrow")
scrollbar.pack(fill="y", side="right")
text_widget_name1.config(yscrollcommand=scrollbar.set)

button_name1 = Button(root, text="Search", command=search_word)
button_name1.pack(fill=X)
button_name1=Button(root, text='Read', command=read_ru)
button_name1.pack(fill=X)
button_name1=Button(root, text='add ru', command=add_rus)
button_name1.pack(fill=X)  
button_name1=Button(root, text='save ru', command=save_ru)
button_name1.pack(fill=X) 
#button = Button(root, text='Start Quiz', command=quiz)
#button.pack(fill=X)
quiz_button = Button(root, text='Start quiz', command=quiz)
quiz_button.pack(fill=X)



root.mainloop()
