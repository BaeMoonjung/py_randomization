import pandas as pd
import random
from string import ascii_uppercase

seed_n = int(input("임의의 숫자 9자리를 입력하세요:"))
participant_n = int(input("시험 대상자 수를 입력하시오:"))
group_n = int(input("시험 그룹 수를 입력하시오:"))
parallel = int(input("직렬 투약인 경우 1, 병렬 투약인 경우 2를 입력하시오:"))

# 무작위 배정 번호 생성

alphabet_list = list(ascii_uppercase)
randomization_n=[]
randomization_group = []  

# 직렬인 경우 무작위 번호 생성

if parallel == 1:
    for i in range(participant_n):
        s = "R" + str(101+i)
        randomization_n.append(s)    
    
    # 시험군 수에 따른 그룹 설정    
    
    for i in range(group_n):
        g = alphabet_list[i]
        randomization_group.append(g)

    randomization_group = randomization_group*int(participant_n/group_n)
        
    # 무작위 배정

    random.seed(seed_n)
    random.shuffle(randomization_group)

    df = pd.DataFrame({"무작위 번호":randomization_n, "투여군": randomization_group})
    df.to_excel("randomization.xlsx")
    print(df)

# 병렬인 경우 무작위 번호 생성       
        
if parallel == 2:
    for i in range(int(participant_n/2)):
        s = "R" + str(101+i)
        randomization_n.append(s)
    for i in range(int(participant_n/2)):
        s = "R" + str(201+i)
        randomization_n.append(s)
    
    # 시험군 수에 따른 그룹 설정          
      
    for i in range(int(group_n)):
        g = alphabet_list[i]
        randomization_group.append(g)

    randomization_group = randomization_group*int(participant_n/group_n)
            
    # 무작위 배정

    random.seed(seed_n)
    random.shuffle(randomization_group)

    df = pd.DataFrame({"무작위 번호":randomization_n, "투여군": randomization_group})
    df.to_excel("randomization.xlsx")
    print(df)