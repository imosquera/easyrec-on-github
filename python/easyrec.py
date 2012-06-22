import urllib
import simplejson
import csv
import os
import time

API_BASE_URL = "http://localhost:8080/easyrec-web/api/1.0"
API_KEY = "71c9d399bf7482eaefb7224851e24f63"
TENANTID = "SOCIALIZE"

def register_event(api_type, item_id, item_description, item_url, user_id, ratingvalue=None):
    session_id = "%sU%s" % (int(time.time()), user_id)
    base_url = "%s/%s?apikey=%s&tenantid=%s&sessionid=%s" % (API_BASE_URL, api_type, API_KEY, TENANTID, session_id)
    url = "%s&itemid=%s&itemdescription=%s&itemurl=%s&user_id=%s" % (base_url, item_id, item_description, item_url, user_id)
    call_api(url)
    
def call_api(url):
    try:
        print "calling", url
        f = urllib.urlopen(url)
        data = f.read()
        f.close()
        print data
    except Exception, ex:
        print ex


def push_data(item_type):
    filepath = os.path.dirname(os.path.realpath(__file__))
    csv_file = "%s/data/socialize_%s_view.csv" % (filepath, item_type)
    
    print "reading...", csv_file
    
    ifile  = open(csv_file, "rb")
    reader = csv.reader(ifile)

    rownum = 0
    query_string = ""
    item_id = ""
    item_description = "some data"
    item_url = "/fakeurl"
    user_id = ""
    for row in reader:
        # Save header row.
        if rownum == 0:
            header = row
        else:
            colnum = 0
            for col in row:
                #print '%-8s: %s' % (header[colnum], col)
                if item_type == "entity":
                    if header[colnum] == "id":
                        item_id = col
                else: #user data
                    if header[colnum] == "user_id":
                        user_id = col
                    if header[colnum] == "entity_id":
                        item_id = col

                colnum += 1
            print query_string
            
            register_event("buy", item_id, item_description, item_url, user_id)
            
            query_string = ""
            break                
        rownum += 1

    ifile.close()







push_data("like")


