import time


def get_G_TK(qq_login):
    flag = 0
    cookies = qq_login.get_cookies()
    for cookie in cookies:
        for cookie_key in cookie.keys():
            try:
                if (cookie[cookie_key].find(u"skey") != -1 and cookie[cookie_key].find(u"p_skey") == -1):
                    skey_text = cookie[u"value"]
                    flag += 1
                    break
            except AttributeError:
                continue
        if(flag == 1):
            break
    if (flag == 0):
        print("Error: get skey failed")
        qq_login.quit()
        exit(1)
    strs = "https://ti.qq.com/cgi-node/honest-say/receive/mine?_client_version=0.0.7&_t=" + str(time.time()) + "&token="
    hash = 5381
    for i in range(len(skey_text)):
        hash += (hash << 5) + ord(skey_text[i])
    return strs + str(hash & 2147483647)
