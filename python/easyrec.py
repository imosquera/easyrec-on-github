import urllib
import simplejson
import csv

def shorten(url):
    try:
        cleaned_url = url.replace("&", "%26")

        bitly_url = "http://api.bit.ly/shorten?version=2.0.1&longUrl=" + cleaned_url + "&login=getsocialize&apiKey"
        
        f = urllib.urlopen(bitly_url)
        json = f.read()
        f.close()
        data = simplejson.loads(json)

        print data

        result = data["results"][url]["shortUrl"]

        print result

        return result

    except Exception, ex:
        print ex
        return url


def read_data(csv_file):

    ifile  = open(csv_file, "rb")
    reader = csv.reader(ifile)

    rownum = 0
    for row in reader:
        # Save header row.
        if rownum == 0:
            header = row
        else:
            colnum = 0
            for col in row:
                print '%-8s: %s' % (header[colnum], col)
                colnum += 1
                
        rownum += 1

    ifile.close()

read_data('/Users/jasonpolites/projects/socialize/test.csv')