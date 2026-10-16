print('A farmer has 5 fields, this program calculates the total and average of the crops planted, how much can packed into 25 sacks totally and the remaining seeds, compare this year with last year and add bonus crops and seeds to the total and remainder respectively.', end='')
print('Field 1 = 358 crops, Field 2 = 412 crops, Field 3 = 349 crops, Field 4 = 573 crops and Field 5 = 427 crops and the weight of 1 crop is 50 grams.',end = '')
print('The harvest from last year was 1889 crops')
ly = 1889
a = 358
b = 412
c = 349
d = 573
e = 427
f = a+b+c+d+e+400
g = (a+b+c+d+e)/5
h = int((358*50)+(412*50)+(349*50)+(573*50)+(427*50)/25000)
i = (((358*50)+(412*50)+(349*50)+(573*50)+(427*50))%25000)+370
print('The total crops along with the added bonus is',f)
print('The average of all 5 fields is',g)
print('The weight of crops that is put in 25kg bags is',h)
print('The remainder of seeds along with the added bonus is',i)
if f<ly:
    print('The harvest of last year is greater than this year')
elif f>ly:
    print('This year, the harvest is greater than last year')
elif f==ly:
    print('The harvest of both years is equal')