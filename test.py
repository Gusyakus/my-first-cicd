from app import sum

def test_sum():
    assert sum(2, 3) == 5, "2 + 3 должно быть 5"
    assert sum(-1, 1) == 0, "-1 + 1 должно быть 0"
    print("Все тесты пройдены!")

if __name__ == "__main__":
    test_sum()

