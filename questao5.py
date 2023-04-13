string = input()
reversa = ''

for i in range(len(string) - 1, -1, -1):
    reversa = reversa + string[i]

print (reversa)
