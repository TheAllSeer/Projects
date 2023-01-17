# ================== import modules ================================
import fcred
import re
import time
from bs4 import BeautifulSoup
import datetime
from datetime import datetime, timedelta
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait       
from selenium.webdriver.common.by import By       
from selenium.webdriver.support import expected_conditions as EC
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
# import fake_useragent
# from fake_useragent import UserAgent
import screeninfo
import pyautogui
import undetected_chromedriver as uc
import sys 

# these 3 lines are encoding related to grab weird charachters as well
if not 'pytest' in sys.modules:  # workaround for https://github.com/pytest-dev/pytest/issues/4843
    sys.stdout.reconfigure(encoding='utf-8', errors='namereplace')
    sys.stderr.reconfigure(encoding='utf-8', errors='namereplace')
#===============================================================================
#========================function definition====================================
def stringToSec(c:str):
    m = re.search(r"^\d{1,2}", c.lower())
    if m:         
        amount = int(m.group())
        # print(f'----debug: amount = {amount}')
    else:
        amount = 1
        # print(f'----debug: amount = {amount}')
    if re.search('\sweeks', c):
        return 604800*amount
    elif re.search('\sweek', c): 
        return 604800*amount
    elif re.search('\sdays', c):
        return 86400*amount
    elif re.search('\sday', c):
        return 86400*amount
    elif re.search('\shours', c):  
        return 3600*amount
    elif re.search('\shour', c):  
        return 3600*amount
    elif re.search('\sminutes', c):
        return 60*amount
    elif re.search('\sminute', c):
        return 60*amount
    elif re.search('\sseconds', c):  
        return 1*amount
    elif re.search('\ssecond', c):  
        return 1*amount
    else:
        return 1*amount


#===============================================================================
#========================function definition====================================
# def initializedriver():
#     opts = Options()
#     opts.add_argument("--window-size=1920,1080")
#     opts.add_argument("--start-maximized")
#     opts.add_argument('disable-infobars')
#     opts.add_argument("--disable-extensions")
#     opts.headless = True
#     prefs = {"profile.default_content_setting_values.notifications" : 2}
#     opts.add_experimental_option('prefs', prefs)
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
#     return driver

# -- cannot use this, due to the fact that in order to have an undetected-chromedriver it has to be initialized inside if name == main.
#===============================================================================
#========================function definition====================================

def facebooklogin(loginmail:str, loginpw:str, driver):
    try:
        driver.get('https://www.facebook.com/login')
        time.sleep(random.uniform(5, 5.5))
        try:
            driver.find_element(By.ID, 'email_container').find_element(By.TAG_NAME, 'input').send_keys(loginmail)
        except:
            return print('----debug: failed at login(1/3).')
        print('----debug: login (1/3) complete. proceeding...')
        time.sleep(random.uniform(5, 5.5))
        try:
            driver.find_element(By.ID, 'pass').send_keys(loginpw)
        except:
            return print('----debug: failed at login(2/3).')
        print('----debug: login (2/3) complete. proceeding...')
        time.sleep(random.uniform(5, 5.5))
        try:
            driver.find_element(By.ID, 'loginbutton').click()
        except:
            return print('----debug: failed at login(3/3).')
        time.sleep(random.uniform(5, 5.5))
        print('----debug: successful login.')
        return driver
    except:
        return 'no driver is currently running.'

#===============================================================================
#========================function definition====================================

