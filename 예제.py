#https://wikidocs.net/7014
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#위 UTF-8 설정으로 한글 출력 
def p(a ):
    print(a)
p("Hello Wolrd!")
p("Mary's cosmetics")
p("신씨가 소리질렀다. \"도둑이야\".")
p('"C:\\Windows"')
p('안녕하세요.\n 만나서\t\t반갑습니다.')
print("naver", "kakao", "samsung", sep=";")#sep은 칸사인에 문자 변경
print("naver", "kakao", "samsung", sep="|")#sep은 칸사인에 문자 변경
print("first");print("second")#;은 한줄에 여러개의 명령을 작성 할때 사용


삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)


시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))


에어컨 = 48584
할부 = 36
총금액 = 에어컨 * 할부

print(총금액)

letters = 'python'

print(letters[0]);print(letters[2])

license_plate = "24가 2210"
print(license_plate[-4:])
string = "홀짝홀짝홀짝"
print(string[::2])