# DO NOT USE "pip install secedgar" (if you already did, use "pip uninstall secedgar" to remove)
# DO USE "pip install git+https://github.com/sec-edgar/sec-edgar.git"
# Or read https://sec-edgar.github.io/sec-edgar/install.html
# Downloads are .txt files that contain html code (change ending to .html using rename-files.py to view in browser)

from secedgar import CompanyFilings, FilingType
from datetime import date

ticker = "GILLETTE CO" #make sure to use the ticker or full company name, the name in the excel is sometimes abbreviated
start_date=date(1996, 1, 1),
end_date=date(2005, 12, 1), #add one year, e.g. to get 10K until fiscal year 2014, set to 2015

my_filings = CompanyFilings(cik_lookup=ticker,
                            filing_type=FilingType.FILING_10K,
                            start_date=start_date,
                            end_date=end_date,
                            user_agent='Thimo Merke (thimo.merke@students.uni-mannheim.de)') #Please change

my_filings.save('./') #Change download folder as you like

my_filings = CompanyFilings(cik_lookup=ticker,
                            filing_type=FilingType.FILING_DEF14A,
                            start_date=start_date,
                            end_date=end_date,
                            user_agent='Thimo Merke (thimo.merke@students.uni-mannheim.de)') #Please change

my_filings.save('./') #Change download folder as you like