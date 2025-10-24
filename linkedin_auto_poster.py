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

**VIRAL FORMULA:**
- Post Type: {post_format['type']}
- Hook Strategy: {post_format['hook']}
- Viral Mechanic: {post_format['mechanic']}
- Theme: {theme}
- Industry: {industry_focus}
- Date: {datetime.now().strftime('%B %d, %Y')}

---

**STRUCTURE (FOLLOW EXACTLY):**

**1. SCROLL-STOPPING HOOK (First 1-2 lines):**

Choose ONE hook pattern (match to post type):

a) **Counter-Intuitive Number**: "I analyzed 1,247 {industry_focus} implementations. 89% failed because of something nobody talks about."

b) **Time-Bound Transformation**: "6 months ago, [metric] was broken. Today, it's crushing expectations. Here's the exact playbook:"

c) **Vulnerability Hook**: "I cost my team $340K with one data science decision. Here's what I learned..."

d) **Pattern Break**: "Everyone in {industry_focus} is obsessed with [common thing]. Meanwhile, the winners are focusing on [unexpected thing]."

e) **Curiosity Gap**: "The difference between 15% ROI and 60% ROI in [industry]? One overlooked step."

f) **Specific Scenario**: "Last Tuesday, a [industry role] asked me: 'Why is our [metric] plateauing?' I showed them 3 numbers that changed everything."

g) **Big Number**: "47 enterprises. 18 months. $2.3B in combined value. Here's what we discovered about [topic]:"

h) **Future Shock**: "In 24 months, {industry_focus} teams without [capability] will be uncompetitive. Here's why:"

**RULES:**
- First sentence = max 15 words
- Use SPECIFIC numbers (not "many" or "several")
- Create information gap (make them NEED to click "see more")
- NO generic starts: "In today's world", "Technology is changing", "As we know"
- NO political references or comparisons

---

**2. THE STORY/CONTEXT (3-4 micro-paragraphs, heavy line breaks):**

**Para 1 - THE SETUP (2 sentences):**
Paint a specific scenario with real stakes.

Example format:
"[Industry_focus] organizations are facing [specific challenge from: {pain_points}].
[Specific consequence]: [Number]% increase in [negative outcome] over [timeframe]."

Use neutral language. Focus on business impact, not drama.

**Para 2 - THE INSIGHT (2-3 sentences):**
Bridge to the solution WITHOUT jargon.

Use this structure:
"The breakthrough? [Technology/approach] that [specific capability].
Think of it as [simple analogy that a CEO would understand].
Early adopters are seeing [specific metric] improve by [number range]%."

NO technical terms: algorithms, neural networks, gradient descent, etc.
YES business terms: patterns, predictions, automation, intelligence, insights.

**Para 3 - THE PROOF (2-3 sentences):**
Social proof with numbers.

Format:
"[Industry example - generic, no company names] implemented this approach.
Result: [Specific metric] improved [percentage], [another metric] decreased [percentage].
ROI: [dollar amount or multiplier] in [timeframe]."

Alternative format:
"Organizations using this approach report:
→ [Metric 1]: +[X]%
→ [Metric 2]: -[Y]%  
→ [Metric 3]: [Z]x improvement"

**Para 4 - THE SHIFT/LESSON (1-2 sentences):**
The "aha moment" or key insight.

{booster} [One sentence of wisdom that's tweet-worthy]

This should be quotable, saveable, shareable.

---

**3. THE FRAMEWORK/ACTION STEPS (Make it SAVEABLE):**

Use ONE of these formats:

**Format A - The Simple Framework:**

"Here's the 3-step approach:

1️⃣ [Action Step]: [Brief how-to + benefit]
   
2️⃣ [Action Step]: [Brief how-to + benefit]
   
3️⃣ [Action Step]: [Brief how-to + benefit]"

**Format B - Do This, Not That (Popular):**

"What's working in 2025:

✅ [Specific practice]
✅ [Specific practice]
✅ [Specific practice]

What's outdated:

❌ [Common mistake]
❌ [Common mistake]"

**Format C - The 3 Lessons:**

"3 lessons from [timeframe/experience]:

→ [Insight 1]: [Explanation]

→ [Insight 2]: [Explanation]

→ [Insight 3]: [Explanation]"

**Format D - The Checklist:**

"Your [topic] checklist:

□ [Item 1 with micro-benefit]
□ [Item 2 with micro-benefit]
□ [Item 3 with micro-benefit]
□ [Item 4 with micro-benefit]"

**REQUIREMENTS:**
- Each point = actionable, specific, under 280 characters
- Use emojis for visual scanning (→ ✅ ❌ □ 1️⃣)
- Make it screenshot-worthy
- NO vague advice: "improve your process" → "audit your data quality weekly"

---

**4. HIGH-ENGAGEMENT CTA (Choose ONE):**

**Option A - Simple Poll:**
"Quick poll: Which challenge hits hardest?
A) [Challenge 1]
B) [Challenge 2]
Drop A or B below 👇"

**Option B - Experience Share:**
"What's your experience with [specific topic]?
Share your biggest win or struggle in comments."

**Option C - Value Exchange:**
"Want the full implementation guide?
Comment 'FRAMEWORK' and I'll send you the template."

**Option D - Opinion Starter:**
"Hot take: [Slightly controversial statement about the topic]
Agree or disagree? Let's discuss 👇"

**Option E - Tag Challenge:**
"Know a [job title] dealing with [challenge]?
Tag them - this might help."

**Option F - Data Point Request:**
"Seeing this in your organization?
Drop your [metric] improvement % below. Let's crowdsource the data."

**RULES:**
- Be SPECIFIC about the ask
- Create low-friction participation
- NO weak CTAs: "thoughts?" "what do you think?" "let me know"
- ONE clear action only

