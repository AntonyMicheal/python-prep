# equation is given in the notes

# this method is for first n natural numbers
N = int(input("Enter the number: "))
print(f"Average of N numbers = {(N*(N+1))/2 /N}")

# second methode (o(n))
avg = 0
for i in range(N+1):
    avg = avg + i

print(avg/N)

