from employee import employee_details

def test_employee_details():
    result = employee_details("Shrilaxmi", "EMP101", "IT", "50000")

    expected = "Name: Shrilaxmi\nEmployee ID: EMP101\nDepartmet: IT\nSalary: 50000"

    assert result ==expected