def setfilters(driver, category, location, rad): 
    driver.get(f'https://www.facebook.com/marketplace')
    time.sleep(random.uniform(5, 5.5))
    # setting location filters.
    for i in range(10):
        try:
            # localfilters=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1q0g3np x87ps6o x1lku1pv x78zum5 x1a2a7pz x1xmf6yo'.replace(' ', '.'))))
            # driver.implicitly_wait(random.uniform(2, 2.5))
            localfilters = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x1f6kntn xvq8zen x1s688f x1qq9wsj'.replace(' ', '.'))))
            localfilters.click()  
            break
        except:
            print(f'----debug: failed to execute. currently at url: driver.current_url = {driver.current_url}. retrying..({i+1}/10)')


    time.sleep(random.uniform(5, 5.5))
    # localbox = driver.find_element(By.CLASS_NAME, 'x1i10hfl xggy1nq x1s07b3s x1kdt53j x1a2a7pz xjbqb8w x76ihet xwmqs3e x112ta8 xxxdfa6 x9f619 xzsf02u x1uxerd5 x1fcty0u x132q4wb x1a8lsjc x1pi30zi x1swvt13 x9desvi xh8yej3 x15h3p50 x10emqs4'.replace(' ', '.'))
    try:
        localbox = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/label/div/div[2]')))
        driver.implicitly_wait(random.uniform(5, 5.5))
    except:
        # print(f'----debug: localbox first attempt failed, trying the other:')
        try:
            localbox = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.x1i10hfl xggy1nq x1s07b3s x1kdt53j x1a2a7pz xjbqb8w x76ihet xwmqs3e x112ta8 xxxdfa6 x9f619 xzsf02u x1uxerd5 x1fcty0u x132q4wb x1a8lsjc x1pi30zi x1swvt13 x9desvi xh8yej3 x15h3p50 x10emqs4'.replace(' ', '.'))))
            driver.implicitly_wait(random.uniform(5, 5.5))
        except:
            print(f'----debug: second localbox attempt failed. ')
        
    time.sleep(3)
    #full xml for localbox: '/html/body/div[3]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/label/div/div[2]/input'
    localbox.send_keys(Keys.CONTROL + "a")# clearing location input box
    localbox.send_keys(location) # filling in the location input box
    time.sleep(random.uniform(5, 5.5))
    localbox.send_keys(Keys.ARROW_DOWN) # selecting the first option on the list with down + enter
    time.sleep(random.uniform(5, 5.5))
    localbox.send_keys(Keys.RETURN)  # enter
    time.sleep(random.uniform(5, 5.5))
    try:
        radbox = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#jsc_c_2hz > div')))
        driver.implicitly_wait(random.uniform(5, 5.5))
    except:
        try:
            radbox = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="jsc_c_2i9"]/div')))
        except:
            try:
                radbox = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div xjyslct xjbqb8w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x78zum5 x1jchvi3 x1fcty0u x132q4wb xdj266r x11i5rnm xat24cr x1mh8g0r x1a2a7pz x9desvi x1pi30zi x1a8lsjc x1n2onr6 x16tdsg8 xh8yej3 x1ja2u2z xzsf02u x1swvt13'.replace(' ', '.'))))
            except:
                radbox = 'you tried'
    radbox.click()
    weirdlist = driver.find_elements(By.CSS_SELECTOR, 'div.x1i10hfl[role=option]')  # weirdlist is radius options. 
    time.sleep(.5)
    for i in range(len(weirdlist)):  # clicking the option that says "rad kilometers"
        w = weirdlist[i]
        time.sleep(.5)
        if 'kilometers' in w.text or 'miles' in w.text:
            try:
                kmN = int(re.search('\d{1,4}', w.text).group())
            except:
                print('----debug: undefined kmn')
            if int(rad) == kmN:
                driver.execute_script("arguments[0].click();", w)
                break
            elif int(rad) < kmN:
                driver.execute_script("arguments[0].click();", w)
                break
            # else:
            #     print('not your option yet.')

    # localbox = driver.find_element(By.CLASS_NAME, 'x1i10hfl xggy1nq x1s07b3s x1kdt53j x1a2a7pz xjbqb8w x76ihet xwmqs3e x112ta8 xxxdfa6 x9f619 xzsf02u x1uxerd5 x1fcty0u x132q4wb x1a8lsjc x1pi30zi x1swvt13 x9desvi xh8yej3 x15h3p50 x10emqs4'.replace(' ', '.'))
    localbox.send_keys(Keys.RETURN)
    time.sleep(random.uniform(5, 5.5))
    # row under me clicks the apply button. 
    # apply = driver.find_element(By.CLASS_NAME, 'x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x1f6kntn xvq8zen x1s688f xtk6v10'.replace(' ', '.'))
    # apply = driver.find_element(By.CSS_SELECTOR, 'span.x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft'.replace(' ', '.')).click()
    # time.sleep(random.uniform(3, 5))
    try:
        apply = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[6]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[2]/div/div/div/div/div/div/div[1]/div/span/span')))
    except:
        try:
            apply = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mount_0_0_o3 > div > div:nth-child(1) > div > div:nth-child(7) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div.x1n2onr6.x1ja2u2z.x9f619.x78zum5.xdt5ytf.x2lah0s.x193iq5w > div > div:nth-child(2) > div > div > div > div > div > div > div.x6s0dn4.x78zum5.xl56j7k.x1608yet.xljgi0e.x1e0frkt > div > span > span')))
        except:
            try:
                #/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[2]/div/div/div/div/div/div/div[1]/div/span
                apply = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[2]/div/div/div/div/div/div/div[1]/div/span')))
            except:
                apply = 'you_tried'
    driver.implicitly_wait(random.uniform(5, 5.5))
    driver.execute_script("arguments[0].click();", apply)
    time.sleep(random.uniform(5, 5.5))
    return driver


