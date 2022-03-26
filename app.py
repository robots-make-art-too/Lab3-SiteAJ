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
    if count == numb:
        sent = win
    else:
        sent = lose    

    

    # Render HTML with count variable
    return render_template("index.html", count=count, sent=sent)

if __name__ == "__main__":
    app.run()
