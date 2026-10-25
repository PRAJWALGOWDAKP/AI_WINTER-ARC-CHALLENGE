# Job Post Extractor

## 📌 Project Overview

The **Job Post Extractor** is a Python project that extracts structured information from a text file containing multiple job postings. It reads job descriptions from `job.txt`, extracts important details, stores them in Python dataclass objects, and converts the extracted data into formatted JSON.

This project demonstrates file handling, string manipulation, functions, dataclasses, list comprehensions, JSON serialization, and handling missing values in Python.

## 🎯 Objectives

- Read job postings from a text file.
- Extract job titles, company names, experience, locations, required skills, and salaries.
- Store the extracted information using a Python dataclass.
- Convert required skills into a list.
- Handle missing company names and experience values using default values.
- Serialize the job objects into readable JSON format.

## 🛠️ Technologies Used

- **Python 3.10+**
- `pathlib` — File path handling.
- `dataclasses` — Structured storage of job information.
- `typing` — Optional type annotations.
- `json` — JSON serialization and formatting.

All imported modules are part of Python's standard library, so no additional packages are required.

## 📂 Project Structure

```text
job-post-extractor/
│
├── main.py
├── job.txt
└── README.md
```

- `main.py` — Contains the extraction logic and JSON conversion.
- `job.txt` — Contains the input job postings.
- `README.md` — Documents the project.

## 📄 Input Format

Each job posting in `job.txt` should contain fields in a consistent format, with a blank line separating individual postings.

```text
Job_Title: Junior Python Developer
Company: Inspity IT Solutions
Location: Bengaluru, Karnataka, India
Experience: 2+ years
Required_Skills: Python, FastAPI, NumPy, Pandas
Salary: 4-6 LPA

Job_Title: Data Analyst
Company: ABC Technologies
Location: Hyderabad, Telangana, India
Experience: 1-3 years
Required_Skills: Python, SQL, Excel, Power BI
Salary: 5-8 LPA
```

## ⚙️ How It Works

### 1. Define the Job Dataclass

The `Job` dataclass represents a job posting as a structured Python object.

It contains the following attributes:

| Attribute | Data type | Description |
|---|---|---|
| `Job_Title` | `Optional[str]` | Title of the job |
| `Company` | `str` | Company offering the job |
| `Location` | `Optional[str]` | Job location |
| `Experience` | `str` | Required experience |
| `Required_Skills` | `list[str]` | List of required skills |
| `Salary` | `Optional[str]` | Salary information |

The `field(default_factory=list)` declaration creates a separate empty skills list for each `Job` instance when no skills are supplied.

### 2. Read the Input File

The `Path` class locates `job.txt`, and the file is opened with UTF-8 encoding. The `read()` method loads its contents into a string.

### 3. Extract Job Details

The extraction functions search through individual job postings and retrieve the value associated with a specified label.

The program uses `split("\n\n")` to separate job postings and `splitlines()` to examine each line. When a matching label is found, `split(":", 1)` separates the field name from its value.

The extracted values are returned as lists, with one entry for each job posting.

### 4. Process Required Skills

The required skills are initially extracted as a comma-separated string. The program uses a list comprehension and `strip()` to separate the skills and remove unnecessary whitespace.

For example:

```python
"Python, FastAPI, NumPy"
```

becomes:

```python
["Python", "FastAPI", "NumPy"]
```

If no skills are found, an empty list is used.

### 5. Create Job Objects

The `zip()` function combines the extracted lists so that the corresponding details are used to create each `Job` instance.

Missing company names are replaced with `"Unknown"`, while missing experience values are replaced with `"Not specified"`.

Each created object is appended to the `job_objects` list.

### 6. Convert Objects to JSON

The `asdict()` function converts each dataclass instance into a dictionary. A list comprehension applies this conversion to every job object.

The `json.dumps()` function then converts the list of dictionaries into formatted JSON.

- `indent=4` makes the JSON easier to read.
- `ensure_ascii=False` preserves non-ASCII characters.

## ▶️ How to Run

**Step 1:** Ensure Python 3.10 or later is installed.

**Step 2:** Place `main.py` and `job.txt` in the same directory.

**Step 3:** Open a terminal in that directory and execute:

```bash
python main.py
```

The program prints the extracted job details in JSON format.

## 📤 Sample Output

```json
[
    {
        "Company": "Inspity IT Solutions",
        "Experience": "2+ years",
        "Job_Title": "Junior Python Developer",
        "Location": "Bengaluru, Karnataka, India",
        "Required_Skills": [
            "Python",
            "FastAPI",
            "NumPy",
            "Pandas"
        ],
        "Salary": "4-6 LPA"
    }
]
```

The actual output depends on the contents of `job.txt`.

## ⏱️ Time and Space Complexity

Let:

- \(N\) = total number of characters in the input file.
- \(J\) = number of job postings.
- \(F\) = number of fields extracted per job.
- \(S\) = total number of required skills across all postings.

| Operation | Complexity |
|---|---|
| Read the file | \(O(N)\) |
| Extract each field using the current functions | \(O(FN)\) |
| Split required skills | \(O(S)\) |
| Create job objects | \(O(J)\) |
| Convert objects to JSON | \(O(N)\), assuming the serialized output is proportional to the input size |

Since the current implementation uses a separate extraction function for every field, it scans the job-posting content multiple times. If the number of fields is fixed, the overall time complexity is **\(O(N)\)**, although the repeated scans increase the constant factor.

The space complexity is **\(O(N)\)** because the program stores the file contents, extracted lists, job objects, and JSON output in memory.

## 🚀 Future Improvements

- Combine the repeated extraction functions into one reusable function.
- Parse each job posting only once to improve efficiency.
- Add input validation for missing or incorrectly formatted fields.
- Support alternative input formats, such as CSV and JSON.
- Add automated unit tests.
- Integrate an AI model to extract structured information from unstructured job descriptions.

## 📚 Concepts Practiced

- File handling with `pathlib`
- String splitting and parsing
- Functions and reusable logic
- Dataclasses and type annotations
- Lists, `zip()`, and list comprehensions
- Default values and optional fields
- JSON serialization
- Time and space complexity analysis

## 👨‍💻 Conclusion

This project transforms text-based job postings into structured JSON data using Python. It provides a foundation for building more advanced job-processing tools, such as job search platforms, resume-matching systems, and automated job description analyzers.
