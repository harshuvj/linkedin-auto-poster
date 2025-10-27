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
    
    # Verify API key exists
    if not GROQ_API_KEY or GROQ_API_KEY == "":
        raise Exception("GROQ_API_KEY environment variable is not set or empty")
    
    # Debug: Show first/last chars of key (for troubleshooting)
    key_preview = f"{GROQ_API_KEY[:10]}...{GROQ_API_KEY[-10:]}" if len(GROQ_API_KEY) > 20 else "KEY TOO SHORT"
    print(f"Using Groq API key: {key_preview}")
    print(f"Key length: {len(GROQ_API_KEY)} characters")
    
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
    
    prompt = f"""You are an AI/ML professional sharing REAL insights about trends, research, and developments. Write like a smart, friendly person explaining something clearly to another person.

CRITICAL TONE REQUIREMENTS:
- Natural, conversational, engaging - like talking to a colleague
- Sound like a confident human, not a textbook or instruction manual
- Direct and plain-spoken
- Break long sentences into shorter, clearer ones
- Thoughtful but human
- NO robotic or overly formal language
- NO corporate buzzwords or marketing-style expressions
- Total post MUST BE UNDER 2800 CHARACTERS

Context:
- Theme: {theme}
- Industry: {industry_focus}
- Focus: AI, Machine Learning, Deep Learning, Agentic AI, latest developments
- Date: {datetime.now().strftime('%B %d, %Y')}

BANNED PHRASES (Sound robotic/corporate):
❌ "In today's fast-paced world..."
❌ "It is imperative to note that..."
❌ "Leveraging synergies to drive impact..."
❌ "Holistic solutions tailored to..."
❌ "Utilizing cutting-edge technology..."
❌ "Seamless integration..."
❌ "Paradigm shift..."
❌ "Revolutionary breakthrough..."
❌ "Game-changing innovation..."
❌ "Best-in-class solutions..."
❌ "Moving forward..." / "Going forward..."
❌ "At the end of the day..."
❌ "Circle back..."
❌ "Low-hanging fruit..."
❌ "Synergy..."
❌ "Ecosystem..."
❌ "Disruptive..."
❌ Unnecessary semicolons, em dashes, passive voice
❌ Excessive double quotes around normal words

WRITE LIKE THIS INSTEAD:
✅ "New research from Stanford shows..." (not "It has been demonstrated that...")
✅ "This matters because..." (not "The significance of this cannot be overstated...")
✅ "The data is clear..." (not "Data-driven insights reveal that...")
✅ "What makes this interesting..." (not "Of particular note is the fact that...")
✅ "Three things changed..." (not "There are three key factors that...")
✅ "Most teams struggle with..." (not "Organizations face challenges in...")
✅ Active voice: "Researchers found..." (not "It was found by researchers...")
✅ Short, clear sentences (not long, winding explanations)

TITLE FORMAT:
{theme}: [Clear, interesting title - no corporate speak]

Good titles:
- "New Research Shows Why Small Models Beat Large Ones"
- "Agentic AI Just Got a Lot More Practical"
- "The Data Quality Problem Finally Has Numbers"

Bad titles (too corporate):
- "Leveraging AI Innovation for Digital Transformation"
- "Optimizing Enterprise ML Performance at Scale"

POST STRUCTURE:

**TITLE:**
{theme}: [Natural, interesting title]

**OPENING (Hook with real info):**
Start with something interesting, stated simply:
- "New research from Stanford analyzed 800+ ML deployments. The findings are surprising."
- "Something interesting is happening with transformer models."
- "The latest data on AI adoption shows a clear pattern."

Write like you're starting a conversation, not a presentation.

**BODY (3-4 paragraphs - conversational):**

Para 1 - What's happening:
"Recent research from [source] looked at [X] cases. The findings: [stat], [stat], [stat]. What makes this interesting is [why it matters]."

Write simply. No need for "It is noteworthy that..." Just say what happened.

Para 2 - Why it matters:
"This is significant because [clear explanation]. The data shows [findings]. This means [realistic implication]."

Talk like you're explaining to a friend, not writing a report.

Para 3 - Real impact:
"According to [source], teams using this approach see [real outcomes]. For example, [specific finding with numbers]. The key factor is [insight]."

Be direct. No passive voice. No jargon.

Para 4 - Takeaway:
"{booster} [Clear insight]

What the research suggests:
→ [Simple recommendation]
→ [Clear approach]
→ [Realistic expectation]"

Make it actionable. No fluff.

**ENGAGEMENT:**
"What do you think? Is [trend] overhyped or underrated?"

OR

"Curious what others are seeing - how does this match your experience?"

Keep it simple and genuine.

**RESOURCES (CRITICAL - VARY SOURCES):**
"📚 Worth reading:
→ [What it covers]: [Source Name] (2024) - [Specific URL]
→ [Why it's useful]: [Different Source] (2024) - [Different URL]"

**IMPORTANT SOURCE VARIATION RULES:**
1. NEVER use McKinsey or MIT in consecutive posts
2. Mix academic + industry sources (not 2 academic or 2 industry)
3. Rotate between different institutions/companies
4. Use specific report/paper names when possible
5. Match sources to topic (e.g., DeepMind for model research, Gartner for adoption)
6. Include open-source projects when relevant
7. Cite specific arXiv papers with actual titles
8. Reference GitHub repos with star counts

**GOOD SOURCE COMBINATIONS:**
✅ UC Berkeley research + Forrester report
✅ Meta AI paper + GitHub trending repo
✅ DeepMind study + Gartner analysis
✅ arXiv paper (with title) + Hugging Face blog
✅ Carnegie Mellon research + Deloitte insights
✅ Nature publication + Papers with Code benchmark

**AVOID:**
❌ Stanford + McKinsey (every post)
❌ MIT + Gartner (every post)
❌ Same 2-3 sources repeatedly
❌ Generic "research shows" without specific source

**HASHTAGS:**
#DataScience #MachineLearning {industry_hashtags} #AI #DeepLearning

WRITING PRINCIPLES:

✅ SHORT SENTENCES: 
- Break complex ideas into bite-sized pieces
- One idea per sentence when possible
- No run-on sentences with multiple clauses

✅ ACTIVE VOICE:
- "Researchers found" (not "It was found")
- "The data shows" (not "It has been demonstrated")
- "Teams see improvements" (not "Improvements are being seen")

✅ CLEAR LANGUAGE:
- "use" not "utilize"
- "help" not "facilitate"  
- "show" not "demonstrate"
- "change" not "transform"
- "improve" not "optimize"
- Common words over fancy words

✅ CONVERSATIONAL FLOW:
- Write like you're explaining over coffee
- Use transitions naturally: "Here's the thing...", "What's interesting..."
- Ask questions: "Why does this matter?"
- Show enthusiasm naturally: "This is pretty cool..."

✅ NO JARGON UNLESS NECESSARY:
- If you must use technical terms, explain them simply
- "neural networks that recognize patterns" > "deep learning architectures"
- But "transformer models" is fine (it's specific and accurate)

❌ AVOID:
- Semicolons (use periods instead)
- Em dashes for dramatic pauses
- Passive constructions
- Nominalizations ("implementation of" → "implementing")
- Abstract nouns ("utilization" → "using")
- Hedging ("somewhat", "relatively", "quite")
- Corporate speak
- Marketing fluff
- Unnecessary complexity

CONTENT FOCUS (VARY TOPICS - Don't repeat patterns):

**Rotate through these areas:**
- Model architectures (transformers, diffusion, SSMs, Mamba)
- Training techniques (RLHF, DPO, curriculum learning, few-shot)
- Agentic AI (multi-agent, tool use, planning, ReAct)
- Deployment & MLOps (quantization, pruning, distillation, serving)
- Data quality & pipelines (synthetic data, data curation, labeling)
- Real-world applications (specific industry use cases)
- Benchmarks & evaluation (new benchmarks, performance comparisons)
- Ethics & safety (bias, fairness, alignment, interpretability)
- Open source releases (new models, frameworks, libraries)
- Research breakthroughs (new papers, surprising findings)
- Industry adoption (survey data, implementation patterns)
- Cost & efficiency (inference costs, training costs, optimization)
- Emerging techniques (RAG, prompt engineering, fine-tuning methods)
- Multimodal AI (vision-language, audio, video)
- Edge & mobile ML (on-device models, TinyML)

**Topic Selection Rules:**
1. Don't repeat same topic category 2 weeks in a row
2. Balance theoretical (research) vs practical (implementation)
3. Mix optimistic (breakthroughs) with realistic (challenges)
4. Rotate between different sub-fields
5. Include emerging areas, not just mainstream topics
6. Cover both advances and practical problems
7. Address different audience levels (beginners to experts)

SOURCES (Use VARIED, relevant ones - DON'T repeat same sources):

**Academic Institutions (Rotate these):**
- Stanford HAI, MIT CSAIL, Carnegie Mellon, UC Berkeley AI Research
- Oxford Future of Humanity Institute, Cambridge AI Lab
- Toronto Vector Institute, Montreal MILA, ETH Zurich
- Max Planck Institute, Allen Institute for AI

**Tech Company Research (Rotate these):**
- Google Research, DeepMind, Google Brain
- Meta AI Research (FAIR), Microsoft Research
- OpenAI Research, Anthropic Research
- NVIDIA AI Research, IBM Research
- Amazon Science, Apple Machine Learning Research
- Hugging Face Research, Cohere Research

**Industry Reports (Vary these):**
- McKinsey (use sparingly, not every post)
- Gartner, Forrester, IDC
- Deloitte Insights, PwC Research
- Accenture Research, BCG Gamma
- CB Insights, Crunchbase News

**Technical Sources:**
- arXiv papers (specific paper titles)
- Papers with Code (benchmarks)
- NeurIPS, ICML, ICLR, CVPR proceedings
- ACM, IEEE publications
- Journal of Machine Learning Research

**Publications & News:**
- MIT Technology Review, Nature, Science
- The Gradient, Towards Data Science
- VentureBeat AI, The Decoder
- AI Index Report (Stanford)
- State of AI Report (Air Street Capital)

**Open Source & Community:**
- GitHub trending (specific repos)
- Hugging Face Hub (model releases)
- Kaggle Competitions, Google Colab
- TensorFlow, PyTorch blogs
- Fast.ai, distill.pub

**Industry-Specific:**
For {industry_focus}:
- Financial: Federal Reserve research, BIS papers, IMF reports
- Healthcare: NEJM, JAMA, WHO reports, FDA publications  
- Retail: NRF research, eMarketer, Shopify research
- Manufacturing: Industry Week, McKinsey Operations

DYNAMIC SOURCE SELECTION RULES:
1. NEVER use same source 2 posts in a row
2. Match source to topic (academic for research, industry for adoption trends)
3. Use specific paper/report names when possible
4. Include lesser-known but credible sources
5. Cite open-source projects when relevant (with GitHub stars)
6. Use industry-specific sources for industry posts
7. Mix 1 academic + 1 industry source per post
8. Prefer recent sources (2024-2025)

EXAMPLE VARIETY:
Post 1: Stanford HAI + Gartner
Post 2: DeepMind research + arXiv paper
Post 3: UC Berkeley + Forrester
Post 4: Hugging Face release + GitHub repo
Post 5: Meta AI + Nature publication
Post 6: Carnegie Mellon + Deloitte

TONE CHECKLIST:
□ Sounds like a person talking, not a robot
□ Direct and clear
□ Confident but not arrogant
□ Enthusiastic about interesting findings
□ No corporate buzzwords
□ No unnecessary formality
□ No marketing speak
□ Short, readable sentences
□ Active voice throughout
□ Natural word choices

LENGTH: 2400-2700 characters

You are someone who:
- Follows AI/ML research closely
- Gets excited about interesting findings
- Explains things clearly without jargon
- Talks to people, not at them
- Values substance over style
- Writes like they speak

Write the complete post now. Make it clear, natural, and genuinely interesting to read."""
    
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
