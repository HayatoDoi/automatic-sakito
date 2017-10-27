import requests
from bs4 import BeautifulSoup

class SakitoScrap:
  def __init__(self, email:str, password:str):
    self.email = email
    self.password = password
    self.__session = self.__login()

  def __login(self):
    s = requests.Session()
    # get authenticity_token
    response = s.get('https://sakito.cirkit.jp/user/sign_in')
    soup = BeautifulSoup(response.text, 'html.parser')
    authenticity_token = soup.body.findAll('form')[0].find(attrs={'name':'authenticity_token'})['value']
    # login
    login_payload = {
      'utf8': '✓',
      'authenticity_token': authenticity_token,
      'user[email]': self.email,
      'user[password]': self.password,
      'user[remember_me]': '0',
      'commit': 'ログイン'
    }
    s.post('https://sakito.cirkit.jp/user/sign_in', data=login_payload)

    return s

  def getPoint(self):
    s = self.__session
    response = s.get('https://sakito.cirkit.jp/user')
    soup = BeautifulSoup(response.text, 'html.parser')
    return int(soup.body.findAll('h1')[0].string)

  def checkNewQusation(self):
    s = self.__session
    response = s.get('https://sakito.cirkit.jp/surveys')
    soup = BeautifulSoup(response.text, 'html.parser')

    newQuestionList = []
    for row in soup.body.findAll(attrs={'class':'panel-success'}):
      if( row.find(attrs={'class':'panel-footer'}).text == '回答する' ):
        newQuestionList.append( row.find(attrs={'class':'panel-heading'}).text )
    return newQuestionList

  def gacha(self):
    s = self.__session
    response = s.get('https://sakito.cirkit.jp/user/point/new')
    soup = BeautifulSoup(response.text, 'html.parser')
    authenticity_token = soup.head.find(attrs={'name':'csrf-token'})['content']
    gacha_payload = {
      '_method': 'post',
      'authenticity_token': authenticity_token,
    }
    response = s.post('https://sakito.cirkit.jp/user/point', data=gacha_payload)
