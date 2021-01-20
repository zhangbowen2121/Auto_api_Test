from telnetlib import EC

from selenium import webdriver  #导入selenium中的webdriver库
import time  #导入时间模块

from selenium.webdriver import ActionChains


driver = webdriver.Firefox()  #实例化出Firefox浏览器
url="http://tocsdemo.tunnel.aitifen.cn/index.html"
driver.get(url)  #登陆web界面
driver.maximize_window()  #窗口最大化

time.sleep(5) #延迟1s
element=driver.find_element_by_class_name('btn-login')
ActionChains(driver).move_to_element(element).perform()
#ul=driver.find_element_by_xpath('//*[@class="login-select"]/ul/li')
driver.find_element_by_xpath('//*[@class="login-select"]/ul/li[2]').click()

driver.find_element_by_xpath('//*[@class="icon"]/input').send_keys("18633002164")  #输入用户名
e=driver.find_element_by_xpath('//*[@class="iconpsword"]/input')
ActionChains(driver).move_to_element(e).perform()
e.send_keys("123456qwe")  #输入密码
#time.sleep(1)
#driver.find_element_by_id("remember").click()   #选中记住密码driver.find_element_by_id("login-submit").click()  #点击登陆
