"""
Constants used across the resume parser.
"""

# Common technical skills (expand as needed)
COMMON_SKILLS = [
    "python", "java", "javascript", "typescript", "sql", "nosql",
    "aws", "azure", "gcp", "docker", "kubernetes", "terraform",
    "tensorflow", "pytorch", "keras", "scikit-learn", "pandas", "numpy",
    "react", "angular", "vue", "node.js", "express", "django", "flask",
    "spring", "springboot", "c++", "c#", "ruby", "go", "rust",
    "html", "css", "sass", "tailwind", "bootstrap",
    "mongodb", "postgresql", "mysql", "redis", "elasticsearch",
    "git", "github", "gitlab", "bitbucket", "jenkins", "github actions",
    "tableau", "power bi", "excel", "spss", "sas", "looker",
    "machine learning", "deep learning", "nlp", "computer vision",
    "data science", "data engineering", "data analysis", "data visualization"
]

# Section headers mapping (variations)
SECTION_MAPPING = {
    "experience": ["experience", "work experience", "employment", "work history", "professional experience"],
    "education": ["education", "academic background", "qualifications", "degrees"],
    "skills": ["skills", "technical skills", "core competencies", "technologies"],
    "projects": ["projects", "personal projects", "side projects"],
    "certifications": ["certifications", "certificates", "licenses"]
}