#===============================================================================
#========================function definition====================================
def fetchdata(driver, keyword:str, category:str, minpricestr, maxpricestr, refresh_sec):
    if category.lower() == 'free stuff':
        category = 'free'
    elif category.lower() == 'property rentals':
        category = 'propertyrentals'
    elif 'garden' in category.lower():
        category = 'garden'
    elif 'pet' in category.lower():
        category = 'pets'
    elif 'sport' in category.lower():
        category = 'sports'
    elif 'toy' in category.lower():
        category = 'toys'
    elif 'office' in category.lower():
        category = 'office-supplies'
    elif 'music' in category.lower():
        category = 'instruments'
    elif category.lower() == 'home sales':
        category = 'propertyforsale'
    elif 'home improvement' in category.lower():
        category = 'home-improvements'
    elif category.lower() == 'home goods':
        category = 'home'
    

    driver.get(f'{driver.current_url}/{category}?sortBy=creation_time_descend&exact=false')
    html_body = driver.find_element(By.TAG_NAME, 'body')
    body_html = html_body.get_attribute('innerHTML')
    soup = BeautifulSoup(body_html, 'html.parser')
    links = soup.select('div.x3ct3a4')

    try:
        refreshrate = int(refresh_sec)
    except:
        pass
    try:
        refreshrate = stringToSec(refresh_sec)
    except:
        return 'please enter a valid refresh rate. (format: __(amount of)____(unit [seconds/minutes/hours]))'

    # driver.get(f'https://www.facebook.com/marketplace/110619208966868/{category}?sortBy=creation_time_descend&exact=false')
    
    relevantdict = {}

    # =====================================loop of links===================================
    for link in links:
        # print(f'----debug: link.text = {link.text}')
        # href = link.select_one('a[role=link]').get('href')
        # print(f"----debug: href = {href}'")
        listingurl = f"https://www.facebook.com{link.select_one('a[role=link]').get('href')}"
        # print(f"----debug: listingurl = {listingurl}'")
        try:
            driver.get(f'{listingurl}')
            listingid = str(int(re.search('(?<!item)\d+(?!\?hoisted)', listingurl).group(0)))
            time.sleep(random.uniform(4, random.uniform(5, 6)))
        except:
            # print(f'----debug: deprecated url. exception failed to reach listingurl at {listingurl}')
            continue

        html_body = driver.find_element(By.TAG_NAME, 'body')
        body_html = html_body.get_attribute('innerHTML')
        souplisting = BeautifulSoup(body_html, 'html.parser')
        try:
            container = souplisting.select_one('div.xyamay9.x1pi30zi.x18d9i69.x1swvt13')
            # print(f'----debug: container = {container}')  # x1s688f, xk50ysn these classes differ with each category. 
            listingtitle = container.select_one('span x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x14z4hjw x3x7a5m xngnso2 x1qb5hxa x1xlr1w8 xzsf02u'.replace(' ', '.')).text
            # print(f'----debug: listingtitle = {listingtitle}')
            try:
                listingprice = container.select_one('span x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x676frb x1jchvi3 x1lbecb7 xzsf02u'.replace(' ', '.')).text
            except:    
                listingprice = 'noprice'
                # print(f'----debug: listingprice = {listingprice}')
            try:
                listingtimeLocation = container.select_one('span.x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x676frb x1pg5gke x1sibtaa xo1l8bm xi81zsa'.replace(' ', '.')).text
            except:
                listingtimeLocation = 'notimelocation'
                # print(f'----debug: listingtimeLocation = {listingtimeLocation}')
            try:
                posttime = re.search(r'Listed (.*) ago in', listingtimeLocation).group(1).strip()
            except:
                posttime = 'noposttime'
                # print(f'----debug: posttime = {posttime}')
            try:
                postlocation = re.search(r'in (.*)', listingtimeLocation).group(1).strip()
            except:
                postlocation = 'nopostlocation'
                # print(f'----debug: postlocation = {postlocation}')
            try:
                postsecondsago = stringToSec(posttime)
            except:
                postsecondsago = 'nopostsecondsago'
                # print(f'----debug: postsecondsago = {postsecondsago}')
            if postsecondsago > refreshrate:
                # print(f'----debug: ({postsecondsago} > {refreshrate} ? postsecondsago > refreshrate = {postsecondsago > refreshrate}')
                # print('because we sort by creation date ascending, as soon as we hit an irrelevant post we can stop.')
                break
            else:
                if re.search(r'\d+', listingprice):
                    listingpricenum = re.search(r'\d+', listingprice.replace(',', '')).group(0)
                    # print(f'----debug: listingpricenum = {listingpricenum}')
                    listingpriceint = int(listingpricenum)
                    # print(f'----debug: listingpriceint = {listingpriceint}')
                else:
                    listingpriceint = 0
                    # print(f'----debug: listingpriceint = {listingpriceint}')
                try:
                    minprice = int(minpricestr)
                    # print(f'----debug: minprice = {minprice}')
                except:
                    minprice = 0
                    # print(f'----debug: minprice = {minprice}')
                try:
                    maxprice = int(maxpricestr)
                    # print(f'----debug: maxprice = {maxprice}')
                except:
                    maxprice = 99999999
                    # print(f'----debug: maxprice = {maxprice}')
                    # print(f'----debug: keyword = {keyword}')
                    # print(f'----debug: keyword in listingtitle = {keyword in listingtitle}')
                if minprice <= listingpriceint <= maxprice and keyword.lower() in listingtitle.lower() :
                    # print(f'----debug: this listing is going to relevantdict. listingtitle = {listingtitle}')
                    relevantdict[listingtitle] = {'listingid':listingid,
                                                    'listingprice':listingprice,  
                                                    'posttime':posttime,
                                                    'postlocation':postlocation,
                                                    'link':listingurl,
                                                    'scrapetime':datetime.strftime(datetime.now(), '%d-%m-%Y, %HH:%MM')}       
                    print(f'saving {listingtitle} to dict...')                 
                # else:
                    # print(f'----debug: keyword in listingtitle = {keyword in listingtitle} (keyword, listingtitle = {keyword, listingtitle})') when you comment this and row below make sure to comment else as well
                    # print(f'----debug: min<listingprice<max = {minprice <= listingpriceint <= maxprice}.')              
        except:
            print(f'----debug: souplisting failed to load for: {listingtitle} at link: {listingurl}.')
        time.sleep(random.uniform(4, 5))

    # driver.get(f'https://www.facebook.com/marketplace/110619208966868/{category}?sortBy=creation_time_descend&exact=false')


    # print(f'----debug: relevantdict = {relevantdict}')
    driver.quit()
    return relevantdict
    
