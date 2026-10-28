from lab_pgm6 import employee_details

def test_employee_details():
    result = employee_details("Shrilaxmi", "101", "IT", 50000.00)
    expected = "Name: shrilaxmi\nEmployee ID: 101\nDepartment: IT\nSalary: $50000.00"
    assert result == expected