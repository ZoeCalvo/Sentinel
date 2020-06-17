from flask import jsonify

from src.database import *
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.holtwinters import ExponentialSmoothing, SimpleExpSmoothing, Holt
from statsmodels.tsa.seasonal import seasonal_decompose
from datetime import datetime, timedelta
import pmdarima

def loading_data(id, since_date, until_date, is_tw, time_serie_type, trend_seasonal, forecast):
    analysis_score=[]
    dates = []
    content = {}
    list_total = []
    list_indv = []
    nivel_significacion = 0.05
    estacionaria = False
    if is_tw == 'true':
        if id[0] == '#':
            data = selectHashtagsForTimeSeries(id, since_date, until_date)
        elif id[0] == '@':
            data = selectUserTwForTimeSeries(id, since_date, until_date)
        else:
            data = selectWordForTimeSeries(id, since_date, until_date)
    else:
        data = selectUserIgForTimeSeries(id, since_date, until_date)

    for d in data:
        analysis_score.append(d[0])
        dates.append(d[1])
        content = {'analysis_score': d[0], 'date': d[1].strftime("%d/%m/%Y")}
        list_indv.append(content)
        content = {}

    fecha = dates[-1]
    print(fecha)
    period = 1
    obj_data = list_indv
    list_total.append(obj_data)
    list_indv = []
    adf, pvalue, _, _, _, _ = adfuller(analysis_score, maxlag=1)

    if pvalue<nivel_significacion:
        estacionaria = True

    data_time_serie, proyeccion = calculate_time_serie(analysis_score, time_serie_type, trend_seasonal, period, forecast)
    tendencia, estacionalidad, residuo = decomposed_time_serie(analysis_score, period, trend_seasonal)

    for d, dt in zip(data, data_time_serie):
        content = {'analysis_score': dt, 'date': d[1].strftime("%d/%m/%Y")}
        list_indv.append(content)
        content = {}

    obj_data_time_serie = list_indv
    list_indv=[]

    for p in proyeccion:
        date = fecha + timedelta(days = period)
        content = {'analysis_score': p, 'date': date.strftime("%d/%m/%Y")}
        list_indv.append(content)
        content = {}
        fecha = date
    obj_proyeccion = list_indv
    list_indv = []


    for e in estacionalidad:
        content = {'data': e}
        list_indv.append(content)
        content = {}
    obj_estacionalidad = list_indv
    list_indv = []

    for t in tendencia:
        content = {'data': t}
        list_indv.append(content)
        content = {}
    obj_tendencia = list_indv
    list_indv = []

    for r in residuo:
        content = {'data': r}
        list_indv.append(content)
        content = {}
    obj_residuo = list_indv


    return obj_data,obj_data_time_serie,obj_proyeccion,estacionaria, obj_estacionalidad, obj_tendencia, obj_residuo

def calculate_time_serie(data, time_serie_type, trend_seasonal, period, forecast):


    if time_serie_type == 'simpsmoothing':
        data_simp_exp = SimpleExpSmoothing(data).fit()
        proyeccion = data_simp_exp.forecast(int(forecast))
        return data_simp_exp.fittedvalues, proyeccion
    elif time_serie_type == 'holt':
        data_holt = Holt(data).fit()
        proyeccion = data_holt.forecast(int(forecast))
        return data_holt.fittedvalues, proyeccion
    elif time_serie_type == 'holt_winters':
        print(trend_seasonal)
        if trend_seasonal == 'add':
            print('periodo',period)
            data_holtwinters = ExponentialSmoothing(data, trend='add', seasonal='add', seasonal_periods=period).fit(
                use_boxcox=True)
            print(data_holtwinters.fittedvalues)
        elif trend_seasonal == 'mult':
            data_holtwinters = ExponentialSmoothing(data, trend='mul', seasonal='mul', seasonal_periods=period).fit(
                use_boxcox=True)
        proyeccion = data_holtwinters.forecast(int(forecast))

        return data_holtwinters.fittedvalues, proyeccion
    elif time_serie_type == 'arima':
        arima = pmdarima.auto_arima(data, seasonal=False, error_action='ignore', suppress_warnings=True)
        proyeccion, int_conf = arima.predict(n_periods = int(forecast), return_conf_int = True)
        prediccion = arima.predict_in_sample()
        print('pro', proyeccion)
        print('pre', prediccion)
        return prediccion, proyeccion
def decomposed_time_serie(data, period, model):
    if model == 'add':
        data_decomposed = seasonal_decompose(data, model='additive', freq=period)
    elif model == 'mult':
        data_decomposed = seasonal_decompose(data, model='multiplicative', freq=period)

    tendencia = data_decomposed.trend
    estacionalidad = data_decomposed.seasonal
    residuo = data_decomposed.resid

    return tendencia, estacionalidad, residuo

