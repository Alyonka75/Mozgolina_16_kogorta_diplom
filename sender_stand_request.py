# Mozgolina Alyona, 16-я когорта — Финальный проект. Инженер по тестированию плюс

import requests

import configuration
import data

def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_body)

def create_order_and_return_track():
    response = post_new_order(data.order_body)
    return response.json()['track']

def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH + str(track))
