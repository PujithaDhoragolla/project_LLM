# 📜 PubMed Research Fetcher with GPT-4 Powered Summaries

## 🚀 Project Overview

This project is a powerful Python-based tool that fetches research papers from PubMed based on user-specified queries and uses **OpenAI's GPT-4 (Large Language Model)** to generate summaries for each research paper. Additionally, it identifies authors affiliated with pharmaceutical or biotech companies, extracts their contact information, and saves all this data in a CSV file.

👉 **This project is perfect for researchers, biotech companies, and pharmaceutical firms to analyze industry-related publications quickly.** 💯🚀

---

## 💡 Why Is This Project Special?

✅ **GPT-4 Powered Summaries:** This project uses OpenAI's GPT-4 to generate concise and accurate research paper summaries, making it easier to understand the paper without reading the full text.

✅ **PubMed API Integration:** It utilizes PubMed's E-utilities API to fetch recent research papers based on a query provided by the user.

✅ **Company Affiliation Extraction:** The script identifies authors who are affiliated with pharmaceutical or biotech companies, making it easier to analyze industry influence.

✅ **Corresponding Author Email Extraction:** It attempts to extract the email of the corresponding author if available.

✅ **CSV File Generation:** All extracted information is saved in a CSV file named `papers.csv` for easy reference.

✅ **Command Line Execution:** The project is designed to be run from the command line, allowing users to pass queries dynamically.

---

## ⚙️ How It Works

### ✅ Step 1: Search Research Papers
The user enters a search query like:
```bash
poetry run get-papers-list "Cancer Research"
```
The script will fetch the top **10 most recent papers** related to the search term.

### ✅ Step 2: Identify Company Affiliated Authors
The script then scans the authors and their affiliations to find if any authors belong to **pharmaceutical or biotech companies** like "Pfizer, AstraZeneca, Novartis, etc.".

### ✅ Step 3: Generate GPT-4 Summaries
Using **OpenAI's GPT-4**, the script generates a concise summary for each research paper based on its title and source.

### ✅ Step 4: Save Everything to CSV
The extracted data including:
- **PubMed ID**
- **Title**
- **Publication Date**
- **Non-Academic Author(s)**
- **Company Affiliation(s)**
- **Corresponding Author Email**
- **GPT-4 Summary**

is saved in a CSV file named `papers.csv`.

---

## 📊 CSV Output Example

Here is how your output CSV will look like:

| PubMedID | Title | Publication Date | Non-Academic Author(s) | Company Affiliation(s) | Corresponding Author Email | Summary |
|-----------|-------|-------------------|-----------------------|-----------------------|-----------------------------|---------|
| 12345678  | Cancer Drug X | 2025-03-11        | John Doe             | Pfizer Inc.          | john.doe@pfizer.com        | This paper explores... |
| 23456789  | Vaccine Study | 2025-03-10        | Alice Smith          | AstraZeneca plc      | alice.smith@az.com        | The study presents... |

---

## 🛠 Tech Stack Used

| Technology | Purpose |
|------------|---------|
| **Python 3.10** | Core language for the project. |
| **OpenAI GPT-4 API** | To generate research summaries. |
| **PubMed API (E-Utilities)** | To fetch research papers. |
| **Pandas** | For data processing and CSV generation. |
| **Dotenv** | To manage API keys securely. |

---

## 💻 Prerequisites

Ensure you have the following installed:
- **Python 3.10+**
- **Poetry (for dependency management)**
- **OpenAI API Key** (Get yours from [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys))

---

## 📥 Installation Steps

### ✅ 1. Clone the Repository
```bash
git clone https://github.com/your-username/PubMedResearchFetcher.git
cd PubMedResearchFetcher
```

### ✅ 2. Install Dependencies
```bash
poetry install
```

### ✅ 3. Create a `.env` File
Create a `.env` file in the root folder and add your OpenAI API key:
```
OPENAI_API_KEY=sk-Your-OpenAI-API-Key
```

---

## 🚀 Running the Project

### ✅ 1. Run the Application
```bash
poetry run get-papers-list "Cancer Research"
```

✅ This will generate a `papers.csv` file with detailed information.

### ✅ 2. Open the CSV File
Simply open the `papers.csv` file to view the results.

---

## 📧 Expected Output
A CSV file named **papers.csv** will be generated containing:
- ✅ **PubMed ID**
- ✅ **Title**
- ✅ **Publication Date**
- ✅ **Non-Academic Author(s)**
- ✅ **Company Affiliation(s)**
- ✅ **Corresponding Author Email**
- ✅ **GPT-4 Generated Summary**

---

## 💯 Future Enhancements

✅ **Increase Paper Fetch Limit:** Modify the script to fetch up to 100 or more papers.
✅ **Advanced Email Extraction:** Extract emails more efficiently using NLP.
✅ **Abstract Extraction:** Extract the full abstract for each paper.
✅ **Enhanced Summaries:** Pass the full abstract to GPT-4 for better summaries.

---

## 🤩 Why This Project Is GAME-CHANGING

💯 This project demonstrates a **real-world application of GPT-4** combined with PubMed APIs. By automating:
- ✅ **Paper fetching**
- ✅ **Company author identification**
- ✅ **GPT-4 summarization**
- ✅ **CSV output generation**

👉 **You have created a PROFESSIONAL-GRADE project** that can be showcased in your resume, portfolio, and interview! 🚀😎

---

## 📝 License
This project is licensed under the **MIT License** - feel free to modify and distribute it.

---

