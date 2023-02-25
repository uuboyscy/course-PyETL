import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.vgchartz.com/tools/hw_date.php?reg=Global&ending=Monthly"

headersStr = """accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6
cache-control: max-age=0
cookie: __qca=P0-1382307012-1662978577564; PHPSESSID=9cko4pq074ej9j4mhcremhp15u; geoCountry=US; uniqueFlag=1; VGCBE=b1; __utma=154313151.1784641658.1662978577.1662978577.1662978577.1; __utmb=154313151; __utmc=154313151; __utmz=154313151.1662978577.1.1.utmccn=(referral)|utmcsr=google.com|utmcct=/|utmcmd=referral; qcSxc=1662978577566; __qca=P0-1382307012-1662978577564; _pbjs_userid_consent_data=3524755945110770; _lr_retry_request=true; _lr_env_src_ats=false; cto_bundle=bX8Qp19MQ2Fjc250Q0FYM2FId094eXFLWlc4dkdiaCUyRlN4YVZQRzdyaEZmdHpwTk9qQ25SQzZaTWxMZkZ1THA1eENPU0UyRFBCWGgwT0VHMnRKeDhxaG56bUswTjF1T0ZaZ0tYT2VYT1RKRldNQ09DRDhZNjZnbklvdEVWeDRrWnpkc2tycGs2WW4zamdjck56REF0Y0RmMjc5QSUzRCUzRA; cto_bidid=bBeOA19NJTJCb0RpdEpNSGx0U2h0Nks4N05WVGpJSDdYbmRlVGF6V3FxRWRNOXklMkZ1YWVSJTJGYmtDYWtyd3hkVFlvRzE0Q0ZrMGIxOU43MzZHMk5UaE1KMEpIJTJCZHRra29Xa3BQUENlaTNES2NOQWFqbEMwJTNE
referer: https://www.vgchartz.com/tools/hw_date.php
sec-ch-ua: "Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"
sec-ch-ua-mobile: ?1
sec-ch-ua-platform: "Android"
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: same-origin
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36"""

headers = {r.split(": ")[0]: r.split(": ")[1] for r in headersStr.split("\n")}

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, "html.parser")

rawJsonObj = soup.select_one('[id="chart_body"] script').text
rawJsonObj = " ".join([i for i in rawJsonObj.split("\n") if "//" not in i])

s = rawJsonObj \
    .split("window.chart = new Highcharts.StockChart(")[1] \
    .split(");")[0] \
    .replace("\n", " ") \
    .replace("\t", " ") \
    .replace("'", "\"") \
    .replace("{", "{ ")

keySet = set(re.findall(r'[a-zA-Z0-9]*:', s))

for kw in keySet:
    newKw = '"' + kw
    newKw = newKw.replace(':', '":')
#     print(newKw)
    s = s.replace(kw, newKw)

jsonData = eval(
    s.replace("true", "True").replace("false", "False")
)


# Print all device names
for deviceInfo in jsonData["series"]:
    deviceName = deviceInfo["name"]
    print(deviceName)


# Output csv
dfList = list()
for deviceInfo in jsonData["series"]:
    deviceName = deviceInfo["name"]
    data = deviceInfo["data"]

    df = pd.DataFrame(data=data)
    df.columns = ["timestamp_ms", "value"]

    df["device_name"] = deviceName
    df["datetime"] = df["timestamp_ms"].apply(lambda ts_ms: pd.to_datetime(ts_ms, unit='ms'))
    df["year"] = df["datetime"].apply(lambda dt: dt.year)
    df["month"] = df["datetime"].apply(lambda dt: dt.month)
    df['YYYYMM'] = df['year'].apply(lambda x:str(x)) + df['month'].apply(lambda x:str(x))
    df['unit(Mu)'] = df['value'] / 1000000
    dfList.append(df)

df = pd.concat(dfList)

df[['YYYYMM','year','month', 'device_name', 'timestamp_ms', 'value', 'unit(Mu)']].to_excel("../vgchartz_rawdata_20221108.xlsx", index=0, encoding="utf-8-sig")