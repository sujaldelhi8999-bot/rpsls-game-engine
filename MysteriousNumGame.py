while True :
    number = int(input("enter the number or to stop enter 0 : "))
    
    if number == 0:
        break
    
    if number == 999:
        print("system shutdown initiated.")
        break
    
    if number <0:
        print("inavlid input")
        continue
    
    if number == 1:
        print("traivial")
        pass
        continue
    
    number_str = str(number)
    
    even_digit = 0
    odd_digit = 0
    sum_digit = 0
    corrupted = False 
    
    for digit_char in number_str:
        digit = int(digit_char)
        
        if digit ==7:
            printf("corrputed num detetcted")
            corrupted = True
            break
        
        sum_digit = sum_digit + digit
        
        if digit % 2 == 0:
            even_digit = even_digit + 1
        else:
            odd_digit = odd_digit+1
            
    if corrupted == True:
        continue
    
    if even_digit == odd_digit:
        print("balanced number ignored")
        continue
    
    print("Even Digit:",even_digit)
    print("Odd Digit:",odd_digit)
    
    number_of_digit = len(number_str)
    
    if sum_digit == number_of_digit * number_of_digit:
        print("Mysterious number")
    else:
        print("not a mysterious number")