#===============================================================================
#========================function definition====================================
def listdictToDataFrame(rd:dict):
    df = pd.DataFrame.from_records(rd).transpose()
    df.reset_index(inplace = True)
    df.rename(columns = {df.columns[0]:'listingtitle'}, inplace = True)
    postTimes = [datetime.now() - timedelta(seconds = stringToSec(df['posttime'].iloc[i])) for i in range(len(df))]  # stringToSec takes a string like '5 minutes' and turns it into seconds in int. timedelta is a datetime object.
    try:    
        df['postdate'] = pd.Series([postTimes[i].strftime('%d/%m/%y %H:%M:%S') for i in range(len(postTimes))], dtype='float64')  # postTimes is the list of [scrapedate - timedelta = time posted]
        if len(df) == 0:
            return df
        return df
    except:
        return df
#===============================================================================
#========================function definition====================================


# def main():

   
    
if __name__ == '__main__':
    



    categories  = ['Vehicles', 'Property Rentals', 'Apparel', 'Classifieds', 'Electronics', 'Entertainment', 'Family', 'Free Stuff', 'Garden & Outdoor', 'Hobbies', 'Home Goods', 'Musical Instruments', 'Office Supplies', 'Pet Supplies', 'Sporting Goods', 'Toys & Games']
    lowerC = [c.lower() for c in categories]
    upperC = [c.upper() for c in categories]

    #==================== test variables=========================
    # category = 'Vehicles'.lower()
    # location = 'austin, texas'
    # rad = '50'
    # minpricestr = '0'
    # maxpricestr = '20000'
    # keyword = ''
    # refresh_sec = '30 minutes'
    # your_mail = '--'
    #============================================================
    # real variables============================================
    while True:
        category = input("please enter a category from the list: \nVehicles, Property Rentals, Apparel, Classifieds, Electronics, Entertainment, Family, Free Stuff , Garden & Outdoor, Hobbies, Home Goods, Musical Instruments, Office Supplies, Pet Supplies, Sporting Goods, Toys & Games:\n")
        if category in lowerC or category in categories or category in upperC:
            category = category.lower()
            break
        else:
            print('invalid category. please make sure the category you have entered is from the list: \nVehicles, Property Rentals, Apparel, Classifieds, Electronics, Entertainment, Family, Free Stuff, Garden & Outdoor, Hobbies, Home Goods, Musical Instruments, Office Supplies, Pet Supplies, Sporting Goods, Toys & Games')

    location = input('please enter a search location:\n')
    rad = input('please enter a search radius:\n')
    while True:
        minpricestr = input('please enter a minimum price for search:\n')
        if re.search('[A-Za-z]+', minpricestr):
            print('invalid number. ')
        else:
            break
    while True:
        maxpricestr = input('please enter a maximum price for search:\n')
        if re.search('[A-Za-z]+', maxpricestr):
            print('invalid number. ')
        else:
            break
    keyword = input('please enter a keyword for search:\n')
    refresh_sec = input("please enter a refresh rate (possible format examples: 5 minutes, 2 days... or amount of seconds in number: 300, 500, 600...):\n")
    while True:
        your_mail = input('please enter your email address:\n')
        if not re.search('\@', your_mail):
            print('invalid email. please make sure you type the correct email address.')
        else:
            break
    #============================================================
    r_sec = stringToSec(refresh_sec)  # for time.sleep for a concurrent run of the script
    print('Initializing search...')
    while True:
        print('Starting scan.')
        # ua = UserAgent()
        # headers = {'User-Agent':ua.random}
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
        screen = screeninfo.get_monitors()[0]
        screen_width, screen_height = screen.width, screen.height
        options = uc.ChromeOptions()
        options.add_argument(f"--window-size={screen_width},{screen_height}")
        options.add_argument("--start-maximized'")
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument("--headless")
        # prefs = {"profile.default_content_setting_values.notifications" : 2}
        driver = uc.Chrome(options = options, desired_capabilities=headers)
        driver.get('https://nowsecure.nl')
        time.sleep(4)
        logindriver = facebooklogin(fcred.mail, fcred.p, driver)
        time.sleep(random.uniform(2, random.uniform(3, 5)))
        filterdriver = setfilters(logindriver, category, location, rad)
        rd = fetchdata(filterdriver, keyword, category, minpricestr, maxpricestr, refresh_sec)
        df = listdictToDataFrame(rd)
        try:
            old_data = pd.read_csv(f'data_{keyword}_{category}.csv')
            joined = pd.concat([df, old_data])
            joined = joined[[joined.columns[i] for i in range(len(joined.columns)) if 'Unnamed' not in joined.columns[i] ]]
            joined.to_csv(f'data_{keyword}_{category}.csv', encoding = 'utf-8-sig')
            leng = len(joined) - len(df)
        except FileNotFoundError:
            df = df[[df.columns[i] for i in range(len(df.columns)) if 'Unnamed' not in df.columns[i] ]]
            df.to_csv(f'data_{keyword}_{category}.csv', encoding='utf-8-sig')
            leng = len(df)


        # Set up the SMTP server

        if leng > 0:
            try:
                server = smtplib.SMTP('smtp-mail.outlook.com', 587)
                server.starttls()
                server.ehlo()
                me = fcred.mailsender
                mypw = fcred.mailsenderpw
                you = your_mail
                server.login(me, mypw)

                # df = pd.read_csv(f'data_{keyword}_{category}.csv')
                # Send the email
                from_address = me
                to_address = you
                # subject = "Test Email"
                # body = "This is a test email sent using Python's smtplib library."
                # message = f'Subject: {subject}\n\n{body}'
                message = MIMEMultipart()
                message['Subject'] = f'You have new data! {len(df)} new listings found.'
                message['From'] = me
                message['to'] = you
                html = MIMEText(df.to_html(), 'html')
                message.attach(html)
                server.sendmail(from_address, to_address, message.as_string())
                # Disconnect from the server
                server.quit()
                print('Data Sent. ')
            except:
                print(f'Unable to send mail. You have {len(df)} new listings.')

        else:
            print('No new data.')


        time.sleep(r_sec)
    