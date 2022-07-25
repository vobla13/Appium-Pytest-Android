from pprint import pprint
from browsermobproxy import Server
from selenium import webdriver
from time import sleep

class ProxyManager:

    __BMP = "/home/gitcha/BMP/bin/browsermob-proxy"
    bmp_port={'port':8090}

    def __init__(self):    
        self.__server = Server(ProxyManager.__BMP, options=ProxyManager.bmp_port)
        self.__client = None
    

    def start_server(self):
        self.__server.start()
        return self.__server

    
    def start_client(self):
        self.__client = self.__server.create_proxy(params={'trustAllServers':'true'})
        return self.__client
    

    @property
    def client(self):
        return self.__client

    
    @property
    def server(self):
        return self.__server


    
if __name__ == "__main__":

    proxy =  ProxyManager()
    server = proxy.start_server()
    client = proxy.start_client()
    
    client.new_har("ya.ru")
    print(client.proxy)

    options = webdriver.ChromeOptions()
    options.add_argument("--proxy-server={}".format(client.proxy))
    options.add_argument('ignore-certificate-errors')
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.ya.ru")
    sleep(3)

    pprint(client.har)
    
    driver.close()
    server.stop()
    driver.quit

         

    

    

