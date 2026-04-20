import sys
from pathlib import Path

# Add project root to Python path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from backend.resume_parser.models.education import Education
from backend.resume_parser.models.experience import Experience
from backend.resume_parser.models.resume import Resume
from backend.resume_parser.models.parsing_result import ParsingResult

# Create education
edu = Education(degree="BSc Computer Science", institution="MIT", year="2020")

# Create experience
exp = Experience(role="Data Scientist", company="Google", years=3)

# Create resume
resume = Resume(
    candidate_id="R_001",
    name="John Doe",
    email="john@example.com",
    skills=["Python", "SQL", "AWS"],
    education=[edu],
    experience=[exp],
    total_experience_years=3
)

# Create parsing result
result = ParsingResult(resume=resume, confidence=0.85)

# Test output
print(result.to_json())