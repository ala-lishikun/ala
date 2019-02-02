# -*- coding: utf-8 -*-

from AllFunc import *
from tqdm import tqdm
import datetime
from datetime import timedelta
import pandas as pd
from faker import Faker
f=Faker(locale='zh_CN')
global car_n
global car_type
import csv
car_n = gen_carn()
car_type = gen_type()



def genPersonlist(num):
    personlist = []
    tellist = getTel()
    email_list = getEmail()
    pre_mail = []
    for i in range(62):
        pre_mail.append(string.printable[:62][i])
    for i in tqdm(range(0, num)):
        name = f.name()
        Id = f.ssn()
        XB = getGender()
        Ma = getMarry()
        Ed = getEdu()
        sg = get_sg()
        mz = gen_mz()
        qq = getQq()
        school = get_school()
        xx = get_xx()
        Tel = f.phone_number()
        Em = ''.join((i) for i in random.sample(pre_mail,7)) + random.choice(email_list)
        Birth = Id[6:14]
        personlist.append([name, Id, Birth, XB, Ma, Ed, Tel, Em, mz, sg, qq, school, xx])
    df = pd.DataFrame(personlist, columns=['姓名', '身份证号', '出生日期', '性别', '婚姻状况', '学历', '手机号', '邮箱', '民族', '身高', 'QQ', '毕业院校','血型'])
    df.to_csv('output/' + str(num) + '_person.csv')
    return 'output/' + str(num) + '_person.csv'


def genTelenvent(personlist, num):
    start_timestamp = int(time.mktime(time.strptime("2017-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")))
    end_timestamp = int(time.mktime(time.strptime("2018-03-01 00:00:00", "%Y-%m-%d %H:%M:%S")))
    tel_list = []
    adr_list = []
    phone = []
    person_path = personlist
    hotel_path = 'conf\hotel.txt'
    with open(hotel_path, 'r', encoding='utf-8') as fd:
        data = fd.readlines()
    for i in range(0, len(data)):
        adr = data[i].split()[0]
        adr_list.append(adr)

    with open(person_path, 'r') as file:
        data = file.readlines()
        for i in range(1, len(data)):
            #phone.append(data[i].split(',')[7])
            phone.append(data[i].split(',')[7])
    # phone.append('13805151233')
    for i in tqdm(range(0, num)):
        calltime = generateTime(start_timestamp, end_timestamp)
        endtime = datetime.datetime.strptime(calltime, "%Y-%m-%d %H:%M:%S") + timedelta(minutes=random.randint(0, 20))
        talktime = int(time.mktime(time.strptime(str(endtime), "%Y-%m-%d %H:%M:%S"))) - int(
            time.mktime(time.strptime(str(calltime), "%Y-%m-%d %H:%M:%S")))

        calltel = random.choice(phone)
        getcall = random.choice(phone)
        # if calltel == '13805151233':
        #     getcall = random.choice(phone)
        if calltel == getcall:
                getcall = random.choice(phone)
        # else:
        #     getcall = '13805151233'
        callAdr = random.choice(adr_list)
        getcallAdr = random.choice(adr_list)

        call_loc_loc = gen_loc()
        call_loc_cel = gen_loc()
        get_loc_loc = gen_loc()
        get_loc_cel = gen_loc()

        tel_list.append(
            [calltel, getcall, calltime, endtime, callAdr, call_loc_loc, call_loc_cel, get_loc_loc, get_loc_cel,
             getcallAdr, talktime])
    df = pd.DataFrame(tel_list, columns=['拨打电话', '接听电话', '拨打时间', '接听时间', '拨打地址', '拨打基站lac',
                                         '拨打基站cel', '接听基站lac', '接听基站cel', '接听地址', '通话时长'])
    df.to_csv('output/' + str(num) + '_tel.csv')



