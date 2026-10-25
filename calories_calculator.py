def ask_number(message, low, high, is_int=False):
    while True:
        try:
            value = int(input(message)) if is_int else float(input(message))
        except ValueError:
            print("Please enter a number only.")
            continue
        if low <= value <= high:
            return value
        print(f"Value must be between {low} and {high}.")

def ask_yes_no(message):
    while True:
        answer = input(message).strip().lower()
        if answer in ("yes","y"):
            return True
        if answer in ("no","n"):
            return False
        print("please enter yes or no.\n")    

def ask_name(message):
    while True:
        name = input(message).strip()
        if name and name.replace(" ", "").isalpha():
            return name
        print("Please enter letters only.")

def ask_reset():
    while True:
        answer = input("\n type reset or exit (r/e):\n ").strip().lower() 
        if answer in("reset","r"):
            return True
        if answer in ("exit","e"):
            return False
        print("please enter reset or exit.")

def welcome () :
      print ("welcome to the smart calories calculator \n")
      name =ask_name("whats your name :\n")
      print( "welcome "+ name) 
      return name


def _age():
    age = ask_number("enter your age by year : \n", 5, 110, is_int=True)
    return age         


def _gender():
      gender = input ("enter your gender male or female : \n").strip().lower() 
      gender_user = gender
      while True :
            if gender  != "male" and gender != "female" :
             gender = input ("enter your gender male or female : \n") 
             gender_user = gender
            else :
             break  
      return gender         

def _weight():
     return ask_number("enter your weight in kg : \n", 20, 300)       


def _height():
     return ask_number("enter your height in cm \n" ,50,250) 
            


def _active ():
      return ask_number(
        "choose your activity level number from 1 to 5 \n"
        "1- sedentary active \n"
        "2- lightly active \n"
        "3- moderately active \n"
        "4- very active \n"
        "5- extra active \n",
        1, 5, is_int=True)



def _calculate(weight,age,height,gender,active):
    weight_x10 =  weight * 10 
    age_x5 = age * 5
    height_x6_25 = height * 6.25
    bmr_for_male = weight_x10 + height_x6_25 -age_x5+5
    bmr_for_female = weight_x10 + height_x6_25 - age_x5 - 161
    if gender == "male" : 
        bmr = bmr_for_male 
    elif gender == "female" : 
        bmr = bmr_for_female
    activity_factor =[ 1.2 , 1.375, 1.55 , 1.725 , 1.9 ]
    calories = bmr * activity_factor[active - 1]    
    return calories
   

def _goal(): 
      return ask_number(
        " enter your goal number from 1 to 3:\n"
        " 1- Maintain \n"
        " 2- Gain \n"
        " 3- lose \n",
        1, 3, is_int=True)


def _macros ( weight,total):
    protein =weight*1.9
    fat= total *0.25 /9
    carbs=(total - protein* 4 -fat *9) /4
    
    print("your daily macros :\n") 
    print(f"protein:{protein:.0f} g \n") 
    print(f"carbs {carbs:.0f} g \n")   
    print(f"fat {fat:.0f} g \n")

  
def main():
    name = welcome()
    age=_age()
    gender =_gender()
    weight =_weight()
    height =_height()
    active = _active()
    calories=_calculate(weight,age,height,gender,active)
    
    goal = _goal()

    if goal ==1:
      total=calories
      print(f"{name} you need {total:.0f} calories everyday")
      
    if goal == 2:
        target = ask_number("how many kg do you want to gain \n", 0.1, 50)
        target_time = ask_number("in how many weeks do you want to achieve this \n", 1, 200, is_int=True)
        rate = target / target_time
        extra = rate * 7700 / 7
        if rate > 0.5:
            safe_weeks = target / 0.5
            print(f"{rate:.2f} kg per week is too fast and not healthy.")
            print("A safe gain is 0.25 to 0.5 kg per week (300 to 500 extra calories a day).")
            print(f"To gain {target} kg safely you need at least {safe_weeks:.0f} weeks.")
            extra = 0.5 * 7700 / 7
            target_time = safe_weeks
            total = calories + extra
            print(f"\n{name} you need about {total:.0f} calories everyday for {target_time:.0f} weeks.")
            
            
    if goal == 3:
            target = ask_number("how many kg do you want to lose \n", 0.1, 50)
            target_time = ask_number("in how many weeks do you want to achieve this \n\n", 1, 200, is_int=True )
            rate = target / target_time
            deficit = rate * 7700 / 7
            if rate > 1:
                safe_weeks = target / 1
                print(f"{rate:.2f} kg per week is too fast and not healthy.")
                print("A safe loss is 0.5 to 1 kg per week.")
                print(f"To lose {target} kg safely you need at least {safe_weeks:.0f} weeks.")
                deficit = 1 * 7700 / 7
                target_time = safe_weeks
                
            total = calories - deficit
            min_cal = 1500 if gender == "male" else 1200
            if total < min_cal:
                total = min_cal
                print(f"Your calories were raised to {min_cal:.0f}, the minimum safe amount.")
                

            print(f"\n{name}, you need about {total:.0f} calories everyday for {target_time:.0f} weeks.")
                
    if ask_yes_no("\n do you want to know your daily macros? (yes or no)\n"):
        _macros(weight,total)  
      
while True:
    main()
    if not ask_reset():
        print("!Goodbye")
        break
    

    
    
        
        

   
    