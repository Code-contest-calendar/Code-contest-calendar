from bs4 import BeautifulSoup
import requests
import json
import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter
import pickle

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""

simplejson = json
url= 'https://www.topcoder.com/challenges/'
r=requests.get(url)
#data=json.loads(r.content)
data=r.content
soup=BeautifulSoup(data)
co=0
z= open("C:\Users\Hai\Desktop\TopComp.txt","w+")

spoilers=[]
complete = 0
number = 1
f = open("data.p","wb")
z.write("S.No\t\tComp_Code\t\tComp_Link\t\tComp_Name\tComp_Start\t\tComp_End\n\n")

for d in soup.find_all("div", {"class": "_3pMa6m"}):
	# for di in d.find_all('div'):
	print d
	print "--------"
	print "\n"
		# for divs in di.find.all("div", {"class": "_3pMa6m"}) :
		# 	print "here"
			# for sen in divs.find_all('a'):
			# 	comp_name = sen.get_text();
			# 	print comp_name
			# 	z.write(comp_name)
			# 	z.write("\n\n")


	# complete = complete + 1
	# if complete == 2 :
	#<div class="_1TmHFU"><div class="_1u9jzQ"><div class="_3L9NgC"><div><span><span class="_3gJ9l9"><div class="_3v4fM_ _1q-1_C">Cd</div><a href="https://www.topcoder.com/tco"><div class="JXTEtN">TCO</div></a></span></span></div></div><div class="_1wy0wX"><a class="vir_2D" href="/challenges/30060181">Test challenge</a><div class="_3zNR-o"><span class="JV6Mui">Ended Nov 29</span><span><button class="UbryEB">Node.js</button><button class="UbryEB">NodeJS</button></span></div></div></div><div class="_3kYYOO"><div class="_3Ms6oa"><div><div><div class="_3U9-m3"><span class="_2Awv5d">$</span>0</div><div class="_2nDhnS">Purse</div></div></div></div><div class="_2B0m21 _2nCOML"><div><a href="/challenges/30060181">Results</a><span class="_3acj8X"><span class="_33wZr0"><div><a disabled="" class="_1Zw5Ka" href="/challenges/30060181"><svg xmlns="http://www.w3.org/2000/svg" width="14" height="16" viewBox="0 0 14 16"><g fill="#C3C3C8" fill-rule="evenodd"><path d="M12 14L12 13.2C11.8723643 13.1407674 11.3220919 12.8840298 11.1840867 12.8217166 9.91660886 12.2494152 8.85493605 12 7 12 5.14506395 12 4.08339114 12.2494152 2.81591327 12.8217166 2.67790809 12.8840298 2.12763575 13.1407674 1.98829514 13.2037815 1.9969955 13.1998401 2 14 2 14L12 14zM14 13.2L14 16 0 16 0 13.2C0 12.417.45 11.705 1.163 11.382 2.461 10.795 3.808 10 7 10 10.192 10 11.539 10.795 12.837 11.382 13.55 11.705 14 12.417 14 13.2zM7 2C8.1 2 9 2.9 9 4L9 5C9 6.1 8.1 7 7 7 5.9 7 5 6.1 5 5L5 4C5 2.9 5.9 2 7 2L7 2zM7 0C4.8 0 3 1.8 3 4L3 5C3 7.2 4.8 9 7 9 9.2 9 11 7.2 11 5L11 4C11 1.8 9.2 0 7 0L7 0z"></path></g></svg><span class="_3SeoC4">0</span></a></div></span><div class="_1J0hx2"><div><a class="_1gn6mD" href="/challenges/30060181"><svg xmlns="http://www.w3.org/2000/svg" width="14" height="16" viewBox="0 0 14 16"><path fill="#C3C3C8" fill-rule="evenodd" d="M14,15 L14,5 L9,0 L1,0 C0.4,0 0,0.4 0,1 L0,15 C0,15.6 0.4,16 1,16 L13,16 C13.6,16 14,15.6 14,15 Z M2,2 L8,2 L8,6 L12,6 L12,14 L2,14 L2,2 Z"></path></svg><span class="_2Kuu31">0</span></a></div></div></span></div></div></div></div>
	# 	break
	# for lis in divs.find_all('tr'):
	# 	track = 0
	# 	temp = ''
	# 	for sub in lis.find_all('td'):
	# 		if  track==0 :
	# 			comp_code = sub.get_text()
	# 			track = track + 1
	# 			comp_link = "https://www.codechef.com/" + comp_code

	# 			z.write(str(number))
	# 			z.write("-----")
	# 			z.write(comp_code)
	# 			z.write("-----")
	# 			z.write(comp_link)
	# 			z.write("-----")
	# 		elif track == 1 :
	# 			comp_name = sub.get_text()
	# 			z.write(comp_name)
	# 			z.write("-----")
	# 			track =  track+1
	# 		elif track ==2 :
	# 			temp = sub.get_text()
	# 			track = track + 1
	# 			comp_start = temp[7]+temp[8]+temp[9]+temp[10]
	# 			if temp[3:6] == "Jan":
	# 				comp_start = comp_start + "01"
	# 			elif temp[3:6] == "Feb":
	# 				comp_start = comp_start + "02"
	# 			elif temp[3:6] == "Mar":
	# 				comp_start = comp_start + "03"
	# 			elif temp[3:6] == "Apr":
	# 				comp_start = comp_start + "04"
	# 			elif temp[3:6] == "May":
	# 				comp_start = comp_start + "05"
	# 			elif temp[3:6] == "Jun":
	# 				comp_start = comp_start + "06"
	# 			elif temp[3:6] == "Jul":
	# 				comp_start = comp_start + "07"
	# 			elif temp[3:6] == "Aug":
	# 				comp_start = comp_start + "08"
	# 			elif temp[3:6] == "Sep":
	# 				comp_start = comp_start + "09"
	# 			elif temp[3:6] == "Oct":
	# 				comp_start = comp_start + "10"
	# 			elif temp[3:6] == "Nov":
	# 				comp_start = comp_start + "11"
	# 			elif temp[3:6] == "Dec":
	# 				comp_start = comp_start + "12"
	# 			comp_start = comp_start + temp[0] + temp[1]
	# 			z.write(comp_start)
	# 			z.write("-----")
	# 		else :
	# 			temp = sub.get_text()
	# 			comp_end = temp[7]+temp[8]+temp[9]+temp[10]
	# 			if temp[3:6] == "Jan":
	# 				comp_end = comp_end + "01"
	# 			elif temp[3:6] == "Feb":
	# 				comp_end = comp_end + "02"
	# 			elif temp[3:6] == "Mar":
	# 				comp_end = comp_end + "03"
	# 			elif temp[3:6] == "Apr":
	# 				comp_end = comp_end + "04"
	# 			elif temp[3:6] == "May":
	# 				comp_end = comp_end + "05"
	# 			elif temp[3:6] == "Jun":
	# 				comp_end = comp_end + "06"
	# 			elif temp[3:6] == "Jul":
	# 				comp_end = comp_end + "07"
	# 			elif temp[3:6] == "Aug":
	# 				comp_end = comp_end + "08"
	# 			elif temp[3:6] == "Sep":
	# 				comp_end = comp_end + "09"
	# 			elif temp[3:6] == "Oct":
	# 				comp_end = comp_end + "10"
	# 			elif temp[3:6] == "Nov":
	# 				comp_end = comp_end + "11"
	# 			elif temp[3:6] == "Dec":
	# 				comp_end = comp_end + "12"
	# 			comp_end = comp_end + temp[0] + temp[1]
	# 			z.write(comp_end)
	# 		spoilers.append(sub.get_text())
		
	# 	if temp != '' :
	# 		z.write("\n\n")
	# 		number = number + 1
z.close	
pickle.dump(spoilers,f)
f.close()			
# <td data-starttime="2016-01-05T00:00:00+05:30" class="start_date">05 Jan 2016 <br> 00:00:00</td>



		# co=co+1
		# for em in lis.find_all('em'):	
		# 	#print "this is em list : "+str(em)
		# 	try:
		# 		url2=em.find('a')['href']
		# 		r2=requests.get(url2)
		# 		data2=r2.content
		# 		soup2=BeautifulSoup(data2)
		# 		for sentence in soup2.find_all('span',{'class':'spoiler'}):
		# 			print sentence.get_text()
		# 			word= sentence.get_text()
		# 			z.write(word)
		# 			spoilers.append(sentence.get_text())
		# 	except:
		# 		pass
		# 	break
		# if co==20:

