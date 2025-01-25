number = input("podaj number")

for number in range (100):
    if (number % 5):
        print(number, 'nie jest podzielny przez 5')
            
    else:
        print(number, ' jest podzielny przez 5')
        if(number % 7):
            print('ale nie jest podzielny przez 7')
        else:
            print('i jest  podzielny przez 7')



input("done")
input()


    
