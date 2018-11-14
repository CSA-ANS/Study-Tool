'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Ammaar Siddiqui
Quizlet Program
Version 1.1
This is my Quizlet clone
You can create, edit, test, and review study sets.
'''

# Ammaar Siddiqui
# Advanced Computer Programming
# 10/16/18

from tkinter import *
from tkinter import ttk
import textwrap


class App():
    def __init__(self, root, *args):
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=self.close_window)
        menubar.add_cascade(label="File", menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.about_top)
        menubar.add_cascade(label="Help", menu=helpmenu)
        root.config(menu=menubar)  # Makes menu with all menubars and seperators, also configs it to the root

        root.protocol("WM_DELETE_WINDOW", self.close_window)  # runs a confirm close when they try and exit the window

        content = Frame(root)
        self.create = Button(content, text="Create New Set", command=self.new_title)
        self.label1 = Label(content)
        self.view = Button(content, text="View Previous Sets", command=self.view_previous)
        self.label2 = Label(content)
        self.edit = Button(content, text="Edit Previous Sets", command=self.edit_previous)
        self.label3 = Label(content)
        self.confirm = Label(content, text="")

        content.grid(column=0, row=0)
        self.create.grid(column=0, row=0)
        self.label1.grid(column=0, row=1)
        self.view.grid(column=0, row=2)
        self.label2.grid(column=0, row=3)
        self.edit.grid(column=0, row=4)
        self.label3.grid(column=0, row=5)
        self.confirm.grid(column=0, row=6)

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)#Makes main menu with all buttons

    def new_title(self):
        try:
            self.top_create.destroy()
        except:
            pass
        try:
            self.add_term_top.destroy()
        except:
            pass
        try:
            self.top_view.destroy()
        except:
            pass
        try:
            self.choose_title_view.destroy()
        except:
            pass
        try:
            self.choose_term_view.destroy()
        except:
            pass
        try:
            self.view_def_top.destroy()
        except:
            pass
        try:
            self.choose_title_test.destroy()
        except:
            pass
        try:
            self.test_q.destroy()
        except:
            pass
        try:
            self.score_view.destroy()
        except:
            pass
        try:
            self.top_edit.destroy()
        except:
            pass
        try:
            self.confirm_erase.destroy()
        except:
            pass
        try:
            self.choose_title.destroy()
        except:
            pass
        try:
            self.append_term_top.destroy()
        except:
            pass
        try:
            self.choose_def_change.destroy()
        except:
            pass
        try:
            self.new_def_top.destroy()
        except:
            pass
        try:
            self.choose_term_change.destroy()
        except:
            pass
        try:
            self.new_term_top.destroy()
        except:
            pass
        try:
            self.choose_title.destroy()
        except:
            pass
        try:
            self.choose_term_delete.destroy()
        except:
            pass
        try:
            self.confirm_top.destroy()
        except:
            pass#closes all other windows
        global all_defs
        global all_terms
        all_terms = []
        all_defs = []
        global terms_amount
        terms_amount = 0
        self.top_create = Toplevel(root)
        self.top_create.resizable(width=False, height=False)
        self.top_create.title("Create New Sets")
        self.top_create.geometry("300x300+20+20")
        self.title_label = Label(self.top_create, text="Title:")
        self.title_label.pack()
        self.title = Entry(self.top_create, textvariable=title_str)
        self.title.pack()
        self.title.delete(0, END)
        self.title.insert(0, "")
        self.spacer = Label(self.top_create)
        self.spacer.pack()
        self.submit = Button(self.top_create, text="Create", command=self.submit_title)
        self.submit.pack()
        self.spacer2 = Label(self.top_create)
        self.spacer2.pack()
        self.warning_label = Label(self.top_create, text="")
        self.warning_label.pack()#asks for title
        
    def submit_title(self):
        test = True
        for x in title_str.get().lower():
            if x != " ":
                test = False
        file1 = open("titles.txt", "r")
        all_titles = file1.readlines()
        all_titles = [x.replace('\n', '') for x in all_titles]
        if title_str.get().lower() in all_titles:
            self.warning_label.config(text="Title Already Exists")
        elif title_str.get().lower() == "":
            self.warning_label.config(text="Please type a title")
        elif test:
            self.warning_label.config(text="Please type a title")
        elif len(title_str.get().lower()) > 100:
            self.warning_label.config(text="Title is too long")
        else:
            self.top_create.destroy()
            file2 = open("titles.txt", "a")
            file2.write(title_str.get().lower() + "\n")
            file2.close()
            self.add_term()
        file1.close()#adds title to file

    def add_term(self):
        self.add_term_top = Toplevel(root)
        self.add_term_top.resizable(width=False, height=False)
        self.add_term_top.title("Add Term")
        self.add_term_top.geometry("300x300+20+20")
        self.term_label = Label(self.add_term_top, text="Term:")
        self.term_label.pack()
        self.term = Entry(self.add_term_top, textvariable=term_str)
        self.term.pack()
        self.spacer = Label(self.add_term_top)
        self.spacer.pack()
        self.term.delete(0, END)
        self.term.insert(0, "")
        self.def_label = Label(self.add_term_top, text="Definition:")
        self.def_label.pack()
        self.definition = Entry(self.add_term_top, textvariable=def_str)
        self.definition.pack()
        self.definition.delete(0, END)
        self.definition.insert(0, "")
        self.spacer3 = Label(self.add_term_top)
        self.spacer3.pack()
        self.submit2 = Button(self.add_term_top, text="Add Term", command=self.save_termdef)
        self.submit2.pack()
        self.spacer4 = Label(self.add_term_top)
        self.spacer4.pack()
        self.done = Button(self.add_term_top, text="Create Set", command=self.done_set)
        self.done.pack()
        self.spacer5 = Label(self.add_term_top)
        self.spacer5.pack()
        self.warning_label2 = Label(self.add_term_top, text="")
        self.warning_label2.pack()
        self.add_term_top.protocol("WM_DELETE_WINDOW", self.close_term_window)#asks for term and definition, then asks whether they wpuld like to save the term and def or save the whol set

    def close_term_window(self):
        confirm = Toplevel(self.add_term_top)
        confirm.resizable(width=False, height=False)
        confirm.title("Confirm Close")
        confirm.geometry("300x100+20+20")
        confirm.resizable(width=False, height=False)
        explain_label = Label(confirm, text="Are you sure you want to exit" + "\n" + "Your set will not be saved")
        explain_label.pack()
        spacer_label2 = Label(confirm, text="")
        spacer_label2.pack()
        button_frame = Frame(confirm)
        button_frame.pack()
        yes = Button(button_frame, text="Yes", command=self.add_term_top.destroy)
        yes.pack(side=LEFT)
        spacer_label3 = Label(button_frame, text="")
        spacer_label3.pack(side=LEFT)
        no = Button(button_frame, text="No", command=confirm.destroy)
        no.pack(side=LEFT)
        file = open("titles.txt", "r")
        all_titles = file.readlines()
        file.close()
        file = open("titles.txt", "w")
        all_titles.pop(-1)
        for x in all_titles:
            x.replace("\n", "")
            file.write(x + "\n")
        file.close()#asks to make sure they want to close it

    def save_termdef(self):
        global terms_amount
        test1 = True
        for x in term_str.get().lower():
            if x != " ":
                test1 = False
        test2 = True
        for x in def_str.get().lower():
            if x != " ":
                test2 = False
        if term_str.get().lower() in all_terms:
            self.warning_label2.config(text="Term Already Exists")
        elif term_str.get().lower() == "":
            self.warning_label2.config(text="Please Enter Term")
        elif test1:
            self.warning_label2.config(text="Please Enter Term")
        elif "|" in term_str.get():
            self.warning_label2.config(text="Term cannot have | symbol")
        elif len(term_str.get().lower()) > 25:
            self.warning_label2.config(text="Term is too long")
        elif def_str.get().lower() == "":
            self.warning_label2.config(text="Please Enter Definition")
        elif test2:
            self.warning_label2.config(text="Please Enter Definition")
        elif "|" in def_str.get():
            self.warning_label2.config(text="Cannot have | symbol in definition")
        elif len(def_str.get().lower()) > 250:
            self.warning_label2.config(text="Definition is too long")
        else:
            all_terms.append(term_str.get().lower())
            all_defs.append(def_str.get().lower())
            terms_file = open("terms.txt", "a")
            defs_file = open("definitions.txt", "a")
            term_str.set(term_str.get().replace("\n", ""))
            def_str.set(def_str.get().replace("\n", ""))
            terms_file.write(term_str.get().lower() + "|")
            defs_file.write(def_str.get().lower() + "|")
            self.add_term_top.destroy()
            self.add_term()
            terms_file.close()
            defs_file.close()
            terms_amount += 1#checks to make sure no errors in the entry

    def done_set(self):
        if terms_amount == 0:
            self.warning_label2.config(text="Please enter at least one" + "\n" + "Before saving the whole set")
        else:
            terms_file = open("terms.txt", "a")
            defs_file = open("definitions.txt", "a")
            terms_file.write("\n")
            defs_file.write("\n")
            self.add_term_top.destroy()
            self.confirm.config(text="Set Successfully Saved")#adds everything

    def view_previous(self):
        try:
            self.top_create.destroy()
        except:
            pass
        try:
            self.add_term_top.destroy()
        except:
            pass
        try:
            self.top_view.destroy()
        except:
            pass
        try:
            self.choose_title_view.destroy()
        except:
            pass
        try:
            self.choose_term_view.destroy()
        except:
            pass
        try:
            self.view_def_top.destroy()
        except:
            pass
        try:
            self.choose_title_test.destroy()
        except:
            pass
        try:
            self.test_q.destroy()
        except:
            pass
        try:
            self.score_view.destroy()
        except:
            pass
        try:
            self.top_edit.destroy()
        except:
            pass
        try:
            self.confirm_erase.destroy()
        except:
            pass
        try:
            self.choose_title.destroy()
        except:
            pass
        try:
            self.append_term_top.destroy()
        except:
            pass
        try:
            self.choose_def_change.destroy()
        except:
            pass
        try:
            self.new_def_top.destroy()
        except:
            pass
        try:
            self.choose_term_change.destroy()
        except:
            pass
        try:
            self.new_term_top.destroy()
        except:
            pass
        try:
            self.choose_title.destroy()
        except:
            pass
        try:
            self.choose_term_delete.destroy()
        except:
            pass
        try:
            self.confirm_top.destroy()
        except:
            pass#closes all other toplevels
        self.top_view = Toplevel(root)
        self.top_view.resizable(width=False, height=False)
        self.top_view.title("View Previous Sets")
        self.top_view.geometry("300x300+20+20")
        file = open("titles.txt", "r")
        all_titles = file.readlines()
        if all_titles == []:
            no_title = Label(self.top_view, text="No Sets created")
            no_title.pack()
        else:
            self.view_label = Label(self.top_view, text="What would you like to do? ")
            self.view_label.pack()
            self.spacer1 = Label(self.top_view)
            self.spacer1.pack()
            self.view_button = Button(self.top_view, text="View Sets", command=self.title_choose_view)
            self.view_button.pack()
            self.spacer = Label(self.top_view)
            self.spacer.pack()
            self.test_button = Button(self.top_view, text="Test Yourself", command=self.title_choose_test)
            self.test_button.pack()#options for viewing sets

    def title_choose_view(self):
        self.top_view.destroy()
        self.choose_title_view = Toplevel(root)
        self.choose_title_view.resizable(width=False, height=False)
        self.choose_title_view.title("Choose set to view")
        self.choose_title_view.geometry("300x300+20+20")
        content = Frame(self.choose_title_view)
        self.title_label = Label(content, text="Please choose a set")
        self.title_lbox = Listbox(content, height=10, exportselection=FALSE)
        file = open("titles.txt", "r")
        all_titles = file.readlines()
        for c in all_titles:
            self.title_lbox.insert(END, c)
        self.scroll = ttk.Scrollbar(content, orient=VERTICAL, command=self.title_lbox.yview)
        self.title_lbox.configure(yscrollcommand=self.scroll.set)
        self.choose = Button(content, text="Choose", command=self.view_sets)
        self.warning_label = Label(content, text="")
        content.grid(column=0, row=0)
        self.title_label.grid(column=0, row=0)
        self.title_lbox.grid(column=0, row=1)
        self.scroll.grid(column=1, row=1, sticky='ns')
        self.choose.grid(column=0, row=2)
        self.warning_label.grid(column=0, row=3)
        self.choose_title_view.columnconfigure(0, weight=1)
        self.choose_title_view.rowconfigure(0, weight=1)
        file.close()#choose title

    def view_sets(self):
        title_view = [self.title_lbox.get(idx) for idx in self.title_lbox.curselection()]
        if title_view == []:
            self.warning_label.config(text="No value selected")
        else:
            self.choose_title_view.destroy()
            index = 0
            file = open("titles.txt")
            all_titles = file.readlines()
            index = all_titles.index(title_view[0])
            file.close()
            file1 = open("terms.txt", "r")
            all_terms = file1.readlines()
            view_terms = all_terms[index]
            file1.close()
            file2 = open("definitions.txt", "r")
            all_defs = file2.readlines()
            view_defs = all_defs[index]
            file2.close()
            view_terms = view_terms.split("|")
            view_defs = view_defs.split("|")
            del view_defs[-1]
            del view_terms[-1]
            title = title_view[0]
            self.choose_term_view = Toplevel(root)
            self.choose_term_view.resizable(width=False, height=False)
            self.choose_term_view.title("Choosing term to view")
            self.choose_term_view.geometry("300x300+20+20")
            content = Frame(self.choose_term_view)
            self.term_label = Label(content, text="Please choose the term's definition you want to view")
            self.term_lbox = Listbox(content, height=10, exportselection=FALSE)
            for c in view_terms:
                self.term_lbox.insert(END, c)
            self.scroll = ttk.Scrollbar(content, orient=VERTICAL, command=self.term_lbox.yview)
            self.term_lbox.configure(yscrollcommand=self.scroll.set)
            self.choose2 = Button(content, text="Choose", command=lambda: self.view_def(title, view_defs, view_terms))
            self.warning_label2 = Label(content, text="")
            content.grid(column=0, row=0)
            self.term_label.grid(column=0, row=0)
            self.term_lbox.grid(column=0, row=1)
            self.scroll.grid(column=0, row=1, sticky='ns', padx=(110, 0))
            self.choose2.grid(column=0, row=2)
            self.warning_label2.grid(column=0, row=3)
            self.choose_term_view.columnconfigure(0, weight=1)
            self.choose_term_view.rowconfigure(0, weight=1)#asks for what definitions they would like to view

    def view_def(self, title, view_defs, view_terms):
        try:
            self.view_def_top.destroy()
        except:
            pass
        index = 0
        term = [self.term_lbox.get(idx) for idx in self.term_lbox.curselection()]
        if term == []:
            self.warning_label2.config(text="No value selected")
        else:
            index = view_terms.index(term[0])
            def_to_show = view_defs[index]
            self.view_def_top = Toplevel(root)
            self.view_def_top.resizable(width=False, height=False)
            self.view_def_top.title(title)
            self.view_def_top.geometry("300x200+20+20")
            self.term_label = Label(self.view_def_top, text="Term:" + "\n" + term[0])
            self.term_label.pack()
            self.spacer = Label(self.view_def_top)
            self.spacer.pack()
            self.def_label = Label(self.view_def_top, text="Definition: " + "\n" + textwrap.fill(def_to_show, 40))
            self.def_label.pack()
            self.spacer2 = Label(self.view_def_top)
            self.spacer2.pack()#shows them definition

    def title_choose_test(self):
        self.top_view.destroy()
        self.choose_title_test = Toplevel(root)
        self.choose_title_test.resizable(width=False, height=False)
        self.choose_title_test.title("Choose set to test")
        self.choose_title_test.geometry("300x300+20+20")
        content = Frame(self.choose_title_test)
        self.title_label = Label(content, text="Please choose a set")
        self.title_lbox = Listbox(content, height=10, exportselection=FALSE)
        file = open("titles.txt", "r")
        all_titles = file.readlines()
        for c in all_titles:
            self.title_lbox.insert(END, c)
        self.scroll = ttk.Scrollbar(content, orient=VERTICAL, command=self.title_lbox.yview)
        self.title_lbox.configure(yscrollcommand=self.scroll.set)
        self.choose = Button(content, text="Choose", command=self.test)
        self.warning_label = Label(content, text="")
        content.grid(column=0, row=0)
        self.title_label.grid(column=0, row=0)
        self.title_lbox.grid(column=0, row=1)
        self.scroll.grid(column=1, row=1, sticky='ns')
        self.choose.grid(column=0, row=2)
        self.warning_label.grid(column=0, row=3)
        self.choose_title_test.columnconfigure(0, weight=1)
        self.choose_title_test.rowconfigure(0, weight=1)
        file.close()#choose title

    def test(self):
        title_test = [self.title_lbox.get(idx) for idx in self.title_lbox.curselection()]
        if title_test == []:
            self.warning_label.config(text="No value selected")
        else:
            self.choose_title_test.destroy()
            file = open("titles.txt", "r")
            all_titles = file.readlines()
            index = 0
            index = all_titles.index(title_test[0])
            file.close()
            file1 = open("terms.txt", "r")
            all_terms = file1.readlines()
            file1.close()
            file2 = open("definitions.txt", "r")
            all_defs = file2.readlines()
            file2.close()
            test_terms = all_terms[index]
            test_defs = all_defs[index]
            test_defs = test_defs.split("|")
            test_terms = test_terms.split("|")
            del test_terms[-1]
            del test_defs[-1]
            answer_terms = []
            amount = len(test_terms)
            done = 0
            self.test_start(test_terms, test_defs, answer_terms, done, amount)#gathers all testing materials

    def test_start(self, test_terms, test_defs, answer_terms, done, amount):
        if amount == done:
            self.score(test_terms, answer_terms)
        else:
            answer_term.set("")
            self.test_q = Toplevel(root)
            self.test_q.resizable(width=False, height=False)
            self.test_q.title("Question " + str(done + 1))
            self.test_q.geometry("350x300+20+20")
            self.def_label_test = Label(self.test_q, text="Definition:" + "\n" + textwrap.fill(test_defs[done], 40))
            self.def_label_test.pack()
            self.spacer1 = Label(self.test_q)
            self.spacer1.pack()
            self.term_label = Label(self.test_q, text="Term:")
            self.term_label.pack()
            self.term_entry = Entry(self.test_q, textvariable=answer_term)
            self.term_entry.pack()
            self.spacer2 = Label(self.test_q)
            self.spacer2.pack()
            self.enter = Button(self.test_q, text="Submit",
                                command=lambda: self.check_answer(test_terms, test_defs, answer_terms, done, amount))
            self.enter.pack()#test question

    def check_answer(self, test_terms, test_defs, answer_terms, done, amount):
        done += 1
        self.test_q.destroy()
        answer_terms.append(answer_term.get())
        self.test_start(test_terms, test_defs, answer_terms, done, amount)#checks whether it is right or not

    def score(self, test_terms, answer_terms):#tells them their score
        score = 0
        outof = len(test_terms)
        for x in range(outof):
            if test_terms[x - 1].lower() == answer_terms[x - 1].lower():
                score += 1
        self.score_view = Toplevel(root)
        self.score_view.resizable(width=False, height=False)
        self.score_view.title("Score")
        self.score_view.geometry("200x200+20+20")
        self.score_label = Label(self.score_view, text="You got " + str(score) + " out of " + str(outof) + " correct")
        self.score_label.pack()
        self.score_percent = Label(self.score_view, text=str(int(score / outof * 100)) + "%")
        self.score_percent.pack()

    def edit_previous(self):
        try:
            self.top_create.destroy()
        except:
            pass
        try:
            self.add_term_top.destroy()
        except:
            pass
        try:
            self.top_view.destroy()
        except:
            pass
        try:
            self.choose_title_view.destroy()
        except:
            pass
        try:
            self.choose_term_view.destroy()
        except:
            pass
        try:
            self.view_def_top.destroy()
        except:
            pass
        try:
            self.choose_title_test.destroy()
        except:
            pass
        try:
            self.test_q.destroy()
        except:
            pass
        try:
            self.score_view.destroy()
        except:
            pass
        try:
            self.top_edit.destroy()
        except:
            pass
        try:
            self.confirm_erase.destroy()
        except:
            pass
        try:
            self.choose_title.destroy()
        except:
            pass
        try:
            self.append_term_top.destroy()
        except:
            pass
        try:
            self.choose_def_change.destroy()
        except:
            pass
        try:
            self.new_def_top.destroy()
        except:
            pass
        try:
            self.choose_term_change.destroy()
        except:
            pass
        try:
            self.new_term_top.destroy()
        except:
            pass
        try:
            self.choose_title.destroy()
        except:
            pass
        try:
            self.choose_term_delete.destroy()
        except:
            pass
        try:
            self.confirm_top.destroy()
        except:
            pass#closes all previous toplevels
        self.top_edit = Toplevel(root)
        self.top_edit.resizable(width=False, height=False)
        self.top_edit.geometry("300x350+20+20")
        self.top_edit.title("Edit Sets")
        file = open("titles.txt", "r")
        all_titles = file.readlines()
        if all_titles == []:
            no_title = Label(self.top_edit, text="No Sets created")
            no_title.pack()
        else:
            self.choice = Label(self.top_edit, text="What would you like to do?")
            self.choice.pack()
            self.sep1 = Label(self.top_edit)
            self.sep1.pack()
            self.delete_set_b = Button(self.top_edit, text="Delete Set", command=self.title_choose_delete)
            self.delete_set_b.pack()
            self.sep2 = Label(self.top_edit)
            self.sep2.pack()
            self.delete_term_b = Button(self.top_edit, text="Delete Term", command=self.title_choose_term_delete)
            self.delete_term_b.pack()
            self.sep3 = Label(self.top_edit)
            self.sep3.pack()
            self.change_term_b = Button(self.top_edit, text="Change Term", command=self.title_choose_term_change)
            self.change_term_b.pack()
            self.sep4 = Label(self.top_edit)
            self.sep4.pack()
            self.change_def_b = Button(self.top_edit, text="Change Definition", command=self.title_choose_def_change)
            self.change_def_b.pack()
            self.sep5 = Label(self.top_edit)
            self.sep5.pack()
            self.add_term_b = Button(self.top_edit, text="Add Term", command=self.title_choose_term_add)
            self.add_term_b.pack()
            self.sep6 = Label(self.top_edit)
            self.sep6.pack()
            self.erase_all_b = Button(self.top_edit, text="Erase All", command=self.erase_all_check)
            self.erase_all_b.pack()
            self.confirm_label = Label(self.top_edit)
            self.confirm_label.pack()
        file.close()

    def erase_all_check(self):
        self.top_edit.destroy()
        self.confirm_erase = Toplevel(root)
        self.confirm_erase.resizable(width=False, height=False)
        self.confirm_erase.title("Confirm Erase")
        self.confirm_erase.geometry("300x100+20+20")
        self.confirm_erase.resizable(width=False, height=False)
        self.explain_label = Label(self.confirm_erase, text="Are you sure you want to erase everything")
        self.explain_label.pack()
        self.spacer_label2 = Label(self.confirm_erase, text="")
        self.spacer_label2.pack()
        button_frame = Frame(self.confirm_erase)
        button_frame.pack()
        self.yes = Button(button_frame, text="Yes", command=self.erase_all)
        self.yes.pack(side=LEFT)
        self.spacer_label3 = Label(button_frame, text="")
        self.spacer_label3.pack(side=LEFT)
        self.no = Button(button_frame, text="No", command=self.confirm_erase.destroy)
        self.no.pack(side=LEFT)

    def erase_all(self):
        open("titles.txt", "w").close()
        open("terms.txt", "w").close()
        open("definitions.txt", "w").close()
        self.confirm_erase.destroy()
        self.top_edit.destroy()
        self.confirm.config(text="Everything Erased")#erase all

    def title_choose_term_add(self):
        self.top_edit.destroy()
        self.choose_title = Toplevel(root)
        self.choose_title.resizable(width=False, height=False)
        self.choose_title.title("Choose set to add term")
        self.choose_title.geometry("300x300+20+20")
        content = Frame(self.choose_title)
        self.title_label = Label(content, text="Please choose a set")
        self.title_lbox = Listbox(content, height=10, exportselection=FALSE)
        file = open("titles.txt", "r")
        all_titles = file.readlines()
        for c in all_titles:
            self.title_lbox.insert(END, c)
        self.scroll = ttk.Scrollbar(content, orient=VERTICAL, command=self.title_lbox.yview)
        self.title_lbox.configure(yscrollcommand=self.scroll.set)
        self.choose = Button(content, text="Choose", command=self.type_term_add)
        self.warning_label = Label(content, text="")
        content.grid(column=0, row=0)
        self.title_label.grid(column=0, row=0)
        self.title_lbox.grid(column=0, row=1)
        self.scroll.grid(column=1, row=1, sticky='ns')
        self.choose.grid(column=0, row=2)
        self.warning_label.grid(column=0, row=3)
        self.choose_title.columnconfigure(0, weight=1)
        self.choose_title.rowconfigure(0, weight=1)
        file.close()

    def type_term_add(self):
        append_title = [self.title_lbox.get(idx) for idx in self.title_lbox.curselection()]
        if append_title == []:
            self.warning_label.config(text="No value selected")
        else:
            title = append_title[0]
            append_term.set("")
            append_def.set("")
            self.choose_title.destroy()
            self.append_term_top = Toplevel(root)
            self.append_term_top.resizable(width=False, height=False)
            self.append_term_top.title("Add Term and Definition")
            self.append_term_top.geometry("300x300+20+20")
            self.term_label = Label(self.append_term_top, text="Term:")
            self.term_label.pack()
            self.term_entry = Entry(self.append_term_top, textvariable=append_term)
            self.term_entry.pack()
            self.spacer = Label(self.append_term_top)
            self.spacer.pack()
            self.def_label = Label(self.append_term_top, text="Definition")
            self.def_label.pack()
            self.def_entry = Entry(self.append_term_top, textvariable=append_def)
            self.def_entry.pack()
            self.spacer2 = Label(self.append_term_top)
            self.spacer2.pack()
            self.add_term_b = Button(self.append_term_top, text="Add", command=lambda: self.check_append_term(title))
            self.add_term_b.pack()
            self.spacer3 = Label(self.append_term_top)
            self.spacer3.pack()
            self.warning_label = Label(self.append_term_top, text="")
            self.warning_label.pack()

    def check_append_term(self, title):
        index = 0
        file = open("titles.txt", "r")
        all_titles = file.readlines()
        file.close()
        index = all_titles.index(title)
        file1 = open("terms.txt", "r")
        all_terms = file1.readlines()
        append_terms = all_terms[index]
        file1.close()
        file2 = open("definitions.txt", "r")
        all_defs = file2.readlines()
        append_defs = all_defs[index]
        file2.close()
        append_terms_split = append_terms.split("|")
        append_defs_split = append_defs.split("|")
        test1 = True
        test2 = True
        for x in append_term.get():
            if x != " ":
                test1 = False
        for x in append_def.get():
            if x != " ":
                test2 = False
        if append_term.get().lower() in append_terms_split:
            self.warning_label.config(text="Term already exists")
        elif append_term.get() == "":
            self.warning_label.config(text="Please enter term")
        elif test1:
            self.warning_label.config(text="Please enter term")
        elif "|" in append_term.get():
            self.warning_label.config(text="Cannot have | symbol in term")
        elif len(append_term.get()) > 25:
            self.warning_label.config(text="Term is too long")
        elif append_def.get() == "":
            self.warning_label.config(text="Please enter definition")
        elif test2:
            self.warning_label.config(text="Please enter definition")
        elif "|" in append_def.get():
            self.warning_label.config(text="Cannot have | symbol in definition")
        elif len(append_def.get()) > 250:
            self.warning_label.config(text="Definition is too long")
        else:
            file = open("titles.txt", "r")
            all_titles = file.readlines()
            file.close()
            file1 = open("titles.txt", "r")
            all_lines = file1.readlines()
            file1.close()
            file2 = open("titles.txt", "w")
            for line in all_lines:
                if line != title:
                    file2.write(line)
            file2.close()
            file3 = open("terms.txt", "r")
            all_terms_lines = file3.readlines()
            file3.close()
            file4 = open("terms.txt", "w")
            for line in all_terms_lines:
                if line != append_terms:
                    file4.write(line)
            file4.close()
            file5 = open("definitions.txt", "r")
            all_defs_lines = file5.readlines()
            file5.close()
            file6 = open("definitions.txt", "w")
            for line in all_defs_lines:
                if line != append_defs:
                    file6.write(line)
            file6.close()
            del append_defs_split[-1]
            del append_terms_split[-1]
            file7 = open("titles.txt", "a")
            file7.write(title)
            file7.close()
            file8 = open("terms.txt", "a")
            for x in append_terms_split:
                file8.write(x + "|")
            file8.write(append_term.get().lower() + "|" + "\n")
            file8.close()
            file9 = open("definitions.txt", "a")
            for x in append_defs_split:
                file9.write(x + "|")
            file9.write(append_def.get() + "|" + "\n")
            file9.close()
            self.confirm.config(text="Term added")
            self.append_term_top.destroy()#adds term

    def title_choose_def_change(self):
        self.top_edit.destroy()
        self.choose_title = Toplevel(root)
        self.choose_title.resizable(width=False, height=False)
        self.choose_title.title("Choose set to change definition")
        self.choose_title.geometry("300x300+20+20")
        content = Frame(self.choose_title)
        self.title_label = Label(content, text="Please choose a set")
        self.title_lbox = Listbox(content, height=10, exportselection=FALSE)
        file = open("titles.txt", "r")
        all_titles = file.readlines()
        for c in all_titles:
            self.title_lbox.insert(END, c)
        self.scroll = ttk.Scrollbar(content, orient=VERTICAL, command=self.title_lbox.yview)
        self.title_lbox.configure(yscrollcommand=self.scroll.set)
        self.choose = Button(content, text="Choose", command=self.change_def)
        self.warning_label = Label(content, text="")
        content.grid(column=0, row=0)
        self.title_label.grid(column=0, row=0)
        self.title_lbox.grid(column=0, row=1)
        self.scroll.grid(column=1, row=1, sticky='ns')
        self.choose.grid(column=0, row=2)
        self.warning_label.grid(column=0, row=3)
        self.choose_title.columnconfigure(0, weight=1)
        self.choose_title.rowconfigure(0, weight=1)
        file.close()

    def change_def(self):
        values = [self.title_lbox.get(idx) for idx in self.title_lbox.curselection()]
        if values == []:
            self.warning_label.config(text="No value selected")
        else:
            index = 0
            file = open("titles.txt", "r")
            lines = file.readlines()
            index = lines.index(values[0])
            file.close()
            file3 = open("definitions.txt", "r")
            all_defs = file3.readlines()
            file3.close()
            file4 = open("terms.txt", "r")
            all_terms = file4.readlines()
            file4.close()
            self.choose_title.destroy()
            change_terms = all_terms[index]
            change_defs = all_defs[index]
            change_terms = change_terms.split("|")
            change_defs = change_defs.split("|")
            del change_defs[-1]
            del change_terms[-1]
            title = values[0]
            self.choose_def_change = Toplevel(root)
            self.choose_def_change.resizable(width=False, height=False)
            self.choose_def_change.title("Choosing definition to change")
            self.choose_def_change.geometry("300x300+20+20")
            content = Frame(self.choose_def_change)
            self.def_label = Label(content, text="Please choose the term's definition you want to change")
            self.def_lbox = Listbox(content, height=10, exportselection=FALSE)
            for c in change_terms:
                self.def_lbox.insert(END, c)
            self.scroll = ttk.Scrollbar(content, orient=VERTICAL, command=self.def_lbox.yview)
            self.def_lbox.configure(yscrollcommand=self.scroll.set)
            self.choose2 = Button(content, text="Choose",
                                  command=lambda: self.change_def_term(change_terms, change_defs, title))
            self.warning_label2 = Label(content, text="")
            content.grid(column=0, row=0)
            self.def_label.grid(column=0, row=0)
            self.def_lbox.grid(column=0, row=1)
            self.scroll.grid(column=0, row=1, sticky='ns', padx=(110,0))
            self.choose2.grid(column=0, row=2)
            self.warning_label2.grid(column=0, row=3)
            self.choose_def_change.columnconfigure(0, weight=1)
            self.choose_def_change.rowconfigure(0, weight=1)
            file.close()

    def change_def_term(self, change_terms, change_defs, title):
        index = 0
        selected_def = [self.def_lbox.get(idx) for idx in self.def_lbox.curselection()]
        if selected_def == []:
            self.warning_label2.config(text="No term selected")
        else:
            index = change_terms.index(selected_def[0])
            old_term = selected_def[0]
            change_terms.remove(selected_def[0])
            self.choose_def_change.destroy()
            self.new_def_top = Toplevel(root)
            self.new_def_top.resizable(width=False, height=False)
            self.new_def_top.title("Change definition to what")
            self.new_def_top.geometry("300x300+20+20")
            self.label = Label(self.new_def_top, text="What would like the new definition to be: ")
            self.label.pack()
            self.sep = Label(self.new_def_top, text="")
            self.sep.pack()
            self.new_def_entry = Entry(self.new_def_top, textvariable=new_def)
            self.new_def_entry.pack()
            self.old_def_label=Label(self.new_def_top, text="Old Definition: "+"\n"+textwrap.fill(change_defs[index], 40))
            self.old_def_label.pack()
            change_defs.remove(change_defs[index])
            self.sep2 = Label(self.new_def_top, text="")
            self.sep2.pack()
            self.changed_button = Button(self.new_def_top, text="Change Definition",
                                         command=lambda: self.change_def_add(change_defs, change_terms, title,
                                                                             old_term))
            self.changed_button.pack()
            self.sep3 = Label(self.new_def_top, text="")
            self.sep3.pack()
            self.warning_label = Label(self.new_def_top, text="")
            self.warning_label.pack()

    def change_def_add(self, change_defs, change_terms, title, old_term):
        test = True
        for x in new_def.get().lower():
            if x != " ":
                test = False
        if new_def.get().lower() == "":
            self.warning_label.config(text="Please enter new definition")
        elif test:
            self.warning_label.config(text="Please enter a new definition")
        elif "|" in new_def.get():
            self.warning_label.config(text="New definition cannot have | symbol")
        elif len(new_def.get().lower()) > 250:
            self.warning_label.config(text="New definition is too long")
        else:
            index = 0
            file = open("titles.txt", "r")
            lines = file.readlines()
            index = lines.index(title)
            file.close()
            file3 = open("definitions.txt", "r")
            all_defs = file3.readlines()
            file3.close()
            file4 = open("terms.txt", "r")
            all_terms = file4.readlines()
            file4.close()
            file3 = open("definitions.txt", "w")
            for line in all_defs:
                if line != all_defs[index]:
                    file3.write(line)
            file3.close()
            file4 = open("terms.txt", "w")
            for line in all_terms:
                if line != all_terms[index]:
                    file4.write(line)
            file4.close()
            file2 = open("titles.txt", "w")
            for line in lines:
                if line != title:
                    file2.write(line)
            self.choose_title.destroy()
            file2.close()
            change_defs.append(new_def.get().lower())
            change_terms.append(old_term.lower())
            file = open("titles.txt", "a")
            file.write(title)
            file.close()
            file = open("definitions.txt", "a")
            for x in change_defs:
                file.write(x + "|")
            file.write("\n")
            file.close()
            file = open("terms.txt", "a")
            for x in change_terms:
                file.write(x + "|")
            file.write("\n")
            file.close()
            self.confirm.config(text="Definition Changed")
            self.new_def_top.destroy()
            self.top_edit.destroy()#changes definition

    def title_choose_term_change(self):
        self.top_edit.destroy()
        self.choose_title = Toplevel(root)
        self.choose_title.resizable(width=False, height=False)
        self.choose_title.title("Choose set to change term")
        self.choose_title.geometry("300x300+20+20")
        content = Frame(self.choose_title)
        self.title_label = Label(content, text="Please choose a set")
        self.title_lbox = Listbox(content, height=10, exportselection=FALSE)
        file = open("titles.txt", "r")
        all_titles = file.readlines()
        for c in all_titles:
            self.title_lbox.insert(END, c)
        self.scroll = ttk.Scrollbar(content, orient=VERTICAL, command=self.title_lbox.yview)
        self.title_lbox.configure(yscrollcommand=self.scroll.set)
        self.choose = Button(content, text="Choose", command=self.change_term)
        self.warning_label = Label(content, text="")
        content.grid(column=0, row=0)
        self.title_label.grid(column=0, row=0)
        self.title_lbox.grid(column=0, row=1)
        self.scroll.grid(column=1, row=1, sticky='ns')
        self.choose.grid(column=0, row=2)
        self.warning_label.grid(column=0, row=3)
        self.choose_title.columnconfigure(0, weight=1)
        self.choose_title.rowconfigure(0, weight=1)
        file.close()

    def change_term(self):
        values = [self.title_lbox.get(idx) for idx in self.title_lbox.curselection()]
        if values == []:
            self.warning_label.config(text="No value selected")
        else:
            index = 0
            file = open("titles.txt", "r")
            lines = file.readlines()
            index = lines.index(values[0])
            file.close()
            file3 = open("definitions.txt", "r")
            all_defs = file3.readlines()
            file3.close()
            file4 = open("terms.txt", "r")
            all_terms = file4.readlines()
            file4.close()
            self.choose_title.destroy()
            change_terms = all_terms[index]
            change_defs = all_defs[index]
            change_terms = change_terms.split("|")
            change_defs = change_defs.split("|")
            del change_defs[-1]
            del change_terms[-1]
            title = values[0]
            self.choose_term_change = Toplevel(root)
            self.choose_term_change.resizable(width=False, height=False)
            self.choose_term_change.title("Choosing term to change")
            self.choose_term_change.geometry("300x300+20+20")
            content = Frame(self.choose_term_change)
            self.term_label = Label(content, text="Please choose a term to change")
            self.terms_lbox = Listbox(content, height=10, exportselection=FALSE)
            for c in change_terms:
                self.terms_lbox.insert(END, c)
            self.scroll = ttk.Scrollbar(content, orient=VERTICAL, command=self.terms_lbox.yview)
            self.terms_lbox.configure(yscrollcommand=self.scroll.set)
            self.choose2 = Button(content, text="Choose",
                                  command=lambda: self.change_term_def(change_terms, change_defs, title))
            self.warning_label2 = Label(content, text="")
            content.grid(column=0, row=0)
            self.term_label.grid(column=0, row=0)
            self.terms_lbox.grid(column=0, row=1)
            self.scroll.grid(column=0, row=1, sticky='ns', padx=(115, 0))
            self.choose2.grid(column=0, row=2)
            self.warning_label2.grid(column=0, row=3)
            self.choose_term_change.columnconfigure(0, weight=1)
            self.choose_term_change.rowconfigure(0, weight=1)
            file.close()

    def change_term_def(self, change_terms, change_defs, title):
        index = 0
        selected_term = [self.terms_lbox.get(idx) for idx in self.terms_lbox.curselection()]
        if selected_term == []:
            self.warning_label2.config(text="No term selected")
        else:
            new_term.set("")
            index = change_terms.index(selected_term[0])
            change_terms.remove(selected_term[0])
            old_def = change_defs[index]
            change_defs.remove(change_defs[index])
            self.choose_term_change.destroy()
            self.new_term_top = Toplevel(root)
            self.new_term_top.resizable(width=False, height=False)
            self.new_term_top.title("Change term to what")
            self.new_term_top.geometry("300x300+20+20")
            self.label = Label(self.new_term_top, text="What would like the new term to be: ")
            self.label.pack()
            self.sep = Label(self.new_term_top, text="")
            self.sep.pack()
            self.new_term_entry = Entry(self.new_term_top, textvariable=new_term)
            self.new_term_entry.pack()
            self.sep2 = Label(self.new_term_top, text="")
            self.sep2.pack()
            self.changet_button = Button(self.new_term_top, text="Change Term",
                                         command=lambda: self.change_term_add(change_defs, change_terms, title,
                                                                              old_def))
            self.changet_button.pack()
            self.sep3 = Label(self.new_term_top, text="")
            self.sep3.pack()
            self.warning_label = Label(self.new_term_top, text="")
            self.warning_label.pack()#changes term

    def change_term_add(self, change_defs, change_terms, title, old_def):
        test = True
        for x in new_term.get().lower():
            if x != " ":
                test = False
        if new_term.get().lower() in change_terms:
            self.warning_label.config(text="Term already exists")
        elif new_term.get().lower() == "":
            self.warning_label.config(text="Please enter new term")
        elif test:
            self.warning_label.config(text="Please enter a new term")
        elif "|" in new_term.get():
            self.warning_label.config(text="New term cannot have | symbol")
        elif len(new_term.get().lower()) > 25:
            self.warning_label.config(text="New term is too long")
        else:
            index = 0
            file = open("titles.txt", "r")
            lines = file.readlines()
            index = lines.index(title)
            file.close()
            file3 = open("definitions.txt", "r")
            all_defs = file3.readlines()
            file3.close()
            file4 = open("terms.txt", "r")
            all_terms = file4.readlines()
            file4.close()
            file3 = open("definitions.txt", "w")
            for line in all_defs:
                if line != all_defs[index]:
                    file3.write(line)
            file3.close()
            file4 = open("terms.txt", "w")
            for line in all_terms:
                if line != all_terms[index]:
                    file4.write(line)
            file4.close()
            file2 = open("titles.txt", "w")
            for line in lines:
                if line != title:
                    file2.write(line)
            file2.close()
            change_terms.append(new_term.get().lower())
            change_defs.append(old_def.lower())
            file = open("titles.txt", "a")
            file.write(title)
            file.close()
            file = open("terms.txt", "a")
            for x in change_terms:
                file.write(x + "|")
            file.write("\n")
            file.close()
            file = open("definitions.txt", "a")
            for x in change_defs:
                file.write(x + "|")
            file.write("\n")
            file.close()
            self.confirm.config(text="Term Changed")
            self.new_term_top.destroy()
            self.top_edit.destroy()

    def title_choose_term_delete(self):
        self.top_edit.destroy()
        self.choose_title = Toplevel(root)
        self.choose_title.resizable(width=False, height=False)
        self.choose_title.title("Choose set to delete term")
        self.choose_title.geometry("300x300+20+20")
        content = Frame(self.choose_title)
        self.title_label = Label(content, text="Please choose a set")
        self.title_lbox = Listbox(content, height=10, exportselection=FALSE)
        file = open("titles.txt", "r")
        all_titles = file.readlines()
        for c in all_titles:
            self.title_lbox.insert(END, c)
        self.scroll = ttk.Scrollbar(content, orient=VERTICAL, command=self.title_lbox.yview)
        self.title_lbox.configure(yscrollcommand=self.scroll.set)
        self.choose = Button(content, text="Choose", command=self.delete_term)
        self.warning_label = Label(content, text="")
        content.grid(column=0, row=0)
        self.title_label.grid(column=0, row=0)
        self.title_lbox.grid(column=0, row=1)
        self.scroll.grid(column=1, row=1, sticky='ns')
        self.choose.grid(column=0, row=2)
        self.warning_label.grid(column=0, row=3)
        self.choose_title.columnconfigure(0, weight=1)
        self.choose_title.rowconfigure(0, weight=1)
        file.close()

    def delete_term(self):
        values = [self.title_lbox.get(idx) for idx in self.title_lbox.curselection()]
        if values == []:
            self.warning_label.config(text="No value selected")
        else:
            index = 0
            file = open("titles.txt", "r")
            lines = file.readlines()
            index = lines.index(values[0])
            file.close()
            file3 = open("definitions.txt", "r")
            all_defs = file3.readlines()
            file3.close()
            file4 = open("terms.txt", "r")
            all_terms = file4.readlines()
            file4.close()
            self.choose_title.destroy()
            delete_terms = all_terms[index]
            delete_defs = all_defs[index]
            delete_terms = delete_terms.split("|")
            delete_defs = delete_defs.split("|")
            del delete_defs[-1]
            del delete_terms[-1]
            title = values[0]
            self.choose_term_delete = Toplevel(root)
            self.choose_term_delete.resizable(width=False, height=False)
            self.choose_term_delete.title("Choosing term to delete")
            self.choose_term_delete.geometry("300x300+20+20")
            content = Frame(self.choose_term_delete)
            self.term_label = Label(content, text="Please choose a term to delete")
            self.terms_lbox = Listbox(content, height=10, exportselection=FALSE)
            for c in delete_terms:
                self.terms_lbox.insert(END, c)
            self.scroll = ttk.Scrollbar(content, orient=VERTICAL, command=self.terms_lbox.yview)
            self.terms_lbox.configure(yscrollcommand=self.scroll.set)
            self.choose2 = Button(content, text="Choose",
                                  command=lambda: self.delete_term_def(delete_terms, delete_defs, title))
            self.warning_label2 = Label(content, text="")
            content.grid(column=0, row=0)
            self.term_label.grid(column=0, row=0)
            self.terms_lbox.grid(column=0, row=1)
            self.scroll.grid(column=0, row=1, sticky='ns', padx=(120, 0))
            self.choose2.grid(column=0, row=2)
            self.warning_label2.grid(column=0, row=3)
            self.choose_term_delete.columnconfigure(0, weight=1)
            self.choose_term_delete.rowconfigure(0, weight=1)
            file.close()

    def delete_term_def(self, delete_terms, delete_defs, title):
        index = 0
        selected_term = [self.terms_lbox.get(idx) for idx in self.terms_lbox.curselection()]
        index = delete_terms.index(selected_term[0])
        if selected_term == []:
            self.warning_label2.config(text="No term selected")
        else:
            index = 0
            file = open("titles.txt", "r")
            lines = file.readlines()
            index = lines.index(title)
            file.close()
            file3 = open("definitions.txt", "r")
            all_defs = file3.readlines()
            file3.close()
            file4 = open("terms.txt", "r")
            all_terms = file4.readlines()
            file4.close()
            file3 = open("definitions.txt", "w")
            for line in all_defs:
                if line != all_defs[index]:
                    file3.write(line)
            file3.close()
            file4 = open("terms.txt", "w")
            for line in all_terms:
                if line != all_terms[index]:
                    file4.write(line)
            file4.close()
            file2 = open("titles.txt", "w")
            for line in lines:
                if line != title:
                    file2.write(line)
            self.choose_title.destroy()
            file2.close()
            index = delete_terms.index(selected_term[0])
            delete_terms.remove(selected_term[0])
            delete_defs.remove(delete_defs[index])
            if delete_terms == []:
                self.confirm.config(text="Term Deleted")
                self.choose_term_delete.destroy()
                self.top_edit.destroy()
            else:
                file = open("titles.txt", "a")
                file.write(title)
                file.close()
                file = open("terms.txt", "a")
                for x in delete_terms:
                    file.write(x + "|")
                file.write("\n")
                file.close()
                file = open("definitions.txt", "a")
                for x in delete_defs:
                    file.write(x + "|")
                file.write("\n")
                file.close()
                self.confirm.config(text="Term Deleted")
                self.choose_term_delete.destroy()
                self.top_edit.destroy()#deletes term

    def title_choose_delete(self):
        self.top_edit.destroy()
        self.choose_title = Toplevel(root)
        self.choose_title.resizable(width=False, height=False)
        self.choose_title.title("Choosing set to delete")
        self.choose_title.geometry("300x300+20+20")
        content = Frame(self.choose_title)
        self.title_label = Label(content, text="Please choose a set")
        self.title_lbox = Listbox(content, height=10, exportselection=FALSE)
        file = open("titles.txt", "r")
        all_titles = file.readlines()
        for c in all_titles:
            self.title_lbox.insert(END, c)
        self.scroll = ttk.Scrollbar(content, orient=VERTICAL, command=self.title_lbox.yview)
        self.title_lbox.configure(yscrollcommand=self.scroll.set)
        self.choose = Button(content, text="Choose", command=self.delete_set)
        self.warning_label = Label(content, text="")
        content.grid(column=0, row=0)
        self.title_label.grid(column=0, row=0)
        self.title_lbox.grid(column=0, row=1)
        self.scroll.grid(column=1, row=1, sticky='ns')
        self.choose.grid(column=0, row=2)
        self.warning_label.grid(column=0, row=3)
        self.choose_title.columnconfigure(0, weight=1)
        self.choose_title.rowconfigure(0, weight=1)
        file.close()

    def delete_set(self):
        values = [self.title_lbox.get(idx) for idx in self.title_lbox.curselection()]
        if values == []:
            self.warning_label.config(text="No value selected")
        else:
            index = 0
            file = open("titles.txt", "r")
            lines = file.readlines()
            index = lines.index(values[0])
            file.close()
            file3 = open("definitions.txt", "r")
            all_defs = file3.readlines()
            file3.close()
            file4 = open("terms.txt", "r")
            all_terms = file4.readlines()
            file4.close()
            file3 = open("definitions.txt", "w")
            for line in all_defs:
                if line != all_defs[index]:
                    file3.write(line)
            file3.close()
            file4 = open("terms.txt", "w")
            for line in all_terms:
                if line != all_terms[index]:
                    file4.write(line)
            file4.close()
            file2 = open("titles.txt", "w")
            for line in lines:
                if line != values[0]:
                    file2.write(line)
            self.confirm.config(text="Set successfully deleted")
            self.top_edit.destroy()
            self.choose_title.destroy()
            file2.close()#deletes set

    def about_top(self):
        explain = Toplevel(root)
        explain.resizable(width=False, height=False)
        explain.title("About Program")
        explain.geometry("300x150+20+20")
        explain.resizable(width=False, height=False)
        about_label = Label(explain, text=(
                "This program is a Quizlet clone" + "\n" + "You can make flash card sets with terms and definitions" + "\n" + "View them and test yourself" + "\n" + "And also edit them" + "\n" + "Possible Usage:" + "\n" + "Keep in the corner of your screen when" + "\n" + "taking a test online and cheat"))
        about_label.pack()
        button = Button(explain, text="Close", command=explain.destroy)
        button.pack()  # Creates a top level and assigns a label and button to it

    def close_window(self):
        try:
            self.confirm_top.destroy()
        except:
            pass
        self.confirm_top = Toplevel(root)
        self.confirm_top.title("Confirm Close")
        self.confirm_top.geometry("300x100+20+20")
        self.confirm_top.resizable(width=False, height=False)
        self.explain_label = Label(self.confirm_top, text="Are you sure you want to exit")
        self.explain_label.pack()
        self.spacer_label2 = Label(self.confirm_top, text="")
        self.spacer_label2.pack()
        button_frame = Frame(self.confirm_top)
        button_frame.pack()
        self.yes = Button(button_frame, text="Yes", command=root.destroy)
        self.yes.pack(side=LEFT)
        self.spacer_label3 = Label(button_frame, text="")
        self.spacer_label3.pack(side=LEFT)
        self.no = Button(button_frame, text="No", command=self.confirm_top.destroy)
        self.no.pack(side=LEFT)  # confirm close top level asks if they are sure they want to close


root = Tk()
title_str = StringVar()
all_terms = []
all_defs = []
term_str = StringVar()
def_str = StringVar()
terms_amount = IntVar()
new_term = StringVar()
new_def = StringVar()
answer_term = StringVar()
append_term = StringVar()
append_def = StringVar()
app = App(root, title_str, all_terms, all_defs, term_str, def_str, terms_amount, new_term, new_def, answer_term,
          append_term, append_def)
root.title("Quizlet")
root.geometry("250x250+20+20")
root.resizable(width=False, height=False)
root.minsize(250, 250)
root.mainloop()
root.destroy()
