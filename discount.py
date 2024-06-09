choice = int(input('Enter 1 to continue and 0 to exit'))
while(choice):
    amount = int(input("Enter Purchase Amount :"))
    if(amount>=2000 and amount<= 3000):
        discount=2
        print("Avail 2% Discount")
    elif(amount>=3001 and amount<= 5000):
        discount=5
        print("Avail 5% Discount")
    elif(amount>=5001 and amount<= 7000):
        discount=8
        print("Avail 8% Discount")
    elif(amount>=7001 and amount<= 10000):
        discount=9
        print("Avail 9% Discount")
    elif(amount>=10001):
        discount=10
        print("Avail 10% Discount")
    else:
        print("You can't avail the disount")
    discounted_amt = amount*discount/100
    new_amount = amount-discounted_amt
    print("Final Amount is : ",new_amount)
    choice = int(input('Enter 1 to continue and 0 to exit'))

