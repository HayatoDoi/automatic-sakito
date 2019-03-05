import config
import SakitoScrap

def main():
  sakitoScrap = SakitoScrap.SakitoScrap(config.sakito['email'], config.sakito['password'])
  
  while sakitoScrap.getExchangePoint() > 4:
    sakitoScrap. prizeExchange()

if __name__ == '__main__':
  main()
