import requests  # εισαγωγή της βιβλιοθήκης 
    
url = input("enter url: ")  # προσδιορισμός του url

with requests.get(url) as response:  # το αντικείμενο response
    headers = response.headers
    print("Website headers are {url} \n, {headers} \n\n")        #all http response headers
 
    print('web servers software: ', headers.get('server'), '\n')    #a) 
    
    print('cookies used, with expiration: ', headers.get('Set-Cookie'), '\n')    #b), c)

    