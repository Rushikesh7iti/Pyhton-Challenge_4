n = int(input("Enter the number of scores: "))
scores = [0]*n
low_risk = []
medium_risk = []
high_risk = []
critical_risk = []
count = 0
count_negative = 0
for i in range(n):
    scores[i] = int(input("Enter the score: "))

for j in range(n):
    if scores[j] < 0:
        count_negative += 1
    elif scores[j] <= 30:
        low_risk = low_risk + [scores[j]]
        count+=1


    elif scores[j] <= 60:
        medium_risk = medium_risk + [scores[j]]
        count+=1


    elif scores[j] < 100:
        high_risk = high_risk + [scores[j]]
        count+=1

    elif scores[j] >= 100:
        critical_risk = critical_risk + [scores[j]]
        count+=1




    else:
        print("Invalid input")
register_digit = int(input("Register Digit(D): "))
print("\n")
print("Low Risk:",low_risk)
print("Medium risk",medium_risk)
print("High Risk:", high_risk)
print("Critical Risk:", critical_risk)
print("\n")
print("After Personalized Filtering:")
if register_digit % 2 != 0:
    print("Low Risk:", low_risk)
    print("Medium risk", medium_risk)
    print("High Risk:", high_risk)
    print("Critical Risk:[]")
elif register_digit % 2 == 0:
    print("Low Risk:[]")
    print("Medium risk", medium_risk)
    print("High Risk:", high_risk)
    print("Critical Risk:", critical_risk)
print("\n")
print("Total Valid Entries", count)
print("Ignored Entries:", count_negative)
if register_digit % 2 == 0:
    print("Removed Due to Personalization:",len(critical_risk))
elif register_digit % 2 != 0:
    print("Removed Due to Personalization:",len(low_risk))




