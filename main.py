import requests


def bypass(url):
  payload = {
    "url": url,
  }

  r = requests.post("https://api.bypass.vip/", data=payload)
  return r.json()


def destination(info):
  x = str(info).split()
  output = x[7] 
  return output.replace("'", "").replace(",", "").replace(" ", "")


def main():
    file = open("links.txt", "r")
    output = open("output.txt", "a")
    i = 1
    for line in file:
      link = line.replace("\r\n", "") #change that !!!!

      print(str(i) + "\t" +link)

      result = bypass(link)
      success = str(result).find("false")
      
      if success == -1:
        output.write(destination(result) + "\n")
      else:
        output.write("failed: " + link  + "\n")

      i += 1
    output.close()
    file.close()


if __name__ == '__main__':
  main()
