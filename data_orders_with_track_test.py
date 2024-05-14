# Mozgolina Alyona, 16-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request

def test_get_order_by_track():
    track = sender_stand_request.create_order_and_return_track()
    order_response = sender_stand_request.get_order_by_track(track)

    assert order_response.status_code == 200
