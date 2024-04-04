import requests
from bs4 import BeautifulSoup
import pandas as  pd

job_positions=[]
company_name=[]
Address = []
response=requests.get("https://realpython.github.io/fake-jobs/")
soup=BeautifulSoup(response.content,"html.parser")
#print (soup)

job_name= soup.find_all('h2', attrs={'class':'title is-5'})
c_name=soup.find_all('h3', attrs={'class': 'subtitle is-6 company'})

add=soup.find_all('p',attrs={'class':'location'})


for item in job_name:
    job_positions.append(item.text)

for item  in c_name:
    company_name.append(item.text)

for item in add:
   Address.append(item.text)

output_dic= {"Job Title":job_positions, "Company Name":company_name, "Address":Address}

table=pd.DataFrame(output_dic)
table.to_excel("job_info.xlsx")