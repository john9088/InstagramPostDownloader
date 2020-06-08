#tinder Bot
#Number Verifiaction remaining
from selenium import webdriver
import time
import urllib.request

temp = open('credentials.txt','r+')
data = []
temp = temp.read()
data = temp.split('\n')
email = data[0]
password = data[1]


class tinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.instagram.com/')
        
    def login(self,x_path):
        print('inside login method:'+x_path)
        self.fb_btn = self.driver.find_element_by_xpath(x_path).click()
        print('inside login method1:'+self.fb_btn)
        
    def enterCredentials(self,email,password):
        #self.window = self.driver.window_handles
        #self.baseWindow = self.window[0]
        #self.popup = self.window[1]
        #self.driver.switch_to_window(self.popup)
        
        self.email = self.driver.find_element_by_xpath('.//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
        self.email.send_keys(email)

        self.pwd = self.driver.find_element_by_xpath('.//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
        self.pwd.send_keys(password)

        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button').click()

        time.sleep(5)
        try:
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        except:
            print("Did not asked to save credentials")

        try:
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        except:
            print("Did not asked to turn on notification")

            
        
        self.firstPost = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[1]/div[3]/div/article[1]/div[1]')

        try:
            self.firstPostImg = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[1]/div[3]/div/article[1]/div[1]/.//img')
            img = self.firstPostImg.get_attribute('src')
            #print(img)
            urllib.request.urlretrieve(img, "download/download.png")
            print("The file is downloaded in download/download.png")
        except:
            print("1st post is not Image")
            try:
                self.firstPostVideo = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[1]/div[3]/div/article[1]/div[1]/.//video')
                video = self.firstPostImg.get_attribute('src')
                #print(video)
                urllib.request.urlretrieve(video, "download/download.mp4")
                print("The file is downloaded in download/download.mp4")
            except:
                print("1st post is not Video")
        
        #print(self.firstPost)
        #self.driver.find_element_by_xpath('//*[@id="u_0_0"]').click()
        #self.driver.find_element_by_xpath('//*[@id="u_0_4"]/div[2]/div[1]/div[1]/button').click()
        #self.driver.switch_to_window(self.baseWindow)
        
        #self.ph_no = self.driver.find_element_by_xpath(ph_no_x_path)
        #self.ph_no.send_keys('9167441331')
        #self.login_click = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button')
        #self.login_click.click()

x_path = '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button'
ph_no_x_path = '//*[@id="modal-manager"]/div/div/div[2]/div[2]/div/input'

bot = tinderBot()
#for i in range(3):
    #time.sleep(2)
    #print(i)
#bot.login(x_path)

time.sleep(5)
    #print(i)
bot.enterCredentials(email,password)
