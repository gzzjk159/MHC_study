# BOJ 2089 - -2진수
# (-2)^0 = 1, (-2)^1 = -2, (-2)^2 = 4, (-2)^3 = -8 ... 제곱이 홀수이면 음수가 된다.
# 10진수 -13 일때 -2진수는 110111 이 된다.

# 1, 110, 111, 100, 101, 11010, 11011, 11000, 11001 .. 은 10진수 1부터 표현방식이다.
# a[0], a[3], a[4], a[1], a[2], ....
# 2개가 연속의 값이 나오고 반복한다는.. 뭔가 보이는 것 같은데 어렵다 이렇게 푸는게 아닌거같다

n = int(input())
binary = ''

if n == 0: # 0인경우를 추가하지않으면 틀렸습니다 출력됨..
    print(0)
    exit()

# 2진수를 구할 때와 동일하게 (bin이용 X) 구한다.
# 음수를 나눌 땐 나머지가 무조건 양수가 되도록 해야한다.
# 예로, -5를 3으로 나누는 경우, 몫이 -2, 나머지가 1이 된다.

while (n != 0) :
    if (n%-2!=0): # 나누어 떨어지지 않는 경우
            binary = '1' + binary # 변수에 '1'이라는 문자를 붙인다.
            # 나누어 떨어지지 않는 경우, 몫을 구하기 위한 +1
            n = n // -2 + 1 # n이 홀수일 경우, 소숫점 0.5가 발생한다.
            # 나머지는 양수여야하므로 +1을 하여 소숫점을 올림한다.

    else: # 나누어 떨어지는 경우
            binary = '0' + binary
            # 나누어 떨어지면 그대로 0만 추가
            n = n // -2

print(binary)