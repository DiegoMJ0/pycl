 


# Creating classes
class BankAccount(object):
    def __init__(self, input_name, input_balance =0):
        self.name = input_name 
        self.balance=input_balance
        # self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            new_balance = self.balance + amount
            self.balance = new_balance
        
    def withdraw(self, amount):
        if amount > 0:
            new_balance = self.balance - amount
            self.balance = new_balance
    
    def __str__(self) -> str:
        return 'Account "' + self.name + '" has a balance of ' + str(self.balance)


b1 = BankAccount('Diego')
print(b1.name)
# # running classes
# acct = BankAccount('MyAccount')
# acct.deposit(100)
# acct.deposit(200)
# acct.withdraw(50)
# print(acct) # Account "MyAccount" has a balance of 250.




# nums = [0, 1, 2, 3, 4, 5, 6]
# nums = ['1', '2', '3', '4', '5', '6']

# nums[0] =6
# seq = 
# for index in range(len(nums)):
#     # value  = nums[index]
#     # print(repr(value), type(value))
#     print(nums[index])
# add_one = set([1, 3, 5])
# mul_by_two = set([2, 4])
# div_by_two = set([4,6])
# output_list = []

# for num in nums:
#     if num in add_one:
#         output_list.append( num + 1)
#     elif num in mul_by_two:
#         output_list.append(num * 2)
#     elif num in div_by_two:
#         output_list.append(num / 2)
  

# indexies = iter(range(len(nums)))
# print(next(indexies))
# print(next(indexies))
# print(next(indexies))
# print(next(indexies))
# print(next(indexies))
# print(next(indexies))
# print(next(indexies))
# nums.

# at_num = iter(nums)
# print(next(at_num))
# print(next(at_num))
# print(next(at_num))

nums = list(x for x in range(1, 6))
# nums = []

name = "Dario"
for num in nums:
    last_name ="Arias"

print(name, last_name)