def genExpress(personlist, num):
    start_timestamp = int(time.mktime(time.strptime("2018-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")))
    end_timestamp = int(time.mktime(time.strptime("2018-03-01 00:00:00", "%Y-%m-%d %H:%M:%S")))
    express_list = []
    adr_list = []
    phone = []
    name = []
    person_path = personlist
    address_path = 'conf\/address.txt'

    with open(address_path, 'r', encoding='utf-8') as fd:
        data = fd.readlines()
    for i in range(0, len(data)):
        adr_list.append(data[i].strip('\n'))

    with open(person_path, 'r') as file:
        data = file.readlines()
        for i in range(1, len(data)):
            phone.append(data[i].split(',')[7])
            name.append(data[i].split(',')[1])

    for index in tqdm(range(0, num)):
        stime = generateTime(start_timestamp, end_timestamp)
        rtime = datetime.datetime.strptime(stime, "%Y-%m-%d %H:%M:%S") + timedelta(days=1)
        rtel = random.choice(phone)
        # rtel = 18170559928
        stel = random.choice(phone)
        if rtel == stel:
            stel = random.choice(phone)
        rname = random.choice(name)
        sname = random.choice(name)
        if rname == sname:
            sname = random.choice(name)
        payment = random.choice(['到付', '寄付', '第三方支付'])
        callAdr = random.choice(adr_list)
        getcallAdr = random.choice(adr_list)
        express_list.append([sname, stel, stime, payment, rname, rtel, rtime,callAdr,getcallAdr])
    df = pd.DataFrame(express_list, columns=['寄件人姓名', '寄件人手机号', '寄件时间', '付款方式', '收件人姓名',
                                             '收件人手机号', '收件时间', '寄件地址', '收件地址'])
    df.to_csv('output/' + str(num) + '_express.csv')


def genHotel(personlist, num):
    start_timestamp = int(time.mktime(time.strptime("2014-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")))
    end_timestamp = int(time.mktime(time.strptime("2017-09-30 00:00:00", "%Y-%m-%d %H:%M:%S")))
    adr_list = []
    person_list = []
    Hotel_list = []
    person_path = personlist
    hotel_path = 'conf\hoteloe.txt'
    with open(hotel_path, 'r', encoding='utf-8') as fd:
        data = fd.readlines()
    for i in range(0, len(data)):
        adr_list.append(data[i].strip('\n'))

    with open(person_path, 'r') as file:
        data = file.readlines()
        for i in range(1, len(data)):
            person_list.append(data[i].strip('\n'))
    with open('output/' + str(num) + '_hotel.csv','w') as file:
        writer = csv.writer(file)
        writer.writerow(['Id', '姓名', '酒店名称', '入住时间', '离店时间', '房间号', '酒店地址', '经度', '纬度'])
        for i in tqdm(range(0, num)):
            atime = generateTime(start_timestamp, end_timestamp)
            ltime = datetime.datetime.strptime(atime, "%Y-%m-%d %H:%M:%S") + timedelta(days=3)
            person = person_list[random.randint(0, len(person_list) - 1)]
            # print(person)
            name = person.split(',')[1]
            Id = person.split(',')[2]
            Hotel = adr_list[random.randint(0, len(adr_list) - 1)]
            Hotel_Name = Hotel.split('\t')[1]
            Hotel_Adr = Hotel.split('\t')[0]
            first = []
            for i in range(97, 123):
                first.append(chr(i).upper())
            first_no = ''.join(random.sample(first, 1))
            Room_Num = first_no + "-" + str(random.randint(0, 1000))
            Hotel_Jd = Hotel.split('\t')[2].split(',')[0]
            Hotel_Wd = Hotel.split('\t')[2].split(',')[1]
        # Hotel_list.append([Id, name, Hotel_Name, atime, ltime, Room_Num, Hotel_Adr, Hotel_Jd, Hotel_Wd])
        # df = pd.DataFrame(Hotel_list, columns=['Id', '姓名', '酒店名称', '入住时间', '离店时间', '房间号', '酒店地址', '经度', '纬度'])
            writer.writerow([Id, name, Hotel_Name, atime, ltime, Room_Num, Hotel_Adr, Hotel_Jd, Hotel_Wd])


