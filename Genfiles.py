# -*- coding: utf-8 -*-
from AllEnvents import *
import configparser
conf = configparser.RawConfigParser()
conf.read('data.ini')
import multiprocessing

if __name__ == '__main__':
    if conf.get("run", "personlist") == "null":
        print('实体(人)')
        personlist = genPersonlist(int(conf.get("run", "personnum")))
    else:
        print('实体(人)')
        personlist = conf.get("run", "personlist")
        ersonlist = personlist
    num = conf.get("run", "num")
    driver = conf.get("run", "driver")
    car_envents = conf.get("run", "car_envents")
    # print('网吧事件')
    # genInternet(personlist, int(num))
    print('通话事件')
    genTelenvent(personlist, int(num))
    print('快递事件')
    genExpress(personlist, int(num))
    print('酒店事件')
    p = multiprocessing.Process(target=genHotel(personlist, int(num)), args=(3,))
    p.start()
    print('手机定位事件')
    phone_loction(personlist,int(num))
    print('行驶证')
    gen_xsz(personlist, int(driver))
    print('卡口过车记录')
    gen_kkgc()
    print('车辆定位事件')
    gen_car_location(int(car_envents))
    print('生成车辆盘查记录')
    gen_car_check(int(car_envents))
    print('停车记录')
    gen_car_park(int(car_envents))
    print('航空事件')
    genFlight(personlist, int(num))
