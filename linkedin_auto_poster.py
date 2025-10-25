import os
import json
import requests
from datetime import datetime

# Configuration from environment variables
LINKEDIN_ACCESS_TOKEN = os.environ.get('LINKEDIN_ACCESS_TOKEN')
LINKEDIN_PERSON_URN = os.environ.get('LINKEDIN_PERSON_URN')
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')

def generate_post_content():
    """Generate viral LinkedIn post content using advanced engagement strategies"""
    
    # Determine day-specific theme
    day_of_week = datetime.now().strftime('%A')
    day_themes = {
        'Monday': '💡 Machine Learning Monday',
        'Tuesday': '🤖 AI Tuesday',
        'Wednesday': '🧠 Deep Learning Wednesday',
        'Thursday': '📊 Analytics Thursday',
        'Friday': '💰 FinTech Friday',
        'Saturday': '🔬 Data Science Saturday',
        'Sunday': '🌐 Industry Insights Sunday'
    }
    theme = day_themes.get(day_of_week, '🚀 Data Science Insights')
    
    # Advanced post type rotation with viral mechanics
    viral_formats = [
        {'type': 'contrarian_insight', 'hook': 'what nobody tells you', 'mechanic': 'pattern_interrupt'},
        {'type': 'transformation_story', 'hook': 'before/after numbers', 'mechanic': 'social_proof'},
        {'type': 'mistake_autopsy', 'hook': 'costly failure', 'mechanic': 'vulnerability'},
        {'type': 'step_by_step', 'hook': 'exact process', 'mechanic': 'save_worthy'},
        {'type': 'trend_analysis', 'hook': 'emerging shift', 'mechanic': 'curiosity_gap'},
        {'type': 'counterintuitive', 'hook': 'opposite of common belief', 'mechanic': 'debate_driver'},
        {'type': 'implementation', 'hook': 'how we built it', 'mechanic': 'transparency'},
        {'type': 'data_story', 'hook': 'surprising statistics', 'mechanic': 'share_worthy'},
        {'type': 'problem_solution', 'hook': 'hidden challenge', 'mechanic': 'relatability'},
        {'type': 'future_forecast', 'hook': 'next 12 months', 'mechanic': 'forward_looking'}
    ]
    day_number = datetime.now().timetuple().tm_yday
    post_format = viral_formats[day_number % len(viral_formats)]
    
    # Industry focus (60% BFSI, 40% others) with neutral positioning
    if day_number % 5 < 3:
        industry_focus = 'BFSI'
        industry_examples = 'major banks, insurance providers, payment processors, wealth management firms'
        industry_hashtags = '#BFSI #FinTech #BankingAnalytics #InsurTech #FinancialServices'
        pain_points = 'fraud detection, risk assessment, customer retention, operational efficiency, regulatory compliance'
    else:
        industries = [
            ('Retail', 'e-commerce platforms, retail chains, consumer brands', '#RetailTech #Ecommerce #CustomerAnalytics', 'inventory optimization, demand forecasting, personalization, supply chain efficiency'),
            ('Healthcare', 'healthcare providers, pharmaceutical companies, health systems', '#HealthTech #HealthcareAI #MedTech', 'patient outcomes, diagnostic accuracy, operational efficiency, cost reduction'),
            ('Manufacturing', 'manufacturing plants, industrial facilities, production lines', '#Industry40 #SmartManufacturing #IoT', 'predictive maintenance, quality control, yield optimization, downtime reduction')
        ]
        industry_focus, industry_examples, industry_hashtags, pain_points = industries[day_number % len(industries)]
    
    # Additional viral mechanics
    engagement_boosters = [
        '📌 Pro tip:',
        '⚡ Quick win:',
        '🎯 Key insight:',
        '💎 Golden rule:',
        '🔑 Critical factor:',
        '⚠️ Watch out:',
        '✨ Breakthrough:',
        '🚨 Reality check:'
    ]
    booster = engagement_boosters[day_number % len(engagement_boosters)]
    
    prompt = f"""You are an ELITE LinkedIn creator (10M+ followers) creating a VIRAL post. Follow this EXACT structure:


    
    headers = {
        'Authorization': f'Bearer {GROQ_API_KEY}',
        'Content-Type': 'application/json'
    }
    
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "system",
                "content": """You are an elite LinkedIn thought leader and data scientist with deep industry expertise. Your posts are known for:

- SUBSTANTIVE content with real data and insights (not just hooks)
- Educational value that teaches readers something new
- Specific statistics, percentages, and dollar amounts
- Technical depth explained in accessible language
- Strategic perspective on industry trends
- Real-world implementation details and timelines
- Proper citations with actual hyperlinks

