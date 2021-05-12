from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser
import time

#options = Options()
#options.add_argument('--headless')

#マイページクリック
def mypageclick():
    login_mypage = driver.find_element_by_css_selector(".btn-primary")
    login_mypage.click()
    time.sleep(1)
    return

#ポイントガチャへ移動
def pointgatya():
    pointg = driver.find_element_by_css_selector(".list-group-item")
    if "ポイントガチャを回す" == str(pointg.text):
        pointg.click()
        #time.(1)
        #ポイントガチャを回す
        try:
            roles = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.btn-success')))
            #roles = driver.find_element_by_css_selector("body > div > div > div > div > a")
            roles.click()
            #getp_path = "#result > div > div > div > h3:nth-child(1)"
            #getpoint = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, getp_path)))
            #getpoint = driver.find_element_by_css_selector("#result > div > div > div > h3:nth-child(1)")
            mypageclick()
            return

        except TimeoutException:
            mypageclick()
            return "本日はこれ以上回せません"
            
    else:
        return "sakito逝っちゃってるぅ↑"

#now points
def my_points(point):
    #所持ポイント
    if point == 1:
        points = driver.find_element_by_css_selector("body > div > div:nth-child(1) > div:nth-child(1) > div > div > div > div.col-xs-9.text-right > h1")
        return points.text
    #ボーナス券
    elif point == 2:
        bpoint_ticket = driver.find_element_by_css_selector("body > div > div:nth-child(1) > div:nth-child(2) > div > div > div > div.col-xs-9.text-right > h1")
        return bpoint_ticket.text
    #ボーナス券までの日付
    elif point == 3:
        bpoint_day = driver.find_element_by_css_selector("body > div > div:nth-child(1) > div:nth-child(3) > div > div > div > div:nth-child(3) > h1")
        return bpoint_day.text

#ticketgatya
def ticket_gatya():
    goticket = driver.find_element_by_css_selector("body > div > div:nth-child(2) > div:nth-child(1) > div > div.panel-body > div > a:nth-child(3)")
    goticket.click()
    try:
        roles = driver.find_element_by_css_selector("body > div > div > div > div > a")
        roles.click()
        time.sleep(5)
        getpoint = driver.find_element_by_css_selector("#result > div > div > div > h3:nth-child(1)")
        mypageclick()
        return str(getpoint.text)

    except NoSuchElementException:
        mypageclick()
        return "できません"


#configparserの宣言とiniファイルの読み込み
config = configparser.ConfigParser()
config.read('C://Users//*********//config.conf', encoding='utf-8')
#config.iniから情報を読み出し
read_email = config['DEFAULT']
email = read_email.get('email')
read_password = config['DEFAULT']
password = read_password.get('password')

#chromedriverの場所を指定
driver = webdriver.Chrome("C://chromedriver//chromedriver.exe")

driver.implicitly_wait(10)
wait = WebDriverWait(driver, 4)
#sakitoにアクセス・ユーザー名・パスワード入力
driver.get("https://sakito.cirkit.jp/user/sign_in")
login_email = driver.find_element_by_css_selector("#user_email")
login_email.send_keys(email)
login_pass = driver.find_element_by_css_selector("#user_password")
login_pass.send_keys(password)

#ログインクリック
login = driver.find_element_by_css_selector("#new_user > input.btn.btn-info.btn-block")
login.click()
print('logined sakito')
mypageclick()
