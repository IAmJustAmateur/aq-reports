colorGreen = '#00de0f'
colorYellow ='#e4aa00'
colorRed = '#cb0000'

T_MIN = 21
T_MAX = 25.49
HUMIDITY_LOW = 30
HUMIDITY_HIGH = 60
CO2_LIMIT = 790
PM_2_5_LIMIT = 25

LIMITS = {
    "CO2" : {
        "YELLOW" : 791,
        "RED" : 899
    },
    "PM10": {
        "YELLOW" : 30,
        "RED" : 51
    },
    "PM2_5": {
        "YELLOW" : 25,
        "RED" : 36
    },

    "FM" :  {
        "YELLOW" : 7,
        "RED" : 20
    },
    "O3" : {
        "YELLOW" : 0.1,
        "RED" : 0.16
    },
    "Noise" : {
        "YELLOW" : 41,
        "RED" : 50
    },
    "Light" : {
        "YELLOW" : 100,
        "RED" : 300
    }
}

def color (param, value):
    limits = LIMITS[param]
    try:
        if value < limits["YELLOW"]:
            return colorGreen
        if value < limits["RED"]:
            return colorYellow
        return colorRed
    except:
        return 'gray'


def humidity(param, value):
    try:
        if (value>=30) & (value<=60):
            styleColor = colorGreen
        elif   (value<30) & (value>=20):
            styleColor =colorYellow
        elif (value>60) & (value<=70):
            styleColor = colorYellow
        elif (value<20) | (value>70):
            styleColor = colorYellow
        else:
            styleColor = 'gray'
        return styleColor
    except:
        return 'gray'

def temperature(param, value, farengheit):
    try:
        if not farengheit:
            value = (value * 9 / 5)+32
        if (value>68) & (value<=77.8):
            styleColor = colorGreen
        elif (value>66) & (value<=68):
            styleColor = colorYellow
        elif (value>=77.8) & (value<82):
            styleColor = colorYellow
        elif (value>=82) | (value<=66):
            styleColor = colorRed
        else:
            styleColor = 'gray'
        return styleColor
    except:
        return 'gray'

def pm10(value):
    try:
        if value<30:
            styleColor = colorGreen
        elif  (value<=50):
            styleColor =colorYellow
        elif (value > 50):
            styleColor = colorRed
        else:
            styleColor = 'gray'
            
        return styleColor

    except:
        return 'gray'

def pm2_5(value):
    try:
        if value<25:
            styleColor = colorGreen
        elif  (value<=35):
            styleColor =colorYellow
        elif (value > 35):
            styleColor = colorRed
        else:
            styleColor = 'gray'
            
        return styleColor
        
    except:
        return 'gray'

def light(value):
    try:
        if value>25:
            styleColor = colorGreen
        elif  (value<=100):
            styleColor = colorRed
        elif (value > 100) & (value < 500):
            styleColor = colorYellow
        else:
            styleColor = 'gray'
            
        return styleColor
        
    except:
        return 'gray'

def noise(value):
    try:
        if (value<=40):
            styleColor = colorGreen
        elif (value>40) & (value<=49):
            styleColor = colorYellow
        elif (value>49):
            styleColor = colorRed
        else:
            styleColor = 'gray'
    
        return styleColor
    except:
        return 'gray'

HVAC_color_functions = {
    "temperature": temperature,
    "humidity": humidity,
    "CO2": color,
    "lux": color,
    "dB_average": color,
    "PM2_5": color,
    "PM10": color,
    "CH2O": color,
    "O3": color,
}

def health_risks(value):
    try:
        if value < 3:
            return colorGreen
        elif value < 7:
            return colorYellow
        elif value >= 7:
            return colorRed
        else:
            return 'gray'
    except:
        return 'gray'

def productivity(value):
    try:
        if value>80:
            return colorGreen
        elif value >=70:
            return colorYellow
        else:
            return colorRed
    except:
        return 'gray'

mental_health_color_functions = {
    "Mental health": health_risks,
    "Sleep quality": productivity,
    "Conditions for physical activity" : productivity,
}

