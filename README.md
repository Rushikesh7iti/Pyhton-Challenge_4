Project Description

This Python program analyzes university student login activity intensity scores to detect suspicious behavior patterns.

It performs:

Data cleaning (ignores invalid scores)

Risk categorization

Personalized security filtering

Final security report generation

Each implementation behaves differently based on the last digit of the student’s register number (D).

 Features

Accepts a list of integer activity scores
Processes data using a for loop
Categorizes scores into risk levels
Applies register-based personalized filtering
Counts valid, ignored, and removed entries
Displays final filtered risk report

Risk Categorization Rules
Score Range	Risk Level
< 0	Invalid (Ignored)
0 – 30	Low Risk
31 – 60	Medium Risk
61 – 100	High Risk
> 100	Critical Risk
Lists are created

The program generates four separate lists:

low_risk

medium_risk

high_risk

critical_risk

Personalized Security Filter

Let:

D = Last digit of Register Number

Filtering logic is applied after categorization.

 If D is EVEN

Remove all Low Risk scores

Keep Medium, High, Critical

 If D is ODD

Remove all Critical Risk scores

Keep Low, Medium, High

Additional Calculations

The program also computes:

Total valid entries

Ignored entries

Entries removed due to personalization
