from bs4 import BeautifulSoup
import requests
import csv
import urllib.request

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

source = requests.get('https://www.amazon.in/s?bbn=1968120031&rh=n%3A1571271031%2Cn%3A%211571272031%2Cn%3A1968024031%2Cn%3A1968120031%2Cp_n_material_browse%3A1974776031&dc&fst=as%3Aoff&qid=1605156449&rnid=1974774031&ref=lp_1968120031_nr_p_n_material_browse_1', headers = headers).text
soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

Names = []
Prices = []
Brands =[]
Images=[]

# for loop

for name in soup.find_all('span', class_='a-size-base-plus a-color-base a-text-normal'):
    string = name.text
    Names.append( string.strip() )

for brand in soup.find_all('span', class_='a-size-base-plus a-color-base'):
    string = brand.text
    Brands.append( string.strip() )

for pr in soup.find_all('span', class_='a-price-whole'):
    Prices.append(pr.text)

Product=list(map(lambda x, y: x+ ' ' +y, Brands, Names))

img_links=soup.find_all('img', class_='s-image')
for i in range(len(img_links)):
    Images.append(img_links[i]['src'])

#print(Images)
for i in range(len(Images)):
    #Copies a network object denoted by a URL to a local file.
    name="C:/Users/Admin/c_trial/Men_Cotton_Tshirts_Images/"+str(i)+".jpg"
    urllib.request.urlretrieve(Images[i], name)


file_name = 'Men_Cotton_Tshirts.csv'

with open(file_name, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Sr.No', 'Product Name', 'Price(Rs)'])
    for i in range(len(Names)):
        writer.writerow([i+1, Product[i], Prices[i]])


"""for image in soup.find_all('img', class_='s-image'):
    i=0
    Images.append(image['src'])
    img_link=img['src']
    #img_name=img.get('alt')
    pic=requests.get('img_link')
    writer.writerow([i+1, Product[i], pic.content, Prices[i]])
    i+=1"""