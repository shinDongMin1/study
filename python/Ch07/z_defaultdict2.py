"""
# -----------------------------------------------------------------------------
# 1) 사전 자료의 생성과 수정
# -----------------------------------------------------------------------------
d = {'a': 3, 'v': 9, 'z': 4}
print(d.keys())
# dict_keys(['a', 'v', 'z'])

d['q'] = 8              # 키를 지정하면서 value를 지정
print(d.keys())
# dict_keys(['a', 'v', 'z', 'q'])


# -----------------------------------------------------------------------------
# 2) list 자료에서 자료의 출현 회수를 기록하는 사전 자료 만들기(1/2)
# 다음 list에서 a, b, c가 몇 개인지 사전 자료형으로 만드시오.
# key=a, b, c.  value=갯수
# -----------------------------------------------------------------------------

# 방법 1 - dict.keys()에 있는지를 활용
s = ['a', 'b', 'c', 'b', 'a', 'b', 'c']
dic = {}
for i in s:                     # i는 key
    if i not in dic.keys():
        dic[i] = 0          # 키를 지정하면서 value를 지정
    dic[i] += 1             # key i의 값을 하나 증가.

print(dic)
# {'a': 2, 'b': 3, 'c': 2}


# 방법 2 - setdefault() 활용
s = ['a', 'b', 'c', 'b', 'a', 'b', 'c']
d = {}
for k in s:
    d.setdefault(k, 0)  # key에 k가 없으면 해당 value에 0을 넣는다. 있으면 기존의 value를 반환한다.=> 안씀.
    d[k] += 1

print(d)
# {'a': 2, 'b': 3, 'c': 2}

print(list(d.items()))
# [('a', 2), ('b', 3), ('c', 2)]

exit(0)
"""



# ---------------------------------------------------------------------------------------------------
# 3) list 자료에서 자료의 출현 회수를 기록하는 사전 자료 만들기
#  특정 color의 수량 합산을 구하시오.
# ---------------------------------------------------------------------------------------------------

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
print(type(s), s)
# <class 'list'> [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]


# 빈 사전자료형에 key가 있는지의 여부에 따라 value를 합산할지를 판단
t = {}

for k, v in s:
    if not k in t:
        t[k] = 0
    t[k] += v       # 특정 key에 value를 누적 합산하는 연산

print(t)
# {'yellow': 4, 'blue': 6, 'red': 1}


# ---------------------------------------------------------------------------------------------------
# 4) list 자료에서 자료의 출현 회수를 기록하는 사전 자료 만들기
#  특정 color의 수량 합산을 구하시오.
# 이 방법이 교재 defaultdict3.py와 가장 유사함.
# ---------------------------------------------------------------------------------------------------

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]


d = {}
for k, v in s:
    d.setdefault(k, []).append(v)
print(d)
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}

t = {}
for k, v in d.items():
    t[k] = sum(v)
print(t)
# {'yellow': 4, 'blue': 6, 'red': 1}