def genInternet(personlist, num):
    start_timestamp = int(time.mktime(time.strptime("2017-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")))
    end_timestamp = int(time.mktime(time.strptime("2017-05-01 00:00:00", "%Y-%m-%d %H:%M:%S")))
    wb_ent = []
    wb_list = []
    person_list = []
    person_path = personlist
    wb_path = 'conf\wangba.txt'
    with open(wb_path, 'r', encoding='utf-8') as fd:
        data = fd.readlines()
    for i in range(0, len(data)):
        adr = data[i].split()[0]
        wb_list.append(adr)
    with open(person_path, 'r') as file:
        data = file.readlines()
        for i in range(1, len(data)):
            person_list.append(data[i].split(',')[1:3])
    for i in tqdm(range(0, num)):
        person = person_list[random.randint(0, len(person_list) - 1)]
        name = person[0]
        Id = person[1]
        start_time = generateTime(start_timestamp, end_timestamp)
        end_time = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S") + timedelta(
            minutes=random.randint(0, 59))
        wb_name = wb_list[random.randint(0, len(wb_list) - 1)].split(',')[0]
        wb_adr = wb_list[random.randint(0, len(wb_list) - 1)].split(',')[1]
        wb_lng = wb_list[random.randint(0, len(wb_list) - 1)].split(',')[2]
        wb_lat = wb_list[random.randint(0, len(wb_list) - 1)].split(',')[3]
        wb_ent.append([Id, name, start_time, end_time, wb_name, wb_adr, wb_lng, wb_lat])
    df = pd.DataFrame(wb_ent, columns=['身份证', '姓名', '上机时间', '下机时间', '网吧名称', '网吧地址', '经度', '纬度'])
    df.to_csv('output/' + str(num) + '_wb.csv')


def gen_kkgc():
    Vlist = [
        [("甘肃省第1路口", "2015/5/5 12:00", "103.8351339", "36.0466427"),
         ("甘肃省第2路口", "2015/5/5 12:03", "103.8383678", "36.0509615"),
         ("甘肃省第6路口", "2015/5/5 12:05", "103.8515908", "36.0485103"),
         ("甘肃省第8路口", "2015/5/5 12:08", "103.8590647", "36.0492691"),
         ("甘肃省第12路口", "2015/5/5 12:13", "103.8632329", "36.0556303"),
         ("甘肃省第14路口", "2015/5/5 12:15", "103.8454824", "36.0598319"),
         ("甘肃省第16路口", "2015/5/5 12:18", "103.8384396", "36.0604154"),
         ("甘肃省第17路口", "2015/5/5 12:23", "103.8383678", "36.0677093"),
         ("甘肃省第18路口", "2015/5/5 12:25", "103.8234559", "36.0693722"),
         ("甘肃省第19路口", "2015/5/5 12:26", "103.8238512", "36.065317"),
         ("甘肃省第20路口", "2015/5/5 12:27", "103.8266179", "36.0631288"),
         ("甘肃省第21路口", "2015/5/5 12:28", "103.8324749", "36.0604738"),
         ("甘肃省第22路口", "2015/5/5 12:33", "103.8327264", "36.0520412")
         ],
        [("吉林第1路口", "2017/03/04 17:20", "124.3841239", "43.1649131"),
         ("吉林第2路口", "2017/03/04 17:21", "124.3973470", "43.1640188"),
         ("吉林第3路口", "2017/03/04 17:22", "124.4353633", "43.1523387"),
         ("吉林第4路口", "2017/03/04 17:23", "124.4400345", "43.1560745"),
         ("吉林第5路口", "2017/03/04 17:24", "124.4297579", "43.1628614"),
         ("吉林第6路口", "2017/03/04 17:25", "124.4024494", "43.1719621"),
         ("吉林第7路口", "2017/03/04 17:26", "124.3909511", "43.1759070"),
         ("吉林第8路口", "2017/03/04 17:27", "124.3752128", "43.1809036"),
         ("吉林第9路口", "2017/03/04 17:28", "124.3666609", "43.1842695"),
         ("吉林第10路口", "2017/03/04 17:29", "124.3583965", "43.1830073"),
         ("吉林第11路口", "2017/03/04 17:30", "124.3637144", "43.1795361"),
         ("吉林第12路口", "2017/03/04 17:31", "124.3595463", "43.1785894"),
         ("吉林第13路口", "2017/03/04 17:32", "124.3632114", "43.1735927"),
         ("吉林第14路口", "2017/03/04 17:33", "124.3711165", "43.1732771"),
         ("吉林第15路口", "2017/03/04 17:34", "124.3668046", "43.1691216"),
         ("吉林第16路口", "2017/03/04 17:35", "124.3841239", "43.1649131")
         ]
    ]
    car_event = []
    car_no = car_n
    car_color = gen_color()
    car_band = gen_band()
    data = Vlist[random.randint(0, 1)]
    for j in tqdm(range(len(data))):
        car_time = data[j][1]
        car_lat = data[j][2]
        car_ldj = data[j][3]
        car_add = data[j][0]
        Bayonet_no = int(car_lat.replace('.', '')) + int(car_ldj.replace('.',''))
        car_event.append([car_no, car_type, car_color, car_time, car_add, car_lat, car_ldj, car_band, Bayonet_no])
    df = pd.DataFrame(car_event, columns=['车牌号', '号牌类型', '号牌颜色', '过车时间', '过车地址', '经度', '纬度',
                                       '车辆品牌', '卡口编号'])
    df.to_csv('output/' + 'kkgc.csv')

