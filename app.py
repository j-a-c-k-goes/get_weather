'''
    get the weather from the command line
'''
import os
path = "http://wttr.in"

def get_weather():
    os.system(f'curl {path}')

if __name__ == "__main__":
    get_weather()
