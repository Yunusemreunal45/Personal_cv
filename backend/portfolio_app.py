import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Yunus Emre Ünal - Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Main container */
    .main {
        background: white;
    }
    
    /* Hero Section */
    .hero-section {
        background: linear-gradient(135deg, #f1f5f9 0%, #ffffff 30%, #ecfdf5 70%, #d1fae5 100%);
        padding: 80px 20px;
        border-radius: 30px;
        margin-bottom: 40px;
        box-shadow: 0 10px 40px rgba(16, 185, 129, 0.1);
        position: relative;
        overflow: hidden;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -10%;
        width: 500px;
        height: 500px;
        background: radial-gradient(circle, rgba(16, 185, 129, 0.08) 0%, transparent 70%);
        border-radius: 50%;
    }
    
    .hero-section::after {
        content: '';
        position: absolute;
        bottom: -30%;
        left: -5%;
        width: 400px;
        height: 400px;
        background: radial-gradient(circle, rgba(59, 130, 246, 0.05) 0%, transparent 70%);
        border-radius: 50%;
    }
    
    .profile-avatar {
        width: 180px;
        height: 180px;
        margin: 0 auto 35px auto;
        background: linear-gradient(135deg, #10b981 0%, #059669 50%, #047857 100%);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 6px solid white;
        box-shadow: 0 15px 50px rgba(16, 185, 129, 0.25), 0 5px 15px rgba(0, 0, 0, 0.1);
        position: relative;
        z-index: 2;
        transition: transform 0.3s ease;
    }
    
    .profile-avatar:hover {
        transform: scale(1.05);
    }
    
    .avatar-text {
        font-size: 5rem;
        font-weight: 900;
        color: white;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }
    
    .hero-title {
        font-size: 4.5rem;
        font-weight: 900;
        color: #0f172a;
        margin-bottom: 15px;
        line-height: 1.1;
        letter-spacing: -0.02em;
        position: relative;
        z-index: 2;
        background: linear-gradient(135deg, #0f172a 0%, #334155 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .hero-subtitle {
        font-size: 2.2rem;
        font-weight: 700;
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 25px;
        position: relative;
        z-index: 2;
    }
    
    .hero-contact {
        font-size: 1.1rem;
        color: #64748b;
        margin-bottom: 10px;
        position: relative;
        z-index: 2;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
    }
    
    .contact-icon {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 24px;
        height: 24px;
        background: #10b981;
        border-radius: 50%;
        color: white;
        font-size: 0.75rem;
    }
    
    /* Stats Cards */
    .stat-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        padding: 40px 30px;
        border-radius: 20px;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
        text-align: center;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        border: 1px solid rgba(16, 185, 129, 0.1);
        position: relative;
        overflow: hidden;
    }
    
    .stat-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #10b981 0%, #059669 100%);
        transform: scaleX(0);
        transition: transform 0.4s ease;
    }
    
    .stat-card:hover::before {
        transform: scaleX(1);
    }
    
    .stat-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 15px 40px rgba(16, 185, 129, 0.2);
        border-color: rgba(16, 185, 129, 0.3);
    }
    
    .stat-value {
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 10px;
        letter-spacing: -0.02em;
    }
    
    .stat-label {
        font-size: 1.05rem;
        color: #64748b;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* Section Titles */
    .section-title {
        font-size: 2.5rem;
        font-weight: 800;
        color: #0f172a;
        text-align: center;
        margin: 60px 0 40px 0;
    }
    
    /* Experience Cards */
    .experience-card {
        background: white;
        padding: 30px;
        border-radius: 15px;
        border-left: 5px solid #10b981;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        margin-bottom: 20px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .experience-card:hover {
        transform: translateX(5px);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
    }
    
    .exp-role {
        font-size: 1.5rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 5px;
    }
    
    .exp-company {
        font-size: 1.2rem;
        font-weight: 600;
        color: #10b981;
        margin-bottom: 5px;
    }
    
    .exp-period {
        font-size: 0.95rem;
        color: #64748b;
        margin-bottom: 15px;
    }
    
    .exp-description {
        font-size: 1rem;
        color: #475569;
        line-height: 1.6;
        margin-bottom: 15px;
    }
    
    /* Skills Tags */
    .skill-tag {
        display: inline-block;
        background: #d1fae5;
        color: #065f46;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.875rem;
        font-weight: 600;
        margin: 4px;
    }
    
    /* Project Cards */
    .project-card {
        background: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        height: 100%;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .project-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
    }
    
    .project-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 15px;
    }
    
    .project-description {
        font-size: 1rem;
        color: #475569;
        line-height: 1.6;
        margin-bottom: 15px;
    }
    
    .project-highlight {
        font-size: 0.95rem;
        color: #334155;
        margin-left: 15px;
        line-height: 1.8;
    }
    
    /* Tech Tags */
    .tech-tag {
        display: inline-block;
        background: #f1f5f9;
        color: #334155;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.875rem;
        font-weight: 500;
        margin: 4px;
        border: 1px solid #e2e8f0;
    }
    
    /* Skills Section */
    .skill-category {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        margin-bottom: 20px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .skill-category:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
    }
    
    .skill-category-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    /* About Section */
    .about-text {
        font-size: 1.2rem;
        color: #475569;
        line-height: 1.8;
        text-align: center;
        max-width: 900px;
        margin: 0 auto;
    }
    
    /* Education Card */
    .education-card {
        background: white;
        padding: 30px;
        border-radius: 15px;
        border-left: 5px solid #10b981;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        max-width: 700px;
        margin: 0 auto;
    }
    
    .edu-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 10px;
    }
    
    .edu-university {
        font-size: 1.2rem;
        font-weight: 600;
        color: #10b981;
        margin-bottom: 10px;
    }
    
    .edu-period {
        font-size: 1rem;
        color: #64748b;
    }
    
    /* Contact Section */
    .contact-section {
        background: linear-gradient(135deg, #f8fafc 0%, #ffffff 50%, #ecfdf5 100%);
        padding: 60px 20px;
        border-radius: 20px;
        text-align: center;
        margin-top: 60px;
    }
    
    .contact-title {
        font-size: 2.5rem;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 20px;
    }
    
    .contact-text {
        font-size: 1.2rem;
        color: #475569;
        margin-bottom: 30px;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        font-weight: 700;
        font-size: 1.1rem;
        padding: 16px 35px;
        border-radius: 15px;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        transition: left 0.5s;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #059669 0%, #047857 100%);
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(16, 185, 129, 0.4);
    }
    
    /* Link Buttons */
    a.stButton, a[data-testid="stLinkButton"] {
        text-decoration: none !important;
    }
    
    a.stButton > button, a[data-testid="stLinkButton"] > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white !important;
        font-weight: 700;
        font-size: 1.05rem;
        padding: 14px 32px;
        border-radius: 12px;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
    }
    
    a.stButton > button:hover, a[data-testid="stLinkButton"] > button:hover {
        background: linear-gradient(135deg, #059669 0%, #047857 100%);
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(16, 185, 129, 0.4);
    }
    
    /* Footer */
    .footer {
        background: #0f172a;
        color: #94a3b8;
        text-align: center;
        padding: 30px;
        border-radius: 15px;
        margin-top: 60px;
    }
</style>
""", unsafe_allow_html=True)

# Personal Information
personal_info = {
    'name': 'Yunus Emre Ünal',
    'title': 'Full-Stack Developer & AI Enthusiast',
    'location': 'Manisa, Turkey',
    'phone': '(+90) 553 798 8488',
    'email': 'yunusemreu623@gmail.com',
    'linkedin': 'https://www.linkedin.com/in/yunus-emre-ünal-aab175263/',
    'github': 'https://github.com/yunusemreunal',
    'website': 'https://cerulean-travesseiro-a187f3.netlify.app',
    'cv_url': 'https://customer-assets.emergentagent.com/job_6cd547df-b864-4d07-b910-1fd41bea082b/artifacts/fqt0nfav_Yunus_Emre_%C3%9Cnal_cv.pdf'
}

about = "Computer Engineering graduate from Manisa Celal Bayar University with strong expertise in full-stack development and AI technologies. Experienced in building scalable web applications, RPA solutions, and intelligent systems. Passionate about creating innovative, data-driven engineering solutions through continuous learning and hands-on project development."

stats = [
    {'label': 'Years Experience', 'value': '3+'},
    {'label': 'Projects Completed', 'value': '15+'},
    {'label': 'Technologies', 'value': '20+'}
]

experience = [
    {
        'role': 'Software Developer',
        'company': 'DGA Yazılım',
        'period': 'Nov 2024 - Present',
        'location': 'Manisa, Turkey',
        'description': 'Developing full-stack educational platforms and desktop applications using RPA tools. Contributing to middleware solutions for system integration and process automation.',
        'skills': ['React', 'Node.js', 'RPA', 'MongoDB']
    },
    {
        'role': 'Software Developer (Internship)',
        'company': 'Türk Şeker',
        'period': 'Aug 2024 - Sep 2024',
        'location': 'Konya, Turkey',
        'description': 'Developed custom accounting application for financial tracking, expense management, and reporting for accurate financial planning.',
        'skills': ['Python', 'Streamlit', 'Data Processing']
    },
    {
        'role': 'Web Developer (Internship)',
        'company': 'Terzion DX',
        'period': 'Jul 2023 - Aug 2023',
        'location': 'Istanbul, Turkey',
        'description': 'Gained practical experience with modern web technologies. Managed content using CMS platforms, applied SEO techniques, and created visual assets.',
        'skills': ['Vue.js', 'Node.js', 'WordPress', 'SEO']
    },
    {
        'role': 'IT Support Specialist',
        'company': 'Manisa Celal Bayar University',
        'period': 'Oct 2022 - Jan 2025',
        'location': 'Manisa, Turkey',
        'description': 'Provided technical support, diagnosed hardware/software issues, performed system maintenance, and ensured smooth IT operations.',
        'skills': ['IT Support', 'Network Management', 'Troubleshooting']
    }
]

skills = {
    '💻 Frontend': ['React', 'Vue.js', 'TypeScript', 'Tailwind CSS', 'HTML/CSS', 'Electron.js'],
    '⚙️ Backend': ['Node.js', 'Express.js', 'Python', 'FastAPI', 'JWT Auth'],
    '🗄️ Database': ['MongoDB', 'SQLite', 'Supabase'],
    '🛠️ Tools & Methods': ['Docker', 'Git', 'RPA', 'Scrum', 'Kanban'],
    '🤖 AI & Data': ['YOLOV5', 'pandas', 'plotly', 'Streamlit']
}

featured_projects = [
    {
        'title': 'DGA-Academy',
        'description': 'Full-stack educational platform with secure HTTPS server, YouTube API integration, and JWT authentication. Features interactive video player, user profiles, and social media sharing.',
        'tech': ['React', 'Node.js', 'MongoDB', 'YouTube API', 'JWT'],
        'highlights': ['Secure Authentication', 'Real-time Learning', 'Social Integration']
    },
    {
        'title': 'Güven-Yaka',
        'description': 'Cross-platform security management application for Android/iOS. Features real-time notifications, interactive maps, chat functionality, and comprehensive admin dashboard.',
        'tech': ['React', 'Capacitor', 'MongoDB', 'JWT', 'Real-time API'],
        'highlights': ['Mobile App', 'Real-time Features', 'Admin Dashboard']
    },
    {
        'title': 'WscadTracer',
        'description': 'Python web application analyzing BOM changes in WSCAD Excel files. Features comparison algorithm, dual database system, and ERP integration with real-time sync.',
        'tech': ['Python', 'SQLite', 'Supabase', 'ERP Integration'],
        'highlights': ['Data Analysis', 'Revision Tracking', 'ERP Integration']
    },
    {
        'title': 'DGA-CAD',
        'description': 'Desktop RPA application for Excel data processing automation with visual workflow designer and Node-RED integration for dynamic workflow creation.',
        'tech': ['Electron', 'MongoDB', 'Node-RED', 'JWT', 'SVG Canvas'],
        'highlights': ['Workflow Automation', 'Visual Designer', 'Process Optimization']
    }
]

# HERO SECTION
st.markdown(f"""
<div class="hero-section">
    <div style="text-align: center; position: relative; z-index: 2;">
        <div class="profile-avatar">
            <span class="avatar-text">YEÜ</span>
        </div>
        <h1 class="hero-title">{personal_info['name']}</h1>
        <p class="hero-subtitle">{personal_info['title']}</p>
        <div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center; margin-top: 20px;">
            <span class="hero-contact">
                <span class="contact-icon">📍</span>
                {personal_info['location']}
            </span>
            <span class="hero-contact">
                <span class="contact-icon">✉️</span>
                {personal_info['email']}
            </span>
            <span class="hero-contact">
                <span class="contact-icon">📱</span>
                {personal_info['phone']}
            </span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Buttons
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
with col2:
    st.link_button("📥 Download CV", personal_info['cv_url'], use_container_width=True)
with col3:
    st.link_button("💼 LinkedIn", personal_info['linkedin'], use_container_width=True)
with col4:
    st.link_button("🔗 GitHub", personal_info['github'], use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# STATS
col1, col2, col3 = st.columns(3)
for idx, stat in enumerate(stats):
    with [col1, col2, col3][idx]:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{stat['value']}</div>
            <div class="stat-label">{stat['label']}</div>
        </div>
        """, unsafe_allow_html=True)

# ABOUT SECTION
st.markdown('<h2 class="section-title">About Me</h2>', unsafe_allow_html=True)
st.markdown(f'<p class="about-text">{about}</p>', unsafe_allow_html=True)

# EXPERIENCE SECTION
st.markdown('<h2 class="section-title">Experience</h2>', unsafe_allow_html=True)
for exp in experience:
    skills_html = ''.join([f'<span class="skill-tag">{skill}</span>' for skill in exp['skills']])
    st.markdown(f"""
    <div class="experience-card">
        <div class="exp-role">{exp['role']}</div>
        <div class="exp-company">{exp['company']}</div>
        <div class="exp-period">{exp['period']} | {exp['location']}</div>
        <div class="exp-description">{exp['description']}</div>
        <div>{skills_html}</div>
    </div>
    """, unsafe_allow_html=True)

# PROJECTS SECTION
st.markdown('<h2 class="section-title">Featured Projects</h2>', unsafe_allow_html=True)
cols = st.columns(2)
for idx, project in enumerate(featured_projects):
    with cols[idx % 2]:
        tech_html = ''.join([f'<span class="tech-tag">{tech}</span>' for tech in project['tech']])
        highlights_html = '<br>'.join([f'• {h}' for h in project['highlights']])
        st.markdown(f"""
        <div class="project-card">
            <div class="project-title">{project['title']}</div>
            <div class="project-description">{project['description']}</div>
            <div style="margin-bottom: 15px;">
                <strong style="font-size: 0.95rem; color: #334155;">Key Features:</strong>
                <div class="project-highlight">{highlights_html}</div>
            </div>
            <div>{tech_html}</div>
        </div>
        """, unsafe_allow_html=True)

# SKILLS SECTION
st.markdown('<h2 class="section-title">Technical Skills</h2>', unsafe_allow_html=True)
cols = st.columns(3)
for idx, (category, techs) in enumerate(skills.items()):
    with cols[idx % 3]:
        skills_html = ''.join([f'<span class="skill-tag">{tech}</span>' for tech in techs])
        st.markdown(f"""
        <div class="skill-category">
            <div class="skill-category-title">{category}</div>
            <div>{skills_html}</div>
        </div>
        """, unsafe_allow_html=True)

# EDUCATION SECTION
st.markdown('<h2 class="section-title">Education</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="education-card">
    <div class="edu-title">Computer Engineering</div>
    <div class="edu-university">Manisa Celal Bayar University</div>
    <div class="edu-period">2020 - 2025 | Manisa, Turkey</div>
</div>
""", unsafe_allow_html=True)

# CONTACT SECTION
st.markdown(f"""
<div class="contact-section">
    <div class="contact-title">Let's Connect</div>
    <div class="contact-text">I'm always interested in hearing about new opportunities and collaborations.</div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("✉️ Send Email", use_container_width=True):
        st.link_button("Open Email", f"mailto:{personal_info['email']}", use_container_width=True)

# FOOTER
st.markdown(f"""
<div class="footer">
    <p>© 2025 {personal_info['name']}. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
