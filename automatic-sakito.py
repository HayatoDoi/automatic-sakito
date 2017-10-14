import requests
from bs4 import BeautifulSoup 

def main():
  print('Login to SAKITO')
  user = input('User:')
  password = input('Password:')
  print('\n')
  scraping(user,password)

def scraping(user,password):
  session = requests.Session()
  # get authenticity_token
  response = session.get('https://sakito.cirkit.jp/user/sign_in')
  soup = BeautifulSoup(response.text, 'html.parser')
  authenticity_token = soup.body.findAll('form')[0].find(attrs={'name':'authenticity_token'})['value']
  # login
  login_payload = {
    'utf8': '✓',
    'authenticity_token': authenticity_token,
    'user[email]': user,
    'user[password]': password,
    'user[remember_me]': '0',
    'commit': 'ログイン'
  }
  session.post('https://sakito.cirkit.jp/user/sign_in', data=login_payload)

  # がちゃを回す
  gacha_payload = {
    '_method': 'post',
    'authenticity_token': authenticity_token,
  }
  response = session.get('https://sakito.cirkit.jp/user')
  response = session.get('https://sakito.cirkit.jp/user/point/new')
  # response = session.post('https://sakito.cirkit.jp/user/point', data=login_payload)
  print(response.text)

if __name__ == '__main__':
  main()