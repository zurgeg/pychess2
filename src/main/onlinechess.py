import os
import json
if mode.upper() == "1 PLAYER":
    gb = os.popen('curl --location --request GET "http://chess-api-chess.herokuapp.com/api/v1/chess/one"')
    #print(gb.read())
    json_string = gb.read().replace("'", "\"")
    gameid = json.loads(json_string)['game_id']
    print(gameid)
    while True:
        cmd = input("You can:\nget moves\nmove\n>")
        brd = os.popen('curl --location --request POST "http://chess-api-chess.herokuapp.com/api/v1/chess/one/fen" \
          --header "Content-Type: application/x-www-form-urlencoded" \
          --data "game_id=' + gameid + '"')
        chck = os.popen('curl --location --request POST "http://chess-api-chess.herokuapp.com/api/v1/chess/one/check" \
          --header "Content-Type: application/x-www-form-urlencoded" \
          --data "game_id=' + gameid + '"')
        json_string = chck.read().replace("'", "\"")
        checker = json.loads(json_string)
        print(brd.read())
        #print(chck.read())
        if checker['status'] == 'game continues':
            pass
        elif checker['status'] == 'checkmate':
            print("Checkmate!!")
            break


        if cmd.lower() == "get moves":
            pos = input("Enter the position of the piece you want to get moves for: ")
            getmoves = os.popen('curl --location --request POST "http://chess-api-chess.herokuapp.com/api/v1/chess/one/moves" \
              --header "Content-Type: application/x-www-form-urlencoded" \
              --data "position=' + pos + '&game_id="' + gameid)
            print(getmoves.read())
        elif cmd.lower() == "move":
            FROM = input("Enter the piece that you want to move: ")
            TO = input("Enter where you want to move it: ")
            MOVE = os.popen('curl --location --request POST "http://chess-api-chess.herokuapp.com/api/v1/chess/one/move/player" \
          --header "Content-Type: application/x-www-form-urlencoded" \
          --data "from=' + FROM + '&to=' + TO + '&game_id=' + gameid + '"')
            #print(MOVE.read())
            json_acceptable_string = MOVE.read().replace("'", "\"")
            MOVEP = json.loads(json_acceptable_string)
            if MOVEP["status"] == "error: invalid move!":
                print("Error: Invalid Move!")
            else:
                ai = os.popen('curl --location --request POST "http://chess-api-chess.herokuapp.com/api/v1/chess/one/move/ai" \
              --header "Content-Type: application/x-www-form-urlencoded" \
              --data "game_id=' + gameid + '"')
elif mode.upper() == "2 PLAYERS":
    print("Initilizing ChessConnect...")
    gid = os.popen('curl --location --request GET "http://chess-api-chess.herokuapp.com/api/v1/chess/two"')
    json_string = gid.read().replace("'", "\"")
    gameid = json.loads(json_string)['game_id']
    print("Use this ID to connect via ChessConnet")
    print("Initilazed.")
    while True:
        cmd = input("You can:\nget moves\nmove\n>")
        brd = os.popen('curl --location --request POST "http://chess-api-chess.herokuapp.com/api/v1/chess/two/fen" \
          --header "Content-Type: application/x-www-form-urlencoded" \
          --data "game_id=' + gameid + '"')
        chck = os.popen('curl --location --request POST "http://chess-api-chess.herokuapp.com/api/v1/chess/two/check" \
          --header "Content-Type: application/x-www-form-urlencoded" \
          --data "game_id=' + gameid + '"')
        json_string = chck.read().replace("'", "\"")
        checker = json.loads(json_string)
        print(brd.read())
        #print(chck.read())
        if checker['status'] == 'game continues':
            pass
        elif checker['status'] == 'checkmate':
            print("Checkmate!!")
            break
            

        if cmd.lower() == "get moves":
            pos = input("Enter the position of the piece you want to get moves for: ")
            getmoves = os.popen('curl --location --request POST "http://chess-api-chess.herokuapp.com/api/v1/chess/two/moves" \
              --header "Content-Type: application/x-www-form-urlencoded" \
              --data "position=' + pos + '&game_id="' + gameid)
            print(getmoves.read())
        elif cmd.lower() == "move":
            FROM = input("Enter the piece that you want to move: ")
            TO = input("Enter where you want to move it: ")
            MOVE = os.popen('curl --location --request POST "http://chess-api-chess.herokuapp.com/api/v1/chess/two/move" \
          --header "Content-Type: application/x-www-form-urlencoded" \
          --data "from=' + FROM + '&to=' + TO + '&game_id=' + gameid + '"')
            print(MOVE.read())
            json_acceptable_string = MOVE.read().replace("'", "\"")
            MOVEP = json.loads(json_acceptable_string)
            if MOVEP["status"] == "error: invalid move!":
                print("Error: Invalid Move!")
            

        
