import requests


def main():
    response = requests.get('http://www.baidu.com')
    print(response.headers)


if __name__=="__main__":
    main()
