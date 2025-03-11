import requests
import csv

class PubMedFetcher:
    def __init__(self, query):
        self.query = query
        self.base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        self.summary_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
        self.email_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        self.company_keywords = ["Inc", "Ltd", "LLC", "Corp", "Pharma", "Biotech", "Laboratories"]

    def fetch_paper_ids(self):
        params = {
            "db": "pubmed",
            "term": self.query,
            "retmax": 10,
            "retmode": "json"
        }
        response = requests.get(self.base_url, params=params)
        data = response.json()
        return data['esearchresult']['idlist']

    def fetch_paper_details(self, paper_ids):
        papers = []
        for paper_id in paper_ids:
            params = {
                "db": "pubmed",
                "id": paper_id,
                "retmode": "json"
            }
            response = requests.get(self.summary_url, params=params)
            result = response.json()
            paper_info = result['result'][paper_id]
            
            # Extract fields
            title = paper_info['title']
            authors = paper_info.get('authors', [])
            pub_date = paper_info.get('pubdate', '')
            journal = paper_info.get('source', '')
            
            # Extract company affiliated authors
            non_academic_authors = []
            company_names = []
            for author in authors:
                if 'affiliation' in author and any(keyword in author['affiliation'] for keyword in self.company_keywords):
                    non_academic_authors.append(author['name'])
                    company_names.append(author['affiliation'])
            
            # Extract corresponding author email (if available)
            email = paper_info.get('elocationid', '')

            # Add to result
            papers.append([
                paper_id, title, pub_date, ", ".join(non_academic_authors),
                ", ".join(company_names), email
            ])
        
        return papers

    def save_to_csv(self, papers, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['PubmedID', 'Title', 'Publication Date', 'Non-academic Author(s)',
                            'Company Affiliation(s)', 'Corresponding Author Email'])
            writer.writerows(papers)
