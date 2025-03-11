import requests
import pandas as pd
from datetime import datetime
import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class PubMedFetcher:
    def __init__(self, query, max_results=10):
        self.query = query
        self.max_results = max_results
        self.base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        self.fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

    def fetch_pubmed_ids(self):
        response = requests.get(
            self.base_url,
            params={
                "db": "pubmed",
                "term": self.query,
                "retmax": self.max_results,
                "retmode": "json"
            }
        )
        response.raise_for_status()
        data = response.json()
        return data["esearchresult"]["idlist"]

    def fetch_details(self, pubmed_ids):
        response = requests.get(
            self.fetch_url,
            params={
                "db": "pubmed",
                "id": ",".join(pubmed_ids),
                "retmode": "json"
            }
        )
        response.raise_for_status()
        return response.json()

    def extract_data(self, details):
        records = []
        for article in details['result'].values():
            if 'uid' not in article:
                continue
            pubmed_id = article.get('uid')
            title = article.get('title')
            pub_date = article.get('pubdate')
            authors = article.get('authors', [])
            company_authors = []

            for author in authors:
                if 'affiliationinfo' in author and author['affiliationinfo']:
                    affiliation = author['affiliationinfo'][0]['affiliation']
                    if any(keyword in affiliation.lower() for keyword in ["pharma", "biotech", "inc.", "ltd"]):
                        company_authors.append({
                            "name": author['name'],
                            "affiliation": affiliation
                        })

            corresponding_author_email = self.get_corresponding_author_email(authors)

            # Fetch summary using GPT-4
            abstract_text = article.get('title') + ' ' + article.get('source')
            summary = self.generate_summary(abstract_text)

            records.append([
                pubmed_id, title, pub_date, 
                ", ".join([a['name'] for a in company_authors]),
                ", ".join([a['affiliation'] for a in company_authors]),
                corresponding_author_email,
                summary
            ])
        return records

    def generate_summary(self, abstract_text):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful research summarizer."},
                    {"role": "user", "content": f"Summarize the following research abstract:\n{abstract_text}"}
                ]
            )
            return response.choices[0].message['content'].strip()
        except Exception as e:
            print(f"GPT-4 Error: {e}")
            return "Summary not available."

    def get_corresponding_author_email(self, authors):
        for author in authors:
            if 'email' in author:
                return author['email']
        return ""

    def save_to_csv(self, records):
        df = pd.DataFrame(records, columns=[
            'PubMedID', 'Title', 'Publication Date', 
            'Non-academic Author(s)', 'Company Affiliation(s)',
            'Corresponding Author Email', 'Summary'
        ])
        df.to_csv('papers.csv', index=False)

    def run(self):
        pubmed_ids = self.fetch_pubmed_ids()
        details = self.fetch_details(pubmed_ids)
        records = self.extract_data(details)
        self.save_to_csv(records)


# ✅ This is the missing main() function
def main():
    query = input("Enter your search query: ")
    fetcher = PubMedFetcher(query)
    fetcher.run()
    print("Data successfully fetched and saved to papers.csv")
