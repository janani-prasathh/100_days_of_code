#password generator project
import random
letters=['a','b','c','d','e','f','h','g','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','^','*','()','@']
print("password generaator")
nletter=int(input("how many letters would you like in your password\n"))
nsymbol=int(input("how many symbols would you like in your password\n"))
nnumbers=int(input("how many numbers would you like in your password\n"))
pass_list=[]
for char in range(1,nletter+1):
    pass_list.append(random.choice(letters))
for char in range(1,nsymbol+1):
    pass_list.append(random.choice(symbols))
for char in range(1,nnumbers+1):
    pass_list.append(random.choice(numbers))
random.shuffle(pass_list)
password=""
for char in pass_list:
    password+=char
print(password)
