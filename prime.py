n = int(input("Enter a number: "))   # Step 1: Get number from user

if n <= 1:
    print("Not Prime")               # Step 2: Prime numbers must be > 1
else:
    for i in range(2, n):            # Step 3: Try dividing n by 2, 3, ..., n-1
        if n % i == 0:               # Step 4: If divisible by any number
            print("Not Prime")       # Not a prime
            break                    # Stop checking more
    else:
        print("Prime")               # If loop completes, it's a prime
