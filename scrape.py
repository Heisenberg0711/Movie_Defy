from selenium import webdriver
wd = webdriver.Chrome()
wd.get("https://www.fandango.com/61801_movietimes?mode=general&q=61801")

elem = wd.find_elements_by_xpath("//div[@class = 'fd-movie__details']")
for ele in elem:
    print(ele.text)
elem.get_attribute('innerHTML')


times = wd.find_elements_by_xpath("//ul[@class = 'fd-movie__showtimes']")
for time in times:
    print(time.text)
    print('this is one movie \n')
