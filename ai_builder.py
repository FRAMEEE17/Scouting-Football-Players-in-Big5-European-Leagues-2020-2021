def compute_winning_prob(droprate, n): #input droprate , n 
    #กำหนดให้ function มีหน้าตาแบบนี้
    fail_once = 1 - droprate
    fail_all = fail_once **n
    winning_prob = 1 - fail_all
    return winning_prob #return output ทำเป็นสมการก็ได้ เช่น return 1 - fail_all
winning_prob_10attempts = compute_winning_prob(0.003, 10) #แทนค่าใน function
print(format(winning_prob_10attempts,"%"))
winning_prob_1000attempts = compute_winning_prob(0.003, 1000)
print(format(winning_prob_1000attempts,"%"))

def area_triangle(a,b,c):
    s = (a+b+c)/2
    area = (s(s-a)(s-b)(s-c))**(1/2)
    return area
print((area_triangle(5,6,8))