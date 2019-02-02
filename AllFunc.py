# coding: utf8
import random
from datetime import timedelta
from datetime import date
import string
import time
global name_list
global tellist
global email_list
from faker import Faker
f=Faker(locale='zh_CN')
def generateTime(start, end):
    timestamp = random.randint(start, end)
    timeArray = time.localtime(timestamp)
    timestr = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return timestr


# def getXing():
#     xing = []
#     with open('conf/xing.txt', encoding='utf-8', errors='ignore') as file:
#         data = file.read()
#         xlist = data.split('\n')
#     for xl in xlist:
#         xing.append(xl)
#     return xing
#
#
# def getMing():
#     ming = []
#     with open('conf/ming.txt', encoding='utf-8', errors='ignore') as file:
#         data = file.read()
#         mlist = data.split('\n')
#     for ml in mlist:
#         ming.append(ml)
#     return ming


# def generateName():
#     name_list=f.name()
#     return name_list





def get_Birth():
    date = f.ssn()
    birth = date[6:14]
    return birth


def getTel():
    tel = f.phone_number()
    return tel


def getGender():
    gender_list = ['男', '女']
    return random.choice(gender_list)


def getMarry():
    marr_list = ['已婚', '未婚', '离异']
    return random.choice(marr_list)


def getAge(id):
    id = id[6:10]
    age = 2017 - int(id)
    return age


def getEdu():
    edulist = ['本科', '硕士', '博士', '高中', '小学', '初中文化']
    return random.choice(edulist)


def getEmail():
    mail = []
    with open('conf/emails.txt', encoding='utf-8',errors='ignore') as file:
        data = file.read()
        mailist = data.split('\n')
    for l in mailist:
        mail.append(l)
    # newchars = ''
    # for i in range(ord('a'), ord('z') + 1):
    #     newchars = newchars + chr(i)
    # print(newchars)
    # email = "0123456789" + newchars + newchars.upper()
    # print(email)
    # email = ''.join((i) for i in random.sample(email,7)) + mail[random.randint(0, len(mail)-1)]
    return mail

def getQq():
    qq = random.randint(100000000,999999999)
    return qq

def gen_loc():
    loc = list(string.printable[0:-38])
    location = ''.join(random.sample(loc, 4))
    return location

def gen_mz():
    mz = random.choice(['汉族', '满族', '回族', '维吾尔族', '蒙古族', '藏族'])
    return mz

def get_sg():
    sg = random.randint(160, 190)
    return sg

def get_school():
    school = random.choice(['北京大学', '天津大学', '南开大学', '北京理工大学', '华中科技大学', '武汉大学'])
    return school

def get_hk():
    hk = random.choice(['农业户口', '城镇户口', '非农业家庭户口'])
    return hk

def get_xx():
    xx = random.choice(['A', 'AB', 'O'])
    return xx

def gen_carjn():
    loc = list(string.printable[0:-38])
    carjn = ''.join(random.sample(loc, 17))
    return carjn


def gen_carn():
    car_list = []
    with open('conf/car.txt', encoding='utf-8', errors='ignore') as file:
        data = file.read()
        car = data.split('\n')
    for i in car:
        car_list.append(i)
    Carn = random.choice(car_list) + str(random.randint(10001, 99999))
    return Carn


def gen_band():
    carbrandlist = ['奔驰', '宝马', '奥迪', '玛莎拉蒂', '五菱宏光', '路虎', '大众', '比亚迪', '丰田', '英菲尼迪', '雷克萨斯', '斯巴鲁', '保时捷', '雷诺', '标志',
                    '凯迪拉克', 'Jeep', '雪铁龙', '福特', '捷豹', '柯尼塞克', '迈巴赫', '宾利', '本田', '日产', '特斯拉']
    car_band = random.choice(carbrandlist)
    return car_band

def gen_color():
    carColor = ['红色', '黄色', '绿色', '黑色', '白色', '银色', '粉色', '蓝色']
    car_color = random.choice(carColor)
    return car_color

def gen_type():
    car_list = ['大型汽车', '小型汽车', '警用汽车','使馆汽车','领馆汽车','境外汽车','外籍汽车','普通摩托车','轻便摩托车','使馆摩托车','领馆摩托车','境外摩托车','外籍摩托车','低速车','拖拉机','挂车','教练汽车','教练摩托车','试验汽车','试验摩托车','临时入境汽车','临时入境摩托车','临时行驶车','警用摩托车','原农机号牌','香港出入境车',
                '澳门出入境车','武警号牌','无号牌','假号牌','挪用号牌','其他号牌']
    car_type = random.choice(car_list)
    return car_type

def gen_classNum():
    num = random.randint(10, 80)
    l = ['A','B','C','D','E','F']
    classNum = str(num)+random.choice(l)
    return classNum

def gen_time():
    a1 = (2017,1,1,0,0,0,0,0,0)
    a2 = (2017,1,2,23,59,59,0,0,0)
    start = time.mktime(a1)
    end = time.mktime(a2)
    for i in range(10):
        t = random.randint(start,end)
        date = time.localtime(t)
        ti = time.strftime("%Y-%m-%d %H:%M:%S",date)
    return ti

if __name__ == '__main__':
    print(getEmail())