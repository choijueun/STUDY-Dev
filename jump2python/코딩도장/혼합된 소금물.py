args = []
for i in range(10):
    input_text = input('농도(%)와 질량(g)을 입력하시오:')
    if input_text == 'end' : break
    args.append(input_text)

weight_list = []
salt_list = []
for val in args:
    val = val.strip()
    
    water_weight = float(val[val.rfind(' ')+1 : val.find('g')])
    weight_list.append(water_weight)
    salt_list.append(float(val[:val.find('%')]) * water_weight / 100)

result_percent = round(sum(salt_list)*100/sum(weight_list), 2)
result_percent = str(result_percent)+'%'
result_weight = str(round(sum(weight_list),2))+'g'

print(result_percent, result_weight)
