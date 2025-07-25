# app/modules/query_parser.py
import re

def parse_query(query: str) -> dict:
    query = query.strip()

    # Age: Look for formats like "46M" or "46-M" or "46 M"
    age_match = re.search(r"(\d+)[\s-]*[MmFf]", query)
    age = int(age_match.group(1)) if age_match else None

    # Gender: 'M' or 'F'
    gender_match = re.search(r"\d+[\s-]*([MmFf])", query)
    gender = "male" if gender_match and gender_match.group(1).lower() == "m" else "female"

    # Procedure: knee/hip/eye/heart surgery
    surgery_match = re.search(r"(knee|heart|eye|hip)\s+surgery", query.lower())
    procedure = surgery_match.group(0) if surgery_match else "unknown"

    # Location: Look for “in <city>”
    location_match = re.search(r"in\s+([A-Za-z]+)", query)
    location = location_match.group(1) if location_match else "unknown"

    # Policy age: “3-month-old” or “3 month old”
    policy_match = re.search(r"(\d+)[\s-]*month", query.lower())
    policy_duration = f"{policy_match.group(1)} months" if policy_match else "unknown"

    return {
        "age": age,
        "gender": gender,
        "procedure": procedure,
        "location": location,
        "policy_duration": policy_duration
    }
