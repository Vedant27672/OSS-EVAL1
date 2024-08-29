# Develop a Python program to manage student grades at a sports 
#school. Use dictionaries to store information such as the student's name, class, height, weight, 
#and the sport they are interested in. Additionally, calculate a diet chart based on the student's 
#weight, height, and calorie intake from the food they consume. Determine whether their 
#consumption is sufficient, and provide feedback on their diet status. Use the following 
#indicators for your comments:

def add_student(name,clas,height,weight,sports):
    temp={
        'name':name,
       'class':clas,
        'height':height,
        'weight':weight,
        'sports':sports
    }
    stud[name]=temp;

def calculate(item,cal):
    height=item['height']
    weight=item['weight']
    BMI=height/weight;
    if BMI<cal:
        ans='red'
    elif BMI==cal:
        ans='orange'
    else:
        ans='green'
    print('BMI : ',BMI)
    return ans;
    
stud={}
response={}
calorie=[180,200,200,1000]


# n=int(input("Enter number of students : "))
# i=0
# for i in range(0,n):
#     name=input("Enter name of student : ")
#     clas=input("Enter class of student : ")
#     height=int(input("Enter height of student : "))
#     weight=int(input("Enter weight of student : "))
#     sport=input("Enter sport of student : ")
#     dict[name]={
#         'name':name,
#         'height':height,
#         'weight':weight,
#         'sports':sport
#     }


add_student('Vedant1','B2',182,70,'football')
add_student('Vedant2','B1',180,72,'cricket')
add_student('Vedant3','B3',178,75,'hockey')
add_student('Vedant4','B3',200,75,'hockey')

i=0
for key,value in stud.items():
    height=value['height']
    calorie[i]=calorie[i]/height
    print('height : ',value['height'])
    i=i+1
print('calorie : ')
print(calorie)
print('Student Dictionary : ')
print(stud)

i=0

for key,value in stud.items():
    res=calculate(value,calorie[i])
    i=i+1
    response[key]=res
    
print('Feedback : ')
# print(stud['Vedant1']['height'])
print(response)