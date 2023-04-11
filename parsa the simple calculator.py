
xxxdeleter=True
print('this only works when u put spaces between eatch mumber like this 3 + 8 - 10 not this 3+8-10')
print('stillworking on somem bugs and planning to add () functions soon')
print()
print('made by prsayazdani and supervised by yusuf sedighi')





# this part handles thru the power off
q=input('enter your qustion :')
question=q.split()
while xxxdeleter==True:
    if 'xx' in question:
        xx=question.index('xx')
        # it basicly findes the where xx is
        answerofxx=float(question[xx-1])**float(question[xx+1])
        # and based on that uses the number before and after that to xx together
        question[xx + 1]=float(answerofxx)
        question.pop(xx)
        question.pop(xx-1)
        # and in here it deletes the xx and the number before that and replaces the number after it with is the answer
    else:
        xxxdeleter=False






# thid parts handles x and /

o=0
for i in question:
    if i=='x':
        o+=1
    if i=='/':
        o+=1
#here we finde out if thee is any / or x in the question
x=0

xdeleter=True
while xdeleter==True:
    if o > 0:
    #here if there is x or / in question we start the protocol if not it will move on to the next protocol
        for i in question:
            if i=='x':
                ix=question.index(i)
                p='x'
                break
            elif i=='/':
                ix=question.index(i)
                p='/'
                break
            #HERE IT FINDEX WHERE IS THE X AND / ARE
        if p=='x':
            x=float(question[ix-1])*float(question[ix+1])
            # here based on where is the x it will find the number before and after it  and x them
            question[ix + 1]=x
            question.pop(ix)
            question.pop(ix - 1)
            o-=1
            # here it will delet the x
            #and the number before it and replace the number after it
            #and it will mines 1 of o (o cheks if there is / or x in the question)
        elif p=='/':
            x=float(question[ix-1])/float(question[ix+1])
            # here based on where is the /  it will find the number before and after it  and / them
            question[ix + 1]=x
            question.pop(ix)
            question.pop(ix - 1)
            o-=1
            # here it will delet the / and the number before it and replace the number after it
            #and it will mines 1 of o (o cheks if there is / or x in the question)

    else:
        xdeleter=False
            

for i in question:
    try:
        if i.isdigit():
            question[question.index(i)]=float(i)
    except:
        pass





# this part handles + and -



num1=0
num2=0
num=True
pro=''
for i in question:
    if type(i)==float and num==True:
        num1+=float(i)
    elif i=='x' or i=='+' or i=='/' or i=='-' or i=='xx':
        pro=i
        num=False
    # here it findes the + or - and findes the numbers before and after ir
    # here there is only + and - left (this was the original code its basicly did the same thing but it dident do the xx befor x and / , any way i was scared to touch it )
    elif type(i)==float and num==False:
        num2=float(i)
        if pro=='+':
            num1+=num2
        elif pro=='x':
            num1*=num2
        elif pro=='-':
            num1-=num2
        elif pro=='/':
            num1/=num2
        elif pro=='xx':
            num1**=num2
        # at last it will do the equasion based on its - or +

print('')
print('')
print(q,'=',num1)