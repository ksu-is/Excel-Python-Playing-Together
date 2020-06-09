#requests
 
import requests  
r = requests.get('https://www.python.org')  
r.status_code   
#import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

res.status_code

len(res.text)
print(res.text[:500])