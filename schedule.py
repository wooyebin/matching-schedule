## 커플시간표

from scipy import spatial


# 과목 시간표 불러오기---서버랑 연결해서??아직모르겠음
subject = {"공학수학 1" : [["ENGR211009 정재정","TUE1A1B2A","THU2B3A3B"],
                       ["ENGR211010 정재정","TUE2B3A3B","THU1A1B2A"],
                       ["ENGR211007 이균경", "MON1A1B2A","WED2B3A3B"],
                       ["ENGR211002 이상문", "MON5B6A6B","WED7A7B8A"],
                       ["ENGR211001 이동호","MON5B6A6B","WED7A7B8A"],
                       ["ENGR211002 이상문","MON5B6A6B","WED7A7B8A"],
                       ["ENGR211003 박준구","MON5B6A6B","WED7A7B8A"]],
           "나의 첫 사업계획서":[["STUP224001 변수룡","MON2B3A3B","FRI1A1B2A"]],
           "기초전자수학" : [["ELEC214001 한준구", "TUE1A1B2A","THU2B3A3B"],
                       ["ELEC214002 최영숙","TUE1A1B2A","THU2B3A3B"],
                       ["ELEC214003 도윤선","TUE1A1B2A","THU2B3A3B"],
                       ["ELEC214004 최현철","TUE1A1B2A","THU2B3A3B"],
                       ["ELEC214006 태흥식","TUE7A7B8A","THU8B9A9B"]],
           "이산수학" : [["COME301001 최현석","MON1A1B2A","MON2B3A3B"],
                     ["COME301002 신미영","WED7A7B8A","FRI1A1B2A"],
                     ["COME301004 소현주","MON1A1B2A","WED5B6A6B"],
                     ["COME301006 소현주","MON5B6A6B","WED2B3A3B"],
                     ["COME301010 아난드 폴","TUE7A7B8A","THU5B6A6B"]],
           "전자회로1" : [["ELEC245001 차한영","TUE8B9A9B","THU8B9A9B"],
                      ["ELEC245009 박종후","TUE5B6A6B","THU5B6A6B"],
                      ["ELEC245004 유상대","MON5B6A6B","FRI5B6A6B"],
                      ["ELEC245007 정연배","TUE2B3A3B","THU7A7B8A"]],
           "자료구조" : [["COME331014 김용태","MON1A1B2A","MON2B3A3B"],
                     ["COME331008 김종화","MON7A7B8A","WED2B3A3B"],
                     ["COME331010 최영숙","MON5B6A6B","WED5B6A6B"],
                     ["COME331005 이경숙", "TUE5B6A6B","THU2B3A3B"],
                     ["COME331006 정임영","WED1A1B2A","FRI5B6A6B"]],
          "기초전자물리학":[["ELEC213001 박홍식","MON7A7B8A","WED8B9A9B"],
                    ["ELEC213005 우경성","WED1A1B2A","FRI2B3A3B"],
                    ["ELEC213006 박정일","WED1A1B2A","FRI2B3A3B"]],
          "C프로그래밍과실습":[["EECS201001 이석진","WED1A1B2A2B","WED3A3B4A4B"],
                    ["EECS201003 최두현","MON1A1B2A2B","MON3A3B4A4B"],
                    ["EECS201006 이동익","THU6A6B7A7B","THU8A8B9A9B"]],
          "기초전자실험 및 설계":[["ELEC211001 김영모","MON6A6B7A7B","MON8A8B9A9B"],
                    ["ELEC211003 장재원","WED6A6B7A7B","WED8A8B9A9B"],
                    ["ELEC211004 배진혁","THU1A1B2A2B","THU3A3B4A4B"]],
          "전자공학실험2":[["ELEC252001 최태호","MON6A6B7A7B","MON8A8B9A9B"],
                    ["ELEC252007 윤병주","FRI6A6B7A7B","FRI8A8B9A9B"],
                    ["ELEC252005 최봉열","TUE1A1B2A2B","TUE3A3B4A4B"],
                    ["ELEC252008 최태호","MON1A1B2A2B","MON3A3B4A4B"],
                    ["ELEC252005 최봉열","THU1A1B2A2B","THU3A3B4A4B"]],
           "파이선 프로그래밍":[["CLTR268002 조규철","FRI1A1B2A2B","FRI3A3B4A4B"],
                    ["CLTR268003 정설영","FRI1A1B2A2B","FRI3A3B4A4B"]],
           "경영의 이해":[["CLTR085001 장성희","TUE7A7B8A","THU7A7B8A"],
                    ["CLTR085002 고성훈","TUE1A1B2A","THU2B3A3B"],
                    ["CLTR085004 마윤주","MON1A1B2A","WED2B3A3B"],
                    ["CLTR085006 박찬권","MON5A5B6A","FRI5B6A6B"]]}

