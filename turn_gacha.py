import requests
import config
from bs4 import BeautifulSoup 

def main():
  scraping(config.sakito['email'], config.sakito['password'])

def scraping(email,password):
  session = requests.Session()
  # get authenticity_token
  response = session.get('https://sakito.cirkit.jp/user/sign_in')
  soup = BeautifulSoup(response.text, 'html.parser')
  authenticity_token = soup.body.findAll('form')[0].find(attrs={'name':'authenticity_token'})['value']
  # login
  login_payload = {
    'utf8': '✓',
    'authenticity_token': authenticity_token,
    'user[email]': email,
    'user[password]': password,
    'user[remember_me]': '0',
    'commit': 'ログイン'
  }
  session.post('https://sakito.cirkit.jp/user/sign_in', data=login_payload)

  # がちゃを回す
  response = session.get('https://sakito.cirkit.jp/user/point/new')
  soup = BeautifulSoup(response.text, 'html.parser')
  authenticity_token = soup.head.find(attrs={'name':'csrf-token'})['content']
  gacha_payload = {
    '_method': 'post',
    'authenticity_token': authenticity_token,
  }
  response = session.post('https://sakito.cirkit.jp/user/point', data=gacha_payload)

  print(gacha_payload)

if __name__ == '__main__':
  main()