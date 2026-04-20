"""
Skill normalizer - converts skill variations to standard names.
"""

import re
from typing import List


class SkillNormalizer:
    """
    Normalizes skill names to standard format.
    
    Examples:
        "sql" -> "SQL"
        "aws" -> "AWS"
        "js" -> "JavaScript"
        "python3" -> "Python"
    """
    
    # Mapping of variations to standard names
    SKILL_MAPPING = {
        # Languages
        "python3": "Python",
        "py": "Python",
        "javascript": "JavaScript",
        "js": "JavaScript",
        "typescript": "TypeScript",
        "ts": "TypeScript",
        "java": "Java",
        "c++": "C++",
        "cpp": "C++",
        "c#": "C#",
        "csharp": "C#",
        "ruby": "Ruby",
        "go": "Go",
        "golang": "Go",
        "rust": "Rust",
        "swift": "Swift",
        "kotlin": "Kotlin",
        
        # Databases
        "sql": "SQL",
        "mysql": "MySQL",
        "postgresql": "PostgreSQL",
        "postgres": "PostgreSQL",
        "mongodb": "MongoDB",
        "mongo": "MongoDB",
        "redis": "Redis",
        "elasticsearch": "Elasticsearch",
        "elastic": "Elasticsearch",
        
        # Cloud
        "aws": "AWS",
        "amazon web services": "AWS",
        "azure": "Azure",
        "gcp": "GCP",
        "google cloud": "GCP",
        
        # DevOps
        "docker": "Docker",
        "kubernetes": "Kubernetes",
        "k8s": "Kubernetes",
        "jenkins": "Jenkins",
        "github actions": "GitHub Actions",
        "gitlab ci": "GitLab CI",
        "terraform": "Terraform",
        
        # Data Science
        "tensorflow": "TensorFlow",
        "tf": "TensorFlow",
        "pytorch": "PyTorch",
        "sklearn": "scikit-learn",
        "scikit-learn": "scikit-learn",
        "pandas": "Pandas",
        "numpy": "NumPy",
        "matplotlib": "Matplotlib",
        "seaborn": "Seaborn",
        
        # Web
        "react": "React",
        "reactjs": "React",
        "angular": "Angular",
        "vue": "Vue.js",
        "vuejs": "Vue.js",
        "node": "Node.js",
        "nodejs": "Node.js",
        "express": "Express.js",
        "django": "Django",
        "flask": "Flask",
        "spring": "Spring",
        "springboot": "Spring Boot",
        
        # AI/ML
        "machine learning": "Machine Learning",
        "ml": "Machine Learning",
        "deep learning": "Deep Learning",
        "dl": "Deep Learning",
        "nlp": "NLP",
        "natural language processing": "NLP",
        "computer vision": "Computer Vision",
        "cv": "Computer Vision",
        
        # Data
        "data science": "Data Science",
        "data engineering": "Data Engineering",
        "data analysis": "Data Analysis",
        "data visualization": "Data Visualization",
        "tableau": "Tableau",
        "power bi": "Power BI",
        "powerbi": "Power BI",
        "excel": "Excel",
    }
    
    def normalize(self, skill: str) -> str:
        """
        Normalize a single skill name.
        
        Args:
            skill: Raw skill string
            
        Returns:
            Normalized skill name
        """
        if not skill:
            return skill
        
        skill_lower = skill.lower().strip()
        
        # Check mapping
        if skill_lower in self.SKILL_MAPPING:
            return self.SKILL_MAPPING[skill_lower]
        
        # Capitalize properly (e.g., "docker" -> "Docker")
        return skill.capitalize()
    
    def normalize_list(self, skills: List[str]) -> List[str]:
        """
        Normalize a list of skills.
        
        Args:
            skills: List of raw skill strings
            
        Returns:
            List of normalized skill names (unique, sorted)
        """
        if not skills:
            return []
        
        normalized = [self.normalize(s) for s in skills if s]
        # Remove duplicates while preserving order
        seen = set()
        unique = []
        for skill in normalized:
            if skill not in seen:
                seen.add(skill)
                unique.append(skill)
        
        return sorted(unique)