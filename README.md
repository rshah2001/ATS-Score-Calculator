### README: Resume Optimizer

---

## 🚀 **Resume Optimizer**

The **Resume Optimizer** is a web application that allows users to upload their resumes, compare them to job descriptions, and receive actionable improvement suggestions to enhance their resumes for specific roles. It includes features such as ATS (Applicant Tracking System) score calculation and tailored recommendations for better job matching.

---

### 🎯 **Features**

- **PDF Resume Upload**: Upload your resume in PDF format for text extraction.
- **Job Description Input**: Paste job descriptions to match your resume to the desired role.
- **ATS Score Calculation**: Analyze the compatibility of your resume with the job description and display an ATS score (out of 100).
- **AI-Powered Suggestions**: Receive AI-driven recommendations to improve your resume based on the job description.
- **Styled Interface**: A visually appealing and easy-to-navigate interface with a custom color palette.

---

### 🛠️ **Installation**

To run the application locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/rshah2001/ATS-Score-Calculator
   cd resume-optimizer
   ```

2. **Install Dependencies**:
   Make sure you have Python installed. Install the required libraries using:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up the OpenAI API Key**:
   - Save your OpenAI API key in a file named `api_key` in the root directory.
   - Alternatively, set it as an environment variable:
     ```bash
     export OPENAI_API_KEY=your_openai_api_key
     ```

4. **Run the Application**:
   Use the following command to launch the app:
   ```bash
   streamlit run app.py
   ```

5. **Access the App**:
   Open your browser and navigate to:
   ```
   http://localhost:8501
   ```

---

### 📂 **File Structure**

```
resume-optimizer/
├── main.py                # Main application file
├── api_key               # File containing the OpenAI API key
├── requirements.txt      # Python dependencies
├── README.md             # This readme file
```

---

### 📑 **How to Use**

1. Launch the app using Streamlit.
2. Upload your resume in PDF format.
3. Paste the job description in the provided text area.
4. Click **"Optimize My Resume"** to:
   - View your current ATS score.
   - Get AI-driven improvement suggestions.
5. Use the recommendations to edit your resume for a better ATS score.

---

### 🔧 **Built With**

- **Streamlit**: Interactive web app framework.
- **OpenAI API**: AI-driven resume recommendations.
- **PyPDF2**: PDF text extraction.
- **FPDF**: For generating tailored resumes (planned feature).

---

### 🛡️ **License**

This project is licensed under the MIT License. Feel free to use, modify, and distribute as per the terms of the license.

---

### 📝 **Acknowledgments**

- [Streamlit Documentation](https://docs.streamlit.io/)
- [OpenAI API](https://platform.openai.com/docs/)
- Inspiration from ATS scoring tools and career coaching practices.

---

If you have any questions or issues, feel free to open an issue in the repository. 🚀
