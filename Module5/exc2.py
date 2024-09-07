nums = []
while True:
     user_input = input(f"Enter a number or quite by pressing enter : ")
     nums.append(user_input)

     if user_input == " ":
         break

nums.sort(reverse=True)
top_five = nums[0:5]
print (f"Five biggest numbers, {top_five} ")