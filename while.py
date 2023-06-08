from statistics import mean

number = input_list = []
# User is asked to input a number continuously.
# User's number input is populated into list. 
# Entering -1 ends program and calculates mean of positive numbers from populated list.


while True:
    if number != -1:
        number = int(input('Enter a number or type -1 to end.:'))
        input_list.append(number)
    elif number.isnumeric(True):
        print('Opps! Please enter a number:')
    else:
        del input_list[-1] 
        print(input_list)
        mean_1 = mean(input_list)
        print('Here is the mean value for the numbers you entered:',mean_1)
        break
