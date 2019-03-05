import config
import SakitoScrap

def main():
  sakitoScrap = SakitoScrap.SakitoScrap(config.sakito['email'], config.sakito['password'])

  while sakitoScrap.getPoint() > 10:
    sakitoScrap.prizeGacha()

if __name__ == '__main__':
  main()
