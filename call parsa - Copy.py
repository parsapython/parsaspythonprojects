import tkinter as tk
root=tk.Tk()
root.geometry('400x400')


but7=tk.Button(master=root,text=7,height=2,width=4,bg='white')
but7.place(x=0,y=100)

but8=tk.Button(master=root,text=8,height=2,width=4,bg='white')
but8.place(x=40,y=100)

but9=tk.Button(master=root,text=9,height=2,width=4,bg='white')
but9.place(x=80,y=100)

but4=tk.Button(master=root,text=4,height=2,width=4,bg='white')
but4.place(x=0,y=144)

but5=tk.Button(master=root,text=5,height=2,width=4,bg='white')
but5.place(x=40,y=144)

but6=tk.Button(master=root,text=6,height=2,width=4,bg='white')
but6.place(x=80,y=144)

but1=tk.Button(master=root,text=1,height=2,width=4,bg='white')
but1.place(x=0,y=188)

but2=tk.Button(master=root,text=2,height=2,width=4,bg='white')
but2.place(x=40,y=188)

but3=tk.Button(master=root,text=3,height=2,width=4,bg='white')
but3.place(x=80,y=188)

but0=tk.Button(master=root,text=0,height=2,width=4,bg='white')
but0.place(x=40,y=233)

butm=tk.Button(master=root,text='+/-',height=2,width=4,bg='gray')
butm.place(x=0,y=232)

butplus=tk.Button(master=root,text='+',height=2,width=4,bg='gray')
butplus.place(x=120,y=188)

butmines=tk.Button(master=root,text='-',height=2,width=4,bg='gray')
butmines.place(x=120,y=144)

butequalls=tk.Button(master=root,text='=',height=2,width=4,bg='gray')
butequalls.place(x=120,y=232)

butdot=tk.Button(master=root,text='.',height=2,width=4,bg='gray')
butdot.place(x=80,y=232)

buttimes=tk.Button(master=root,text='x',height=2,width=4,bg='gray')
buttimes.place(x=120,y=100)


butdevide=tk.Button(master=root,text='/',height=2,width=4,bg='gray')
butdevide.place(x=120,y=56)


butdevide=tk.Button(master=root,text='xx',height=2,width=4,bg='gray')
butdevide.place(x=80,y=56)

butdevide=tk.Button(master=root,text='del',height=2,width=4,bg='gray')
butdevide.place(x=40,y=56)

butbroket=tk.Button(master=root,text=')(',height=2,width=4,bg='gray')
butbroket.place(x=0,y=56)

eqasion=tk.Label(root,text='enter ur equasion',height=2,width=21,bg='red')
eqasion.place(x=3,y=12)

answer=tk.Label(root,text='enter ur equasion',height=2,width=21,bg='red')
answer.place(x=3,y=276)
root.mainloop()