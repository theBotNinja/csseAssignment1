for number in range(0,1000):
    if number < 2 :
        print(number," is neither a prime nor a composite number.")
    else:
        for i in range(2,number):
            if (number%i==0):
                print(number," is not prime.")
                break
        else:
            print(number," is prime.")
