def grasshopper(s1: int, s2: int, s3: int) -> str:
    score: int = (s1+s2+s3)//3

    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'
    
def main() -> None:
    s1: int = int(input("Введите 1-ую оценку: "))
    s2: int = int(input("Введите 2-ую оценку: "))
    s3: int = int(input("Введите 3-ю оценку: "))

    print(grasshopper(s1, s2, s3))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("👌")