# 시간을 숫자로 변환
for i in subject:
    subList = []
    for j in range(len(subject.get(i))):
        subList.append([subject.get(i)[j][0]])
        for k in range(1,len(subject.get(i)[j])):
            time = subject.get(i)[j][k]
            day = time[0:3]
            if day == "MON":
                dayNumber = 0
            elif day == "TUE":
                dayNumber = 100
            elif day == "WED":
                dayNumber = 200
            elif day == "THU":
                dayNumber = 300
            elif day == "FRI":
                dayNumber = 400
            elif day == "SAT":
                dayNumber = 500
            else:
                dayNumber = 600
                
            if time[4] == "A":
                timeNumber1 = int(time[3])*2-1
            else:
                timeNumber1 = int(time[3])*2
            if time[-1] == "A":
                timeNumber2 = int(time[-2])*2-1
            else:
                timeNumber2 = int(time[-2])*2

            
            number1 = dayNumber+timeNumber1
            number2 = dayNumber+timeNumber2
            
            subList[j].append([number1,number2])
    subject[i] = subList


### 함수들
# 입력값에 따라 타임 가져오기
def get_schedule(subjectList):
    global subject
    schedule = dict()
    for i in subjectList:
        list = subject.get(i)
        schedule[i] = list
    return schedule

# 우선, 중복포함한 시간표 만들기---보완필요
def make_timetable(subject, times):
    length = len(subject)
    if length == 1:
        list1 = [[i] for i in times.get(subject[0])]
    elif length == 2:
        list1 = [[i,j] for i in times.get(subject[0]) for j in times.get(subject[1])]
    elif length == 3:
        list1 = [[i,j,k] for i in times.get(subject[0]) for j in times.get(subject[1])\
                 for k in times.get(subject[2])]
    elif length == 4:
        list1 = [[i,j,k,l] for i in times.get(subject[0]) for j in times.get(subject[1])\
                 for k in times.get(subject[2]) for l in times.get(subject[3])]
    elif length == 5:
        list1 = [[i,j,k,l,m] for i in times.get(subject[0]) for j in times.get(subject[1])\
                 for k in times.get(subject[2]) for l in times.get(subject[3]) \
                 for m in times.get(subject[4])]
    elif length == 6:
        list1 = [[i,j,k,l,m,n] for i in times.get(subject[0]) for j in times.get(subject[1])\
                 for k in times.get(subject[2]) for l in times.get(subject[3]) \
                 for m in times.get(subject[4]) for n in times.get(subject[5])]
    elif length == 7:
        list1 = [[i,j,k,l,m,n,o] for i in times.get(subject[0]) for j in times.get(subject[1])\
                 for k in times.get(subject[2]) for l in times.get(subject[3])\
                 for m in times.get(subject[4]) for n in times.get(subject[5])\
                 for o in times.get(subject[6])]
    elif length == 8:
        list1 = [[i,j,k,l,m,n,o,p] for i in times.get(subject[0]) for j in times.get(subject[1])\
                 for k in times.get(subject[2]) for l in times.get(subject[3])\
                 for m in times.get(subject[4]) for n in times.get(subject[5])\
                 for o in times.get(subject[6]) for p in times.get(subject[7])]
    elif length == 9:
        list1 = [[i,j,k,l,m,n,o,p,q] for i in times.get(subject[0]) for j in times.get(subject[1])\
                 for k in times.get(subject[2]) for l in times.get(subject[3])\
                 for m in times.get(subject[4]) for n in times.get(subject[5])\
                 for o in times.get(subject[6]) for p in times.get(subject[7])\
                 for q in times.get(subject[8])]                      
    elif length == 10:
        list1 = [[i,j,k,l,m,n,o,p,q,r] for i in times.get(subject[0]) for j in times.get(subject[1])\
                 for k in times.get(subject[2]) for l in times.get(subject[3])\
                 for m in times.get(subject[4]) for n in times.get(subject[5])\
                 for o in times.get(subject[6]) for p in times.get(subject[7])\
                 for q in times.get(subject[8]) for r in times.get(subject[9])]
    return list1

