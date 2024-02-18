import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
f=pd.read_csv('cardio_train.csv',sep=';')

#A function to find BMI for Dataframe
def bmi(r):
    h=f.iloc[r,3]
    w=f.iloc[r,4]
    bmi=w/((h/100)**2)
    '''if bmi<=18.5:
        print('Underweight')
    elif bmi>18.5 and bmi<29.9:
        print('Normal Weight')
    elif bmi>=30:
        print('Obesity')
    else: 
        pass'''
    return(bmi)
#A function to find BMI for given
def bmin(h,w):
    bmi=w/((h/100)**2)
    '''if bmi<=18.5:
        print('Underweight')
    elif bmi>18.5 and bmi<29.9:
        print('Normal Weight')
    elif bmi>=30:
        print('Obesity')
    else: 
        pass'''
    return(bmi)

#print(f)

def inp():
#Getting Input

    age=int(input('Enter AGE in days : '))
    gender=int(input('Enter 1 for MALE and 2 for FEMALE : '))
    height=int(input('Enter Height in cm : '))
    weight=int(input('Enter weight in kg : '))
    hibp=int(input('Enter the High Action Pulse (AP) : '))
    lwbp=int(input('Enter the Low Action Pulse (AP) : '))
    chl=int(input('Enter Cholesterol 1/2/3 : '))
    glu=int(input('Enter Glucose 1/2/3 : '))
    smo=int(input('Do you Smoke? 0/1 : '))
    alco=int(input('Do you consume Alcohol? 0/1: '))
    car=int(input('Doing Cardio? 0/1 : '))

# Using numpy  where function can be sort the list by required condition
    
    _a=np.where(f['age']+5<=age)
    _b=np.where(f['gender']==gender)
    _c=np.where(f['ap_hi']<=hibp)
    _d=np.where(f['ap_lo']>=lwbp)
    _e=np.where(f['cholesterol']<=chl)
    _f=np.where(f['gluc']==glu)
    _g=np.where(f['smoke']==smo)
    _h=np.where(f['alco']==alco)
    _z=np.where(f['cardio']==car)

# Converting the Input data into set
     
    seta=set(dict.fromkeys(_a[0]))
    setb=set(dict.fromkeys(_b[0]))
    setc=set(dict.fromkeys(_c[0]))
    setd=set(dict.fromkeys(_d[0]))
    sete=set(dict.fromkeys(_e[0]))
    setf=set(dict.fromkeys(_f[0]))
    setg=set(dict.fromkeys(_g[0]))
    seth=set(dict.fromkeys(_h[0]))
    setz=set(dict.fromkeys(_z[0]))
    set_int=setz.intersection(seth.intersection(setg.intersection(setf.intersection(sete.intersection(setd.intersection(setc.intersection(setb.intersection(seta))))))))
    return(set_int,height,weight,chl,glu,age,gender,hibp,lwbp,smo,alco,car)

#Condition when zero occurs

def zero():
    possi=0
#BMI
    if bmin(height,weight)>=30:
        possi+=25
    elif bmin(height,weight)<30 and bmin(height,weight)>=25:
        possi+=18
    else:
        pass
#High Action Potential
    if hibp>=135:
        possi+=7
    elif hibp<135 and hibp>=115:
        possi+=5
    else:
        pass
#Low Action Potential
    if lobp<=60 and lobp>45:
        possi+=4
    elif lobp<=45:
        possi+=7
    else:
        pass
#cholestrol
    if chlo==3:
        possi+=18
    elif chlo==2:
        possi+=14
    elif chlo==1:
        possi+=8
    else:
        pass
#Glucose
    if gluo==3:
        possi+=14
    elif gluo==2:
        possi+=8
    elif gluo==1:
        possi+=3
    else:
        pass
#Smoking
    if smo==1:
        possi+=14
    else:
        possi+=4
#Alcohol
    if alco==1:
        possi+=5
    else:
        pass
#Age and Gender
    if gen==1:
        if age>=16447:
            possi+=7
        elif age<16447 and age>=10950:
            possi+=3
        elif age<10950 and age>=7320:
            possi+=1
        else:
            pass
    elif gen==2:
        if age>=20289:
            possi+=5
        elif age<16447 and age>=10950:
            possi+=2
        elif age<10950 and age>=7320:
            possi+=1
        else:
            pass
#cardio
    if car==1:
        possi-=10
    else:
        pass

    if possi>=40:
        print("\n This Person may have Cardio Problem!.\n Kindly visit Hospital. \n Don't Smoke and Don't Drink")
    elif possi<40:
        print("\n This Person does not have any thread to Cardio Problem.\n Don't Smoke and Don't Drink")  

# Declaring Variable
_var1,height,weight,chlo,gluo,age,gen,hibp,lobp,smo,alco,car=inp()

#Decided whether to use Data or Program
if len(_var1)==0:
    #print('Program at Starting')
    zero()
else:
    n_active=0
    n_count=0
    for i in _var1:
        if bmin(height,weight)>=bmi(i):
            #print('BMI executed!!!')
            if chlo==f.iloc[i,7] or gluo==f.iloc[i,8]:
                n_count+=1
                #print(n_count)
                #print('Chlo or Gluo executed!!')
                #print(f.iloc[i,11])
                if f.iloc[i,11]==1:
                    n_active+=1
                    #print(f.iloc[i])
    print('\n Total number of Case similar to Given Data : ',n_count)
    print('\n Total number of Active Case in the Data : ',n_active)
    if n_count==0:
        #print('Program at End')
        zero()
    elif (n_active/n_count)*100>=60:
        #print('Machine Learning')
        print("\n This Person may have Cardio Problem!.\n Kindly visit Hospital. \n Don't Smoke and Don't Drink")
    else:
        #print('Machine Learning')
        print("\n This Person does not have any thread to Cardio Problem.\n Don't Smoke and Don't Drink")

#Plot for reference
f.plot.bar(x='active',y='age',rot=0)
plt.show()