import random
def password_generator(length,password):
    for i in range(length):
        if(len(password)<length):
            password+= chr(random.randint(45,125))
        else:
            break
    return password
length = int(input("Enter the length of the password that need to be generated: "))
password = ''
print(password_generator(length,password))