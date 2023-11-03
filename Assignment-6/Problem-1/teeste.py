import string

abc = list(string.ascii_uppercase)
shifts = list(range(0,26))
num_abc = {}

n = 0
for i in abc:
    num_abc [i] = shifts[n]
    n = n + 1

print((25+26)%26)
print(num_abc)

# message = input("Teext: ")

# for i in message:
#     message[i] = 