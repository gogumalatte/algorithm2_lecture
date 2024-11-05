def calculate_fourth_point(x1, y1, x2, y2, x3, y3, x4, y4):
    """
    평행사변형의 인접한 두 변의 좌표가 주어졌을 때 네 번째 점의 좌표를 계산합니다.
    
    Args:
        x1, y1: 첫 번째 변의 시작점 좌표
        x2, y2: 첫 번째 변의 끝점 좌표
        x3, y3: 두 번째 변의 시작점 좌표
        x4, y4: 두 번째 변의 끝점 좌표
    
    Returns:
        tuple: 네 번째 점의 (x, y) 좌표
    """
    # 두 변이 공유하는 점을 찾습니다
    if (x2, y2) == (x3, y3):
        shared_point = (x2, y2)
        p1 = (x1, y1)
        p3 = (x4, y4)
    elif (x2, y2) == (x4, y4):
        shared_point = (x2, y2)
        p1 = (x1, y1)
        p3 = (x3, y3)
    elif (x1, y1) == (x3, y3):
        shared_point = (x1, y1)
        p1 = (x2, y2)
        p3 = (x4, y4)
    else:  # (x1, y1) == (x4, y4)
        shared_point = (x1, y1)
        p1 = (x2, y2)
        p3 = (x3, y3)
    
    # 평행사변형의 성질을 이용하여 네 번째 점의 좌표를 계산합니다
    # 네 번째 점 = p1 + p3 - shared_point
    fourth_x = p1[0] + p3[0] - shared_point[0]
    fourth_y = p1[1] + p3[1] - shared_point[1]
    
    # 소수점 셋째 자리에서 반올림하여 mm 단위까지 표시
    return round(fourth_x, 3), round(fourth_y, 3)

def main():
    while True:
        try:
            # 8개의 실수를 입력받습니다
            coords = list(map(float, input().split()))
            if len(coords) != 8:
                break
                
            # 네 번째 점의 좌표를 계산합니다
            result = calculate_fourth_point(*coords)
            
            # 결과를 출력합니다 (소수점 셋째 자리까지)
            print(f"{result[0]:.3f} {result[1]:.3f}")
            
        except EOFError:
            break

if __name__ == "__main__":
    main()