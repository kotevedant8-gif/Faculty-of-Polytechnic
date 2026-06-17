#avg
def avrage_of_three(m1,m2,m3):
    return round(m1,m2,m3)/3
#result  
def classify_result(a):
    if a>=75:
        return("distinction")
    elif a>=35:
        return("pass")
    else:
        return("fall")
        
#grade
  def classify_result(a):
    if a>=90:
        return("A")
    elif a>=80:
        return("B")
    elif a>=70:
        return("C")
    elif a>=60:
        return("d")
    elif a<60:
        return("F")
#format markes
 def format_marks(m1,m2,m3):
    return(f"{m1},{m2},{m3}")
