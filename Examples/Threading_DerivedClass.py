# Thread Derived Class
import threading, requests, time

# Example A
def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    print(url, len(resp.text), ' chars')

t1 = threading.Thread(target=getHtml, args=('https://google.com',))
t1.start()

print('## End ##')


# Example B
class HtmlGetter(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        resp = requests.get(self.url)
        time.sleep(1)
        print(self.url, len(resp.text), ' chars')

t = HtmlGetter('http://google.com')
t.start()

# demon example
def getHtml2(url):
    resp = requests.get(url)
    time.sleep(1)
    print(url, len(resp.text), ' chars')

# demon
t1 = threading.Thread(target=getHtml2, args=('http://google.com',))
t1.daemon = True
t1.start()

print('## Daemon End ##')

