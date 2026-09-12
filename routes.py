# ============================================================
# DIKSHANT BALISH — PORTFOLIO
# routes.py
# ============================================================

from datetime import datetime
from pathlib import Path
from typing import Optional

from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from database import (
    DatabaseNotConfiguredError,
    DatabaseUnavailableError,
    save_contact_message,
)


# ============================================================
# CONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)

router = APIRouter()


# ============================================================
# SITE CONFIGURATION
# ============================================================

SITE = {
    "name": "Dikshant Balish",
    "short_name": "Dikshant",
    "title": "Software Engineer & AI Developer",

    "description": (
        "Software Engineer and AI Developer focused on backend "
        "engineering, AI/ML, agentic AI and practical software systems."
    ),

    "location": "Yamunanagar, Haryana, India",

    "email": "sharmadikshant223@gmail.com",

    # Keep URLs as plain URLs.
    # Do NOT use Markdown here.
    "github": "https://github.com/dikshantbalish",
    "linkedin": "https://linkedin.com/in/dikshantbalish",

    # Resume PDF
    "resume": "/static/documents/DIKSHANT_RESUME.pdf",
}


# ============================================================
# PROJECT DATA
# ============================================================

PROJECTS = [
    {
        "slug": "multi-agent-ai-research-system",
        "title": "Multi-Agent AI Research System",
        "short_title": "Multi-Agent Research",
        "category": "AI / Agentic AI",
        "year": "2026",
        "featured": True,
        "status": "Completed",

        "description": (
            "A multi-agent research system that orchestrates specialized "
            "AI agents to plan research, search the web, extract information, "
            "generate reports and evaluate output quality."
        ),

        "long_description": (
            "Designed as an agentic workflow using LangChain and LangGraph. "
            "The system separates research responsibilities into specialized "
            "agents instead of relying on a single LLM call."
        ),

        "tech": [
            "Python",
            "LangChain",
            "LangGraph",
            "OpenAI API",
            "Agentic AI",
        ],

        "features": [
            "Research planning agent",
            "Web search and information retrieval",
            "Content extraction",
            "Report generation",
            "Automated quality evaluation",
            "Multi-agent workflow orchestration",
            "Prompt optimization",
        ],

        "highlights": [
            "5 specialized agents",
            "End-to-end research workflow",
            "LLM-based self-review",
            "Reduced redundant API calls",
        ],

        "github": "https://github.com/dikshantbalish",
        "demo": None,
    },

    {
        "slug": "ai-finance-tracker",
        "title": "AI Finance Tracker",
        "short_title": "Finance Tracker",
        "category": "Full Stack / AI",
        "year": "2025",
        "featured": True,
        "status": "Completed",

        "description": (
            "A full-stack personal finance platform combining transaction "
            "management, investment tracking, debt analysis and AI-powered "
            "financial assistance."
        ),

        "long_description": (
            "A MERN-based finance platform enhanced with OpenAI capabilities "
            "for natural-language transaction processing, receipt understanding, "
            "bill parsing and conversational financial assistance."
        ),

        "tech": [
            "React.js",
            "Node.js",
            "Express.js",
            "MongoDB",
            "JWT",
            "OpenAI API",
        ],

        "features": [
            "JWT authentication",
            "Transaction management",
            "Investment tracking",
            "Debt analysis",
            "Receipt understanding",
            "AI expense parsing",
            "Bill parsing",
            "Conversational finance assistant",
            "Spending categorization",
        ],

        "highlights": [
            "500+ sample transactions",
            "90%+ categorization accuracy",
            "AI-assisted transaction processing",
            "Automated financial insights",
        ],

        "github": "https://github.com/dikshantbalish/FinanceTracker",
        "demo": None,
    },

    {
        "slug": "trip-mate-ai",
        "title": "Trip-Mate AI",
        "short_title": "Trip-Mate AI",
        "category": "AI / Agents",
        "year": "2026",
        "featured": True,
        "status": "Active Development",

        "description": (
            "An agentic travel assistant built around FastAPI and LangGraph "
            "for intelligent trip planning, flight and hotel discovery and "
            "multi-step travel workflows."
        ),

        "long_description": (
            "Trip-Mate AI explores the use of graph-based agent orchestration "
            "for practical travel planning. The system integrates external APIs "
            "and persistent state to coordinate multi-step travel tasks."
        ),

        "tech": [
            "Python",
            "FastAPI",
            "LangGraph",
            "LangChain",
            "Groq",
            "Tavily",
            "PostgreSQL",
            "Docker",
        ],

        "features": [
            "Agentic trip planning",
            "Flight search",
            "Hotel search",
            "Web research",
            "LangGraph workflow orchestration",
            "Persistent conversation state",
            "FastAPI backend",
            "Docker deployment",
        ],

        "highlights": [
            "Graph-based agent architecture",
            "External API integrations",
            "Persistent state",
            "Cloud-deployable backend",
        ],

        "github": "https://github.com/dikshantbalish/Trip-Mate-AI",
        "demo": None,
    },

    {
        "slug": "prerental",
        "title": "PreRental",
        "short_title": "PreRental",
        "category": "Full Stack",
        "year": "2025",
        "featured": True,
        "status": "Completed",

        "description": (
            "A rental platform designed to simplify property discovery "
            "and management for tenants and property owners."
        ),

        "long_description": (
            "A modular full-stack rental platform with property management, "
            "user profiles, image handling, search and location-based filtering."
        ),

        "tech": [
            "React.js",
            "Node.js",
            "Express.js",
            "MongoDB",
            "REST APIs",
        ],

        "features": [
            "Property management",
            "User profiles",
            "CRUD REST APIs",
            "Image handling",
            "Real-time search",
            "Location-based filtering",
            "Modular MVC architecture",
        ],

        "highlights": [
            "100+ concurrent listings",
            "15+ REST APIs",
            "Modular MVC architecture",
            "Search and filtering system",
        ],

        "github": "https://github.com/dikshantbalish",
        "demo": None,
    },
]


