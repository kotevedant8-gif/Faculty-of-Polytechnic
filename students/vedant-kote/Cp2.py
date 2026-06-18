#problem1
def ask_text():
    while True:
        name = input("What is your name? ")
        if name == "":
            return("Can't be empty. Try again.")
        else:
            return(name)
            break
    while True:
        sub_name = input("Enter subject name? ")
        if sub_name == "":
            return("Can't be empty. Try again.")
        else:
            return(sub_name)
            break

  #problem2
  def ask_marks(): 
    while True: 
        user_input = input("Enter your marks 1-100: ") 
        if user_input.isdigit(): 
            return(user_input)
            break
        else: 
            return("Enter whole number only")
ask_marks() 

  #problem3
 def ask_y_n():
    while True:
        user_input=input("do you want to add another subject:-")
        if user_input == "y":
            return(True)
            break
        elif user_input == "n":
            return(False)
            break
        else:
            print("type only y/n only")
ask_y_n()
#problem4
 def collect():
    TN=ask_text()
    AM1=ask_marks()
    AM2=ask_marks()
    AM3=ask_marks()
    YN=ask_y_n()
    return(TN,AM1,AM2,AM3,YN)
collect()
