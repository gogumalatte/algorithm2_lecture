import sys

def ask(person):
    print(f"? {person}")
    sys.stdout.flush()
    response = int(input())
    return response

def find_birthday(people):
    possible_birthday = None
    
    for person in people:
        first_answer = ask(person)
        second_answer = ask(person)
        
        # 두 번 모두 1이면 생일 확정
        if first_answer == 1 and second_answer == 1:
            print(f"! {person}")
            sys.stdout.flush()
            return
        
        # 한 번만 1이면 거짓말 가능성
        if first_answer == 1 or second_answer == 1:
            possible_birthday = person
    
    # 만약 두 번 모두 1인 사람이 없으면, 한 번만 1이었던 사람이 생일임
    if possible_birthday:
        print(f"! {possible_birthday}")
        sys.stdout.flush()

def main():
    N = int(input())
    people = [input().strip() for _ in range(N)]
    
    find_birthday(people)

if __name__ == "__main__":
    main()
