from selenium import webdriver
import os
import time
path = os.getcwd()
path1=path+"\\zips.txt"
with open (path1) as f:
	zips=f.readlines()
print zips


PROXY = "52.173.248.143:8080" # IP:PORT or HOST:PORT

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)
name=''
email=''
org=''
phone=''
address=''
city=''
state=''
zp=''
language=''
website=''


chrome = webdriver.Chrome(chrome_options=chrome_options)
for items in zips:
	chrome.get("https://www.deltadental.com/DentistSearch/DentistSearchController.ccl?Action=ViewDentistSearchForm")
	time.sleep(3)
	court_selector=chrome.find_elements_by_xpath('//*[@id="in3"]')
	length= len(court_selector)
	if length>0:		
		court_selector[0].click()
		ret=items.split('\n')
		print (ret)
		court_selector[0].clear()
		court_selector[0].send_keys(items)
	time.sleep(2)
	for i in range(1,10):
		xp='//*[@id="moreInfoIcon_'+str(i)+'"]/img'  #more info
		court_selector=chrome.find_elements_by_xpath(xp)
		length= len(court_selector)
		if length>0:		
			court_selector[0].click()
		xp='//*[@id="zebraStripe"]/tbody/tr['+str(i)+']/td/table/tbody/tr[1]/td[1]/span'
		court_selector=chrome.find_elements_by_xpath(xp)
		length= len(court_selector)
		if length>0:
			name=str(court_selector[0].text)
		print name
		
		#//*[@id="zebraStripe"]/tbody/tr[2]/td/table/tbody/tr[1]/td[1]/text()[1]  org
		#//*[@id="zebraStripe"]/tbody/tr[2]/td/table/tbody/tr[1]/td[1]/text()[2]  Address
		#//*[@id="zebraStripe"]/tbody/tr[2]/td/table/tbody/tr[1]/td[1]/text()[3]  Ctity state zip
		#//*[@id="zebraStripe"]/tbody/tr[2]/td/table/tbody/tr[1]/td[1]/text()[4]  phone
		#//*[@id="moreInfoData_5"]/td[2]/a  email
		#//*[@id="moreInfoData_5"]/td[2]/text()[1] language
		sx=chrome.find_element_by_xpath('//*[@id="zebraStripe"]/tbody/tr['+str(i)+']/td/table/tbody/tr[1]/td[1]').text
		print sx.split('\n')
		sx=sx.split('\n')
		org=str(sx[1])
		address=str(sx[2])
		st=str(sx[3])
		print st
		sp=st.split(',')
		print sp
		city=sp[0]
		st=sp[1].split(' ')
		state=st[1]
		zp=st[2]
		phone=str(sx[4])
		
		
		"""
		xp='//*[@id="zebraStripe"]/tbody/tr['+str(i)+']/td/table/tbody/tr[1]/td[1]/text()[1]'
		court_selector=chrome.find_elements_by_xpath(xp)
		length= len(court_selector)
		if length>0:
			org=str(court_selector[0].text)
		xp='//*[@id="zebraStripe"]/tbody/tr['+str(i)+']/td/table/tbody/tr[1]/td[1]/text()[2]'
		court_selector=chrome.find_elements_by_xpath(xp)
		length= len(court_selector)
		if length>0:
			address=str(court_selector[0].text)
		xp='//*[@id="zebraStripe"]/tbody/tr['+str(i)+']/td/table/tbody/tr[1]/td[1]/text()[3]'
		court_selector=chrome.find_elements_by_xpath(xp)
		length= len(court_selector)
		if length>0:
			city=str(court_selector[0].text)
			st=city
			sp=st.split(',')
			city=sp[0]
			st=sp[1].split(' ')
			state=st[1]
			zp=st[2]
		xp='//*[@id="zebraStripe"]/tbody/tr['+str(i)+']/td/table/tbody/tr[1]/td[1]/text()[4]'
		court_selector=chrome.find_elements_by_xpath(xp)
		length= len(court_selector)
		if length>0:
			phone=str(court_selector[0].text)
		"""
		xp='//*[@id="moreInfoData_'+str(i)+'"]/td[2]/a'
		court_selector=chrome.find_elements_by_xpath(xp)
		length= len(court_selector)
		if length>0:
			email=str(court_selector[0].text)
		more=chrome.find_element_by_xpath('//*[@id="moreInfoData_'+str(i)+'"]/td[1]').text
		more=more.split('\n')
		temp=str(more[1]).split(':')
		gender=temp[1]
		len2=len(more)
		if len2>2:
			temp=str(more[3]).split(':')
			language=temp[1]
		"""
		xp='//*[@id="moreInfoData_'+str(i)+'"]/td[2]/text()[1]'
		court_selector=chrome.find_elements_by_xpath(xp)
		length= len(court_selector)
		if length>0:
			language=str(court_selector[0].text)
		xp='//*[@id="moreInfoData_'+str(i)+'"]/td[1]/text()[1]'
		court_selector=chrome.find_elements_by_xpath(xp)
		length= len(court_selector)
		if length>0:
			gender=str(court_selector[0].text)
			"""
		file = open("output.csv","a")
		finalst=name+','+address+','+city+','+state+','+phone+', ,'+email+', , , ,\n'
		file.write(finalst)
		file.close()
		name=''
		email=''
		org=''
		phone=''
		address=''
		city=''
		state=''
		zp=''
		language=''
		website=''
	"""
	court_selector=chrome.find_elements_by_xpath('//*[@id="in15"]')
	length= len(court_selector)
	if length>0:		
		court_selector[0].click()
		"""