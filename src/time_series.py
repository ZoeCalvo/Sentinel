from flask import jsonify

from src.database import *
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.holtwinters import ExponentialSmoothing, SimpleExpSmoothing, Holt
from statsmodels.tsa.seasonal import seasonal_decompose
from scipy.fftpack import fft

def loading_data(id, since_date, until_date, is_tw, time_serie_type, trend_seasonal, forecast):
    num_intervalos = 0
    content = {}
    list_total = []
    list_indv = []
    nivel_significacion = 0.05
    estacionaria = False
    if is_tw == 'true':
        if id[0] == '#':
            data = selectHashtagsForTimeSeries(id, since_date, until_date)

    for d in data:
        num_intervalos = num_intervalos + 1
        content = {'analysis_score': d[0], 'date': d[1]}
        list_indv.append(content)
        content = {}

    obj_data = jsonify({'data_original':list_indv})
    list_total.append(obj_data)
    list_indv = []
    frequence = fft(data[0]) / num_intervalos
    period = 1 / frequence
    adf, pvalue, _, _, _, _ = adfuller(data[0], maxlag=1)
    if pvalue<nivel_significacion:
        estacionaria=True

    data_time_serie, proyeccion = calculate_time_serie(data, time_serie_type, trend_seasonal, period, forecast)
    decomposed_time_serie(data, period, trend_seasonal)

    for d in data_time_serie:
        content = {'analysis_score': d[0], 'date': d[1]}
        list_indv.append(content)
        content = {}
    obj_data_time_serie = jsonify({'data_time_serie': list_indv})
    list_total.append(obj_data_time_serie)
    list_indv=[]

    for d in proyeccion:
        content = {'analysis_score': d[0], 'date': d[1]}
        list_indv.append(content)
        content = {}
    obj_proyeccion = jsonify({'proyeccion': list_indv})
    list_total.append(obj_proyeccion)

    content = {'estacionaria': estacionaria}
    list_total.append(content)

    return list_total

def calculate_time_serie(data, time_serie_type, trend_seasonal, period, forecast):

    if time_serie_type == 'simple_exp_smoothing':
        data_simp_exp = SimpleExpSmoothing(data).fit()
        proyeccion = data_simp_exp.forecast(forecast)
        return data_simp_exp, proyeccion
    elif time_serie_type == 'holt':
        data_holt = Holt(data).fit()
        proyeccion = data_holt.forecast(forecast)
        return data_holt, proyeccion
    elif time_serie_type == 'holt_winters':
        if trend_seasonal == 'add':
            data_holtwinters = ExponentialSmoothing(data, trend='add', seasonal='add', seasonal_periods=period).fit(
                use_boxcox=True)
        elif trend_seasonal == 'mul':
            data_holtwinters = ExponentialSmoothing(data, trend='mul', seasonal='mul', seasonal_periods=period).fit(
                use_boxcox=True)
        proyeccion = data_holtwinters.forecast(forecast)
        return data_holtwinters, proyeccion

def decomposed_time_serie(data, period, model):
    if model == 'add':
        data_decomposed = seasonal_decompose(data, model='additive', freq=period)
    elif model == 'mul':
        data_decomposed = seasonal_decompose(data, model='multiplicative', freq=period)

    tendencia = data_decomposed.trend
    estacionalidad = data_decomposed.seasonal
    residuo = data_decomposed.resid

    return tendencia, estacionalidad, residuo

