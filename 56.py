import csv
import time

data = csv.reader(open('gword.csv')) # 명언파일 불러오기
next(data) # 첫 행에 있는 제목내용 넘기기
gword = [] # 명언을 저장한 변수

# csv파일에서 불러온 데이터를 gword 변수에 저장하기
for row in data :
  gword.append(row[1])


print("근심 걱정이 많으시군요. 당신의 고민을 해결해 주는 처방을 내려드립니다.")
number = input("1에서 100사이의 숫자 중에서 마음에 드시는 숫자를 3초 안에 눌러주세요.")
print("당신의 깊은 고민은 아래의 처방으로 해결됩니다.")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("***********************************************************")
print(gword[int(number)%len(gword)])
print("***********************************************************")
