#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from decode_modules import decode
from people_class import people
from get_gtk import get_G_TK

if __name__ == '__main__':
    with open("./QQ_information.txt", "r") as qq_information_file:
        user_name = qq_information_file.readline()
        # print user_name
        user_password = qq_information_file.readline()
        # print user_password

    qq_login = webdriver.PhantomJS()
    url = "https://qzone.qq.com/"

    try:
        qq_login.get(url)
        qq_login.maximize_window()
        qq_login.switch_to.frame("login_frame")
        qq_login.find_element_by_id("switcher_plogin").click()
        qq_login.find_element_by_id("u").clear()
        qq_login.find_element_by_id("u").send_keys(user_name)
        qq_login.find_element_by_id("p").clear()
        qq_login.find_element_by_id("p").send_keys(user_password)
        qq_login.find_element_by_id("login_button").click()
    except Exception as msg:
        print("Error: URL open failed")
        print("Exception: %s" % repr(msg))
        qq_login.quit()
        exit(1)
    else:
        print("get URL modules success")

    try:
        wait = WebDriverWait(qq_login, 60)
        wait.until(expected_conditions.visibility_of_element_located((By.ID, "tb_setting_i")))
    except Exception as msg:
        print("Error: timeout, please check password")
        print("Exception: %s" % repr(msg))
        qq_login.quit()
        sys.exit(1)
    else:
        print("log in modules success")

    try:
        gtkurl = get_G_TK(qq_login)
        qq_login.get(gtkurl)
    except Exception as msg:
        print("Error: get gtk failed")
        print("Exception: %s" % repr(msg))
        qq_login.quit()
        sys.exit(1)

    try:
        wait = WebDriverWait(qq_login, 60)
        wait.until_not(expected_conditions.visibility_of_element_located((By.ID, "tb_setting_i")))
    except Exception as msg:
        print("Error: refresh timeout")
        print("Exception: %s" % repr(msg))
        qq_login.quit()
        sys.exit(1)
    else:
        print("refresh success")

    try:
        qq_result = {}
        json = {}
        json_text = qq_login.find_element_by_xpath("/html/body/pre").get_attribute('textContent')
        # 用json对象更方便
        json_text = json_text[json_text.find('[') + 1: json_text.find(']')]
        extract_strs = re.findall(r'{(.*?)}', json_text)
        for i in range(len(extract_strs)):
            temp_result = people()
            temp_str = r"json[i] = {" + extract_strs[i] + "}"
            exec(temp_str)
            temp_result.qq_number = decode(json[i]["fromEncodeUin"].lstrip('*S1*'))
            temp_result.nick_name = json[i]["fromNick"]
            temp_result.topic_name = json[i]["topicName"]
            qq_result[str(i)] = temp_result

        print("----------------------------------result----------------------------------\n")
        for i in range(len(extract_strs)):
            qq_result[str(i)].display()
            # print("------------------------topic_name = %s------------------------" % (qq_result[str(i)].topic_name))
            # print("nick_name = ", qq_result[str(i)].nick_name)
            # print("%-13s%s" % ("qq_number = ", qq_result[str(i)].qq_number[0]))
            # for j in range(len(qq_result[str(i)].qq_number)):
            #     if j == 0:
            #         continue
            #     else:
            #         print("%-13s%s" % ("", qq_result[str(i)].qq_number[j]))
        qq_login.quit()
    except Exception as msg:
        print("Error: resolve failed")
        print("Exception: %s" % repr(msg))
        qq_login.quit()
        sys.exit(1)
