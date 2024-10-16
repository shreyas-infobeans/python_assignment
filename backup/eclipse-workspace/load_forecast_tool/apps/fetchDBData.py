# import pandas as pd
import cx_Oracle
import sys
import os
from datetime import datetime
import math
import random


    # sys.exit(1);
# Below are the details about the DB
# CONN_INFO = {
# 'host': '',
# 'port': ,
# 'user': '',
# 'psw': '',
# 'service': ''
# }

# CONN_STR = '{user}/{psw}@{host}:{port}/{service}'.format(**CONN_INFO)

class DB:
    def __init__(self):
        pass
        # try:
        #     if sys.platform.startswith("darwin"):
        #         lib_dir = os.path.join(os.environ.get("HOME"), "Downloads",
        #                             "instantclient_19_8")
        #         cx_Oracle.init_oracle_client(lib_dir=lib_dir)
        #     elif sys.platform.startswith("win32"):
        #     # Change the below path to you instaclient directory
        #         lib_dir=r"C:\Users\rraj036\Downloads\instantclient_21_3"
        #         cx_Oracle.init_oracle_client(lib_dir=lib_dir)
        # except Exception as err:
        #     print("Whoops!")
        #     print(err);
        # self.conn = cx_Oracle.connect(CONN_STR)

    # def qquery(self, query):
    #     cursor = self.conn.cursor()
    #     result = cursor.execute(query).fetchall()
    #     cursor.close()
    #     return result

    def qquery(self,query):
        return (1,2,3,4,5,6,7,8,9,10);

db = DB()

def fetch_data(fdate):

    # query  = ""
    # query = ""
    query = ""
    
    # print(query)
    result = db.qquery(query)
    # print(result)

    query = ""
    # print(query)
    result_scada = db.qquery(query)
    # print(result_scada)

    query = ""
    # print(query)
    result_UP_forecast = db.qquery(query)
    # print(result_UP_forecast)
    
    res = []
    cnt = 0
    total_error = 0
    max_err = 0
    min_err = 100
    mape = 0
    rmse = 0
    total_rmse = 0
    error_percent = {"Error <1%":0,"Error 1-3%":0,"Error 3-5%":0,"Error >5%":0}
    for i in range(96):
        try:
            dt = result[i][0]
            dt = datetime.strptime(dt, '%Y-%m-%d')
            dt = dt.strftime('%d-%b-%Y').upper()
        except:
            dt = '-'
        try:
            forecasted_val = round(float(result[i][2]))
            time_block  = result[i][1]
            city_name = result[i][3]
        except:
            forecasted_val = 0
            time_block = 0
            city_name = ""
        try:
            actual_val = round(float(result_scada[i][2]))
        except:
            actual_val = 0
        try:
            upForecast_val = round(float(result_UP_forecast[i][2]))
        except:
            upForecast_val = 0
        try:
            error_sw = round(((actual_val-forecasted_val)/actual_val)*100,2)

            if abs(error_sw) <1.0:
                error_percent["Error <1%"] += 1
            elif abs(error_sw) >=1.0 and abs(error_sw) <3.0:
                error_percent["Error 1-3%"] += 1
            elif abs(error_sw) >=3.0 and abs(error_sw) <5.0:
                error_percent["Error 3-5%"] += 1
            else:
                error_percent["Error >5%"] += 1

            error = actual_val-forecasted_val
            error_square = error**2
            # print("error ", error_square)
            total_rmse += error_square
            cnt += 1
            total_error += abs(error_sw)
            max_err = max(max_err,abs(error_sw))
            min_err = min(min_err,abs(error_sw))
        except ZeroDivisionError:
            error_sw = 0
        try:    
            error_up = round(((actual_val-upForecast_val)/actual_val)*100,2)
        except ZeroDivisionError:
            error_up = 0

        temp = {'date':dt,'time_block':time_block,'forecast':forecasted_val,
        'actual':actual_val,'city':city_name,'error':error_sw,
        'upforecast':upForecast_val,'error_up':error_up}
        res.append(temp)
    print(total_error,cnt,total_rmse)
    print(error_percent)
    try:
        mape = round(total_error/cnt,2)
        rmse = round(math.sqrt((total_rmse)/cnt),2)
    except:
        mape = '-'
    return res,mape,max_err,min_err,rmse,error_percent


# def fetch_data_date(fdate):


#     query  = ""
#     print(query)
#     result = db.qquery(query)

#     query = ""
#     # print(query)
#     result_scada = db.qquery(query)

#     query = ""
#     # print(query)
#     result_UP_forecast = db.qquery(query)

