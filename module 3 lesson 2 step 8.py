# ваша реализация, напишите assert и сообщение об ошибке
def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, "Несовпадение введенных чисел!"
    return f"Ожидалось {expected_result}, Получено {actual_result}"