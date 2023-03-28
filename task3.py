swim = int(input("Enter time taken for swimming in minutes : "))
print("Time taken for Swimming task: ",swim)

cycl = int(input("Enter time taken for cycling in minutes : "))
print("Time taken for Cycling task: ",cycl)

run = int(input("Enter time taken for running in minutes : "))
print("Time taken for Running task: ",run)

Total_time=swim+cycl+run
print("Total time taken for triathlon: ",Total_time)

if (Total_time < 100):
    print("Provincial Colors")
elif (Total_time > 100 and Total_time <=105):
    print("Provincial Half Colors")
elif (Total_time >105 and Total_time <=110):
    print("Provincial Scroll")
else:
    print("No award")