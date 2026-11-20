import os
import pymupdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

def build_monochrome_one_page_cv(output_path):
    # A4: 595.27 x 841.89 points
    # Margins: 36pt (0.5 inch) left/right, 32pt top/bottom
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=32,
        bottomMargin=32
    )

    content_width = A4[0] - 72  # 523.27 pt

    styles = getSampleStyleSheet()

    # Monochromatic Jake's Resume Typography Styles
    name_style = ParagraphStyle(
        'Name',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=21,
        alignment=1, # Center
        textColor=colors.HexColor("#000000")
    )

    contact_style = ParagraphStyle(
        'Contact',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        alignment=1, # Center
        textColor=colors.HexColor("#111111")
    )

    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=12,
        textColor=colors.HexColor("#000000"),
        spaceBefore=7,
        spaceAfter=2,
        keepWithNext=True
    )

    item_title = ParagraphStyle(
        'ItemTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11.5,
        textColor=colors.HexColor("#000000")
    )

    item_right = ParagraphStyle(
        'ItemRight',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        alignment=2, # Right
        textColor=colors.HexColor("#222222")
    )

    item_right_bold = ParagraphStyle(
        'ItemRightBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11.5,
        alignment=2, # Right
        textColor=colors.HexColor("#000000")
    )

    item_sub = ParagraphStyle(
        'ItemSub',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor("#222222")
    )

    bullet_style = ParagraphStyle(
        'Bullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor("#111111"),
        leftIndent=10,
        firstLineIndent=-10,
        spaceAfter=1.5
    )

    skill_style = ParagraphStyle(
        'SkillLine',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor("#111111"),
        spaceAfter=1.5
    )

    story = []

    # 1. HEADER
    story.append(Paragraph("ASMAN MAKERO MUSA", name_style))
    story.append(Spacer(1, 2))
    contact_text = (
        "Nairobi, Kenya &nbsp;|&nbsp; "
        "<a href='mailto:makeromusa17@gmail.com'>makeromusa17@gmail.com</a> &nbsp;|&nbsp; "
        "<a href='https://github.com/makeromusa'>github.com/makeromusa</a> &nbsp;|&nbsp; "
        "<a href='https://www.makeromusa.me'>makeromusa.me</a>"
    )
    story.append(Paragraph(contact_text, contact_style))
    story.append(Spacer(1, 3))
    story.append(HRFlowable(width="100%", thickness=0.75, color=colors.HexColor("#000000"), spaceAfter=3))

    # Helper function for section headings with full underline
    def add_section(title):
        story.append(Paragraph(title, section_heading))
        story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#444444"), spaceAfter=3))

    # 2. EDUCATION
    add_section("EDUCATION")
    edu_row = [
        [
            Paragraph("<b>University of Nairobi</b>", item_title),
            Paragraph("Nairobi, Kenya", item_right)
        ],
        [
            Paragraph("<i>Bachelor of Science in Computer Science</i>", item_sub),
            Paragraph("Expected Dec 2029", item_right_bold)
        ]
    ]
    t_edu = Table(edu_row, colWidths=[370, content_width - 370])
    t_edu.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(t_edu)
    story.append(Paragraph("<b>Relevant Coursework:</b> Linear Algebra, Multivariate Calculus, Probability &amp; Statistics, Discrete Mathematics, Data Structures &amp; Algorithms, Database Management Systems, Systems Programming (C/C++).", bullet_style))
    story.append(Spacer(1, 2))

    # 3. PROFESSIONAL EXPERIENCE
    add_section("PROFESSIONAL EXPERIENCE")
    exp_row = [
        [
            Paragraph("<b>Equity Bank Kenya</b> &nbsp;|&nbsp; <i>Equity Leaders Program</i>", item_title),
            Paragraph("Nairobi, Kenya", item_right)
        ],
        [
            Paragraph("<i>Intern – Bancassurance Operations &amp; Customer Service</i>", item_sub),
            Paragraph("Feb 2024 – Jul 2024", item_right)
        ]
    ]
    t_exp = Table(exp_row, colWidths=[380, content_width - 380])
    t_exp.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(t_exp)
    story.append(Paragraph("• Managed high-volume bancassurance agency operations and resolved customer policy inquiries under strict turnaround SLAs.", bullet_style))
    story.append(Paragraph("• Observed firsthand how non-technical users interact with financial workflows, shaping a user-first approach to reliable software design.", bullet_style))
    story.append(Paragraph("• Maintained rigorous document verification, audit readiness, and operational compliance across client financial and credit records.", bullet_style))
    story.append(Spacer(1, 2))

    # 4. TECHNICAL & AI PROJECTS
    add_section("TECHNICAL &amp; AI PROJECTS")

    # Project 1: EduRAG Scholar
    p1_row = [
        [
            Paragraph("<b>EduRAG Scholar</b> &nbsp;|&nbsp; <i>Next.js 15, ChromaDB, Gemini AI, TypeScript, Vercel</i>", item_title),
            Paragraph("<a href='https://learningassistant-chi.vercel.app'>Live Demo</a> &nbsp;|&nbsp; <a href='https://github.com/makeromusa/edurag-scholar'>GitHub</a>", item_right)
        ]
    ]
    t_p1 = Table(p1_row, colWidths=[380, content_width - 380])
    t_p1.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(t_p1)
    story.append(Paragraph("• Engineered an academic Retrieval-Augmented Generation (RAG) platform indexing 7 core University of Nairobi Computer Science units.", bullet_style))
    story.append(Paragraph("• Implemented dense vector embeddings using ChromaDB and cosine similarity retrieval; optimized text-chunk boundaries on complex lecture notes to prevent hallucinated academic proofs and definitions.", bullet_style))
    story.append(Paragraph("• Deployed responsive serverless architecture on Vercel with structured source-attribution citation chips for auditability.", bullet_style))
    story.append(Spacer(1, 2))

    # Project 2: Agentic FPL Manager
    p2_row = [
        [
            Paragraph("<b>Agentic FPL Manager</b> &nbsp;|&nbsp; <i>Next.js 15, Google Gemini 1.5 Pro, PostgreSQL, Supabase</i>", item_title),
            Paragraph("<a href='https://agentic-fpl.vercel.app'>Live Demo</a> &nbsp;|&nbsp; <a href='https://github.com/makeromusa/agentic-fpl'>GitHub</a>", item_right)
        ]
    ]
    t_p2 = Table(p2_row, colWidths=[380, content_width - 380])
    t_p2.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(t_p2)
    story.append(Paragraph("• Developed a multi-agent Fantasy Premier League tactical copilot utilizing Gemini 1.5 Pro with structured JSON schema tool-calling.", bullet_style))
    story.append(Paragraph("• Prevented hallucinated statistics by routing tactical reasoning through deterministic SQL queries against verified PostgreSQL player databases.", bullet_style))
    story.append(Paragraph("• Engineered 5-gameweek transfer horizon and mini-league rival ownership algorithms, balancing retrieval latency (~800ms) with 100% mathematical fidelity.", bullet_style))
    story.append(Spacer(1, 2))

    # Project 3: AzureVibe
    p3_row = [
        [
            Paragraph("<b>AzureVibe</b> &nbsp;|&nbsp; <i>Express.js, Supabase, PostgreSQL, Microsoft Azure (AZ-900), HTML5/CSS3</i>", item_title),
            Paragraph("<a href='https://azurevibe-opj1.vercel.app'>Live Demo</a> &nbsp;|&nbsp; <a href='https://github.com/makeromusa/azurevibe'>GitHub</a>", item_right)
        ]
    ]
    t_p3 = Table(p3_row, colWidths=[380, content_width - 380])
    t_p3.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(t_p3)
    story.append(Paragraph("• Built an AZ-900 exam preparation engine featuring Leitner active-recall flashcards and a domain-weighted scoring model (Concepts, Architecture, Governance) calibrated to Microsoft's 700/1000 threshold.", bullet_style))
    story.append(Paragraph("• Identified and mitigated 'analogy drift' in LLM study tutors by constraining analogies strictly to formal Azure architectural taxonomies.", bullet_style))
    story.append(Spacer(1, 2))

    # 5. TECHNICAL SKILLS & CERTIFICATIONS
    add_section("TECHNICAL SKILLS &amp; CREDENTIALS")
    story.append(Paragraph("<b>Languages:</b> C, C++, Python, TypeScript, SQL, HTML5/CSS3", skill_style))
    story.append(Paragraph("<b>Systems &amp; Databases:</b> Red Hat Enterprise Linux, PostgreSQL (Row-Level Security), Oracle Database, SQL Server, 3NF Modeling", skill_style))
    story.append(Paragraph("<b>AI &amp; Cloud:</b> RAG Pipelines, Dense Vector Embeddings (ChromaDB), LLM Evaluation &amp; Benchmarking, AWS Bedrock, Microsoft Azure (AZ-900), Next.js 15, Vercel", skill_style))
    story.append(Paragraph("<b>Verified Certifications:</b> Microsoft Certified: Azure Fundamentals (AZ-900, ID: B489EE0F3C55EFF8) &nbsp;|&nbsp; Cisco C++ Advanced &nbsp;|&nbsp; Red Hat Linux (RH104)", skill_style))

    doc.build(story)
    print(f"Built CV: {output_path}")

if __name__ == "__main__":
    out_assets = os.path.abspath("assets/Asman_Makero_Musa_CV.pdf")
    out_downloads = os.path.abspath(os.path.expanduser("~/Downloads/Asman_Makero_Musa_CV.pdf"))
    
    build_monochrome_one_page_cv(out_assets)
    build_monochrome_one_page_cv(out_downloads)
    
    # Check page count
    doc = pymupdf.open(out_assets)
    print(f"A4 Page Count: {len(doc)}")
