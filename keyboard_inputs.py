import requests
print("start")
while True:
    key = input('Enter your input:')
    if key != 'q':
        speeds = [str(x) for x in range(0,10)]
        turns = ['h','l']
        if key in speeds:
            command = {'type':'speed','value':key}
            r = requests.post('http://localhost:8888/post',json={'command':command})
            print(r.text)
        elif key in turns:
            command = {'type':'turn','value':key}
            r = requests.post('http://localhost:8888/post',json={'command':command})
    else:
        break
print("end")