# ============================================================
# CERTIFICATIONS
# ============================================================

CERTIFICATIONS = [
    {
        "title": "ServiceNow Certified System Administrator",
        "short": "ServiceNow CSA",
        "issuer": "ServiceNow",
        "year": "2025",
        "category": "Cloud / Enterprise",
        "pdf": "documents/certifications/ServiceNowCSA.pdf",
    },
    {
        "title": "ServiceNow Certified Application Developer",
        "short": "ServiceNow CAD",
        "issuer": "ServiceNow",
        "year": "2025",
        "category": "Application Development",
            "pdf": "documents/certifications/ServiceNowCAD.pdf",
    },
    {
        "title": "Master Python by Building 100 Projects",
        "short": "Master Python",
        "issuer": "Udemy",
        "year": "",
        "category": "Python",
            "pdf": "documents/certifications/Python.pdf",
    },
    {
        "title": "Web Development Internship",
        "short": "Web Development",
        "issuer": "CodSoft",
        "year": "2024",
        "category": "Web Development",
            "pdf": "documents/certifications/codsoft.pdf",
    },
]


# ============================================================
# SKILLS
# ============================================================

SKILLS = {
    "languages": [
        "Python",
        "Java",
        "C++",
        "JavaScript",
    ],

    "backend": [
        "FastAPI",
        "Django",
        "Node.js",
        "Express.js",
        "REST APIs",
    ],

    "frontend": [
        "React.js",
        "HTML5",
        "CSS3",
        "JavaScript",
    ],

    "ai": [
        "LangChain",
        "LangGraph",
        "OpenAI API",
        "RAG",
        "Prompt Engineering",
        "Agentic AI",
    ],

    "databases": [
        "MongoDB",
        "MySQL",
        "PostgreSQL",
    ],

    "tools": [
        "Git",
        "GitHub",
        "Postman",
        "VS Code",
        "Docker",
        "Render",
    ],
}


# ============================================================
# EXPERIENCE
# ============================================================

