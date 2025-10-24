import os
import json
import requests
from datetime import datetime

# Configuration from environment variables
LINKEDIN_ACCESS_TOKEN = os.environ.get('LINKEDIN_ACCESS_TOKEN')
LINKEDIN_PERSON_URN = os.environ.get('LINKEDIN_PERSON_URN')
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')

def generate_post_content():
    """Generate LinkedIn post content using Groq (free tier)"""
    
    # Determine day-specific theme
    day_of_week = datetime.now().strftime('%A')
    day_themes = {
        'Monday': 'Machine Learning Monday',
        'Tuesday': 'AI Tuesday',
        'Wednesday': 'Deep Learning Wednesday',
        'Thursday': 'Analytics Thursday',
        'Friday': 'FinTech Friday',
        'Saturday': 'Data Science Saturday',
        'Sunday': 'Industry Insights Sunday'
    }
    theme = day_themes.get(day_of_week, 'Data Science Insights')
    
    # Rotate post types based on day
    post_types = ['insight/trend', 'breaking news/research', 'tutorial/best practice', 'opinion/strategic perspective']
    day_number = datetime.now().timetuple().tm_yday
    post_type = post_types[day_number % len(post_types)]
    
    # Determine industry focus (60% BFSI, 40% others)
    industry_focus = 'BFSI (Banking, Financial Services, Insurance)' if day_number % 5 < 3 else 'cross-industry (retail, healthcare, manufacturing)'
    
    prompt = f"""Generate a professional LinkedIn post following this EXACT structure:

**Theme for today ({day_of_week})**: {theme}
**Post type**: {post_type}
**Industry focus**: {industry_focus}
**Date**: {datetime.now().strftime('%B %d, %Y')}

STRUCTURE (MUST FOLLOW):

1. **HEADLINE/OPENING LINE** 
   - Start with "{theme}:"
   - Use a strong insight, provocative question, or attention-grabbing statement
   - Must relate to business impact, not just technology

2. **BODY (3-4 paragraphs, each 2-3 sentences)**
   
   Paragraph 1 - CONTEXT:
   - Describe a current business pain point, industry challenge, or recent development
   - Make it relevant to decision-makers
   
   Paragraph 2 - TECHNOLOGY LINK:
   - Explain how ML/AI/Analytics addresses this challenge
   - Focus on capability, not technical details
   - Avoid mathematical jargon
   
   Paragraph 3 - BUSINESS VALUE:
   - Emphasize {industry_focus} applications
   - Quantify outcomes: ROI, risk reduction, efficiency gains, competitive advantage
   - Use concrete examples (real companies if possible, anonymized if needed)
   
   Paragraph 4 - PRACTICAL TAKEAWAY:
   - What should readers do? (evaluate, pilot, invest, rethink strategy)
   - Make it actionable for executives/managers

3. **RESOURCES** (CRITICAL - MUST INCLUDE)
   - Provide 1-2 credible, open-access resources
   - Format: "📚 Resources: [Brief description] - [URL or publication name]"
   - Examples: McKinsey reports, Harvard Business Review, research papers, GitHub repos, industry whitepapers
   - Use real, verifiable sources when possible

4. **HASHTAGS** (5-8 hashtags)
   - Mix of broad (#DataScience #AI #MachineLearning) and niche tags
   - Include industry-specific: #BFSI #BankingAnalytics #FinTech #InsurTech (for BFSI posts)
   - Or #RetailAnalytics #HealthcareAI #Manufacturing (for other industries)

5. **CALL TO ACTION**
   - Encourage engagement: "What's your experience with...?" or "Tag a colleague who..." or "Share your thoughts..."

TONE & STYLE REQUIREMENTS:
- Corporate, consulting-style, polished and professional
- Active voice, short paragraphs (2-3 sentences max)
- Digestible for non-technical decision-makers
- No casual slang, no overly technical math/code
- Clear link between technology and business value
- Use bullet points or numbered lists if they enhance readability

CONTENT RULES:
- Total length: 250-350 words
- Do NOT repeat common topics (vary between ML algorithms, data strategy, AI governance, automation, predictive analytics, etc.)
- Summarize in your own words; never copy-paste copyrighted text
- Include specific, actionable insights

Generate the complete post now, ready to publish."""
    
    headers = {
        'Authorization': f'Bearer {GROQ_API_KEY}',
        'Content-Type': 'application/json'
    }
    
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "system",
                "content": "You are an expert LinkedIn content creator specializing in data science, AI, and ML for business audiences. You write compelling, executive-friendly posts that connect technology to business outcomes. You always include credible resources and follow structured formats precisely."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.8,
        "max_tokens": 800
    }
    
    response = requests.post(
        'https://api.groq.com/openai/v1/chat/completions',
        headers=headers,
        json=data,
        timeout=30
    )
    
    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content'].strip()
    else:
        raise Exception(f"Groq API error: {response.status_code} - {response.text}")

def get_person_urn():
    """Get LinkedIn person URN (user ID) - tries multiple methods"""
    headers = {
        'Authorization': f'Bearer {LINKEDIN_ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    
    # Try method 1: OpenID Connect
    try:
        response = requests.get('https://api.linkedin.com/v2/userinfo', headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json().get('sub')
    except:
        pass
    
    # Try method 2: Legacy /me endpoint
    try:
        response = requests.get('https://api.linkedin.com/v2/me', headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json().get('id')
    except:
        pass
    
    raise Exception("Failed to get Person URN from LinkedIn API")

def post_to_linkedin(content):
    """Post content to LinkedIn"""
    headers = {
        'Authorization': f'Bearer {LINKEDIN_ACCESS_TOKEN}',
        'Content-Type': 'application/json',
        'X-Restli-Protocol-Version': '2.0.0'
    }
    
    # Get person URN - either from env var or fetch it
    person_urn = LINKEDIN_PERSON_URN
    if not person_urn or person_urn == "":
        print("Person URN not provided, fetching automatically...")
        person_urn = get_person_urn()
        print(f"Fetched Person URN: {person_urn}")
    
    post_data = {
        "author": f"urn:li:person:{person_urn}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": content
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
    
    response = requests.post(
        'https://api.linkedin.com/v2/ugcPosts',
        headers=headers,
        json=post_data
    )
    
    return response

def save_post_record(content, status):
    """Save posted content to track history"""
    record = {
        'timestamp': datetime.now().isoformat(),
        'content': content,
        'status': status
    }
    
    # Append to posts.json file
    try:
        with open('posts.json', 'r') as f:
            posts = json.load(f)
    except FileNotFoundError:
        posts = []
    
    posts.append(record)
    
    with open('posts.json', 'w') as f:
        json.dump(posts, f, indent=2)

def main():
    try:
        # Generate content
        print("Generating post content...")
        content = generate_post_content()
        print(f"Generated content:\n{content}\n")
        
        # Post to LinkedIn
        print("Posting to LinkedIn...")
        response = post_to_linkedin(content)
        
        if response.status_code == 201:
            print("✅ Successfully posted to LinkedIn!")
            save_post_record(content, 'success')
        else:
            print(f"❌ Failed to post: {response.status_code}")
            print(f"Response: {response.text}")
            save_post_record(content, f'failed: {response.status_code}')
            exit(1)
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        save_post_record("", f'error: {str(e)}')
        exit(1)

if __name__ == "__main__":
    main()
