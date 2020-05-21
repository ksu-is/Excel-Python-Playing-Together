#find all method for regular expressions
import re
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneRegex

#phoneRegex.findall()
resume = '''Ivy Haddington

Chicago, IL • 
Home:123-456-7891
Cell: 234-555-1212
ihaddington@email.com
SUMMARY

Customer-oriented full sales cycle SMB Account Executive with 3+ years of experience maximizing sales, crushing quotas, and building trusted, loyal relationships with high-profile clients.
EDUCATION
NORTHWEST VERMONT UNIVERSITY
Aug '10 - May '14

Bachelor of Science in Communications
EXPERIENCE
TRADELOT, Account Executive
Jun '16 - Current

    Aggressively hunt and prospect for new business opportunities by making 50+ daily cold calls and following up on leads in order to ensure pipeline sufficiency
    Built and nurtured 20+ strong customer relationships with local businesses within first 6 months, accounting for over $50K in revenue
    Explain complicated software features to senior-level clients through effective product demos conducted in-person, over the phone, and via Skype

CRANE & JENKINS, Account Executive
Current - Current

    Leveraged cold calling and email prospecting (~3,000 emails and ~500 calls monthly) to generate leads
    Consistently performed among top 5% of salespeople in region (out of 150+ account executives) each year
    Exceeded sales goals each quarter - regularly achieving 115%+ quota attainment - while maintaining optimal customer service record
    Increased revenue for Cloudpoint account by 32% and Essence Security account by 38%

SKILLS

    Client relationship management
    Lead generation/qualification
    Product demos
    Needs analysis'''
phoneRegex.search(resume)
print(phoneRegex.search(resume)) 

phoneRegex.findall(resume)
print(phoneRegex.findall(resume)) #find all will find all patterns


phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print(phoneRegex.findall(resume)) #find all will find all patterns with groups

phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
print(phoneRegex.findall(resume)) #find all will find all patterns with groups of groups



