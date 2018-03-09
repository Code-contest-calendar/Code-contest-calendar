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
url= 'http://codeforces.com/contests?complete=true'
r=requests.get(url)
#data=json.loads(r.content)
data=r.content
soup=BeautifulSoup(data)
co=0
z= open("C:\Users\Hai\Desktop\pastComp.txt","w+")

spoilers=[]
complete = 0
number = 1
f = open("data.p","wb")
z.write("S.No\t\tComp_Code\t\tComp_Link\t\tComp_Name\tComp_Start\t\tComp_End\n\n")

no = 0

for d in soup.find_all("div", {"class","contests-table"}):
	print "them-2"
	for di in d.find_all("div", {"class","datatable"}):
		print "yeah\n"
		for div in di.find_all("table"):
			# print "there-1\n\n\n"
			no =no + 1

			print "\n\n\n\n\nHey\n\n\n\n\n"
			# print div
			print "\n\n\n\n\nHey\n\n\n\n\n"
			if no == 3:
				break
			# print "\n\n\ntuhi\n\n\n"
			for value in range(950,1200) :
				strvalue = str(value) 
				#print "\n\n\nOkayy\n\n\n"
				if div.find("tr" ,{"data-contestid", strvalue }) != None :
					for divs in div.find("tr" ,{"data-contestid", strvalue }):
						print "Heyyyyyy\n"
					#no = no+1
				# if no == 3 :
				# 	break
				# print '\n\n\nBefore-1\n\n'
				# print divs
				# print "\n\n\nAfter-1\n\n\n"



	# # complete = complete + 1
	# # if complete == 2 :
	# # 	break
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