def gen_car_location(car_envents):
    start_timestamp = int(time.mktime(time.strptime("2015-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")))
    end_timestamp = int(time.mktime(time.strptime("2016-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")))
    location = []
    car_location_envents = []
    car_no = car_n
    location_path = 'conf\/allpoi.txt'
    with open(location_path, 'r') as fd:
        data = fd.readlines()
    for i in range(0, len(data)):
        location.append(data[i].strip('\n'))
    for i in tqdm(range(car_envents)):
        car_location_list = location[random.randint(0, len(location) - 1)]
        car_location = car_location_list.split('\t')[0]
        location_time = generateTime(start_timestamp, end_timestamp)
        car_location_envents.append([car_no, car_type, car_location, location_time])
    df = pd.DataFrame(car_location_envents, columns=['车牌号码','车牌号码种类','定位地址','定位开始时间'])
    df.to_csv('output/' + 'car_location.csv')

def gen_car_check(car_envents):
    start_timestamp = int(time.mktime(time.strptime("2015-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")))
    end_timestamp = int(time.mktime(time.strptime("2016-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")))
    location = []
    car_location_envents = []
    car_no = car_n
    location_path = 'conf\/allpoi.txt'
    with open(location_path, 'r') as fd:
        data = fd.readlines()
    for i in range(0, len(data)):
        location.append(data[i].strip('\n'))
    for i in tqdm(range(car_envents)):
        car_location_list = location[random.randint(0, len(location) - 1)]
        car_location = car_location_list.split('\t')[0]
        location_time = generateTime(start_timestamp, end_timestamp)
        car_location_envents.append([car_no, car_type, car_location, location_time])
    df = pd.DataFrame(car_location_envents, columns=['车牌号码','车牌号码种类','盘查地址','盘查时间'])
    df.to_csv('output/' + 'car_check.csv')

def gen_car_park(car_envents):
    start_timestamp = int(time.mktime(time.strptime("2015-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")))
    end_timestamp = int(time.mktime(time.strptime("2016-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")))
    location = []
    car_location_envents = []
    car_no = car_n
    location_path = 'conf\/allpoi.txt'
    with open(location_path, 'r') as fd:
        data = fd.readlines()
    for i in range(0, len(data)):
        location.append(data[i].strip('\n'))
    for i in tqdm(range(car_envents)):
        car_location_list = location[random.randint(0, len(location) - 1)]
        car_location = car_location_list.split('\t')[0]
        location_time = generateTime(start_timestamp, end_timestamp)
        car_location_envents.append([car_no, car_type, car_location, location_time])
    df = pd.DataFrame(car_location_envents, columns=['车牌号码', '车牌号码种类', '停车场地址', '驶入时间'])
    df.to_csv('output/' + 'car_park.csv')



