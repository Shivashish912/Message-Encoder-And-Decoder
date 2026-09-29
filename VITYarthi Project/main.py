import random
import string
import hashlib


def random_chars():
    rnd1=""
    rnd2=""
    chars=string.ascii_letters + string.digits
    for i in range(5):
        rnd1 +=random.choice(chars)
        rnd2 +=random.choice(chars)
    return rnd1,rnd2


def encode_message(message):
    rnd1, rnd2 = random_chars()
    inverted_message=message[::-1]
    coded_message=rnd1 + inverted_message + rnd2
    return coded_message


def decode_message(coded_message):
    normal_message=coded_message[5:-5]
    original_message=normal_message[::-1]
    return original_message


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()[:12]


def check_password(password,stored_hash):
    entered_hash=hash_password(password)
    return entered_hash==stored_hash
    

while True:
    print("="*16 + "\n" + "MESSAGE ENCODER\n" + "="*16)
    print("1. Encode a message\n2. Decode a message\n3. Exit")
    choice =input("\n Enter Your Choice:")

    if choice=="1":
        message=input("\nEnter the message you want to encode:")
        coded_message=encode_message(message)
        password_choice=input("Do You Want Password Protection? (yes/no): ")

        if password_choice.lower()=="yes":
            password=input("Enter Password:")
            password_hash=hash_password(password)
            coded_message="*"+password_hash+"|"+coded_message
            print("\nYour message has been encoded successfully !!!")
            print("Coded Message:",coded_message)
        else:
            print("\nYour message has been encoded successfully !!!")
            print("Coded Message:",coded_message)

    elif choice=="2":
        coded_message=input("\n Enter the coded Message")

        if coded_message.startswith("*"):
           coded_message=coded_message[1:]
           data=coded_message.split("|",1)
           stored_hash=data[0]
           actual_coded_message=data[1]
           password=input("Enter Password:")
           if check_password(password,stored_hash):
                    original_message=decode_message(actual_coded_message)
                    print("\nPassword Verified. Decoded Message: \n",original_message)
           else:
                print("\nIncorrect Password. Access Denied. \n Exiting...") 

        else:
            original_message=decode_message(coded_message)
            print("\nDecoded Message:",original_message)

    elif choice=="3":
        print("\nThank you for using the Message Encoder. Goodbye!")
        break       

    else:
        print("\nInvalid Choice.Please Enter 1,2,3.")