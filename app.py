from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def index():

    # Load current count
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()

    # Increment the count
    count += 1

    # Overwrite the count
    f = open("count.txt", "w")
    f.write(str(count))
    f.close()

    numb = random.randint(1,15)
    win = """Congratulations, you've won the prize of a free trip to Los Santos all expenses paid"""
    lose = """You didn't win any prize"""
    sent = ""
    webcount = ""

    if count == 1:
        webcount == """1st"""
    elif count == 2:
        webcount == "2nd"
    elif count == 3:
        webcount == "3rd"
    elif count == 4:
        webcount == "4th"
    elif count == 5:
        webcount == "5th"
    elif count == 6:
        webcount == "6th"
    elif count == 7:
        webcount == "7th"
    elif count == 8:
        webcount == "8th"
    elif count == 9:
        webcount == "9th"
    elif count == 10:
        webcount == "10th"
    elif count == 11:
        webcount == "11th"
    elif count == 12:
        webcount == "12th"
    elif count == 13:
        webcount == "13th"
    elif count == 14:
        webcount == "14th"
    else:
        webcount == "15th"



    if count == numb:
        sent = win
    else:
        sent = lose    

    

    # Render HTML with count variable
    return render_template("index.html", webcount=webcount, sent=sent)

if __name__ == "__main__":
    app.run()
