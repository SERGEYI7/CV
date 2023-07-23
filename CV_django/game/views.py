from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.exceptions import bad_request
from django.http import HttpResponseBadRequest
from bs4 import BeautifulSoup as bs
import requests


class Field:
    def __init__(self):
        self.field : dict[dict] = {}
        self.queue = ""

    def make_field(self):
        alphabet = []
        for i in range(ord("A"), ord("Z") + 1):
            alphabet.append(chr(i))
        self.field = {
            "A": {1: None, 2: None, 3: None},
            "B": {1: None, 2: None, 3: None},
            "C": {1: None, 2: None, 3: None},
        }

    def screen_field(self):
        str_field = f"{str():^4}{1:^5} {2:^5} {3:^5}\n"
        for key, row in self.field.items():
            str_field = str_field + f"{key:^3} "
            for key2, column in row.items():
                str_field = str_field + f"{str(column):^5} "
            str_field = str_field + "\n"
        return str_field


fi = Field()

class AppIP(APIView):

    def get(self, request, format=None):
        html = requests.get("https://2ip.ru/").text
        my_ip = bs(html, "html.parser").find("div", class_="ip").text.replace("\n", "")
        return Response(data={"ip": my_ip})


class Game(APIView):

    def post(self, request: Request, format=None):
        if not fi.field:
            fi.make_field()
        data = request.query_params.dict()
        row = data["row"].upper()
        column = int(data["column"])
        player = data["player"].upper()
        if fi.queue == '':
            fi.queue = player
        elif fi.queue != player:
            return Response(data={"message": "Не твоя очередь"})
        try:
            cell = fi.field[row][int(column)]
        except:
            return Response(data={"message": "bad_request"}, status=404)
        if cell:
            return Response(data={"message": "occupied", "field": fi.field})
        move = ''
        if player == 'X':
            move = 'O'
        elif player == 'O':
            move = 'X'

        fi.field[row][int(column)] = player
        fi.queue = move

        column_moves = [[], [], []]
        up_down = []
        down_up = []
        for row_index, row_i in enumerate(fi.field.items()):

            rows = list(row_i[1].values())
            up_down.append(rows[row_index])
            down_up.append(rows[(row_index + 1) * (-1)])
            if set(player) == set(rows):
                return Response(data={"message": f"Player {player} you win"})
            for index, column_i in enumerate(rows):
                column_moves[index].append(column_i)
        if (set(player) == set(up_down)) or (set(player) == set(down_up)):
            return Response(data={"message": f"Player {player} you win"})
        for i in column_moves:
            if set(player) == set(i):
                return Response(data={"message": f"Player {player} you win"})
        print(fi.screen_field())
        return Response(data={"field": fi.field}, content_type="application/json")
