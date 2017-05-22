############################################

test = 1;

#################

# Test for-loop in range(From, To, Step)
for i in range(10, 20, 5):
    print(i);

# While-loop
while test < 10:
    print(test);
    test +=2;

############################################

exampleNumber = 10

#################

# Test for-loop with break at 10
for i in range(100):
    if i is exampleNumber:
        print("Nice!", i)
        break
    else:
        print(i)

############################################

numbers = [2, 3, 6, 8, 10, 15, 23]

#################

for i in range(1,10):
    if i in numbers:
        continue
    print("i: ", i)