EXPERIENCE = [
    {
        "role": "Web Development Intern",
        "company": "Alpha Intern",
        "period": "May 2024 — Jun 2024",

        "description": (
            "Built responsive, mobile-first web pages and components "
            "using HTML5, CSS3 and JavaScript while maintaining "
            "cross-browser compatibility and visual consistency."
        ),

        "skills": [
            "HTML5",
            "CSS3",
            "JavaScript",
            "Responsive Design",
        ],
    },
]


# ============================================================
# EDUCATION
# ============================================================

EDUCATION = [
    {
        "degree": "B.Tech in Computer Science",
        "institution": (
            "Maharishi Markandeshwar (Deemed to be University)"
        ),
        "period": "2022 — 2026",
        "result": "CGPA: 7.73",
    },

    {
        "degree": "CBSE Class XII",
        "institution": "SD Public School",
        "period": "2021 — 2022",
        "result": "79%",
    },

    {
        "degree": "CBSE Class X",
        "institution": "SD Public School",
        "period": "2019 — 2020",
        "result": "90.4%",
    },
]


# ============================================================
# HELPERS
# ============================================================

def base_context(
    request: Request,
    **kwargs,
) -> dict:
    """
    Shared context available to every template.
    """

    # Keep the templates focused on presentation while adapting the
    # compact data model used by this file to their display fields.
    view_projects = [
        {
            **project,
            "name": project["title"],
            "technologies": project.get("tech", []),
        }
        for project in PROJECTS
    ]

    view_certifications = [
        {
            **certification,
            "name": certification["title"],
            "date": certification.get("year", ""),
            "pdf": (
                certification.get("pdf")
                if (
                    certification.get("pdf")
                    and (BASE_DIR / "static" / certification["pdf"]).exists()
                )
                else None
            ),
        }
        for certification in CERTIFICATIONS
    ]

    view_experience = [
        {
            **item,
            "duration": item.get("period", ""),
            "responsibilities": item.get("skills", []),
        }
        for item in EXPERIENCE
    ]

    view_education = [
        {
            **item,
            "duration": item.get("period", ""),
        }
        for item in EDUCATION
    ]

    context = {
        "request": request,
        "site": SITE,
        "projects": view_projects,
        "certifications": view_certifications,
        "skills": [skill for group in SKILLS.values() for skill in group],
        "skills_by_category": SKILLS,
        "experience": view_experience,
        "education": view_education,
        "current_year": datetime.now().year,
    }

    context.update(kwargs)

    return context


def get_project(slug: str) -> Optional[dict]:
    """
    Return a project by slug.
    """

    return next(
        (
            project
            for project in PROJECTS
            if project["slug"] == slug
        ),
        None,
    )


def get_categories() -> list[str]:
    """
    Return unique project categories in alphabetical order.
    """

    return sorted(
        {
            project["category"]
            for project in PROJECTS
            if project.get("category")
        }
    )


# ============================================================
# HOME
# ============================================================

@router.get(
    "/",
    response_class=HTMLResponse,
    name="home",
)
async def home(request: Request):

    featured_projects = [
        project
        for project in base_context(request)["projects"]
        if project.get("featured", False)
    ]

    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context=base_context(
            request,
            page="home",
            featured_projects=featured_projects,
        ),
    )


# ============================================================
# PROJECTS
# ============================================================

@router.get(
    "/projects",
    response_class=HTMLResponse,
    name="projects",
)
async def projects(
    request: Request,
    category: Optional[str] = None,
):

    categories = get_categories()

    if category and category in categories:

        filtered_projects = [
            project
            for project in PROJECTS
            if project["category"] == category
        ]

    else:

        filtered_projects = PROJECTS

        # Invalid/empty category behaves like "all".
        if category not in (None, ""):
            category = None

    return templates.TemplateResponse(
        request=request,
        name="projects.html",
        context=base_context(
            request,
            page="projects",
            categories=categories,
            selected_category=category,
            projects=[
                {
                    **project,
                    "name": project["title"],
                    "technologies": project.get("tech", []),
                }
                for project in filtered_projects
            ],
        ),
    )


