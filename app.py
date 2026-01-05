from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Store expenses in a list of dictionaries
expenses = []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        date = request.form["date"]
        category = request.form["category"]
        amount = float(request.form["amount"])

        expense = {
            "date": date,
            "category": category,
            "amount": amount
        }

        expenses.append(expense)
        return redirect("/")

    total = sum(e["amount"] for e in expenses)
    highest = max(expenses, key=lambda x: x["amount"], default=None)

    return render_template(
        "index.html",
        expenses=expenses,
        total=total,
        highest=highest
    )


if __name__ == "__main__":
    app.run(debug=True)
