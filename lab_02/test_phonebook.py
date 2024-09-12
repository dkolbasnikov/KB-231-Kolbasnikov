import pytest
from phonebook import load_data, save_data

def test_load_data():
    students = load_data('test_input.csv')
    assert len(students) == 2  
    assert students[0]['Name'] == 'Bob'
    assert students[0]['Phone'] == '1112233'
    assert students[1]['Name'] == 'Dilan'
    assert students[1]['Phone'] == '2223344'

def test_save_data():
    students = [{"Name": "Danil", "Phone": "228"}]
    save_data('test_output.csv', students)
    loaded_students = load_data('test_output.csv')
    assert len(loaded_students) == 1
    assert loaded_students[0]['Name'] == 'Danil'
    assert loaded_students[0]['Phone'] == '228'
