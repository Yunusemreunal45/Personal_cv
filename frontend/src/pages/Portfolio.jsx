import React from 'react';
import { Github, Linkedin, Mail, Phone, MapPin, Download, ExternalLink, Code2, Database, Globe, Terminal } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card, CardContent } from '../components/ui/card';
import { Badge } from '../components/ui/badge';

const Portfolio = () => {
  const personalInfo = {
    name: 'Yunus Emre Ünal',
    title: 'Full-Stack Developer & AI Enthusiast',
    location: 'Manisa, Turkey',
    phone: '(+90) 553 798 8488',
    email: 'yunusemreu623@gmail.com',
    linkedin: 'https://www.linkedin.com/in/yunus-emre-ünal-aab175263/',
    github: 'https://github.com/yunusemreunal',
    website: 'https://cerulean-travesseiro-a187f3.netlify.app',
    cvLink: 'https://customer-assets.emergentagent.com/job_6cd547df-b864-4d07-b910-1fd41bea082b/artifacts/fqt0nfav_Yunus_Emre_%C3%9Cnal_cv.pdf'
  };

  const about = "Computer Engineering graduate from Manisa Celal Bayar University with strong expertise in full-stack development and AI technologies. Experienced in building scalable web applications, RPA solutions, and intelligent systems. Passionate about creating innovative, data-driven engineering solutions through continuous learning and hands-on project development.";

  const stats = [
    { label: 'Years Experience', value: '3+' },
    { label: 'Projects Completed', value: '15+' },
    { label: 'Technologies', value: '20+' }
  ];

  const experience = [
    {
      role: 'Software Developer',
      company: 'DGA Yazılım',
      period: 'Nov 2024 - Present',
      location: 'Manisa, Turkey',
      description: 'Developing full-stack educational platforms and desktop applications using RPA tools. Contributing to middleware solutions for system integration and process automation.',
      skills: ['React', 'Node.js', 'RPA', 'MongoDB']
    },
    {
      role: 'Software Developer (Internship)',
      company: 'Türk Şeker',
      period: 'Aug 2024 - Sep 2024',
      location: 'Konya, Turkey',
      description: 'Developed custom accounting application for financial tracking, expense management, and reporting for accurate financial planning.',
      skills: ['Python', 'Streamlit', 'Data Processing']
    },
    {
      role: 'Web Developer (Internship)',
      company: 'Terzion DX',
      period: 'Jul 2023 - Aug 2023',
      location: 'Istanbul, Turkey',
      description: 'Gained practical experience with modern web technologies. Managed content using CMS platforms, applied SEO techniques, and created visual assets.',
      skills: ['Vue.js', 'Node.js', 'WordPress', 'SEO']
    },
    {
      role: 'IT Support Specialist',
      company: 'Manisa Celal Bayar University',
      period: 'Oct 2022 - Jan 2025',
      location: 'Manisa, Turkey',
      description: 'Provided technical support, diagnosed hardware/software issues, performed system maintenance, and ensured smooth IT operations.',
      skills: ['IT Support', 'Network Management', 'Troubleshooting']
    }
  ];

  const skills = {
    'Frontend': ['React', 'Vue.js', 'TypeScript', 'Tailwind CSS', 'HTML/CSS', 'Electron.js'],
    'Backend': ['Node.js', 'Express.js', 'Python', 'FastAPI', 'JWT Auth'],
    'Database': ['MongoDB', 'SQLite', 'Supabase'],
    'Tools & Methods': ['Docker', 'Git', 'RPA', 'Scrum', 'Kanban'],
    'AI & Data': ['YOLOV5', 'pandas', 'plotly', 'Streamlit']
  };

  const featuredProjects = [
    {
      title: 'DGA-Academy',
      description: 'Full-stack educational platform with secure HTTPS server, YouTube API integration, and JWT authentication. Features interactive video player, user profiles, and social media sharing.',
      tech: ['React', 'Node.js', 'MongoDB', 'YouTube API', 'JWT'],
      highlights: ['Secure Authentication', 'Real-time Learning', 'Social Integration']
    },
    {
      title: 'Güven-Yaka',
      description: 'Cross-platform security management application for Android/iOS. Features real-time notifications, interactive maps, chat functionality, and comprehensive admin dashboard.',
      tech: ['React', 'Capacitor', 'MongoDB', 'JWT', 'Real-time API'],
      highlights: ['Mobile App', 'Real-time Features', 'Admin Dashboard']
    },
    {
      title: 'WscadTracer',
      description: 'Python web application analyzing BOM changes in WSCAD Excel files. Features comparison algorithm, dual database system, and ERP integration with real-time sync.',
      tech: ['Python', 'SQLite', 'Supabase', 'ERP Integration'],
      highlights: ['Data Analysis', 'Revision Tracking', 'ERP Integration']
    },
    {
      title: 'DGA-CAD',
      description: 'Desktop RPA application for Excel data processing automation with visual workflow designer and Node-RED integration for dynamic workflow creation.',
      tech: ['Electron', 'MongoDB', 'Node-RED', 'JWT', 'SVG Canvas'],
      highlights: ['Workflow Automation', 'Visual Designer', 'Process Optimization']
    }
  ];

  return (
    <div className="min-h-screen bg-white scroll-smooth">
      {/* Hero Section */}
      <section className="relative bg-gradient-to-br from-slate-50 via-white to-emerald-50 pt-20 pb-32 px-6">
        <div className="max-w-6xl mx-auto">
          <div className="flex flex-col md:flex-row items-center md:items-start gap-12">
            {/* Profile Image Placeholder */}
            <div className="flex-shrink-0">
              <div className="w-40 h-40 rounded-full bg-gradient-to-br from-slate-200 to-emerald-100 border-4 border-white shadow-xl flex items-center justify-center">
                <span className="text-6xl font-bold text-slate-700">{personalInfo.name.split(' ').map(n => n[0]).join('')}</span>
              </div>
            </div>

            {/* Hero Content */}
            <div className="flex-1 text-center md:text-left">
              <h1 className="text-5xl md:text-6xl font-bold text-slate-900 mb-3">
                {personalInfo.name}
              </h1>
              <p className="text-2xl md:text-3xl text-emerald-600 font-semibold mb-6">
                {personalInfo.title}
              </p>
              
              <div className="flex flex-wrap gap-4 justify-center md:justify-start mb-8 text-slate-600">
                <span className="flex items-center gap-2">
                  <MapPin className="w-4 h-4" />
                  {personalInfo.location}
                </span>
                <span className="flex items-center gap-2">
                  <Mail className="w-4 h-4" />
                  {personalInfo.email}
                </span>
              </div>

              {/* CTA Buttons */}
              <div className="flex flex-wrap gap-4 justify-center md:justify-start mb-12">
                <Button 
                  className="bg-emerald-600 hover:bg-emerald-700 text-white px-6 py-6 text-lg shadow-lg hover:shadow-xl transition-all"
                  onClick={() => window.open(personalInfo.cvLink, '_blank')}
                >
                  <Download className="w-5 h-5 mr-2" />
                  Download CV
                </Button>
                <Button 
                  variant="outline" 
                  className="border-2 border-slate-300 hover:border-emerald-600 hover:bg-emerald-50 px-6 py-6 text-lg transition-all"
                  onClick={() => window.location.href = `mailto:${personalInfo.email}`}
                >
                  <Mail className="w-5 h-5 mr-2" />
                  Contact Me
                </Button>
              </div>

              {/* Social Links */}
              <div className="flex gap-4 justify-center md:justify-start">
                <Button
                  variant="ghost"
                  size="icon"
                  className="w-12 h-12 rounded-full hover:bg-slate-100 transition-colors"
                  onClick={() => window.open(personalInfo.linkedin, '_blank')}
                >
                  <Linkedin className="w-6 h-6 text-slate-700" />
                </Button>
                <Button
                  variant="ghost"
                  size="icon"
                  className="w-12 h-12 rounded-full hover:bg-slate-100 transition-colors"
                  onClick={() => window.open(personalInfo.github, '_blank')}
                >
                  <Github className="w-6 h-6 text-slate-700" />
                </Button>
                <Button
                  variant="ghost"
                  size="icon"
                  className="w-12 h-12 rounded-full hover:bg-slate-100 transition-colors"
                  onClick={() => window.open(personalInfo.website, '_blank')}
                >
                  <Globe className="w-6 h-6 text-slate-700" />
                </Button>
              </div>
            </div>
          </div>

          {/* Stats */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-16">
            {stats.map((stat, index) => (
              <Card key={index} className="border-none shadow-md hover:shadow-lg transition-shadow bg-white">
                <CardContent className="pt-6 pb-6 text-center">
                  <div className="text-4xl font-bold text-emerald-600 mb-2">{stat.value}</div>
                  <div className="text-slate-600 font-medium">{stat.label}</div>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* About Section */}
      <section className="py-20 px-6 bg-white">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-4xl font-bold text-slate-900 mb-8 text-center">About Me</h2>
          <p className="text-lg text-slate-600 leading-relaxed max-w-4xl mx-auto text-center">
            {about}
          </p>
        </div>
      </section>

      {/* Experience Section */}
      <section className="py-20 px-6 bg-slate-50">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-4xl font-bold text-slate-900 mb-12 text-center">Experience</h2>
          <div className="space-y-8">
            {experience.map((exp, index) => (
              <Card key={index} className="border-l-4 border-emerald-600 shadow-md hover:shadow-lg transition-shadow">
                <CardContent className="pt-6">
                  <div className="flex flex-col md:flex-row md:items-start md:justify-between mb-4">
                    <div>
                      <h3 className="text-2xl font-bold text-slate-900">{exp.role}</h3>
                      <p className="text-lg text-emerald-600 font-semibold">{exp.company}</p>
                      <p className="text-slate-500">{exp.location}</p>
                    </div>
                    <span className="text-slate-600 font-medium mt-2 md:mt-0">{exp.period}</span>
                  </div>
                  <p className="text-slate-600 mb-4">{exp.description}</p>
                  <div className="flex flex-wrap gap-2">
                    {exp.skills.map((skill, idx) => (
                      <Badge key={idx} variant="secondary" className="bg-emerald-100 text-emerald-700 hover:bg-emerald-200">
                        {skill}
                      </Badge>
                    ))}
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Projects Section */}
      <section className="py-20 px-6 bg-white">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-4xl font-bold text-slate-900 mb-12 text-center">Featured Projects</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            {featuredProjects.map((project, index) => (
              <Card key={index} className="border-none shadow-md hover:shadow-xl transition-all hover:-translate-y-1 duration-300">
                <CardContent className="pt-6">
                  <h3 className="text-2xl font-bold text-slate-900 mb-3">{project.title}</h3>
                  <p className="text-slate-600 mb-4">{project.description}</p>
                  
                  <div className="mb-4">
                    <p className="text-sm font-semibold text-slate-700 mb-2">Key Features:</p>
                    <ul className="space-y-1">
                      {project.highlights.map((highlight, idx) => (
                        <li key={idx} className="text-sm text-slate-600 flex items-center gap-2">
                          <span className="w-1.5 h-1.5 bg-emerald-600 rounded-full"></span>
                          {highlight}
                        </li>
                      ))}
                    </ul>
                  </div>

                  <div className="flex flex-wrap gap-2">
                    {project.tech.map((tech, idx) => (
                      <Badge key={idx} variant="outline" className="border-slate-300 text-slate-700">
                        {tech}
                      </Badge>
                    ))}
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Skills Section */}
      <section className="py-20 px-6 bg-slate-50">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-4xl font-bold text-slate-900 mb-12 text-center">Technical Skills</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {Object.entries(skills).map(([category, techs], index) => (
              <Card key={index} className="border-none shadow-md hover:shadow-lg transition-shadow">
                <CardContent className="pt-6">
                  <div className="flex items-center gap-2 mb-4">
                    {category.includes('Frontend') && <Code2 className="w-5 h-5 text-emerald-600" />}
                    {category.includes('Backend') && <Terminal className="w-5 h-5 text-emerald-600" />}
                    {category.includes('Database') && <Database className="w-5 h-5 text-emerald-600" />}
                    <h3 className="text-xl font-bold text-slate-900">{category}</h3>
                  </div>
                  <div className="flex flex-wrap gap-2">
                    {techs.map((tech, idx) => (
                      <Badge key={idx} variant="secondary" className="bg-slate-100 text-slate-700 hover:bg-emerald-100 hover:text-emerald-700 transition-colors">
                        {tech}
                      </Badge>
                    ))}
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Education Section */}
      <section className="py-20 px-6 bg-white">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-4xl font-bold text-slate-900 mb-12 text-center">Education</h2>
          <Card className="border-l-4 border-emerald-600 shadow-md max-w-3xl mx-auto">
            <CardContent className="pt-6">
              <h3 className="text-2xl font-bold text-slate-900 mb-2">Computer Engineering</h3>
              <p className="text-lg text-emerald-600 font-semibold mb-2">Manisa Celal Bayar University</p>
              <p className="text-slate-600">2020 - 2025 | Manisa, Turkey</p>
            </CardContent>
          </Card>
        </div>
      </section>

      {/* Contact Section */}
      <section className="py-20 px-6 bg-gradient-to-br from-slate-50 via-white to-emerald-50">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-4xl font-bold text-slate-900 mb-6">Let's Connect</h2>
          <p className="text-lg text-slate-600 mb-8">
            I'm always interested in hearing about new opportunities and collaborations.
          </p>
          <div className="flex flex-wrap gap-4 justify-center">
            <Button 
              className="bg-emerald-600 hover:bg-emerald-700 text-white px-8 py-6 text-lg shadow-lg hover:shadow-xl transition-all"
              onClick={() => window.location.href = `mailto:${personalInfo.email}`}
            >
              <Mail className="w-5 h-5 mr-2" />
              Send Email
            </Button>
            <Button 
              variant="outline" 
              className="border-2 border-slate-300 hover:border-emerald-600 hover:bg-emerald-50 px-8 py-6 text-lg transition-all"
              onClick={() => window.open(personalInfo.linkedin, '_blank')}
            >
              <Linkedin className="w-5 h-5 mr-2" />
              LinkedIn Profile
            </Button>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-slate-900 text-white py-8 px-6">
        <div className="max-w-6xl mx-auto text-center">
          <p className="text-slate-400">© 2025 {personalInfo.name}. All rights reserved.</p>
        </div>
      </footer>
    </div>
  );
};

export default Portfolio;