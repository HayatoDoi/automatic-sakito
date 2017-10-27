import config
import SakitoScrap

def main():
  sakitoScrap = SakitoScrap.SakitoScrap(config.sakito['email'], config.sakito['password'])

  beforePoint = sakitoScrap.getPoint()
  sakitoScrap.gacha()
  afterPoint = sakitoScrap.getPoint()

  print(afterPoint - beforePoint)

if __name__ == '__main__':
  main()
