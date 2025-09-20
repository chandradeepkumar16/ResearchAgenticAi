import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from newagent import agent

from fpdf import FPDF

def save_to_pdf(text, filename="research_report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in text.split("\n"):
        pdf.multi_cell(0, 10, line)

    pdf.output(filename)

# def save_to_pdf(text, filename="research_report.pdf"):
#     """Save text output into a PDF file."""
#     doc = SimpleDocTemplate(filename)
#     styles = getSampleStyleSheet()
#     story = []

#     for line in text.split("\n"):
#         story.append(Paragraph(line, styles["Normal"]))
#         story.append(Spacer(1, 12))

#     doc.build(story)

# --- Streamlit Interface ---
st.title("🧑‍🔬 Agentic Research Assistant")

topic = st.text_input("Enter research topic:")
if st.button("Generate Report"):
    with st.spinner("Researching... Please wait ⏳"):
        report = agent.run(topic)
    
    st.success("✅ Done! Here's the research report:")
    st.write(report)

    # Download as PDF
    save_to_pdf(report)
    with open("research_report.pdf", "rb") as f:
        st.download_button(
            label="📥 Download Report as PDF",
            data=f,
            file_name="research_report.pdf",
            mime="application/pdf"
        )
