#########################################
import string

# def encrypt(msg, key):
#     shift_msg = ""
#     for i in msg:
#         shift_msg += str((i + key) % 26)
#     return shift_msg

# def decrypt(msg, key):
#     shift_msg = ""
#     for i in msg:
#         shift_msg += str((i - key) % 26)
#     return shift_msg

def encrypt(msg, key):
    shift_msg = []
    for i in msg:
        shift_msg.append((i + key) % 26)
    return shift_msg

def decrypt(msg, key):
    shift_msg = []
    for i in msg:
        shift_msg.append((i - key) % 26)
    return shift_msg

def map_abc(msg):
    new_msg = []
    for i in msg:
        new_msg.append(num_abc.get(i))
    return new_msg

def map_nums(msg):
    new_msg = ""
    for i in msg:
        for key, value in num_abc.items():
            if value == i:
                new_msg += str(key)
    return new_msg

abc = list(string.ascii_uppercase)
shifts = list(range(0,26))
num_abc = {}
    
n = 0
for i in abc:
    num_abc[i] = shifts[n]
    n = n + 1

num_abc[" "] = " "

#########################################

print("[1]Encrypt\n[2]Decrypt")
while True:
    try:
        selected_option = int(input("Choose a menu option, or press 0 to Exit: "))
    except ValueError:
        print("Not a valid option, try again.")
        continue
    else:
        break

if (selected_option == 0):
     quit()

while True:
    try:
        if (selected_option == 1):
            shift_key = int(input("Choose a number of shifts from 1-26: "))
        if (selected_option == 2):
            shift_key = int(input("Choose a number of shifts back from 1-26: "))
        # if (shift_key):
        #     try:
        #         shift_key = shift_key in shifts
        #     except ValueError:
        #         print("Not a valid number, try again.")
        #     else:
        #         break
    except ValueError:
        print("Not a valid input, try again.")
        continue
    else:
        break

# input_message = (input("Text to encrypt: ")).upper()

# print(num_abc)
# print(len(input_message))

#########################################

if (selected_option == 1):
    input_message = (input("Text to encrypt: ")).upper()
    print(input_message)
    num_message = map_abc(input_message)
    # print(num_message)
    ciph_message = encrypt(num_message,1)
    # print(ciph_message)
    encrypted_message = map_nums(ciph_message)
    print(encrypted_message)

    
    # print(encrypt(num_message,shift_key))

if (selected_option == 2):
    input_message = (input("Text to decrypt: ")).upper()
    print(input_message)
    d_num_message = map_abc(input_message)
    # print(d_num_message)
    deciph_message = decrypt(d_num_message,1)
    # print(deciph_message)
    decrypted_message = map_nums(deciph_message)
    print(decrypted_message)

#print(selected_option)