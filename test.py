from selenium import webdriver
import chromedriver_binary 
import time

def kansuu_test():
    print('kansuu_test')
    print('kansuu_test')
    print('kansuu_test')
    print('kansuu_test')
    print('kansuu_test')
    print('kansuu_test')
    print('kansuu_test')

def my_sum(a, b):
    sum = a + b
    return sum

# コメント
# my_list = ["たんじろう", "ぎゆう", "かなお", "むざん"]
# for name in my_list:
#     if name == "むざん":
#         print(name + "は、鬼です。")
#     else:
#         print(name + "は、人間です。")

def scrape():
    driver = webdriver.Chrome()
    driver.get("https://google.co.jp")
    time.sleep(10)

scrape()