You NEVER write:
- Shallow, clickbait-only content
- Posts that are just hooks without substance
- Generic advice without specifics
- Fake or unverifiable statistics
- Political or controversial social content
- Template headers or section labels

Your writing style:
- Professional but conversational
- Data-driven storytelling
- Technical accuracy with business context
- Authoritative without being arrogant
- Informative and genuinely helpful

Readers spend 90-120 seconds on your posts because they contain valuable, actionable insights worth their time."""
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.82,
        "max_tokens": 1400,
        "top_p": 0.92,
        "frequency_penalty": 0.3,
        "presence_penalty": 0.4
    }
    
    response = requests.post(
        'https://api.groq.com/openai/v1/chat/completions',
        headers=headers,
        json=data,
        timeout=30
    )
    
    if response.status_code == 200:
        result = response.json()
        content = result['choices'][0]['message']['content'].strip()
        
        # Post-processing: Ensure no political/comparison content
        banned_patterns = [
            'trump', 'biden', 'democrat', 'republican', 'liberal', 'conservative',
            'vs.', ' vs ', 'versus', 'better than', 'worse than', 'compared to',
            'beats', 'destroys', 'crushes [competitor]'
        ]
        
        content_lower = content.lower()
        for pattern in banned_patterns:
            if pattern in content_lower:
                # Regenerate if problematic content detected
                print(f"⚠️ Detected banned pattern '{pattern}', regenerating...")
                return generate_post_content()  # Recursive retry
        
        return content
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
    
    # If successful, try to add resource links as first comment
    if response.status_code == 201:
        try:
            post_urn = response.headers.get('x-restli-id')
            if post_urn:
                add_resource_comment(post_urn, person_urn, content)
        except Exception as e:
            print(f"Note: Could not add resource comment: {e}")
            # Don't fail the whole post if comment fails
    
    return response

def add_resource_comment(post_urn, person_urn, original_content):
    """Add a comment with resource links to the post"""
    
    # Resource link database
    resource_links = {
        "McKinsey": "https://www.mckinsey.com/mgi/our-research",
        "Harvard Business Review": "https://hbr.org/topic/subject/data-and-analytics",
        "Gartner": "https://www.gartner.com/en/research",
        "Deloitte": "https://www2.deloitte.com/us/en/insights.html",
        "MIT Technology Review": "https://www.technologyreview.com/",
        "PwC": "https://www.pwc.com/gx/en/issues/data-and-analytics.html",
        "Forrester": "https://www.forrester.com/research/",
        "BCG": "https://www.bcg.com/beyond-consulting/bcg-gamma/default",
        "Stanford": "https://hai.stanford.edu/research",
        "Nature": "https://www.nature.com/subjects/machine-learning",
        "arXiv": "https://arxiv.org/list/cs.LG/recent",
        "GitHub": "https://github.com/topics/machine-learning",
        "Kaggle": "https://www.kaggle.com/datasets",
        "Papers with Code": "https://paperswithcode.com/",
        "Google Research": "https://research.google/",
        "Federal Reserve": "https://www.federalreserve.gov/publications.htm",
        "World Bank": "https://www.worldbank.org/en/topic/financialinclusion"
    }
    
    # Extract resource mentions from content
    mentioned_resources = []
    for source_name, url in resource_links.items():
        if source_name.lower() in original_content.lower():
            mentioned_resources.append(f"→ {source_name}: {url}")
    
    # If resources were mentioned, create comment with links
    if mentioned_resources:
        comment_text = "📚 Resource Links:\n\n" + "\n".join(mentioned_resources)
        
        # Add some helpful additional links
        comment_text += "\n\n🔗 More Reading:"
        comment_text += "\n→ AI/ML Papers: https://paperswithcode.com/"
        comment_text += "\n→ Industry Reports: https://www.mckinsey.com/mgi/our-research"
        comment_text += "\n→ Open Datasets: https://www.kaggle.com/datasets"
        
        headers = {
            'Authorization': f'Bearer {LINKEDIN_ACCESS_TOKEN}',
            'Content-Type': 'application/json',
            'X-Restli-Protocol-Version': '2.0.0'
        }
        
        comment_data = {
            "actor": f"urn:li:person:{person_urn}",
            "object": post_urn,
            "message": {
                "text": comment_text
            }
        }
        
        try:
            comment_response = requests.post(
                'https://api.linkedin.com/v2/socialActions/{post_urn}/comments',
                headers=headers,
                json=comment_data,
                timeout=10
            )
            
            if comment_response.status_code == 201:
                print("✅ Added resource links as first comment!")
            else:
                print(f"ℹ️ Could not add comment: {comment_response.status_code}")
        except:
            pass  # Silent fail - comment is optional

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
