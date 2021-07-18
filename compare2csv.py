import csv
import urllib.request
import io
from post_to_DB import post_to_DB 
def compare2csv(id):

    with open('dict.csv', 'r') as viewer_csv:  
        reader_viewer = viewer_csv.readlines()
        #time of existance of a viewer on the camera
    url = 'https://campaign.utrender.com/'+id+'.csv'
    response = urllib.request.urlopen(url)
    reader_ids = csv.reader(io.TextIOWrapper(response))
    #with open('9.csv', 'r') as ids_csv:  
    #    reader_ids = ids_csv.readlines()
    #the ids of images and time of appearing on screen
    ids=[]
    for row_v in reader_viewer:
        for row_i in reader_ids:
            #print str(row_v.split(",")[1]) +"bader_"+ str(row_v.split(",")[2])+"__"+str(row_i[0])
            if float(row_i[0])/1000 >= float(row_v.split(",")[1]) and float(row_i[0])/1000 <= (float(row_v.split(",")[1]))+10: 
            #time on php is 1000 time bigger then tome on python, so i had scale it down by ten__this if is to see the viewers who didnt last on the camera more then 10 seconds--long sto
             #   print row_i.split(",")[0] + "__a10__" + row_v.split(",")[1]
                ids.append(row_i[2])
                print(row_v)
            elif float(row_i[0])/1000 >= float(row_v.split(",")[1]) and float(row_i[0])/1000<= float(row_v.split(",")[2]):
              #  print str(float(row_i.split(",")[0])/1000) + "__ab__" + row_v.split(",")[1] + " " + row_v.split(",")[2]
                ids.append(row_i[2])
                print(row_v)
            #print float(row_i.split(",")[0])/1000 -float(row_v.split(",")[1])
    print(ids)
    for id in ids:
        post_to_DB(id,1)
    
