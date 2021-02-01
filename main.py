def star_triangle(endline):
    star = 1
    for i in range(endline,0, -1):
        print(' ' * i, '*'*star, ' ' * i)
        star += 2



star_triangle(5) 
print()       
print('솔이의 대 모험')
print()

print('='*167)

print()
print('''한가한 저녁... 솔이는 포트폴리오를 만들기 위해 노트북을 켰다.

[간만에 컴퓨터나 켜불까....??]

갑자기 모니터가 번쩍이더니 화면 속으로 솔이가 빨려 들어갔다.

[헐..!! 말도 안돼!! 내가 컴퓨터 속에 갇히다니!!]

''')


count = 0

while True:


    ans1 = input('''솔이가 컴퓨터에 갇혔습니다! 
주인공인 솔이를 도와 컴퓨터 밖으로 탈츨을 도우려면 1, 나 몰라라 할거라면 2 를 선택하세요 : 
''')

    if ans1 == str(1):
        print('역시 당신은 좋은 사람이군요!! 솔이가 컴퓨터 세계를 탈출할 수 있도록 도와주세요')
        break

    elif ans1 == str(2):
        print('''[으아아아악 ---- !!! 당신도 갇혀버렸네요]
        게임 종료 훙칫뿡''')
        break


    else:
        print('제발 다른 건 누르지 말아요! 묻는 말에 얼른 대답 좀!!!!!')
        count += 1


        if count >= 5:
            print('장난을 치다니 용서할 수 없군요!!! 솔이에게 케이쿠를 사주세요 훙훙')
            print('게임 종료 훙칫뿡')
            break


        print()
        continue

print()        
print('='*167)
print('에피소드 1) 솔이의 마스터소드')
print('='*167)
print()




print('='*167)

print()
print('''솔이는 컴퓨터 세계에 맞서 싸우기 위해 무기를 먼저 무기를 찾기로 했어요.

[아무래도 컴퓨터 속이니까 코딩으로 맞서 싸워야겠지...??]

깜깜한 터미널 동굴에 들어가 무기(프로그래밍 언어)를 찾기 시작했어요''')

print('솔이를 선택한 마스터소드의 이름은 과연 무엇일까요?')
ans2 = input('파이썬은 1, C++은 2, 자바는 3을 선택하세요 ')


while True:

    if ans2 == str(1) or ans2 == '파이썬':
        print()
        print('[나 귀도 반 로섬이 선택한 자여... 파이썬을 들어 에러를 처치하라..!!!]')
        print('명검 파이썬을 획득했어요 ◟( ˘ ³˘)◞ ')
        print('다음 스테이지 진출')
        print()
        break


    elif ans2 == str(2) or ans2 == 'C++':
        print()
        print('C++을 뽑자 칼 날이 저기 먼 다른 곳을 가리키더니 번쩍!! 하고 날라갔어요')
        print('솔이는 무기를 잃고 게임 종료')
        break

    elif ans2 == str(3) or ans2 == '자바':
        print()
        print('자바를 뽑아든 솔이...!!')
        print('[검이 너무 무거워서 휘두르질 못하겠어 ㅜㅜ]')
        print('솔이는 어깨가 빠져 게임 종료')
        break

    else:
        print()
        print('[그런 무기는 안보이는데?? 다시 확인해봐]')
        print()
        continue










