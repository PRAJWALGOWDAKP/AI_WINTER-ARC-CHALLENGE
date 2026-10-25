from pathlib import Path
from dataclasses import dataclass,field,asdict
from typing import Optional
import json

@dataclass
class Job:
    Company: str  
    Experience: str
    Job_Title: Optional[str]=None
    Location: Optional[str] = None
    Required_Skills: list[str] = field(default_factory=list)
    Salary: Optional[str] =None

file_path = Path("job.txt")

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()


def extract_jobs(content, label):
    results = []

    for job in content.split("\n\n"):
        value = None

        for line in job.splitlines():
            if line.startswith(label):
                value = line.split(":", 1)[1].strip()
                break

        results.append(value)

    return results

def extract_company(content, label):
    results = []

    for job in content.split("\n\n"):
        value = None

        for line in job.splitlines():
            if line.startswith(label):
                value = line.split(":", 1)[1].strip()
                break

        results.append(value)

    return results

def extract_exp(content, label):
    results = []

    for job in content.split("\n\n"):
        value = None

        for line in job.splitlines():
            if line.startswith(label):
                value = line.split(":", 1)[1].strip()
                break

        results.append(value)

    return results

def extract_loc(content, label):
    results = []

    for job in content.split("\n\n"):
        value = None

        for line in job.splitlines():
            if line.startswith(label):
                value = line.split(":", 1)[1].strip()
                break

        results.append(value)

    return results

def extract_skills(content, label):
    results = []

    for job in content.split("\n\n"):
        value = None

        for line in job.splitlines():
            if line.startswith(label):
                value = line.split(":", 1)[1].strip()
                break

        results.append(value)

    return results

def extract_salary(content, label):
    results = []

    for job in content.split("\n\n"):
        value = None

        for line in job.splitlines():
            if line.startswith(label):
                value = line.split(":", 1)[1].strip()
                break

        results.append(value)

    return results

titles = extract_jobs(content, "Job_Title")
companies = extract_company(content, "Company")
experiences = extract_exp(content, "Experience")
locations = extract_loc(content, "Location")
skills_raw = extract_skills(content, "Required_Skills")
salaries = extract_salary(content, "Salary")

job_objects=[]

for title, company, exp, loc, skills, salary in zip(titles, companies, experiences, locations, skills_raw, salaries):
    skill_list=[s.strip() for s in skills.split(",")] if skills else []

    job_instance=Job(
        Job_Title=title,
        Company=company if company else "Unknown",
        Experience=exp if exp else "Not specified",
        Location=loc,
        Required_Skills=skill_list,
        Salary=salary
    )
    job_objects.append(job_instance)

pretty_json=json.dumps([asdict(j) for j in job_objects],indent=4,ensure_ascii=False)
print(pretty_json)












