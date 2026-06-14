from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "dev-secret-key"

@app.route("/")
def index():
    if "board" not in session:
        session["board"] = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]
    if "turn" not in session:
        session["turn"] = "○"

    if "winner" not in session:
        session["winner"] = ""

    return render_template(
        "index.html",
        board=session["board"],
        turn=session["turn"],
        winner=session["winner"]
    )

@app.route("/move", methods=["POST"])
def move():
    #Handle a move made by a player.
    if session.get("winner", "") != "":
        return redirect(url_for("index"))
    
    row = int(request.form["row"])
    col = int(request.form["col"])

    board = session["board"]
    turn = session.get("turn", "○")

    if board[row][col] == "":
        board[row][col] = turn
        session["turn"] = "×" if turn == "○" else "○"

    session["board"] = board
    winner = check_winner(board)
    session["winner"] = winner

    return redirect(url_for("index"))

@app.route("/reset", methods=["POST"])
def reset():
    session.pop("board", None)
    session.pop("turn", None)
    session.pop("winner", None)
    return redirect(url_for("index"))

def check_winner(board):
    board = sum(board, [])
    win_index_pattern_array = [
                        [0,1,2],
                        [3,4,5],
                        [6,7,8],
                        [0,3,6],
                        [1,4,7],
                        [2,5,8],
                        [0,4,8],
                        [6,4,2],
                    ]
    for win_index_pattern in win_index_pattern_array:
        # print(f"Checking pattern: {win_index_pattern}")
        figure = ""
        for index in win_index_pattern:
            # print(f"Checking index {index}: {board[index]}, figure: {figure}")
            if figure == "":
                figure = board[index]
            elif figure != board[index]:
                break
        else:
            if figure != "":
                return figure
    return ""

if __name__ == "__main__":
    app.run(debug=True)
