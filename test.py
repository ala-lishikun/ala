# encoding: utf-8
import random
from AllFunc import *
'''
all_path = 'D:\PycharmProjects\pythoncodes\CreateData\conf\/all.txt'
al_path = 'D:\PycharmProjects\pythoncodes\CreateData\conf\/al.txt'
alone = []
all_key = []
all_value = []
with open(al_path, 'r') as fd:
    al_data = fd.readlines()
    for j in range(0, len(al_data)):
        al = al_data[j].split()[0]
        alone.append(al)
with open(all_path, 'r') as file:
    data = file.readlines()
    for i in range(0,len(data)):
        value = data[i].split()[0]
        key=data[i].split()[1]
        all_key.append(key)
        all_value.append(value)
    my_dict = dict(zip(all_key,all_value))
    for key in my_dict:
        if key in alone:
             print(key,my_dict[key])
'''




#
# kk = []
# with open(person_path, 'r') as file:
#     data = file.readlines()
#     for i in range(1, len(data)):
#         kk.append(data[i].split(',')[1:3])
# print(kk)
# print(kk[random.randint(0, len(kk))][0])
'''
# 随机1000个数字，去重排序
L = []
a = []
for i in range(0, 1000):
    a.append(random.randint(0, 1000))
[L.append(h) for h in a if not h in L]
print(sorted(L))

# 输出元素出现的次数（第三方库）
import collections
a = []
for i in range(0, 1000):
    a.append(random.randint(0, 1000))
L = collections.Counter(a)
print(L)

# 输出元素出现的次数（字典）
a = [1,1,2,5,8,8,8,8]
d = {}
for c in a:
    if c in d:
        d[c]=d[c]+1
    else:
        d[c]=1
print(d)
# 字典通过values排序


def ala(data):
   for j in range(len(data)-1):
      for i in range(len(data)-1):
        if data[i]>data[i+1]:
           data[i], data[i + 1] = data[i + 1], data[i]
   print(data)

numbers = [5,9,3,8,6,4,1,2,0]
print(ala(numbers))




# def is_true(s):
#     if s in string.printable:
#         return 0
#     else:
#         return 1
# def main():
#     s = input("请输入：")
#     if is_true(s)==0:
#         print('True')
#     else:
#         print('False')
# if __name__ == '__main__':
#     main()




# def quick_sort(lists, left, right):
#     if left >= right:
#        return lists
#     key = lists[left]
#     low = left
#     high = right
#     while left < right:
#         while left < right and lists[right] >= key:
#             right -= 1
#         lists[left] = lists[right]
#         while left < right and lists[left] < key:
#             left += 1
#         lists[right] = lists[left]
#     lists[right] = key
#     quick_sort(lists, low, left - 1)
#     quick_sort(lists, left + 1, high)
#     return lists
#
# if __name__ == '__main__':
#      print(quick_sort([6,7,8,1,9],0,4))



#20输出一次
low = 0
high = 300
step = 20
while low < high:
    C = 5 * (low - 32) / 9
    print("%d\t %d\n" %(low, C))
    low += step

for i in range(0,300,20):
    C = 5 * (i - 32) / 9
    print(i,C)



def get_num(digit_number):
    data = []
    count = []
    for i in range(digit_number+1):
        data.append(i)
    for j in range(len(data)):
        if str(3) in str(data[j]):
            count.append(data[j])
    print(count)
    c = str(count)
    return c.count('3')
if __name__ == '__main__':
    print(get_num(14))

def del_ele(a,b):
    r = ''
    for i in [x for x in a if x not in b]:
        r = r+i

    return r
print(del_ele('asdb','sd'))
'''
import pandas as pd
import random
from tqdm import tqdm
import string

# data = []
# data1 = []
# data2 = []
# wb_ent = []
# with open('D:\PycharmProjects\DataCode\conf\T1.txt', 'r') as file:
#     data.append(file.readlines())
# for i in tqdm(range(100001)):
#     data1.append(data[0][0:7])
#     data2.append(data[0][-7:])
#     code = random.sample(data1[0],1)
#     address = random.sample(data2[0],1)
#     wb_ent.append([code, address])
# df = pd.DataFrame(wb_ent, columns=['code', 'address'])
# df.to_csv('output/' + str(i) + '_wb.csv')
# datas = []
# adr = []
# with open('D:\PycharmProjects\DataCode\conf\jichang.txt', 'r') as file:
#     for i in range(4):
#         datas.append(file.readline())
# print(len(datas))
# adr_list = []
# hotel_path = 'D:\PycharmProjects\Datacode\conf\hotel.txt'
# with open(hotel_path, 'r', encoding='utf-8') as fd:
#     data = fd.readlines()
# for i in range(0, len(data)):
#     adr_list.append(data[i].strip('\n'))
# print(data[0:3])
from datetime import timedelta
import time

goods_dict = {

    "001": {"name": "爱马仕腰带", "price": 1999},

    "002": {"name": "劳力士男表", "price": 19999},

    "003": {"name": "巴宝莉眼镜", "price": 4999},

    "004": {"name": "路虎发现四", "price": 99999}

}

shop_car = []
while True:
    print('------------------' + '商品列表' + '---------------------')
    print('商品编号' + '        ' + '商品名称' + '         ' + '商品价格')
    number = goods_dict.keys()
    name = goods_dict.values()
    for i in number:
        print(i + '           ' + goods_dict.get(i)['name'] + '           '
              + str(goods_dict.get(i)['price']))
    t = input('请输入你想要的商品编号，退出请输入Q:')
    if t != 'Q':
        if t in number:
            while True:
                count = input("请输入你想要的数量：")
                if count.isdigit():
                    goods_dict[t]['count']=count
                    shop_car.append(goods_dict.get(t))
                    break
                else:
                    continue
            print('商品加入购物车成功')
        else:
            print("输入的商品编号错误,请重新输入")

    else:
        print('结束购物')
        break

print('---------------------欢迎来到订单结算页面---------------------')
for i in range(len(shop_car)):
    print('商品名称:' + shop_car[i]['name']+'      '+'商品单价:'+ str(shop_car[i]['price'])
          +'      '+'数量:'+str(shop_car[i]['count'])+'     '+
          '商品总价:' + str(int(shop_car[i]['price']) * int(shop_car[i]['count'])))
Sum = 0
for i in range(len(shop_car)):
    Sum = Sum + int(shop_car[i]['price']) * int(shop_car[i]['count'])
print('订单总额:' + str(Sum))

while True:
    pay = input('请您付款:')
    if pay.isdigit():
            if int(pay) == Sum:
                print('付款成功')
                break
            elif int(pay) < Sum:
                print('付款失败，输入金额小于定单总额！')
            elif int(pay) > Sum:
                print("付款成功，找您"+str(int(pay)-Sum)+'元!')
                break
    elif pay in string.ascii_letters or string.punctuation:
        print('请输入合法金额！')

print('--------------------------本次购物结束，期待您的下次光临------------------------')


