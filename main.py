from tkinter import *
import wikipedia

root = Tk()
root.title("Encrypted password generator")
root.geometry("800x800")

instruction_label1 = Label(root, text="Enter the title of a wikipedia page:")
instruction_label1.place(x=0,y=0)

prompt_1 = Entry(root, width=50, text="Enter wikipedia page")
prompt_1.place(x=250,y=0)


def Search():
    summary = wikipedia.summary(prompt_1.get())
    count = 0
    res = ""
    for ele in summary:
        if ele == ' ':
            count = count + 1
            res = res + " "
        else:
            if count % 6 == 0:
                res = res + ele

        if len(res) > 150:
            break

    label_wikipedia_result = Label(root, text=res)
    label_wikipedia_result.place(x=0,y=50)

button_search = Button(root, text="Search article", command=Search)
button_search.place(x=600,y=0)

instruction_label2 = Label(root, text="Choose a keyword from the above choices and enter it here to be encrypted")
instruction_label2.place(x=0,y=400)
prompt_2 = Entry(root, width=50, text="Enter keyword")
prompt_2.place(x=0,y=425)
button_encrypt = Button(root, text="Enter keyword")
button_encrypt.place(x=330,y=425)




root.mainloop()