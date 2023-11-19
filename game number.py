
import random


print("Best  case   : O(1)   ")
print("Worst case   : O(logn)")
print("Average      : O(logn)")
print("Smart search : O(logn)")
print("--------------------------------------------------")
print("****Welcome to the number guessing game****")
print("--------------------------------------------------")



    
def binary_search_game():
    
    number = random.randint(100, 999)
    print("number is:",number)
    low = 100
    high = 999
    mid = None

    
    count = 0

    while mid != number:
        mid = (high + low) // 2
        print(f"mid: {mid}")
        
        count += 1

        if mid < number:
            print("The number is larger.")
            low = mid + 1
        elif mid > number:
            print("The number is smaller.")
            high = mid - 1

    print(f"Random number: {mid}")
    print(f"number of search: {count}")





binary_search_game()
input()
