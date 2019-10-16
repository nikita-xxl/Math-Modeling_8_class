x = 1999
if x%4==0 and (x%4==0 and x%100==0 and x%400==0):
    print('Високосный')
elif x%4==1 and x%100==1:
        print('Обычный')
else:
            print('Обычный')