# ============================================================
# PROJECT DETAIL
# ============================================================

@router.get(
    "/projects/{slug}",
    response_class=HTMLResponse,
    name="project",
)
async def project_detail(
    request: Request,
    slug: str,
):

    project = get_project(slug)

    if project is None:
        return RedirectResponse(
            url="/projects",
            status_code=303,
        )

    project = {
        **project,
        "name": project["title"],
        "technologies": project.get("tech", []),
    }

    related_projects = [
        item
        for item in PROJECTS
        if (
            item["slug"] != slug
            and item["category"] == project["category"]
        )
    ][:3]

    related_projects = [
        {
            **item,
            "name": item["title"],
            "technologies": item.get("tech", []),
        }
        for item in related_projects
    ]

    return templates.TemplateResponse(
        request=request,
        name="project.html",
        context=base_context(
            request,
            page="project",
            project=project,
            related_projects=related_projects,
        ),
    )


# ============================================================
# RESUME
# ============================================================

@router.get(
    "/resume",
    response_class=HTMLResponse,
    name="resume",
)
async def resume(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="resume.html",
        context=base_context(
            request,
            page="resume",
        ),
    )


# ============================================================
# CERTIFICATIONS
# ============================================================

@router.get(
    "/certifications",
    response_class=HTMLResponse,
    name="certifications",
)
async def certifications(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="certifications.html",
        context=base_context(
            request,
            page="certifications",
        ),
    )


# ============================================================
# CONTACT — GET
# ============================================================

@router.get(
    "/contact",
    response_class=HTMLResponse,
    name="contact",
)
async def contact(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="contact.html",
        context=base_context(
            request,
            page="contact",
            submitted=False,
            errors=[],
            form={
                "name": "",
                "email": "",
                "message": "",
            },
        ),
    )


# ============================================================
# CONTACT — POST
# ============================================================

@router.post(
    "/contact",
    response_class=HTMLResponse,
    name="contact_submit",
)
async def contact_submit(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...),
):

    # --------------------------------------------------------
    # Normalize input
    # --------------------------------------------------------

    name = name.strip()
    email = email.strip()
    message = message.strip()

    errors: list[str] = []


    # --------------------------------------------------------
    # Validation
    # --------------------------------------------------------

    if not name:
        errors.append("Name is required.")

    if not email:
        errors.append("Email is required.")

    elif (
        "@" not in email
        or "." not in email.split("@")[-1]
    ):
        errors.append(
            "Please enter a valid email address."
        )

    if not message:
        errors.append("Message is required.")

    elif len(message) < 10:
        errors.append(
            "Message must contain at least 10 characters."
        )


    # --------------------------------------------------------
    # Validation failure
    # --------------------------------------------------------

    if errors:

        return templates.TemplateResponse(
            request=request,
            name="contact.html",
            context=base_context(
                request,
                page="contact",
                submitted=False,
                errors=errors,
                form={
                    "name": name,
                    "email": email,
                    "message": message,
                },
            ),
            status_code=400,
        )


    try:
        save_contact_message(
            name=name,
            email=email,
            message=message,
        )
    except DatabaseNotConfiguredError:
        errors.append(
            "Contact storage is not configured. Please try again later."
        )
    except DatabaseUnavailableError:
        errors.append(
            "Your message could not be saved. Please try again later."
        )

    if errors:
        return templates.TemplateResponse(
            request=request,
            name="contact.html",
            context=base_context(
                request,
                page="contact",
                submitted=False,
                errors=errors,
                form={
                    "name": name,
                    "email": email,
                    "message": message,
                },
            ),
            status_code=503,
        )

    return templates.TemplateResponse(
        request=request,
        name="contact.html",
        context=base_context(
            request,
            page="contact",
            submitted=True,
            errors=[],
            form={
                "name": "",
                "email": "",
                "message": "",
            },
        ),
    )


# ============================================================
# HEALTH CHECK
# ============================================================

@router.get(
    "/health",
    include_in_schema=False,
)
async def health():

    return {
        "status": "ok",
        "service": "portfolio",
    }