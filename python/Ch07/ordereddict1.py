d = {}
d['x'] = 100
d['l'] = 500
d['y'] = 200
d['z'] = 300

print(d)        # 선언한 순서대로 사전자료 d에 저장되는지는 보장할 수 없다 함.
# {'x': 100, 'l': 500, 'y': 200, 'z': 300}  -> 이 결과가 컴퓨터에 따라 다를 수 있다고 함.
# 수차례 반복하면 순서가 바뀔 수 있다고 하는데 아직 관찰된 바는 없음.

for k, v in d.items():
    print(k, v)
# x 100
# l 500
# y 200
# z 300