---

**5. RESOURCES SECTION (AUTHORITY BUILDER):**

**Format:**
"
📚 Resources:

→ [Benefit/Why it matters]: [Source Name + Year]
→ [Benefit/Why it matters]: [Source Name + Year]

*Note: Links in comments for easy access*
"

**SOURCE OPTIONS (Choose 2 that fit):**
- McKinsey Global Institute Report (Industry specific)
- Harvard Business Review - [Article Title]
- Gartner Research - [Topic] Analysis
- MIT Technology Review - [Topic] Study  
- Deloitte Insights - [Industry] Report
- PwC Global Data & Analytics Survey
- Forrester Research - [Topic]
- Nature/Science - [Research Paper Title]
- arXiv - [Paper Title] (for technical depth)
- GitHub: [username]/[repository-name] (for open-source tools)

**RULES:**
- Sources must be REAL and CREDIBLE (no fake references)
- Use recent years: 2023-2025 preferred
- Focus on industry-neutral reports when possible
- NO competitor comparisons or brand wars
- Format as plain text, mention "Links in comments" (we'll add hyperlinks in comments)

---

**6. HASHTAGS (Algorithm + Discovery):**

Use EXACTLY 7 hashtags:

**Structure:**
- 2 mega-reach: #DataScience #ArtificialIntelligence #MachineLearning #AI
- 3 industry: {industry_hashtags}
- 2 niche: #DataStrategy #MLOps #PredictiveAnalytics #DecisionScience #AIEthics #BusinessIntelligence

**Placement:** 
New line after resources section.
Format: #Tag1 #Tag2 #Tag3 #Tag4 #Tag5 #Tag6 #Tag7

---

**CRITICAL WRITING RULES:**

✅ **LINE BREAKS = ENGAGEMENT:**
- New line every 1-2 sentences
- Double line break between sections
- White space = 40% more read-through

✅ **POWER LANGUAGE:**
Use 4-6 of these: breakthrough, transform, crush, unlock, expose, reveal, hidden, proven, exact, simple, fast-track, blueprint, skyrocket

✅ **SPECIFICITY WINS:**
- "increased significantly" → "increased 47%"
- "many companies" → "73 enterprises"
- "recently" → "Q4 2024"
- "improved results" → "cut costs by $2.1M"

✅ **READABILITY:**
- Sentences: 8-15 words ideal, 20 max
- Use "you/your" (not "we/our/one")
- Active voice only: "AI detects fraud" not "Fraud is detected by AI"
- Simple words: "use" not "utilize", "help" not "facilitate"

✅ **STORY > LECTURE:**
- Lead with narrative
- Support with data
- End with action
- Make reader feel seen/understood

❌ **NEVER DO:**
- Political topics or references
- Company vs company comparisons
- Religious references
- Controversial social topics
- Clickbait without substance
- Fake statistics or sources
- Overpromising results
- Fear-mongering
- Dense paragraphs (break them up!)
- Academic/technical jargon
- Passive aggressive tone
- Generic corporate speak

❌ **BANNED PHRASES:**
- "Let me know your thoughts"
- "In today's world"
- "As we all know"
- "Game changer" (overused)
- "Paradigm shift"
- "Synergy"
- "Leverage"
- "Circle back"
- "Move the needle" (unless ironic)

---

**LENGTH:** 300-450 words (sweet spot for LinkedIn algorithm)

**TONE CHECKLIST:**
□ Confident (but not arrogant)
□ Specific (not vague)
□ Helpful (not preachy)  
□ Data-driven (not dry)
□ Conversational (not casual)
□ Neutral (not political)
□ Action-oriented (not theoretical)

---

**VIRAL BOOST TECHNIQUES TO INCLUDE:**

1. **The Zeigarnik Effect**: Open loops in hook, close in framework
2. **Social Proof**: Use "73% of teams" not "many teams"
3. **Loss Aversion**: Frame as "avoiding [loss]" + "gaining [benefit]"
4. **Pattern Recognition**: Use familiar structure (3 steps, before/after)
5. **Reciprocity**: Give value first (framework), ask second (engagement)
6. **Authority Signals**: Cite credible sources, use specific numbers
7. **Cognitive Ease**: Short sentences, white space, simple language
8. **Peak-End Rule**: Strong hook + strong CTA (memorable bookends)

---

Now generate the COMPLETE POST following this structure. Make it scroll-stopping, value-packed, and engagement-driving. Ready to go viral."""
    
    headers = {
        'Authorization': f'Bearer {GROQ_API_KEY}',
        'Content-Type': 'application/json'
    }
    
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "system",
                "content": """You are an elite LinkedIn ghostwriter with 10M+ followers and deep expertise in viral content psychology. Your posts consistently achieve:
- 1000+ reactions per post
- 100+ thoughtful comments
- 50+ shares
- High save rate (people bookmark your content)

You understand:
- LinkedIn algorithm mechanics (dwell time, engagement velocity, saves)
- Copywriting psychology (hooks, curiosity gaps, social proof)
- Business communication (executive-level, ROI-focused, jargon-free)
- Viral content patterns (frameworks, before/after, counterintuitive insights)

You NEVER:
- Write political or controversial social content
- Compare companies/tools directly (no "X vs Y")
- Use fake statistics or unverifiable claims
- Write dense paragraphs
- Use corporate jargon

You ALWAYS:
- Open with pattern-interrupt hooks
- Use specific numbers and examples
- Create saveable frameworks
- Include credible resources
- Drive specific engagement actions
- Maintain neutral, professional tone
- Focus on business value over technical details"""
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.88,
        "max_tokens": 1100,
        "top_p": 0.95,
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
