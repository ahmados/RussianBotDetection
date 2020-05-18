import urllib3

http = urllib3.PoolManager()
with open('bots.txt', 'r') as content_file:
    content = content_file.read()
bots = content.split('\n')
for bot in bots:
    r = http.request('get', 'https://gosvon.ru/?usr=' + str(bot))
    with open(str(bot) + '.html', 'wb') as fid:
        fid.write(r.data)
