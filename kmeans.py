import os
import sqlite3
from flask import Flask , request , session , g , redirect , url_for , abort , \
     render_template , flash
from flask import send_from_directory
import math
from random import randint

app = Flask(__name__)

@app.route("/")
def show_homepage():
    return render_template("HomePage.html")

@app.route("/input")
def show_form():
    return render_template("index.html")

@app.route("/result",  methods=['POST'])
def show_result():
    result = []
    result = kmeans()
    # pos = request.form['']
    # result.append(pos)
    return render_template("result.html", result = result)



def fillArray(arr):
    for x in range(1,5):
        for y in range (1,9):
            arr.append([x,y])

def evalCluster(x,y,cn,cy):
    c_yes = (50-(math.pow((x-(-1)), 2)+math.pow((y-4.5), 2)))*65/100+(math.pow((x-(cy[0])), 2)+math.pow((y-cy[1]), 2))*13/100
    
    c_no = (50-(math.pow((x-(-1)), 2)+math.pow((y-4.5), 2)))*50/100+(math.pow((x-(cn[0])), 2)+math.pow((y-cn[1]), 2))*35/100
   # print(arr)
    if (c_yes > c_no):
        val = 0
    else:
        val = 1
    return val

def cluster(arr,cn,cy):
    m = []
   
    for i in arr:
        i.append(evalCluster(i[0],i[1],cn,cy))
        m.append(i)
    return m

def setCentroid(arr):
    cn = []
    cy = []
    sumX_y = 0
    sumY_y = 0
    sumX_x = 0
    sumY_x = 0
    ny = 0
    nx = 0
    for i in arr:
        if (i[2] == 1):
            sumX_y += i[0]
            sumY_y += i[1]
            ny += 1
        else:
            sumX_x += i[0]
            sumY_x += i[1]
            nx += 1
    cy = [sumX_y/ny, sumY_y/ny]
    cn = [sumX_x/nx, sumY_x/nx]
    return cn,cy

def kmeans():
    arr = []

    fillArray(arr)
    cn_init = [1,(randint(0,8)%8+1)]
    cy_init = [4,(randint(0,8)%8+1)]
    cn_new = []
    cy_new = []
    x = []

    x = cluster(arr,cn_init,cy_init)
    print(x)
    print(cn_init)
    print(cy_init)

    cn_new, cy_new = setCentroid(arr)
    print()
    print(cn_new)
    print(cy_new)


    while not ((cn_init == cn_new) and (cy_init == cy_new)) :
        print("yes")
        cn_init = cn_new
        cy_init = cy_new
        x = cluster(arr,cn_init,cy_init)
        print(x)
        cn_new, cy_new = setCentroid(arr)
        print(cn_new)
        print(cy_new)

        print()
    print()
    print(x)
    return x