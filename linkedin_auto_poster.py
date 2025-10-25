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
    
    prompt = f"""You are an AI/ML professional sharing REAL insights about trends, research, and developments in the field. Write naturally and conversationally, but NEVER fabricate personal stories or experiences.

CRITICAL REQUIREMENTS:
- Share REAL research, trends, and developments
- Natural, conversational tone (not robotic corporate speak)
- NO fake personal stories ("I worked with...", "I consulted for...")
- Focus on: recent research findings, industry trends, new techniques, surprising data
- Total post MUST BE UNDER 2800 CHARACTERS

Context:
- Theme: {theme}
- Industry: {industry_focus}
- Focus Areas: AI, Machine Learning, Deep Learning, Agentic AI, latest developments
- Date: {datetime.now().strftime('%B %d, %Y')}

TITLE FORMAT:
{theme}: [Interesting, conversational title about the topic]

Good title examples (informative, not fabricated):
- "New Research on Transformer Models Just Changed Everything"
- "Why LLMs Are Getting Better at Reasoning (MIT Study)"
- "The Agentic AI Pattern Everyone's Talking About"
- "What 500+ ML Papers Reveal About Model Performance"

Bad title examples (fake personal stories):
- "What I Learned Working With 50 Banks"
- "After Consulting 200 Teams, Here's What I Found"

YOUR POST STRUCTURE:

**TITLE:**
{theme}: [Natural, informative title about real development/trend]

**OPENING (Natural hook about real information):**
Start with something interesting you learned/discovered:
- "New research from [Stanford/MIT/Google] just published findings on [topic]..."
- "There's an interesting pattern emerging in [area]..."
- "Recent data from [credible source] shows something surprising about [topic]..."
- "The latest developments in [technology] are worth paying attention to..."

**BODY (3-4 paragraphs - informative and conversational):**

Para 1 - What's happening (real research/trends):
"Recent research from [real source] analyzed [X] cases of [topic]. The findings: [real statistic], [real statistic], [real statistic]. What makes this interesting is [why it matters]."

Para 2 - Why it matters (context and implications):
"Here's why this is significant: [explain the trend/development]. The data shows [real findings from research]. This suggests [realistic implication based on evidence]."

Para 3 - Real-world impact (based on actual studies/data):
"According to [credible source], organizations implementing this approach are seeing [real documented outcomes]. For example, [real published case study or research finding with specific metrics]. The key factor appears to be [evidence-based insight]."

Para 4 - Practical takeaway (based on research, not fake experience):
"{booster} [Interesting insight from the research]

What the research suggests:
→ [Evidence-based recommendation from studies]
→ [Data-backed approach from research]
→ [Timeline/expectation based on documented cases]"

**ENGAGEMENT (Genuine, thoughtful question):**
"What are your thoughts on this development? Have you explored [specific aspect]?"

OR

"Curious what others think - is [trend/development] overhyped or underrated?"

**RESOURCES (Real, specific sources):**
"📚 Worth reading:
→ [Specific paper/report title]: [Source] (2024) - [URL]
→ [Specific study/article]: [Source] (2024) - [URL]

These dive deeper into [specific aspect]."

**HASHTAGS:**
#DataScience #MachineLearning {industry_hashtags} #AI #DeepLearning

WRITING STYLE - NATURAL BUT TRUTHFUL:

✅ DO WRITE LIKE THIS:
- "Recent research from Stanford shows..."
- "There's an interesting pattern in the latest LLM papers..."
- "The data on this is pretty clear..."
- "What makes this development interesting is..."
- "According to the latest benchmarks..."
- "New findings from Google Research..."
- "This trend has been gaining traction..."

❌ DON'T WRITE LIKE THIS:
- "I worked with a team that..." (unless you actually did)
- "Last week, I consulted for..." (fake story)
- "In my experience with 50 companies..." (fabricated)
- "I was surprised to find..." (unless sharing real personal research)
- "One client of mine..." (fake client story)
- Generic corporate speak

CONTENT FOCUS AREAS (Choose 1-2 per post):
- Latest AI/ML research findings (transformer architectures, training techniques)
- Agentic AI developments (AutoGPT, multi-agent systems, tool use)
- Deep learning breakthroughs (vision, NLP, multimodal)
- Industry adoption trends (backed by real surveys/reports)
- Performance benchmarks (real published results)
- New techniques/architectures (papers, open-source projects)
- Ethical considerations (real studies on bias, safety)
- Emerging patterns in production ML (real data from reports)

SOURCES TO REFERENCE (Use real ones):
- Academic: Stanford HAI, MIT CSAIL, Google Research, Meta AI Research
- Industry: McKinsey, Gartner, Forrester reports
- Technical: arXiv papers, Papers with Code benchmarks
- News: MIT Technology Review, Nature, Science
- Open source: GitHub trends, Hugging Face developments

TONE GUIDELINES:
- Conversational but professional
- Enthusiastic about developments (naturally curious)
- Analytical (share what data/research shows)
- Educational (help readers understand)
- Humble (present findings, not opinions as facts)
- Authentic (only share real information)

AVOID:
- Fabricated personal stories
- Made-up client examples
- Fake consulting experience
- Invented statistics
- Exaggerated claims
- Overpromising results
- Corporate jargon

LENGTH: 2400-2700 characters total

Write as someone who:
- Follows AI/ML research closely
- Shares interesting findings they discover
- Explains complex topics clearly
- Stays current with developments
- Values accuracy over sensationalism

Write the complete post now. Make it informative, natural, and TRUTHFUL."""
    
    headers = {
        'Authorization': f'Bearer {GROQ_API_KEY}',
        'Content-Type': 'application/json'
    }
    
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "system",
                "content": "You are an AI/ML professional who shares valuable insights about real research, trends, and developments in the field. You write naturally and conversationally, but you NEVER fabricate personal stories or consulting experiences. You focus on real academic research, industry reports, and documented findings. Your tone is: informative, analytical, curious, and helpful. You present information clearly and help readers understand complex topics. You're knowledgeable but humble, always backing claims with real sources. You write like someone passionate about AI/ML who enjoys sharing interesting discoveries, not like a consultant pitching services or a bot generating content."
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
