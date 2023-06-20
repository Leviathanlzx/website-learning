from flask import Flask,render_template

app=Flask(__name__)

jobs=[
    {
        "id":1,
        "title":"刚刚吃了川菜你们呢",
        "time":"2023",
        "member":"米诺"
    },
    {
        "id": 2,
        "title": "刚刚没吃饭",
        "time": "2023",
        "member": "米诺"
    }
]
@app.route("/")
def hello_world():
    return render_template("csshome.html",info=jobs)

if __name__=="__main__":
    app.run(host="localhost",debug=True)