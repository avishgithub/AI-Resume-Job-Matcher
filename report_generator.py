from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors
from io import BytesIO


def generate_pdf_report(score, skill_results, recommendations):
    buffer = BytesIO()
    document = SimpleDocTemplate(
        buffer,
        pagesize=A4
    )

    styles = getSampleStyleSheet()
    content = []

    content.append(
        Paragraph("AI Resume & Job Matcher", styles["Title"])
    )

    content.append(
        Paragraph("Resume Analysis Report", styles["Heading2"])
    )

    content.append(Spacer(1, 0.3 * inch))

    content.append(
        Paragraph(
            f"Text Similarity: {score}%",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Skill Coverage: {skill_results['coverage']}%",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 0.2 * inch))

    content.append(
        Paragraph("Matched Skills", styles["Heading2"])
    )

    matched = ", ".join(skill_results["matched"]) or "None"

    content.append(
        Paragraph(matched, styles["Normal"])
    )

    content.append(
        Paragraph("Missing Skills", styles["Heading2"])
    )

    missing = ", ".join(skill_results["missing"]) or "None"

    content.append(
        Paragraph(missing, styles["Normal"])
    )

    content.append(
        Paragraph("Additional Resume Skills", styles["Heading2"])
    )

    extra = ", ".join(skill_results["extra"]) or "None"

    content.append(
        Paragraph(extra, styles["Normal"])
    )

    content.append(
        Paragraph("Improvement Recommendations", styles["Heading2"])
    )

    if recommendations:
        for item in recommendations:
            content.append(
                Paragraph(
                    f"<b>{item['skill']}</b>: {item['suggestion']}",
                    styles["Normal"]
                )
            )
            content.append(Spacer(1, 0.1 * inch))

    else:
        content.append(
            Paragraph(
                "No missing skillsidentified.",
                styles["Normal"]
            )
        )

    document.build(content)
    buffer.seek(0)
    return buffer.getvalue()
