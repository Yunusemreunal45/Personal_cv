import streamlit as st

st.set_page_config(
    page_title="Yunus Emre Ünal | Computer Engineer",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===================== PERSONAL INFO =====================
personal_info = {
    "name": "Yunus Emre Ünal",
    "title": "Computer Engineer | Full-Stack Developer | AI & Data Science Enthusiast",
    "location": "Konya, Turkey",
    "phone": "(+90) 553 798 8488",
    "email": "yunusemreu623@gmail.com",
    "linkedin": "https://www.linkedin.com/in/yunus-emre-ünal-aab175263/",
    "github": "https://github.com/Yunusemreunal45",
    "website": "https://cerulean-travesseiro-a187f3.netlify.app",
    "cv_url": "https://customer-assets.emergentagent.com/job_6cd547df-b864-4d07-b910-1fd41bea082b/artifacts/fqt0nfav_Yunus_Emre_%C3%9Cnal_cv.pdf"
}

# ===================== ABOUT =====================
about = """
Computer Engineering graduate from Manisa Celal Bayar University with hands-on experience in software development,
data science, and artificial intelligence gained through internships, technical projects, and competitions.
Actively participated in TEKNOFEST, worked in the University IT Department, and contributed to student clubs.

Completed internships at Terzion DX, TürkŞeker, and DGA Yazılım, gaining experience in full-stack development,
process automation, data analysis, and system integration.

Successfully completed the Mastering Applied Data Science Bootcamp (January 2026) and a U.S.-based Artificial
Intelligence Camp, with a strong focus on applied machine learning, data analysis, and intelligent systems.
"""

# ===================== STATS =====================
stats = [
    {"label": "Years Experience", "value": "3+"},
    {"label": "Completed Projects", "value": "20+"},
    {"label": "Technologies Used", "value": "25+"}
]

# ===================== EXPERIENCE =====================
experience = [
    {
        "role": "Software Developer",
        "company": "DGA Yazılım",
        "period": "Nov 2024 – Jun 2025",
        "location": "Manisa, Turkey",
        "description": (
            "Developed full-stack educational platforms and desktop RPA applications. "
            "Built middleware solutions to integrate EZCAD, WSCAD, and ERP systems. "
            "Implemented automation workflows and system integrations."
        ),
        "skills": ["Node.js", "Electron", "MongoDB", "RPA", "JWT", "Node-RED"]
    },
    {
        "role": "IT Support & Technical Assistance",
        "company": "Manisa Celal Bayar University",
        "period": "Oct 2022 – Jan 2025",
        "location": "Manisa, Turkey",
        "description": (
            "Provided hardware and software support, network troubleshooting, system setup, "
            "maintenance, and ensured stable IT infrastructure operations."
        ),
        "skills": ["IT Support", "Networking", "System Maintenance"]
    },
    {
        "role": "Software Developer Intern",
        "company": "TürkŞeker",
        "period": "Aug 2024 – Sep 2024",
        "location": "Konya, Turkey",
        "description": (
            "Developed a custom accounting application for income tracking, expense management, "
            "and financial reporting using Python."
        ),
        "skills": ["Python", "Streamlit", "Data Processing"]
    },
    {
        "role": "Web Developer Intern",
        "company": "Terzion DX",
        "period": "Jul 2023 – Aug 2023",
        "location": "Istanbul, Turkey",
        "description": (
            "Worked with modern web technologies, managed CMS content, applied SEO techniques, "
            "and created visual assets."
        ),
        "skills": ["HTML", "CSS", "JavaScript", "Vue.js", "WordPress", "SEO"]
    }
]

# ===================== SKILLS =====================
skills = {
    "💻 Programming": ["Python", "JavaScript", "TypeScript", "Java"],
    "🌐 Frontend": ["React", "Vue.js", "HTML", "CSS", "Tailwind", "Bootstrap"],
    "⚙️ Backend": ["Node.js", "Express.js", "FastAPI", "JWT"],
    "🗄️ Databases": ["MongoDB", "SQLite", "Supabase"],
    "🤖 AI & Data": ["pandas", "Streamlit", "YOLOv5", "Data Analysis", "Machine Learning"],
    "🛠️ Tools": ["Git", "Docker", "RPA", "Node-RED", "Scrum", "Kanban"]
}

# ===================== PROJECTS =====================
projects = [
    {
        "title": "WscadTracer",
        "description": (
            "Web application that analyzes BOM changes in WSCAD Excel files. "
            "Includes revision comparison, ERP integration, hybrid SQLite–Supabase database, "
            "authentication, and real-time reporting."
        ),
        "tech": ["Python", "Streamlit", "SQLite", "Supabase", "pandas", "plotly"]
    },
    {
        "title": "DGA-CAD",
        "description": (
            "Desktop RPA application with visual workflow designer for Excel automation. "
            "Features Node-RED integration, JWT authentication, and workflow export/import."
        ),
        "tech": ["Electron", "Node-RED", "MongoDB", "JWT", "SVG"]
    },
    {
        "title": "DGA-Academy",
        "description": (
            "Full-stack educational platform with HTTPS, YouTube API integration, "
            "JWT authentication, course tracking, and AI-powered learning assistance."
        ),
        "tech": ["Node.js", "Express", "MongoDB", "EJS", "YouTube API", "JWT"]
    },
    {
        "title": "Güven-Yaka",
        "description": (
            "Cross-platform security management system with real-time notifications, maps, chat, "
            "admin dashboard, and mobile deployment via Capacitor."
        ),
        "tech": ["React", "TypeScript", "Tailwind", "Capacitor", "React Query"]
    }
]

# ===================== CERTIFICATIONS =====================
certifications = [
    {
        "title": "Mastering Applied Data Science",
        "org": "The Data Science Bootcamp",
        "date": "January 2026",
        "desc": (
            "Project-based data science program covering EDA, feature engineering, "
            "supervised and unsupervised learning, model evaluation, and deployment workflows."
        )
    },
    {
        "title": "Network Basics",
        "org": "BTK Akademi",
        "date": "April 2024",
        "desc": (
            "Fundamentals of networking including OSI & TCP/IP models, IP addressing, "
            "subnetting, routing, switching, and network protocols."
        )
    }
]
