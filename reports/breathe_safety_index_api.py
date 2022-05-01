from random import random
import requests
import json

api_key = "623d80b709d4bd0023a37070"
health_risks_api_urls = {
    "CVS": "http://api.djinnsensor.com/cvs-indoor",
    "Brain": "http://api.djinnsensor.com/brain",
    "Respiratory" : "http://api.djinnsensor.com/respiratory",
    "Sensorial" : "http://api.djinnsensor.com/sensorial",
    "Allergy": "http://api.djinnsensor.com/allergy",
    "Mental" : "http://api.djinnsensor.com/mental",
    
    }
productivity_api_url = "http://api.djinnsensor.com/productivity"

life_quality_api_url = "http://api.djinnsensor.com/lifequality"
api_url = "http://api.djinnsensor.com/allrisks"
#api_url = "http://localhost:5000/allrisks"

headers = {
        "Content-Type" : "application/json",
        "apiKey": api_key,
    }

def health_risks(aq_params: list, system: str) -> list:
    request =  {
        "request": aq_params
    }
    respond = requests.post(url=health_risks_api_urls[system], headers = headers, data=json.dumps(request))
    risk_list = respond.json()
    risks = map(lambda item: float(item[system]['risk']), risk_list)
    return list(risks)



def cv(aq_params: dict) -> float:
    request =  {
        "request": aq_params
    }
    rsp = requests.post(url=health_risks_api_urls["cv"], headers = headers, data=json.dumps(request))
    cv_list = rsp.json()
    cv_risks = map(lambda item: float(item["CVS"]['risk']), cv_list)
    return cv_risks


def respiratory (aq_params: dict) -> float:
    return round(random() *9 )

def brain (aq_params: dict) -> float:
    return round(random() *9 )

def mental (aq_params: dict) -> float:
    return round(random() *9 )

def allergy (aq_params: dict) -> float:
    return round(random() *9 )

def old_health_risks(aq_params: dict) -> dict:
    return {
        "cv": cv(aq_params),
        "respiratory": respiratory(aq_params),
        "brain": brain(aq_params),
        "mental": mental(aq_params),
        "allergy": allergy(aq_params),
    }

#Integral	Basic activity	Applied activity	Focused activity	Task orientation	Initiative	Information search	Information usage	Breath of approach	Basic strategy

def integral_productivity(aq_params: dict) -> float:
    return round(random() * 100, 2)

def basic_activity(aq_params: dict) -> float:
    return round(random() * 100, 2)

def applied_activity(aq_params: dict) -> float:
    return round(random() * 100, 2)

def focused_activity(aq_params: dict) -> float:
    return round(random() * 100, 2)

def task_orientation(aq_params: dict) -> float:
    return round(random() * 100, 2)

def initiative(aq_params: dict) -> float:
    return round(random() * 100, 2)

def information_search(aq_params: dict) -> float:
    return round(random() * 100, 2)

def information_usage(aq_params: dict) -> float:
    return round(random() * 100, 2)

def breadth_of_approach(aq_params: dict) -> float:
    return round(random() * 100, 2)

def basic_strategy(aq_params: dict) -> float:
    return round(random() * 100, 2)

def old_productivity(aq_params: dict) -> dict:
    return {
        "Integral" : integral_productivity(aq_params),
        "Basic activity": basic_activity(aq_params),
        "Applied activity": applied_activity(aq_params),
        "Focused activity": focused_activity(aq_params),
        "Task orientation": task_orientation(aq_params),
        "Initiative": initiative(aq_params),
        "Information search": information_search(aq_params),
        "Information usage": information_usage(aq_params),
        "Breath of approach": breadth_of_approach(aq_params),
        "Basic strategy": basic_strategy(aq_params),
    }

def productivity(aq_params: list) -> list:
    request =  {
        "request": aq_params
    }
    respond = requests.post(url=productivity_api_url, headers = headers, data=json.dumps(request))
    risk_list = respond.json()
    return risk_list

def mental_health(aq_params: dict) -> float:
    return mental(aq_params)

def sleep_quality(aq_params: dict) -> float:
    return round(random() * 100, 2)

def physical_activity(aq_params: dict) -> float:
    return round(random() * 100, 2)

def life_quality(aq_params: dict) -> dict:
    return {
        "Mental health": mental_health(aq_params),
        "Sleep quality": sleep_quality(aq_params),
        "Conditions for physical activity" : physical_activity(aq_params),
    }

def get_all_risks(aq_params: list) -> list:
   
    request =  {
        "request": aq_params
    }
    data = json.dumps(request)
    respond = requests.post(url= api_url, headers = headers, data=data)
    risk_list = respond.json()
    return risk_list
    
    """ risks = []
    for param in aq_params:
        request = {
            "request": [param]
        }
        data = json.dumps(request)
        respond = requests.post(url= api_url, headers = headers, data=data)
        risk = respond.json()
        print(risk)
        risks.append(risk) """
    
    return risks



if __name__ == "__main__":
      
    request =  {
        "request":[
        
        {'CO2': 660.3, 'PM10': 3.2, 'PM1_0': 2.5, 'PM2_5': 2.5, 'TVOC': 2527.9, 'dB_average': 50.7, 'Humidity': 58.31, 'Light': 0.5,  'Temperature': 11.847999999999999, 'CH2O': 16.1, 'NO2': 0, 'O3': 0},
        {'CO2': 660.3, 'PM10': 3.2,  'Humidity': 58.31, 'Light': 0.5, 'Temperature': 11.847999999999999 }
        
        ]
    }
    '''
        {"Humidity":30,"PM10":40,"PM2_5":15,"FM":15,"Ozone":30,"Timestamp":1231098723123,"lat":123123,"lon":123122},
        {"Humidity":30,"PM10":40,"PM2_5":15,"FM":15,"Ozone":30,"Timestamp":1231098723123, "CO2": 1500},
    '''

    rsp = requests.post(url= api_url, headers = headers, data=json.dumps(request))
    rsp = rsp.json()
    #rsp = requests.post(url=api_url, data = data)
    print(rsp)
