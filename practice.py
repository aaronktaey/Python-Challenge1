print('================ DATA TYPE START =================')
input("DATA TYPE 시작...")
a_string = "like this"
a_number = 3
a_float = 1.12
a_boolean = False 
a_none = None
a_list = [1,2,3,4]
a_tuple_single = ('a',)
a_tuple_single_x = ('a')
a_tuple_multi = ('a','b','c')
a_dictionary = {
  str:"taeyeon",
  "str":"useok",
  dict:('a','b','c')
}
print(str)
print(a_dictionary["str"])
print(a_dictionary[dict])

print('a_string : ',type(a_string)) 
print('a_number : ',type(a_number)) 
print('a_float : ',type(a_float)) 
print('a_boolean : ',type(a_boolean)) 
print('a_none : ',type(a_none)) 
print('a_list : ',type(a_list)) 
print('a_tuple_single : ',type(a_tuple_single)) 
print('a_tuple_single_x : ',type(a_tuple_single_x)) 
print('a_tuple_multi : ',type(a_tuple_multi)) 
input("DATA TYPE 끝...")
print('================ DATA TYPE END =================')


print('================ 조건문 START =================')

a = input("조건문 시작... 값을 입력하세요.")

if a == 'WHITE':
 print('if : 입력한 값은... 하얀색')
 print('if : 입력한 값은... 하얀색')
 print('if : 입력한 값은... 하얀색')
 print('if : 입력한 값은... 하얀색')
elif a == 'BLACK':
  print('elif : 입력한 값은... 검은색')
elif a == '' :
  print('elif empty : 입력한 값이 없습니다...')
else :
  print('else : 입력한 값은 ...',a)
  
input("조건문 끝...")
  
print('================ 조건문 END =================')


print('================ 반복문 START =================')

input("반복문 시작...")

weekdays_tuple = ('월','화','수','목','금','토','일')
weekdays = ''
for day in weekdays_tuple:
  weekdays = weekdays+day
print(weekdays)

input("반복문2 시작...")
weekdays = ''
for day in weekdays_tuple[:-1]:
  weekdays = weekdays+day
print(weekdays)

input("반복문3 시작...")
weekdays = ''
for day in weekdays_tuple[1:]:
  weekdays = weekdays+day
print(weekdays)

input("반복문4 시작...")
weekdays = ''
for day in weekdays_tuple[3:-2]:
  weekdays = weekdays+day
print(weekdays)

input("반복문 끝...")

print('================ 반복문 END =================')


print('================ 함수 START =================')

input("함수1 시작...")

def fun_no_param():
  print('no_param: ')

fun_no_param()

b = input("함수2 시작... 값을 입력하세요.")


input("함수 끝...")

print('================ 함수 END =================')

def fun_param(param1, param2):
  print('param1: ', param1)
  print('param2: ', param2)

fun_param(1,2)