#     t_block = []
#     forecast = []
#     actual = []
#     UPForecast = []
#     for i in range(96):
#         try:
#             forecast.append(result[i][2])
#         except:
#             forecast.append(result[i][2])
#         actual.append(result_scada[i][2])
#         UPForecast.append(result_UP_forecast[i][2])
#     return forecast,actual,UPForecast


def fetch_intraday_forecast(fdate):


    
    query = ""
    # print(query)
    result = db.qquery(query)
    # SAMPLE - ('2022-09-04', 2, 23640.623145, 'ABC', 1)
    # print(result)
    query = ""
    # print(query)
    result_scada = db.qquery(query)

    query = ""
    # print(query)
    result_UP_forecast = db.qquery(query)

    t_block = []
    forecast = []
    actual = []
    UPForecast = []
    for i in range(96):
        try:
            forecast.append(result[i][2])
        except:
            forecast.append(0)
        try:
            UPForecast.append(result_UP_forecast[i][2])
        except:
            UPForecast.append(0)
        try:
            if(int(result_scada[i][2]) == 1):
                continue
        except:
            continue
        actual.append(result_scada[i][2])
    forecast = []
    forecast = [random.random() for i in range(96)]
    actual = [-0.23 for i in range(96)]
    UPForecast = [0.23 for i in range(96)]
    return forecast,actual,UPForecast

def fetch_dayAhead_forecast(fdate):


    query  = ""
    # print(query)
    result = db.qquery(query)
    # SAMPLE - ('2022-09-04', 2, 23640.623145, 'ABC', 1)
    # print(result)
 

    t_block = []
    forecast = []
    actual = []
    UPForecast = []
    for i in range(96):
        try:
            forecast.append(result[i][2])
        except:
            forecast.append(0)
        # actual.append(result_scada[i][2])
        # UPForecast.append(result_UP_forecast[i][2])
    return forecast
	
def fetch_data_crep(fdate):

   
    query = ""
    
    # print(query)
    result = db.qquery(query)
    # print(result)

    query = ""
    print(query)
    result_scada = db.qquery(query)
    # print(result_scada)

    query = ""
    # print(query)
    result_UP_forecast = db.qquery(query)
    # print(result_UP_forecast)
    
    res = []
    cnt = 0
    total_error = 0
    max_err = 0
    min_err = 100
    mape = 0
    rmse = 0
    total_rmse = 0
    error_percent = {"Error <1%":0,"Error 1-3%":0,"Error 3-5%":0,"Error >5%":0}
    for i in range(96):
        try:
            dt = result[i][0]
            dt = datetime.strptime(dt, '%Y-%m-%d')
            dt = dt.strftime('%d-%b-%Y').upper()
        except:
            dt = '-'
        try:
            forecasted_val = round(float(result[i][2]))
            time_block  = result[i][1]
            city_name = result[i][3]
        except:
            forecasted_val = 0
            time_block = 0
            city_name = ""
        try:
            actual_val = round(float(result_scada[i][2]))
        except:
            actual_val = 0
        try:
            upForecast_val = round(float(result_UP_forecast[i][2]))
        except:
            upForecast_val = 0
        try:
            error_sw = round(((actual_val-forecasted_val)/actual_val)*100,2)

            if abs(error_sw) <1.0:
                error_percent["Error <1%"] += 1
            elif abs(error_sw) >=1.0 and abs(error_sw) <3.0:
                error_percent["Error 1-3%"] += 1
            elif abs(error_sw) >=3.0 and abs(error_sw) <5.0:
                error_percent["Error 3-5%"] += 1
            else:
                error_percent["Error >5%"] += 1

            error = actual_val-forecasted_val
            error_square = error**2
            # print("error ", error_square)
            total_rmse += error_square
            cnt += 1
            total_error += abs(error_sw)
            max_err = max(max_err,abs(error_sw))
            min_err = min(min_err,abs(error_sw))
        except ZeroDivisionError:
            error_sw = 0
        try:    
            error_up = round(((actual_val-upForecast_val)/actual_val)*100,2)
        except ZeroDivisionError:
            error_up = 0

        temp = {'date':dt,'time_block':time_block,'forecast':forecasted_val,
        'actual':actual_val,'city':city_name,'error':error_sw,
        'upforecast':upForecast_val,'error_up':error_up}
        res.append(temp)
    print(total_error,cnt,total_rmse)
    print(error_percent)
    try:
        mape = round(total_error/cnt,2)
        rmse = round(math.sqrt((total_rmse)/cnt),2)
    except:
        mape = '-'
    return res,mape,max_err,min_err,rmse,error_percent