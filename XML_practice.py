# -*- coding: utf-8 -*-
from xml.parsers.expat import ParserCreate
from urllib import request

res = {}

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        if 'city' in attrs:
            res['city'] = attrs['city']
        if 'forecast' in name:
            if 'forecast' not in res:
                res['forecast'] = []

            forecast = res['forecast']

            forecast.append({
                'date': attrs['date'],
                'high': attrs['high'],
                'low': attrs['low']
            })
            res['forecast'] = forecast

    def end_element(self, name):
        pass
    def char_data(self, text):
        pass

def parseXml(xml_str):
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)
    return res

# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'
