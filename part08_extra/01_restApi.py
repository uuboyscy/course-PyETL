'''

1. getTownIDDict(self)
    return town_id_dict -> {'Town_name' : [City_id, Town_id]}

2. setTownID(self, location_name = '中壢')
    reset city_id and town_id in constructor
    return town_id

3. getAllCities(self)
    return data_city_dict

4. getTown(self)
    return data_towns_dict

5. getTownInformation(self)
    return data_towns_information_dict

6. getTownWeatherInformation(self)
    return data_weather_information_dict

#7. getTownWeatherInformationDetail(self)


#8. getTownWeatherInformationHistory(self)

'''
from urllib import request
import json
import os
import ssl

# used to fix Python SSL CERTIFICATE_VERIFY_FAILED
if not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(
    ssl, '_create_unverified_context', None
):
    ssl._create_default_https_context = ssl._create_unverified_context


class WeatherAPI:
    def __init__(self, town_id=81):
        #         self.city_id = city_id
        self.city_id = 8
        self.town_id = town_id
        self.url_all_cities = 'https://works.ioa.tw/weather/api/all.json'
        self.url_get_towns_by_cities = (
            'https://works.ioa.tw/weather/api/cates/%s.json'  ###
        )
        self.url_get_towns_information = (
            'https://works.ioa.tw/weather/api/towns/%s.json'  ###
        )
        self.url_get_url = 'https://works.ioa.tw/weather/api/url.json'
        self.url_get_towns_weather = (
            'https://works.ioa.tw/weather/api/weathers/%s.json'  ###
        )
        self.url_img_path_dir = json.loads(request.urlopen(self.url_get_url).read())[
            'img'
        ]

        # weather information
        self.img_url = ''
        self.desc = ''
        self.temperature = 0
        self.felt_air_temp = 0
        self.humidity = 0
        self.rainfall = 0
        self.sunrise = ''
        self.sunset = ''
        self.update_time = ''
        self.specials = {
            'title': '',
            'status': '',
            'update_time': '',
            'desc': '',
            'img_url': '',
        }
        # weather history
        self.histories = {}

    def getTownIDDict(self):
        town_id_dict = {}
        data_city_dict = self.getAllCities()

        for ct in data_city_dict:
            for tn in ct['towns']:
                town_id_dict['%s,%s' % (ct['name'], tn['name'])] = [ct['id'], tn['id']]

        return town_id_dict

    def setTownID(self, location_name='中壢'):
        town_id_dict = self.getTownIDDict()
        for n in town_id_dict:
            if location_name in str(n):
                self.city_id = town_id_dict[n][0]
                self.town_id = town_id_dict[n][1]
                return self.town_id

        return 81

    def getAllCities(self):
        data_city = request.urlopen(self.url_all_cities).read().decode('utf-8')
        data_city_dict = json.loads(data_city)

        return data_city_dict

    def getTown(self):
        data_towns = (
            request.urlopen(self.url_get_towns_by_cities % (self.city_id))
            .read()
            .decode('utf-8')
        )
        data_towns_dict = json.loads(data_towns)

        return data_towns_dict

    def getTownInformation(self):
        data_towns_information = (
            request.urlopen(self.url_get_towns_information % (self.town_id))
            .read()
            .decode('utf-8')
        )
        data_towns_information_dict = json.loads(data_towns_information)

        return data_towns_information_dict

    def getTownWeatherInformation(self):
        data_weather_information = (
            request.urlopen(self.url_get_towns_weather % (self.town_id))
            .read()
            .decode('utf-8')
        )
        data_weather_information_dict = json.loads(data_weather_information)

        return data_weather_information_dict

    def getTownWeatherInformationDetail(self):
        tmp_dict = self.getTownWeatherInformation()
        self.img_url = self.url_img_path_dir + tmp_dict['img']
        self.desc = tmp_dict['desc']
        self.temperature = tmp_dict['temperature']
        self.felt_air_temp = tmp_dict['felt_air_temp']
        self.humidity = tmp_dict['humidity']
        self.rainfall = tmp_dict['rainfall']
        self.sunrise = tmp_dict['sunrise']
        self.sunset = tmp_dict['sunset']
        self.update_time = tmp_dict['at']
        self.specials = tmp_dict['specials']

        return [
            self.img_url,
            self.desc,
            self.temperature,
            self.felt_air_temp,
            self.humidity,
            self.rainfall,
            self.sunrise,
            self.sunset,
            self.update_time,
        ]

    def getTownWeatherInformationHistory(self):
        tmp_dict = self.getTownWeatherInformation()
        self.specials = tmp_dict['histories']

        return 0


# Test
if __name__ == '__main__':
    #     location1 = WeatherAPI(8, 81)
    location1 = WeatherAPI()

    # Get all cities
    print('Get all cities :')
    print(location1.getAllCities())

    print()

    # Get towns by city
    print('Get towns by city ID :')
    print(location1.getTown())

    print()

    # Get towns information
    print('Get towns information by town ID :')
    print(location1.getTownInformation())
    print('Location image url : %s' % (location1.getTownInformation()['img']))

    print()

    # Get town weather
    print('Get town weather :')
    print(location1.getTownWeatherInformation())

    # Get image url of town weather status
    status = location1.url_img_path_dir + location1.getTownWeatherInformation()['img']
    print('Get image url of town weather status : %s' % (status))

    print()

    # Get town ID by name
    print('Get town ID by name dict :')
    print(location1.getTownIDDict())

    print()

    # Set town ID
    request_location = '楠西'
    print('Get town ID :')
    print('%s : %s' % (request_location, location1.setTownID(request_location)))
    # Get towns information again
    print('Get towns information by town ID again :')
    print(location1.getTownInformation())
    print('Location image url : %s' % (location1.getTownInformation()['img']))

    print()
