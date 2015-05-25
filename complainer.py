import fb #To install this package run: sudo pip install fb
from facepy import GraphAPI #To install this package run: sudo pip install facepy
import time


# get the damn access permissions right
# https://www.facebook.com/dialog/oauth?client_id=933124603406845&redirect_uri=https://www.pyoopil.com/&scope=manage_pages
# https://www.facebook.com/dialog/oauth?client_id=933124603406845&redirect_uri=https://www.pyoopil.com/&scope=publish_actions


#You need to get a user access token, here are the steps:
# just create a new facebook app at https://developers.facebook.com/ and get App ID and App secret 
# suppose the app you created is called "MTSTeraMuKaala".
# go to https://developers.facebook.com/tools/explorer/
# select the app you created "MTSTeraMuKaala" and click get access token
# Select "Extended Permissions" 
# check mark manage_pages and publish_actions
# generate and paste the token here

token=""#Insert access token here.  
facebook=fb.graph.api(token)
graph1 = GraphAPI(token)


#mts ka vid = 192081154169158
#found from http://findmyfacebookid.com/
#https://www.facebook.com/MTSIndia
vid=192081154169158 #This is MTS page's facebook id
query=str(vid)+"/posts?fields=id&limit=250"
r=graph1.get(query)



idlist=[x['id'] for x in r['data']]
print("There are "+ str(len(idlist)) +" commentable posts.")

char1='y'
count=0
if char1=='y':
    nos=input("Enter number of posts to be commented on: ")
    if nos<=len(idlist):
       for indid in idlist[len(idlist)-(nos):len(idlist)-1]:
    	  count=count+1
          facebook.publish(cat="comments",id=indid,message="DISGUSTING CUSTOMER SUPPORT - recharged 1499 for prepaid MTS MBLAZE number 8459857098. Getting less than 128 Kbps of speed all over Delhi. Customer care says too many users logged in. All over delhi really?? refund my money or fix my speed. sending email complaints are of no use!! Shame on you disgusting people!!"+str(count))
	  time.sleep(6)
	  
          
          print("Complaint number:"+str(count)+" on www.facebook.com/"+str(indid).split('_')[0]+"/posts/"+str(indid).split('_')[1])
	  
    else: 
          print("Not that many commentable posts available. ")
else :
  print("No complaints made.")
