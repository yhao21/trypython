
#==============# Step 1 Scrapping


from selenium import webdriver
# beautifulsoup-like package in selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# wait until page is loaded out.
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# set up headless webbrowser
from selenium.webdriver.chrome.options import Options 

options = Options()
options.headless = True

driver = webdriver.Chrome(options = options)

# if you run on server without gpu, use the following code
#options = Options()
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')
#driver = webdriver.Chrome(options=options)



driver.get('https://cosmos.bigdipper.live/validator/cosmosvaloper1m73mgwn3cm2e8x9a9axa0kw8nqz8a492ms63vn')

# wait until specific content is loaded by using <EC.presence_of_element_located>
# "." for the value of each class when you inspect the web page
uptime_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.value.text-right.col-4')))
content = driver.find_element_by_css_selector('.value.text-right.col-4')

'''
the results from uptime_element and content are exactly the same.

<selenium.webdriver.remote.webelement.WebElement (session="cb5f804f1467f
4da170b02e977c6124f", element="4a5ac45e-f627-4391-be8b-aac1ca5c738b")>
<selenium.webdriver.remote.webelement.WebElement (session="cb5f804f1467f
4da170b02e977c6124f", element="4a5ac45e-f627-4391-be8b-aac1ca5c738b")>
'''
print(uptime_element)
print(content)


# use uptime_element.text to acquire the text content
# 99.95%
uptime = float(uptime_element.text.replace('%',''))
print(uptime)





#==============# Step 2 Send email
#--------#
## Send a email when the program is finished

# use it to send email

#import smtplib
#
#
#
#gmail_user = 'your-email-address@gmail.com'
#gmail_password = 'jhywwepmqsxlddgb'
#
## add receiver
#to = [
#        'aaa@gmail.com',
#        'bbb@163.com'
#        ]
#
#
#
#subject = 'testing email'
#body = 'hahahah\nhahahah'
#email_text = 'From: ' + gmail_user + '\n' + 'To: ' + ', '.join(to) + '\n' + 'Subject: ' + subject + '\n\n' +  body
#
#
#try:
#    # port: 465
#    # simple mail transfer protocol (SMTP)
#    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#    server.ehlo()
#    server.login(gmail_user, gmail_password)
#    server.sendmail(gmail_user, to, email_text)
#    server.close()
#
#except:
#    print('sendig error')









