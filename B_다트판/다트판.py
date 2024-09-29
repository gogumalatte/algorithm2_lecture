'''
B번-다트판
'''

dart = list(map(int, input().split()))

bob = 10.5
alice = 0


for i in range(20):
    if dart[i] == 20:
        alice = (dart[(i-1)%20] + dart[i%20] + dart[(i+1)%20]) / 3
        break

if bob == alice:
    print("Tie")
elif bob > alice:
    print("Bob")
else:
    print("Alice")
