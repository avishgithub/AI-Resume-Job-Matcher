from report_generator import generate_pdf_report
from recommendations import generate_recommendations
from skill_matcher import compare_skills
from matcher import calculate_similarity
from skill_extractor import extract_skills
from text_preprocessing import clean_text, tokenize_text
from pypdf import PdfReader
import streamlit as st
st.set_page_config(
    page_title="AI Resume & Job Matcher",
    page_icon="📄",
    layout="wide"
)


st.title("📄 AI Resume & Job Matcher")

st.markdown(
    """
    ### Analyze your resume against a job description.

    Upload your resume, paste the job description,
    and discover your skill gaps and improvement areas.
    """
)

st.divider()

# st.write("Upload your resume to extract its text.")

uploaded_file = st.file_uploader("Upload your Resume (PDF)",
                                 type=["pdf"])

if uploaded_file is not None:

    try:
        reader = PdfReader(uploaded_file)
        extracted_text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                extracted_text += page_text + "\n"

        if extracted_text.strip():
            st.success("Resume text extracted successfully!")

            st.text_area(
                "Extracted Resume Text",
                extracted_text,
                height=300
            )

            cleaned_resume = clean_text(extracted_text)
            tokens = tokenize_text(cleaned_resume)
            st.subheader("Cleaned Resume Text")

            st.text_area(
                "Processed Text",
                cleaned_resume,
                height=250
            )

            resume_skills = extract_skills(cleaned_resume)

            st.subheader("Extracted Techncial skills")

            if resume_skills:
                st.success(f"found {len(resume_skills)} skills")
                st.write(resume_skills)

            else:
                st.warning("No techncial skills found.")

            st.subheader("Resume Tokens")
            st.write(tokens)

            st.subheader("Job Description")
            job_description = st.text_area(
                "Paste the job Description here",
                height=200
            )

            if st.button("Calculate Resume Match"):
                if not job_description.strip():
                    st.warning("Please enter a job descripton.")

                elif len(job_description.strip()) < 30:
                    st.warning("Please enter a more detailed job descripti.on")

                elif not cleaned_resume.strip():
                    st.warning("No readable resume text found.")

                else:
                    cleaned_job = clean_text(job_description)

                    score = calculate_similarity(
                        cleaned_resume,
                        cleaned_job
                    )

                    job_skills = extract_skills(cleaned_job)
                    skill_results = compare_skills(
                        resume_skills,
                        job_skills
                    )

                    st.subheader("Resume Match Result")

                    col1, col2 = st.columns(2)

                    with col1:
                        st.metric(
                            "Text Similarity",
                            f"{score}%"
                        )

                    with col2:
                        st.metric(
                            "Skill Coverage",
                            f"{skill_results['coverage']}%"
                        )

                    st.caption(
                        "Text similarity and skill coverage are separate metrics.")
                    st.progress(
                        min(max(int(skill_results["coverage"]), 0), 100)
                    )

                    st.subheader("Skills Matching Result")

                    tab1, tab2, tab3 = st.tabs([
                        "Skills Overview",
                        "Improvement Suggestions",
                        "Download Report"
                    ])
                    with tab1:

                        st.subheader("Matched Skills")
                        st.write(skill_results["matched"])

                        st.subheader("Missing Skills")
                        st.write(skill_results["missing"])

                        st.subheader("Additional Resume Skills")
                        st.write(skill_results["extra"])

                        st.subheader("Resume Improvement Suggestions")

                        recommendations = generate_recommendations(
                            skill_results["missing"]
                        )

                    with tab2:

                        st.subheader("Resume Improvement Suggestions")

                        if recommendations:

                            for item in recommendations:
                                st.warning(
                                    f"Missing Skill: {item['skill']}"
                                )
                                st.write(item["suggestion"])

                        else:
                            st.success(
                                "Great! No missing skills found."
                            )

                    pdf_report = generate_pdf_report(
                        score,
                        skill_results,
                        recommendations
                    )

                    with tab3:

                        st.subheader("Download Your Report")

                        st.download_button(
                            label="Download Analysis Report",
                            data=pdf_report,
                            file_name="resume_analysis_report.pdf",
                            mime="application/pdf"
                        )

        else:
            st.warning(
                "No readable text found in this PDF."
            )

    except Exception as e:
        st.error(f"Error reading PDF: {e}")
