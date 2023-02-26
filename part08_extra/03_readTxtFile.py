import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

audil_url = 'https://translate.google.com/translate_tts?ie=UTF-8&q=%E5%A4%A7%E5%AE%B6%E5%A5%BD&tl=zh-CN&total=1&idx=0&textlen=3&tk=985881.634498&client=webapp&prev=input'
audio_url = 'https://translate.google.com/translate_tts?ie=UTF-8&q=%E5%B9%B9%E4%BD%A0%E5%A8%98&tl=zh-CN&total=1&idx=0&textlen=5&tk=403482.36225&client=webapp&prev=input'

res = requests.get(audio_url, headers=headers)

with open(r'./test.mp3', 'wb') as w:
    w.write(res.content)
