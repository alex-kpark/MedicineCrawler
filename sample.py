#-*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from selenium.webdriver import ActionChains

import urllib.request
import requests

import os
from time import sleep

import xlrd
import json

# Step 1 : Driver 정의 및 URL 설정

chrome_path = 'C:/Users/ALEXa/AppData/Local/Programs/Python/chromedriver.exe'

driver = webdriver.Chrome(executable_path=chrome_path) #driver 실행, 빈 브라우저를 띄워주는 기능

driver.get('http://www.health.kr/searchDrug/search_detail.asp')

# Step 2 : 약학정보원 사이트 접근

def search_medicine(query):
    effect_query = driver.find_element_by_xpath("//input[@id='input_effect']") #효능, 효과 검색어 입력창을 선택 (id는 HTML 상에서 유일한 값을 갖기 때문에 버그 가능성이 적음)
    effect_query.send_keys(query) #query - 검색할 효능, 효과 쿼리를 검색어 입력창 안에 넣어줌

    general_select = driver.find_element_by_xpath("//label[@for='tb2_2'][@class='ico']") #label 태그를 잡아서 일반 항목 클릭하는 Element를 만들고
    general_select.click() #체크박스 클릭

    start_search_btn = driver.find_element_by_xpath("//button[@id='btn_detail_search']")
    start_search_btn.click()

    sleep(3)
    specific_result = driver.find_element_by_xpath("//a[@id='anchor_proy_more']") #검색결과 더보기 버튼\
    specific_result.click()

    #10개보기를 100개보기로 확장
    view_expansion = driver.find_element_by_xpath("//a[@id='line_selectBoxTitle']")
    view_expansion.click()
    hundred_list = driver.find_element_by_xpath("//li[@id='line_li_100']")
    hundred_list.click()
    sleep(2)

# Step 3 : 세부 데이터를 수집하기

# 인코딩 문제 해결 못함
def get_info():
    move_into_btns = driver.find_elements_by_xpath("//td[@class='txtL'][@style='cursor:pointer']") #len() 하면 100개 출력, 배열(list) 형태로 각 약 이름들이 들어가있음
    move_into_btns[0].click() #100개 뜬 약물 이름들 중 첫 번째 것 CLICK
    
    #약의 이름
    drug_data = driver.find_element_by_xpath("//td[@id='result_drug_name']").text
    drug_name = str(drug_data).encode('utf-8')
    print('success')
    print(type(drug_name))
    print(drug_name)


    


# Step 4 : for문 돌면서 약 리스트 돌기



search_medicine('두통')
get_info()

