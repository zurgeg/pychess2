import json
import os
print("Loading...")
gameid = input("Enter game ID")
print("OK.")
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
