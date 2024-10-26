zero_32bit = [0 for _ in range(32)]
num = int(input())
component_num = 2**32 - num
num_bit = bin(num)[2:]
component_bit = bin(component_num)[2:]

answer = 32 - len(num_bit)
compare_bit = component_bit[answer: ]
for i in range(len(compare_bit)):
    if compare_bit[i] != num_bit[i]:
        answer += 1
print(answer)
