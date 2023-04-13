from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {"max_salary": 100, "min_salary": 2, "date_posted": "2022-01-01"},
        {"max_salary": 300, "min_salary": 1, "date_posted": "2021-01-01"},
        {"max_salary": 200, "min_salary": 0, "date_posted": "2023-01-01"},
    ]

    sorted_by_max = [
        {"max_salary": 300, "min_salary": 1, "date_posted": "2021-01-01"},
        {"max_salary": 200, "min_salary": 0, "date_posted": "2023-01-01"},
        {"max_salary": 100, "min_salary": 2, "date_posted": "2022-01-01"},
    ]

    sorted_by_min = [
        {"max_salary": 200, "min_salary": 0, "date_posted": "2023-01-01"},
        {"max_salary": 300, "min_salary": 1, "date_posted": "2021-01-01"},
        {"max_salary": 100, "min_salary": 2, "date_posted": "2022-01-01"},
    ]

    sorted_by_date = [
        {"max_salary": 200, "min_salary": 0, "date_posted": "2023-01-01"},
        {"max_salary": 100, "min_salary": 2, "date_posted": "2022-01-01"},
        {"max_salary": 300, "min_salary": 1, "date_posted": "2021-01-01"},
    ]

    sort_by(jobs, "max_salary")
    assert jobs == sorted_by_max

    sort_by(jobs, "min_salary")
    assert jobs == sorted_by_min

    sort_by(jobs, "date_posted")
    assert jobs == sorted_by_date
