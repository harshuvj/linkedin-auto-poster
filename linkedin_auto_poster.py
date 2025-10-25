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
        {'type': 'contrarian_insight', 'hook': 'what nobody tells you', 'title_style': 'The [Stat]% Truth About [Topic]'},
        {'type': 'transformation_story', 'hook': 'before/after numbers', 'title_style': 'How [Company Type] Saved $[Amount] With [Tech]'},
        {'type': 'mistake_autopsy', 'hook': 'costly failure', 'title_style': 'Why [Stat]% of [Initiatives] Fail (And How to Avoid It)'},
        {'type': 'step_by_step', 'hook': 'exact process', 'title_style': 'The [Number]-Step Framework to [Outcome]'},
        {'type': 'trend_analysis', 'hook': 'emerging shift', 'title_style': '[Stat]% of [Industry] Are Making This Shift'},
        {'type': 'counterintuitive', 'hook': 'opposite of common belief', 'title_style': 'Why [Common Belief] Is Wrong About [Topic]'},
        {'type': 'implementation', 'hook': 'how we built it', 'title_style': 'Inside [Company Type]\'s $[Amount] [Tech] Rollout'},
        {'type': 'data_story', 'hook': 'surprising statistics', 'title_style': '[Stat]% of [Industry] Still Don\'t Know This'},
        {'type': 'problem_solution', 'hook': 'hidden challenge', 'title_style': 'Solving the $[Amount] [Problem] in [Industry]'},
        {'type': 'future_forecast', 'hook': 'next 12 months', 'title_style': 'What [Industry] Will Look Like in [Timeframe]'}
    ]
    day_number = datetime.now().timetuple().tm_yday
    post_format = viral_formats[day_number % len(viral_formats)]
    
    # Industry focus (60% BFSI, 40% others) with neutral positioning
    if day_number % 5 < 3:
        industry_focus = 'BFSI'
        industry_hashtags = '#BFSI #FinTech #BankingAnalytics'
        pain_points = 'fraud detection, risk assessment, customer retention, operational efficiency'
    else:
        industries = [
            ('Retail', '#RetailTech #Ecommerce #CustomerAnalytics', 'inventory optimization, demand forecasting, personalization'),
            ('Healthcare', '#HealthTech #HealthcareAI #MedTech', 'patient outcomes, diagnostic accuracy, operational efficiency'),
            ('Manufacturing', '#Industry40 #SmartManufacturing #IoT', 'predictive maintenance, quality control, yield optimization')
        ]
        industry_focus, industry_hashtags, pain_points = industries[day_number % len(industries)]
    
    # Additional viral mechanics
    engagement_boosters = ['📌 Pro tip:', '⚡ Quick win:', '🎯 Key insight:', '💎 Golden rule:', '🔑 Critical factor:', '⚠️ Watch out:', '✨ Breakthrough:', '🚨 Reality check:']
    booster = engagement_boosters[day_number % len(engagement_boosters)]
    
    prompt = f"""You are an ELITE LinkedIn creator. Write a DATA-RICH, SUBSTANTIVE post with a CATCHY TITLE.

CRITICAL: 
- Post MUST start with a ONE-LINE catchy title
- Title format: "{theme}: [Your Catchy Subtitle]"
- Subtitle should be attention-grabbing and relevant to the post content
- Total post MUST BE UNDER 2800 CHARACTERS (LinkedIn limit is 3000)
- DO NOT include section headers or template labels in the body

Context:
- Theme: {theme}
- Industry: {industry_focus}
- Post Type: {post_format['type']}
- Title Style Inspiration: {post_format['title_style']}
- Pain Points: {pain_points}
- Date: {datetime.now().strftime('%B %d, %Y')}

TITLE EXAMPLES (Choose a style that fits your content):
- "{theme}: Why 68% of Fraud Models Fail (And How to Fix Yours)"
- "{theme}: The $23M Mistake Most Banks Are Making"
- "{theme}: How Regional Banks Are Beating Big Tech at AI"
- "{theme}: The 3-Step Framework That Cut Costs 47%"
- "{theme}: What 247 Implementations Reveal About ROI"
- "{theme}: The Hidden $850B Opportunity in Healthcare Data"

YOUR POST STRUCTURE:

**TITLE LINE (Max 100 characters after theme):**
{theme}: [Create a specific, data-driven, catchy subtitle that hooks the reader]

[Blank line]

**OPENING (1-2 lines with data):**
"New research from [Source] reveals [X]% of {industry_focus} organizations face [challenge]. Here's what top performers do differently."

**CORE CONTENT (3-4 paragraphs):**

Para 1 - Problem with DATA:
"According to [source], the numbers are stark: [stat 1], [stat 2], [stat 3]. For a [typical org size], that's $[amount] annually."

Para 2 - Root Causes:
"Three factors drive this: [reason 1 with brief data], [reason 2 with brief data], [reason 3 with brief data]."

Para 3 - Solution with Impact:
"[Technology/approach] addresses this through [mechanism]. Real implementation data: [Company type] saw [metric 1]: [X]% → [Y]% ([Z]% gain), [metric 2]: saved $[amount], ROI: [multiple]x in [timeframe]."

Para 4 - Practical Steps:
"{booster} [Key insight]

Quick implementation:
→ Phase 1 (Months 1-2): [Action with budget]
→ Phase 2 (Months 3-4): [Action with budget]
→ ROI timeline: [months]"

**ENGAGEMENT:**
"What's your experience? A) [scenario] or B) [scenario]? Drop A or B 👇"

**RESOURCES:**
"📚 Resources:
→ [Benefit]: [Source] (2024) - https://www.mckinsey.com/mgi/our-research
→ [Benefit]: [Source] (2024) - https://www.gartner.com/en/research"

**HASHTAGS:**
"#DataScience #AI {industry_hashtags} #DataStrategy #PredictiveAnalytics"

STRICT REQUIREMENTS:
- Title must be ONE LINE, catchy, professional, data-driven
- MAXIMUM 2800 characters TOTAL (including title)
- 400-450 words MAX
- 6-8 specific statistics
- 3-4 paragraphs only
- Keep resources brief (2 links)
- Short paragraphs (2-3 sentences)
- Line breaks for readability

TITLE GUIDELINES:
- Use specific numbers when possible: "68%", "$23M", "247 cases"
- Create curiosity gap: "Why...", "What...", "How..."
- Show value proposition: benefit or problem solved
- Professional tone, not clickbait
- Max 100 characters after the theme emoji

Write the complete post now, starting with the title. UNDER 2800 CHARACTERS TOTAL."""
    
    headers = {
        'Authorization': f'Bearer {GROQ_API_KEY}',
        'Content-Type': 'application/json'
    }
    
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "system",
                "content": "You are an elite LinkedIn thought leader. Your posts are substantive, data-rich, and educational. You include real statistics, technical depth, strategic insights, and proper hyperlinks. You never write shallow clickbait or include template headers in output."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.82,
        "max_tokens": 850,
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
        
        # CRITICAL: LinkedIn has 3000 character limit
        if len(content) > 2950:
            print(f"⚠️ Content too long ({len(content)} chars), truncating to fit LinkedIn limit...")
            # Truncate intelligently at last complete sentence before 2900 chars
            truncated = content[:2900]
            last_period = truncated.rfind('.')
            last_newline = truncated.rfind('\n')
            cut_point = max(last_period, last_newline)
            if cut_point > 2000:  # Only truncate at sentence if reasonable
                content = content[:cut_point + 1]
            else:
                content = content[:2900] + "..."
            print(f"✂️ Truncated to {len(content)} characters")
        
        # Post-processing: Ensure no political/comparison content
        banned_patterns = [
            'trump', 'biden', 'democrat', 'republican', 'liberal', 'conservative',
            'vs.', ' vs ', 'versus', 'better than', 'worse than', 'compared to'
        ]
        
        content_lower = content.lower()
        for pattern in banned_patterns:
            if pattern in content_lower:
                print(f"⚠️ Detected banned pattern '{pattern}', regenerating...")
                return generate_post_content()
        
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