def gen_xsz(personlist, driver):
    xsz = []
    person_list = []
    person_path = personlist
    with open(person_path, 'r') as file:
        data = file.readlines()
        for i in range(1, len(data)):
            person_list.append(data[i].split(',')[1:3])
    for i in tqdm(range(0, driver)):
        person = person_list[random.randint(0, len(person_list) - 1)]
        person_name = person[0]
        person_id = person[1]
        car_color = gen_color()
        car_jno = gen_carjn()
        car_band = gen_band()
        regist_time = '2015/01/01'
        xsz.append([car_n,car_type,car_color,car_jno,regist_time,car_band,person_id,person_name])
    df = pd.DataFrame(xsz, columns=['车牌号', '号牌类型', '号牌颜色', '车架号', '注册时间', '车辆品牌','身份证号','姓名' ])
    df.to_csv('output/' + str(driver) + '_xsz.csv')



def phone_loction(personlist, num):
    phone_list = []
    adr = []
    location_envent = []
    person_path = personlist
    with open(person_path, 'r') as file:
        data = file.readlines()
        for i in range(1, len(data)):
            phone_list.append(data[i].split(',')[7])
    address_path = 'conf\/address.txt'
    with open(address_path, 'r', encoding='utf-8') as fd:
        data = fd.readlines()
    for i in range(0, len(data)):
        adr.append(data[i].strip('\n'))
    for i in tqdm(range(0, num)):
        phone = random.choice(phone_list)
        location = random.choice(adr)
        start_timestamp = int(time.mktime(time.strptime("2018-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")))
        end_timestamp = int(time.mktime(time.strptime("2018-03-01 00:00:00", "%Y-%m-%d %H:%M:%S")))
        start_time = generateTime(start_timestamp, end_timestamp)
        end_time = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S") + timedelta(days=1)
        location_envent.append([phone, location, start_time, end_time])
    df = pd.DataFrame(location_envent, columns=['手机号', '定位地址', '定位开始时间', '定位结束时间'])
    df.to_csv('output/' + str(num) + '_location.csv')


def genFlight(personlist, num):
    start_timestamp = int(time.mktime(time.strptime("2014-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")))
    end_timestamp = int(time.mktime(time.strptime("2017-09-30 00:00:00", "%Y-%m-%d %H:%M:%S")))
    company = ['东方航空','中国国际航空', '深圳航空', '海南航空', '四川航空', '中国联合航空']
    class_level = ['经济舱', '商务舱', '头等舱']
    flight = []
    flight_list = []
    person_list = []
    person_path = personlist
    flight_path = 'conf\jichang.txt'
    with open(flight_path, 'r', encoding='utf-8') as fd:
        data = fd.readlines()
        for i in range(len(data)):
            flight.append(data[i].strip('\n'))
    #从构造的人里边取出姓名和身份证号
    with open(person_path, 'r') as file:
        data = file.readlines()
        for i in range(1, len(data)):
            person_list.append(data[i])
    for f in tqdm(range(0, num)):
        start_time = generateTime(start_timestamp, end_timestamp)
        arrive_time = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S") + timedelta(hours=4)
        person = person_list[random.randint(0, len(person_list) - 1)]
        name = person.split(',')[0]
        Id = person.split(',')[1]
        country = flight[random.randint(0, len(flight) - 1)]
        f_country = country.split(',')[0]
        f_jd = country.split(',')[1]
        f_wd = country.split(',')[2]
        d_country = flight[random.randint(0, len(flight) - 1)]
        destination = d_country.split(',')[0]
        if f_country == destination:
            destination = d_country.split(',')[0]
        d_jd = d_country.split(',')[1]
        d_wd = d_country.split(',')[2]
        f_company = random.choice(company)
        class_num = gen_classNum()
        f_class = random.choice(class_level)
        flight_list.append([name, Id, start_time, f_country, f_jd, f_wd, destination, d_jd, d_wd, arrive_time, f_company, class_num, f_class])
    df = pd.DataFrame(flight_list, columns=['姓名', '身份证号','实际出发时间','出发地','出发经度','出发地纬度','目的地','目的地经度','目的地纬度','实际到达时间', '航空公司', '座位号','舱位级别'])
    df.to_csv('output/'+str(num)+'_flight.csv')
