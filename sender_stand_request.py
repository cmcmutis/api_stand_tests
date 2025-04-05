import configuration
import requests
import data

def get_docs():
    return requests.get(configuration.url_service + configuration.doc_path)

response = get_docs()
print(response.status_code)

def get_logs():
    return requests.get(configuration.url_service + configuration.log_main_path, params={"count":20})

response = get_logs()
print(response.status_code)
print(response.headers)

def get_users_table():
    return requests.get(configuration.url_service + configuration.users_table_path)

response = get_users_table()
print(response.status_code)

def post_products_kits(products_ids):
    return requests.post(configuration.url_service + configuration.products_kits_path,
    json=products_ids,
     headers=data.headers)

response = post_products_kits(data.product_ids);
print(response.status_code)
print(response.json())

def post_new_user(body):
    return requests.post(configuration.url_service + configuration.create_user_path,
    json=body,
    headers=data.headers)

response = post_new_user(data.user_body)
print(response.status_code)

def post_new_user(body):
    return requests.post(configuration.url_service + configuration.create_user_path,
    json=body,
    headers=data.headers)

response = post_new_user(data.user_body);
print(response.status_code)
print(response.json())

def test_create_user_15_letter_in_first_name_get_success_response():
    positive_assert("Aaaaaaaaaaaaaaa")

def negative_assert_symbol(first_name):
    user_body = get_user_body(first_name)
    response = sender_stand_request.post_new_user(user_body)

    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "Has introducido un nombre de usuario no válido. " \
                                         "El nombre solo puede contener letras del alfabeto latino,  " \
                                         "la longitud debe ser de 2 a 15 caracteres"

def test_create_user_1_letter_in_first_name_get_error_response():
    negative_assert_symbol("A")

def test_create_user_16_letter_in_first_name_get_error_response():
    negative_assert_symbol("Aaaaaaaaaaaaaaaa")

def test_create_user_has_space_in_first_name_get_error_response():
    negative_assert_symbol("A Aaa")

def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("\"№%@\",")

def test_create_user_has_number_in_first_name_get_error_response():
    negative_assert_symbol("123")


def negative_assert_no_firstname(user_body):
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400

    assert response.json()["message"] == "No se enviaron todos los parámetros requeridos"

def test_create_user_no_first_name_get_error_response():
    user_body = data.user_body.copy()
    user_body.pop("firstName")
    negative_assert_no_firstname(user_body)

    def test_create_user_empty_first_name_get_error_response():
      user_body = get_user_body("")
     negative_assert_no_firstname(user_body)

def test_create_user_number_type_first_name_get_error_response():
    user_body = get_user_body(12)
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400