# 중복제거
def duplicate(table):
    remove=[]
    for i in table:
        tf = 1
        check = []
        for j in i:
            for k in range(1,len(j)):
                check.append(j[k])
        for m in range(len(check)-1):
            for n in range(m+1,len(check)):
                a = check[m][0]
                b = check[m][1]
                c = check[n][0]
                d = check[n][1]
                if (a-c)*(a-d)>0 and (b-c)*(b-d)>0 and (a-c)*(b-d)>0:
                    tf = tf*1
                else:
                    tf = tf*0
        if tf==0:
            remove.append(i)
    for i in remove:
        table.remove(i)
    return table

# 숫자로 변환, 정렬까지
def convert_to_number(timetable):
    numberList = []
    for i in range(len(timetable)):
        numberList.append([])
        for j in timetable[i]:
            for k in range(1, len(j)):
                a=j[k][0]
                b=j[k][1]
                if b-a<=1:
                    numberList[i].append(a)
                    numberList[i].append(b)
                else:
                    number=1
                    numberList[i].append(a)
                    while not(a+number>b):
                        numberList[i].append(a+number)
                        number+=1
        numberList[i]=sorted(numberList[i])
        divisionList = [[]]*7
        for element in numberList[i]:
            if element <100:
                divisionList[0].append(element)
            elif element <200:
                divisionList[1].append(element)
            elif element <300:
                divisionList[2].append(element)
            elif element <400:
                divisionList[3].append(element)
            elif element <500:
                divisionList[4].append(element)
            elif element <600:
                divisionList[5].append(element)
            else:
                divisionList[6].append(element)
        numberList[i]=divisionList
            
    return numberList

# 유사도 분석 및 최대값 구하기
def calculate_similarity(list1,list2):
    result = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            similar = 0
            for first in list1[i]:
                for second in list2[j]:
                    similar += 1 - spatial.distance.cosine(first, second)
            result.append([i,j,similar])
    max = [0]
    for per in range(len(result)):
        if result[per][2] > max[0]:
            max = [result[per][2],per]
        elif result[per][2] == max[0]:
            max.append(per)
    resultMax = []
    for good in range(1,len(max)):
        resultMax.append(result[max[good]])
    return resultMax

def main():
    # 과목 입력---input으로 받을 예정
    right=1
    person1 = ["공학수학 1", "나의 첫 사업계획서","기초전자수학","기초전자물리학",
               "C프로그래밍과실습", "기초전자실험 및 설계"]
    person2 = ["이산수학", "전자회로1", "자료구조", "전자공학실험2","파이선 프로그래밍","경영의 이해"]
    while right == 1:
        person1subject = input("person1 과목을 입력하세요. 다 입력하면 0을 입력하세요:")
        if person1subject != "0":
            person1.append(person1subject)
        else:
            right = 0
    while right == 0:
        person2subject = input("person2 과목을 입력하세요. 다 입력하면 0을 입력하세요:")
        if person2subject != "0":
            person2.append(person2subject)
        else:
            right = 1
    
    # getSchedule 함수 사용
    person1Sub = get_schedule(person1)
    person2Sub = get_schedule(person2)
    
    # makeTimetable 함수 사용
    person1Timetable = make_timetable(person1, person1Sub)
    person2Timetable = make_timetable(person2, person2Sub)
    
    # duplicate 함수 사용
    person1Timetable = duplicate(person1Timetable)
    person2Timetable = duplicate(person2Timetable)

    # convert_to_number 함수 사용
    person1numberList = convert_to_number(person1Timetable)
    person2numberList = convert_to_number(person2Timetable)
    
    # calculate_similarity 함수 사용
    resultMax=calculate_similarity(person1numberList,person2numberList)

    # 결과 도출
    for maxlist in resultMax:
        print(person1Timetable[maxlist[0]],person2Timetable[maxlist[1]])
    
    
main()
