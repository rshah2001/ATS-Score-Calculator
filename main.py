import streamlit as st
from openai import OpenAI
import PyPDF2
import re
from fpdf import FPDF
import os


class ResumeOptimizer:
    def __init__(self):
        # Initialize Streamlit configuration
        st.set_page_config(page_title="Resume Optimizer", page_icon="📄", layout="wide")

        # Custom CSS with your color palette
        st.markdown("""
        <style>
        .highlight-box {
            background-color: #C4CDC1; /* Light background from the palette */
            border-left: 5px solid #658B6F; /* Accent border */
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 5px;
        }
        .improvement-title {
            color: #2F575D; /* Darker green/blue for headings */
            font-weight: bold;
        }
        .metric-title {
            font-size: 1.5em;
            color: #6D9197; /* Soft blue for metric titles */
        }
        .stButton>button {
            background-color: #2F575D; /* Button color */
            color: #DEE1DD; /* Button text color */
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #28363D; /* Darker hover color */
            color: #DEE1DD; /* Keep text consistent */
        }
        body {
            background-color: #DEE1DD; /* Lightest background for the overall app */
            color: #28363D; /* Dark text for readability */
        }
        </style>
        """, unsafe_allow_html=True)

        # Initialize OpenAI Client
        self.client = self._initialize_openai_client()

    def _initialize_openai_client(self):
        """Safely initialize OpenAI client"""
        try:
            api_key = os.getenv('OPENAI_API_KEY') or self._read_api_key()
            return OpenAI(api_key=api_key)
        except Exception as e:
            st.error(f"API Key Error: {e}")
            return None

    def _read_api_key(self):
        """Read API key from file"""
        try:
            with open("api_key", "r") as key_file:
                return key_file.read().strip()
        except FileNotFoundError:
            st.error("API key file not found. Set OPENAI_API_KEY environment variable.")
            return None

    def extract_text_from_pdf(self, pdf_file):
        """Advanced PDF text extraction with error handling"""
        try:
            reader = PyPDF2.PdfReader(pdf_file)
            return ' '.join(page.extract_text() or '' for page in reader.pages)
        except Exception as e:
            st.error(f"PDF Extraction Error: {e}")
            return ''

    def calculate_ats_score(self, resume_text, job_description):
        """Improved ATS score calculation with weighted keywords"""
        job_keywords = set(re.findall(r'\b\w+\b', job_description.lower()))
        resume_keywords = set(re.findall(r'\b\w+\b', resume_text.lower()))

        # Weighted matching
        matches = len(job_keywords.intersection(resume_keywords))
        total_keywords = len(job_keywords)

        # Exponential scoring to reward higher matches
        score = min(int((matches / total_keywords) ** 1.5 * 100), 100)
        return max(score, 0)

    def generate_tailored_improvements(self, resume_text, job_description):
        """Enhanced AI-powered resume improvement suggestions"""
        if not self.client:
            return "OpenAI client not initialized"

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert career coach specializing in resume optimization."
                    },
                    {
                        "role": "user",
                        "content": f"""Analyze this resume and job description:
                        Resume: {resume_text}
                        Job Description: {job_description}
                        Provide 3 strategic, data-driven improvement recommendations."""
                    }
                ],
                max_tokens=300,
                temperature=0.7
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            st.error(f"Improvement Generation Error: {e}")
            return "Unable to generate improvements"

    def run(self):
        """Main Streamlit application flow"""
        st.title("🚀 Resume Optimizer")

        # File and job description upload
        resume_file = st.file_uploader("Upload Resume (PDF)", type=['pdf'])
        job_description = st.text_area("Paste Job Description", height=200)

        if st.button("Optimize My Resume"):
            if resume_file and job_description:
                # Text extraction
                resume_text = self.extract_text_from_pdf(resume_file)

                if not resume_text:
                    st.error("Could not extract text from PDF")
                    return

                # ATS scoring and improvements
                with st.spinner("Optimizing Resume..."):
                    ats_before = self.calculate_ats_score(resume_text, job_description)
                    improvements = self.generate_tailored_improvements(resume_text, job_description)

                    # Display results
                    st.metric("Initial ATS Score", f"{ats_before}%")
                    st.markdown("<div class='highlight-box'>", unsafe_allow_html=True)
                    st.markdown("<h3>🔍 Resume Improvement Recommendations</h3>", unsafe_allow_html=True)

                    for i, point in enumerate(improvements.split('\n'), 1):
                        if point.strip():
                            st.markdown(f"**{i}.** {point.strip()}")

                    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    optimizer = ResumeOptimizer()
    optimizer.run()