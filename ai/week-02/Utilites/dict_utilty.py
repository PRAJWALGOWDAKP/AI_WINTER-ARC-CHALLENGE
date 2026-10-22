marks={
  "Arun":89,
  "Bharath":50,
  "Suresh":20,
  "Avinash":25,
  "Ravi":56
      }

passed={
  name:score
  for name,score in marks.items()
  if score>40
}

status={
  name: "Pass" if score>40
  else "Fail"
  for name ,score in marks.items()
}

print(f"Total Students: {marks}")
print(f"Passed: {passed}")
print(f"Status of the student: {status}")
