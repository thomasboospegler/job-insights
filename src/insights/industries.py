from typing import List, Dict
import csv


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    with open(path, encoding="utf-8") as file:
        jobs_list = csv.DictReader(file, delimiter=",", quotechar='"')
        industries_list = []
        for job in jobs_list:
            if job["industry"] not in industries_list and (
                job["industry"] != ""
            ):
                industries_list.append(job["industry"])
        return industries_list


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
