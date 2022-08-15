import requests

s = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
while True:
    if not s.text.startswith('We'):
        s = requests.get("https://stepic.org/media/attachments/course67/3.6.3/" + s.text )
        continue
    else:
        print(s.text)
    break