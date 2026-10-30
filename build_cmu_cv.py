import os
import pymupdf
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    """Two-pass canvas to dynamically compute and print 'Page X of Y'."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#718096"))
        page_text = f"Page {self._pageNumber} of {page_count}"
        footer_text = "Asman Makero Musa — Curriculum Vitae | Carnegie Mellon University Africa Application"
        
        # Header bar on Page 2+
        if self._pageNumber > 1:
            self.setStrokeColor(colors.HexColor("#CBD5E0"))
            self.setLineWidth(0.5)
            self.line(36, 11 * inch - 26, 8.5 * inch - 36, 11 * inch - 26)
            self.drawString(36, 11 * inch - 22, "Asman Makero Musa — Computer Science & Applied AI Systems")
            self.drawRightString(8.5 * inch - 36, 11 * inch - 22, "makeromusa17@gmail.com | +254 743 844 451")

        # Bottom footer line on all pages
        self.setStrokeColor(colors.HexColor("#CBD5E0"))
        self.setLineWidth(0.5)
        self.line(36, 30, 8.5 * inch - 36, 30)
        self.drawString(36, 20, footer_text)
        self.drawRightString(8.5 * inch - 36, 20, page_text)
        self.restoreState()

def build_cv(output_pdf_path):
    # Standard Letter: 612 x 792 pt. Margins: 36 pt (0.5 in) left/right, 32 pt top, 36 pt bottom
    doc = SimpleDocTemplate(
        output_pdf_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=32,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()
    
    # Custom Palette
    C_PRIMARY = colors.HexColor("#0F294A")    # Deep Navy
    C_SECONDARY = colors.HexColor("#1A365D")  # Slate Blue
    C_BODY = colors.HexColor("#2D3748")       # Charcoal
    C_MUTED = colors.HexColor("#4A5568")      # Muted Slate
    C_LINE = colors.HexColor("#CBD5E0")       # Border grey
    C_ACCENT = colors.HexColor("#0078FF")     # Tech Blue

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=19,
        leading=21,
        textColor=C_PRIMARY,
        alignment=1
    )

    tagline_style = ParagraphStyle(
        'Tagline',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=11.5,
        textColor=C_ACCENT,
        alignment=1
    )

    contact_style = ParagraphStyle(
        'ContactLine',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=C_MUTED,
        alignment=1
    )

    sec_heading_style = ParagraphStyle(
        'SecHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=11.5,
        textColor=C_PRIMARY,
        spaceBefore=0,
        spaceAfter=0
    )

    item_title_style = ParagraphStyle(
        'ItemTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11,
        textColor=C_SECONDARY
    )

    item_meta_style = ParagraphStyle(
        'ItemMeta',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=11,
        textColor=C_MUTED,
        alignment=2
    )

    item_sub_style = ParagraphStyle(
        'ItemSub',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=10.5,
        textColor=C_BODY
    )

    bullet_style = ParagraphStyle(
        'BulletText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=C_BODY,
        leftIndent=11,
        firstLineIndent=-11,
        spaceBefore=1,
        spaceAfter=1
    )

    skills_label_style = ParagraphStyle(
        'SkillsLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=C_PRIMARY
    )

    skills_val_style = ParagraphStyle(
        'SkillsVal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=C_BODY
    )

    summary_style = ParagraphStyle(
        'SummaryText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=C_BODY,
        alignment=4
    )

    story = []

    def section_header(title, space_before=4):
        p = Paragraph(title.upper(), sec_heading_style)
        hr = HRFlowable(width="100%", thickness=1, color=C_PRIMARY, spaceBefore=2, spaceAfter=4)
        return [Spacer(1, space_before), p, hr]

    # ================= PAGE 1 =================

    # --- 1. HEADER ---
    story.append(Paragraph("ASMAN MAKERO MUSA", title_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("Computer Science Undergraduate &amp; Applied AI Engineer", tagline_style))
    story.append(Spacer(1, 3))
    
    contact_text = (
        "Nairobi, Kenya &nbsp;&bull;&nbsp; "
        "+254 743 844 451 &nbsp;&bull;&nbsp; "
        "makeromusa17@gmail.com &nbsp;&bull;&nbsp; "
        '<font color="#0078FF"><a href="https://www.makeromusa.me">makeromusa.me</a></font> &nbsp;&bull;&nbsp; '
        '<font color="#0078FF"><a href="https://github.com/makeromusa">github.com/makeromusa</a></font> &nbsp;&bull;&nbsp; '
        '<font color="#0078FF"><a href="https://linkedin.com/in/asman-musa-872405371">linkedin.com/in/asman-musa</a></font>'
    )
    story.append(Paragraph(contact_text, contact_style))
    story.append(HRFlowable(width="100%", thickness=0.75, color=C_LINE, spaceBefore=4, spaceAfter=4))

    # --- 2. PROFESSIONAL PROFILE ---
    story.extend(section_header("Professional Profile", space_before=1))
    profile_p = (
        "Analytical Computer Science undergraduate at the University of Nairobi with a rigorous mathematical foundation in "
        "linear algebra, multivariate calculus, and probability/statistics, combined with practical engineering experience in "
        "systems programming (C/C++) and modern machine learning pipelines. Experienced in designing Retrieval-Augmented Generation "
        "(RAG) engines, autonomous multi-agent decision copilots, and cloud integrations with schema-enforced tool calling. "
        "Demonstrated track record of building data-driven AI systems tailored to educational accessibility and operational "
        "challenges across Africa. Eager to advance machine learning competencies through the Carnegie Mellon University Africa AI Certificate."
    )
    story.append(Paragraph(profile_p, summary_style))

    # --- 3. EDUCATION & FOUNDATIONAL MATHEMATICS ---
    story.extend(section_header("Education &amp; Foundational Mathematics", space_before=4))
    edu_table_data = [
        [
            Paragraph("<b>University of Nairobi</b> &mdash; Nairobi, Kenya", item_title_style),
            Paragraph("Expected Graduation: <b>Dec 2029</b>", item_meta_style)
        ],
        [
            Paragraph("<i>Bachelor of Science in Computer Science</i>", item_sub_style),
            Paragraph("Current Status: Year 3", item_meta_style)
        ]
    ]
    t_edu = Table(edu_table_data, colWidths=[380, 160])
    t_edu.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_edu)
    story.append(Spacer(1, 2))
    
    math_courses = (
        "&bull; <b>Foundational Mathematics (CMU Prerequisites):</b> Linear Algebra (Vector spaces, matrix transformations, eigenvalues/eigenvectors), "
        "Calculus (Multivariate differentiation, optimization, partial derivatives), Probability &amp; Statistics (Bayesian inference, probability distributions, hypothesis testing), "
        "Discrete Mathematics (Graph algorithms, combinatorics, Boolean logic)."
    )
    story.append(Paragraph(math_courses, bullet_style))
    
    cs_courses = (
        "&bull; <b>Core Computer Science Foundations:</b> Data Structures &amp; Algorithms (Algorithm complexity, dynamic programming, tree traversals), "
        "Low-Level Systems Programming (POSIX, pointers, memory hierarchies), Operating Systems (Processes, concurrency), Relational Database Management Systems (3NF normalization, SQL query optimization)."
    )
    story.append(Paragraph(cs_courses, bullet_style))

    # --- 4. TECHNICAL SKILLS & DOMAIN EXPERTISE ---
    story.extend(section_header("Technical Skills &amp; Domain Expertise", space_before=4))
    skills_data = [
        [
            Paragraph("AI &amp; Machine Learning:", skills_label_style),
            Paragraph("Retrieval-Augmented Generation (RAG), Multi-Agent Systems, LLM Benchmarking &amp; Evaluation, Prompt Engineering, Function Calling / Tool Calling (JSON Schema), Vector Embeddings, Amazon Bedrock Foundation Models.", skills_val_style)
        ],
        [
            Paragraph("Programming Languages:", skills_label_style),
            Paragraph("Python (FastAPI, PyPDF, Streamlit, Pandas, NumPy), C, C++ (Cisco Advanced Certified), SQL (PostgreSQL, Oracle, SQL Server), JavaScript / TypeScript (Next.js 15).", skills_val_style)
        ],
        [
            Paragraph("Databases &amp; Vector Stores:", skills_label_style),
            Paragraph("ChromaDB, Supabase (pgvector), PostgreSQL, Oracle Database, SQL Server, 3NF Relational Architecture, Data Pipeline Design.", skills_val_style)
        ],
        [
            Paragraph("Systems, Linux &amp; Tools:", skills_label_style),
            Paragraph("Red Hat Enterprise Linux (RH104), Bash Shell Scripting, Git/GitHub, REST APIs, JSON/YAML, CI/CD, Postman, SSMS, Zapier Automation.", skills_val_style)
        ]
    ]
    t_skills = Table(skills_data, colWidths=[130, 410])
    t_skills.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_skills)

    # --- 5. MAJOR APPLIED AI PROJECTS (PART 1) ---
    story.extend(section_header("Applied AI &amp; Software Engineering Projects", space_before=4))

    # Project 1: EduRAG
    p1_head = [
        [
            Paragraph("<b>EduRAG — Academic AI Copilot &amp; Multi-Unit Knowledge Retrieval Engine</b>", item_title_style),
            Paragraph("<i>Python, FastAPI, ChromaDB, Gemini Embeddings</i>", item_meta_style)
        ]
    ]
    t_p1 = Table(p1_head, colWidths=[350, 190])
    t_p1.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t_p1)
    story.append(Paragraph(
        "&bull; Architected a unit-isolated Retrieval-Augmented Generation (RAG) study system to index complex university lecture slides, textbooks, "
        "and past papers across 7 heavy CS courses, eliminating generic LLM hallucinations via strict vector citation grounding.",
        bullet_style
    ))
    story.append(Paragraph(
        "&bull; Implemented semantic chunking pipelines with header and slide-boundary awareness, tagging embeddings with structured metadata "
        "(Unit Code, Topic, Week, Document Name, Page Number) stored in ChromaDB vector collections.",
        bullet_style
    ))
    story.append(Paragraph(
        "&bull; Engineered top-k cosine similarity retrieval with metadata pre-filtering and prompt synthesis to generate verified page-level answers, "
        "automated multi-choice practice exams with distractor justifications, and high-yield revision cheat sheets.",
        bullet_style
    ))
    story.append(Spacer(1, 3))

    # Project 2: Agentic FPL Manager
    p2_head = [
        [
            Paragraph("<b>Agentic FPL Manager — Autonomous Multi-Agent Tactical Decision Engine</b>", item_title_style),
            Paragraph("<i>Python, Gemini 1.5 Pro, Game Theory, JSON Schema</i>", item_meta_style)
        ]
    ]
    t_p2 = Table(p2_head, colWidths=[350, 190])
    t_p2.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t_p2)
    story.append(Paragraph(
        "&bull; Architected an autonomous multi-agent decision copilot featuring orchestrator and specialist analytical agents collaborating "
        "sequentially to model complex game-theory strategies under budget and formation constraints.",
        bullet_style
    ))
    story.append(Paragraph(
        "&bull; Enforced strict JSON schema validation for Google Gemini 1.5 Pro tool calling, executing deterministic API queries against live "
        "football telemetry with zero syntax failure rates.",
        bullet_style
    ))
    story.append(Paragraph(
        "&bull; Engineered mini-league rival intelligence algorithms computing Monte Carlo catch-up probability and modeling opponent chip usage "
        "patterns across a rolling 5-gameweek planning horizon.",
        bullet_style
    ))

    # ================= PAGE BREAK =================
    story.append(PageBreak())

    # ================= PAGE 2 =================
    story.extend(section_header("Applied AI &amp; Software Engineering Projects (Continued)", space_before=0))

    # Project 3: AzureVibe
    p3_head = [
        [
            Paragraph("<b>AzureVibe — Cloud Architecture &amp; AZ-900 Readiness Platform</b>", item_title_style),
            Paragraph("<i>Next.js 15, FastAPI, Supabase, LLM Analogy Engine</i>", item_meta_style)
        ]
    ]
    t_p3 = Table(p3_head, colWidths=[350, 190])
    t_p3.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t_p3)
    story.append(Paragraph(
        "&bull; Engineered an intelligent cloud exam preparation suite integrating active recall flashcards, 3D flip card mechanics, and Leitner "
        "spaced-repetition algorithms to accelerate cloud certification pass rates for African developers.",
        bullet_style
    ))
    story.append(Paragraph(
        "&bull; Designed an AI Study Buddy leveraging customized system prompting to demystify abstract cloud architectures and distributed systems "
        "concepts through relatable African analogies (e.g., regional logistics corridors, agricultural cooperative pooling).",
        bullet_style
    ))
    story.append(Paragraph(
        "&bull; Developed full-stack PostgreSQL/Supabase schema supporting real-time student quiz diagnostics, answer review history, and domain readiness scores.",
        bullet_style
    ))
    story.append(Spacer(1, 4))

    # Project 4: Bundesliga Wrapped & Data Analytics
    p4_head = [
        [
            Paragraph("<b>Bundesliga Wrapped — Sports Analytics &amp; Video Telemetry Pipeline</b>", item_title_style),
            Paragraph("<i>Python, Streamlit, YouTube Data API, REST</i>", item_meta_style)
        ]
    ]
    t_p4 = Table(p4_head, colWidths=[350, 190])
    t_p4.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t_p4)
    story.append(Paragraph(
        "&bull; Developed an interactive sports analytics application consuming live match telemetry, standings, and highlight streams from "
        "Football-Data.org and YouTube Data API v3.",
        bullet_style
    ))
    story.append(Paragraph(
        "&bull; Designed responsive data filtering, statistical aggregation charts, and deployed the application live on Streamlit Cloud.",
        bullet_style
    ))
    story.append(Spacer(1, 4))

    # Project 5: Systems Programming C/C++
    p5_head = [
        [
            Paragraph("<b>Low-Level Systems Programming &amp; Algorithm Optimization</b>", item_title_style),
            Paragraph("<i>C, C++, POSIX, Memory Management, Linux</i>", item_meta_style)
        ]
    ]
    t_p5 = Table(p5_head, colWidths=[350, 190])
    t_p5.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t_p5)
    story.append(Paragraph(
        "&bull; Implemented core systems programming modules in C and C++, focusing on dynamic memory allocation, pointer arithmetic, custom data "
        "structure serialization, and algorithmic complexity optimization.",
        bullet_style
    ))
    story.append(Paragraph(
        "&bull; Earned Cisco Certified Advanced C++ (CPA) credential, demonstrating mastery of Object-Oriented paradigms, Standard Template Library (STL), "
        "templates, exception safety, and low-level resource management.",
        bullet_style
    ))

    # --- 6. PROFESSIONAL EXPERIENCE ---
    story.extend(section_header("Professional Experience", space_before=4))
    exp_head = [
        [
            Paragraph("<b>Equity Bank Kenya</b> &mdash; Nairobi, Kenya", item_title_style),
            Paragraph("<b>2024</b>", item_meta_style)
        ],
        [
            Paragraph("<i>Intern &mdash; Operations, Credit Documentation &amp; Customer Systems</i>", item_sub_style),
            Paragraph("Corporate Banking Division", item_meta_style)
        ]
    ]
    t_exp = Table(exp_head, colWidths=[380, 160])
    t_exp.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t_exp)
    story.append(Spacer(1, 2))
    story.append(Paragraph(
        "&bull; Executed client financial documentation auditing and end-to-end loan credit validation workflows within a high-volume corporate banking environment.",
        bullet_style
    ))
    story.append(Paragraph(
        "&bull; Collaborated with cross-functional branch teams utilizing enterprise CRM platforms and Microsoft Teams to streamline documentation pipelines and customer support operations.",
        bullet_style
    ))
    story.append(Paragraph(
        "&bull; Applied rigorous analytical verification standards to guarantee 100% compliance with institutional regulatory requirements and internal record accuracy policies.",
        bullet_style
    ))

    # --- 7. VERIFIED CERTIFICATIONS & ACCREDITATIONS ---
    story.extend(section_header("Verified Certifications &amp; Accreditations", space_before=4))
    
    certs_data = [
        [
            Paragraph("&bull; <b>AWS &amp; Udacity AI Practitioner Challenge:</b> Foundation models, Amazon Bedrock, LLM benchmarking &amp; fine-tuning.", skills_val_style),
            Paragraph("<i>Udacity &amp; AWS (2026)</i>", item_meta_style)
        ],
        [
            Paragraph("&bull; <b>Cisco Certified Advanced C++ (CPA):</b> Advanced OOP, templates, memory management, STL algorithms.", skills_val_style),
            Paragraph("<i>Cisco &amp; OpenEDG (2026)</i>", item_meta_style)
        ],
        [
            Paragraph("&bull; <b>AI Safari &mdash; Generative AI &amp; Prompt Engineering:</b> Multi-agent workflows, prompt design, AI engineering.", skills_val_style),
            Paragraph("<i>PLP &amp; Emurgo Africa (2026)</i>", item_meta_style)
        ],
        [
            Paragraph("&bull; <b>Red Hat Linux System Administration (RH104):</b> Linux CLI, POSIX process management, permissions, shell scripts.", skills_val_style),
            Paragraph("<i>Red Hat Academy (2025)</i>", item_meta_style)
        ],
        [
            Paragraph("&bull; <b>Google Foundations of Cybersecurity:</b> Network defense, security architectures, threat mitigation.", skills_val_style),
            Paragraph("<i>Google &amp; Coursera (2025)</i>", item_meta_style)
        ],
        [
            Paragraph("&bull; <b>Cisco C++ Essentials 1 &amp; 2:</b> Fundamental C/C++ control flow, memory handling, functional decomposition.", skills_val_style),
            Paragraph("<i>Cisco &amp; OpenEDG (2025)</i>", item_meta_style)
        ]
    ]
    t_certs = Table(certs_data, colWidths=[400, 140])
    t_certs.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_certs)

    # Build Document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated {output_pdf_path}")

if __name__ == "__main__":
    build_cv("Asman_Makero_Musa_CMU_Africa_CV.pdf")
    build_cv("assets/Asman_Makero_Musa_CV.pdf")
