# 빨간색: 620nm 이상 780nm 이하
# 주황색: 590nm 이상 620nm 미만
# 노란색: 570nm 이상 590nm 미만
# 초록색: 495nm 이상 570nm 미만
# 파란색: 450nm 이상 495nm 미만
# 남색: 425nm 이상 450nm 미만
# 보라색: 380nm 이상 425nm 미만
# 별의 색을 출력한다. 빨간색이면 "Red", 주황색이면 "Orange", 노란색이면 "Yellow", 초록색이면 "Green", 파란색이면 "Blue", 남색이면 "Indigo", 보라색이면 "Violet"을 출력한다.

n = int(input())

if n >= 620 and n <= 780:
    print("Red")
elif n >= 590 and n < 620:
    print("Orange")
elif n >= 570 and n < 590:
    print("Yellow")
elif n >= 495 and n < 570:
    print("Green")
elif n >= 450 and n < 495:
    print("Blue")
elif n >= 425 and n < 450:
    print("Indigo")
else:
    print("Violet")