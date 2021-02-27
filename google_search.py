from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
from time import sleep
import csv
import datetime

# 検索ワードの設定
search_word="python"
# 検索するページ数
page=2

options=Options()
options.add_argument('--headless')
driver=webdriver.Chrome(options=options)
driver.get("https://www.google.co.jp")

search_bar=driver.find_element_by_name("q")
search_bar.send_keys(search_word)
search_bar.submit()

try:
    date=datetime.datetime.today().strftime("%Y%m%d")
    csv_file_name="google_search_" + date + ".csv"
    f=open(csv_file_name, mode="w")
    
    writer=csv.writer(f, lineterminator="\n")
    csv_columns=["検索順位", "タイトル", "URL"]
    writer.writerow(csv_columns)
    
    i=0
    item=1
    while True:
        i=i+1
        for tag_h3 in driver.find_elements_by_xpath("//a/h3"):
            tag_a=tag_h3.find_element_by_xpath("..")
            print(tag_h3.text)
            print(tag_a.get_attribute("href"))
            csv_list=[]
            csv_list.append(str(item))
            csv_list.append(tag_h3.text)
            csv_list.append(tag_a.get_attribute("href"))
            writer.writerow(csv_list)
            item=item+1
        next_link=driver.find_element_by_id("pnnext")
        driver.get(next_link.get_attribute("href"))
        if i>page:
            break
    f.close()
except csv.Error as e:
    print(e)