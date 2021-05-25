import webbrowser as wb
def webbrowser():
    chrome_path="C:\Program Files\Google\Chrome\Application\chrome.exe %s"
    URLS=(
          "web.whatsapp.com",
          "github.com/Shuvo31",
    )
    for url in URLS:
        print('Opening :'+url)
        wb.get(chrome_path).open(url)
webbrowser()