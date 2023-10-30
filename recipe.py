from tkinter import *
import requests
import pyttsx3
import json










root = Tk()
root.title("Quick Recipes")
root.geometry("800x800")
root.configure(bg="black")
root.after(1, lambda: root.focus_force())
# Mainframe
mainframe = Frame(root, bg="black")






def get():
    #query = search_entry.get()
    global outputING
    query = search_entry.get()
    api_url = 'https://api.api-ninjas.com/v1/recipe?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': 'mqWkDRhByilkgzMjVmPQMg2Fnnwiwq86XQPzjXz3'})
    whole = json.loads(response.text)
    recipeTitle = whole[0]["title"]
    recipeIngredients = whole[0]["ingredients"]
    recipeInstructions = whole[0]["instructions"]
    formattedPrep = recipeInstructions.split('.')
    formattedIng= recipeIngredients.split(';')
    for stri in recipeIngredients:
        if stri == '|':
            formattedIng = recipeIngredients.split('|')
            break
    ingredients_holder.configure(text=formattedIng)
    prep_holder.configure(text=formattedPrep)





title_label = Label(mainframe, text="Q Quick Recipes R", font=("Arial", 20), bg="black", fg="white")
title_label.place(y=20,x=280)

header_label = Label(mainframe,text="QR allows you to get recipes to almost every type of meal in the world in a few seconds.\nJust search for your meal below ",bg='pink',fg='black',font=(20))
header_label.place(y=100,x=80)

search_label = Label(bg='orange',fg='black',text='Enter meal',width=15)
search_label.place(y=250,x=250)

search_entry = Entry(bg='gray',fg='black',width=50,font=('Arial',15))
search_entry.place(y=290,x=10)

submit = Button(mainframe,text='search',width=10,border=2,bg='brown',fg='black',font=('Arial',10),command=get)
submit.place(y=290,x=580)

ingredients_label = Label(mainframe,bg='yellow',fg='black',text='Ingredients',width=15)
ingredients_label.place(y=380,x=120)

ingredients_holder = Label(mainframe,bg='black',wraplength=350, justify='left',fg='white',text='',font=('Arial',9))
ingredients_holder.place(y=410,x=5)


prep_label = Label(mainframe,bg='yellow',fg='black',text='Preparation',width=15)
prep_label.place(y=380,x=530)

prep_holder = Label(mainframe,bg='black',wraplength=400, justify='left',fg='white',text='',font=('Arial',9))
prep_holder.place(y=410,x=380)



mainframe.pack(expand=True,fill=BOTH)

















root.mainloop()
