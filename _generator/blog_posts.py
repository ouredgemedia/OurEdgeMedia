import re, os
from layout import *

RB = "../"  # root prefix from /blog/

POSTS = [
# ---------------------------------------------------------------------------
{
"slug": "instagram-marketing-gorakhpur-get-more-customers",
"title": "How to Get More Customers from Instagram for Your Gorakhpur Business",
"seo_title": "Instagram Marketing in Gorakhpur: Get More Customers",
"desc": "Posting daily but getting no enquiries? A practical Instagram marketing guide for Gorakhpur shops, cafés, clinics and coaching centres to turn followers into paying customers.",
"excerpt": "Lots of likes, zero enquiries? Here's how Gorakhpur businesses can turn Instagram from a hobby into a steady source of local customers.",
"category": "Social media", "cover": "cover-1", "icon": "fa-brands fa-instagram", "read": 7,
"keywords": "instagram marketing gorakhpur, social media marketing gorakhpur, get customers from instagram, gorakhpur business marketing",
"body": """
<div class="callout problem"><p><strong>The problem:</strong> You post regularly, your friends like everything, but nobody from Gorakhpur actually calls, visits or orders because of Instagram.</p></div>
<p>This is the most common complaint we hear from business owners in Golghar, Civil Lines and Medical College Road. The good news: it's almost never because "Instagram doesn't work in Gorakhpur". It's usually because the account is set up like a personal profile instead of a shop window. Here's how to fix that, step by step.</p>

<h2>1. Make your profile answer "what, where and how" in 3 seconds</h2>
<p>When someone in Gorakhpur lands on your profile, they decide almost instantly whether to follow, message or leave. Your bio must answer three questions:</p>
<ul>
<li><strong>What do you sell?</strong> "Custom bridal lehengas", not "Fashion lover ✨".</li>
<li><strong>Where are you?</strong> Write the locality: "Golghar, Gorakhpur" or "Near Taramandal". Local people search by area.</li>
<li><strong>How do they contact you?</strong> Add a WhatsApp button or link, your phone number and a clear call to action like "DM for price".</li>
</ul>
<p>Switch to a <strong>Business or Creator account</strong> so you can add a contact button, address and category, and see insights.</p>

<h2>2. Post for your customers, not for other businesses</h2>
<p>Many local pages copy what big brands post. But a coaching centre in Betiahata doesn't need cinematic brand films. It needs content that answers what parents and students actually worry about. Use this simple mix every week:</p>
<ul>
<li><strong>Proof:</strong> results, happy customers (with permission), before/after, behind the scenes.</li>
<li><strong>Help:</strong> quick tips that show your expertise, like "3 ways to check pure silver".</li>
<li><strong>Offer:</strong> one clear post or Reel about what you sell, the price range and how to order.</li>
<li><strong>Local:</strong> festivals, Gorakhpur landmarks, local events. People love seeing their own city.</li>
</ul>

<h2>3. Use Reels to reach new people in Gorakhpur</h2>
<p>Static posts mostly reach people who already follow you. <strong>Reels are how new local customers discover you.</strong> Keep them short, start with a strong hook in the first second, add on-screen text (many people watch without sound) and end with a clear next step. If your Reels aren't getting views, read our guide on <a href="reels-not-getting-views-gorakhpur.html">fixing Reels that don't get views</a>.</p>

<h2>4. Tag your location and use local hashtags</h2>
<p>Always tag "Gorakhpur" or your specific area as the location. Mix a few broad tags with local ones, such as #gorakhpur, #gorakhpurfood, #gorakhpurcity, #golghar, plus tags for your niche. Five to ten relevant hashtags beat thirty random ones.</p>

<h2>5. Reply fast. Every DM is a customer.</h2>
<p>A message that waits 6 hours is often a lost sale; the customer has already asked your competitor. Set up quick replies for common questions (price, location, timings) and check messages at fixed times every day. Move serious enquiries to WhatsApp or a call quickly.</p>

<h2>6. Collect reviews and show them</h2>
<p>Gorakhpur is a word-of-mouth city. Ask happy customers to share a Story and tag you, then save those to a "Reviews" Highlight. Pair this with Google reviews. Our <a href="google-maps-ranking-gorakhpur-business.html">Google Maps guide</a> explains how.</p>

<h2>7. Track what actually brings enquiries</h2>
<p>Followers are nice; enquiries pay the rent. Once a month, check which posts brought DMs, profile visits and website clicks. Do more of those, drop what doesn't work. Even a simple notebook tally of "where did you hear about us?" helps.</p>

<h2>When to get professional help</h2>
<p>If you don't have time to plan, shoot, edit and post consistently, that's normal. You're running a business. A local team can handle content calendars, Reel editing, design and reporting for you. Our <a href="../Pricing.html">social media management plans in Gorakhpur</a> start at ₹12,000 per month.</p>
""",
"faqs": [
("How long does Instagram marketing take to show results for a local business?", "Most Gorakhpur businesses see more profile visits and enquiries within 4–8 weeks of consistent posting and quick replies. Strong, steady growth usually takes about 3 months."),
("How often should a small business in Gorakhpur post on Instagram?", "Aim for 3–4 Reels and 2–3 posts per week, plus daily Stories. Consistency matters more than volume."),
("Should I post in Hindi or English?", "Use whatever your customers speak. For most Gorakhpur audiences, Hinglish captions and Hindi voiceovers with English on-screen text work very well."),
],
},
# ---------------------------------------------------------------------------
{
"slug": "reels-not-getting-views-gorakhpur",
"title": "Reels Not Getting Views? 9 Fixes for Gorakhpur Shops, Cafés & Coaching Centres",
"seo_title": "Reels Not Getting Views? 9 Fixes for Gorakhpur Businesses",
"desc": "Stuck at 200 views on every Reel? Nine practical fixes covering hooks, editing, captions, audio and timing that help Gorakhpur businesses get more Reel views and local reach.",
"excerpt": "Stuck at a few hundred views per Reel? These nine editing and posting fixes help local Gorakhpur businesses break out of the low-views loop.",
"category": "Video", "cover": "cover-2", "icon": "fa-solid fa-fire", "read": 6,
"keywords": "reels not getting views, reel editing gorakhpur, how to increase reel views, instagram reels gorakhpur",
"body": """
<div class="callout problem"><p><strong>The problem:</strong> You spend an hour making a Reel, post it, and it stops at 150–300 views. Meanwhile a café down the road gets thousands.</p></div>
<p>Low views almost always come down to the first few seconds, the editing pace, or how the Reel is posted. Here are nine fixes we apply to every Reel we edit for Gorakhpur businesses.</p>

<h2>1. Hook viewers in the first second</h2>
<p>People decide to keep watching or scroll almost immediately. Don't start with your logo or "Hello friends". Start with the most interesting moment: the sizzling dish, the finished product, the result, or a bold line of text like <em>"Gorakhpur's crispiest momos are hiding in Shahpur"</em>.</p>

<h2>2. Keep it short and cut the dead time</h2>
<p>Remove every pause, "umm" and slow walk-in. For most local businesses, 7–20 seconds is plenty. A tighter Reel gets watched to the end more often, and completion helps reach.</p>

<h2>3. Add on-screen text and captions</h2>
<p>Many people watch Reels on mute. Add subtitles and a clear headline on screen. Keep text inside the safe area so the Instagram buttons and caption don't cover it.</p>

<h2>4. Use trending audio, but make it fit</h2>
<p>Trending sounds can help discovery, but only when they match your content. A wedding jeweller using a random meme sound looks odd. Pick trends that fit your brand and adapt them to your product.</p>

<h2>5. Shoot vertical, in good light</h2>
<p>Shoot 9:16 vertical in natural daylight near a window or outside. Clean your phone lens. Steady shots and clear sound matter more than an expensive camera.</p>

<h2>6. Edit to the beat</h2>
<p>Cutting clips on the beat of the music makes a Reel feel professional and keeps energy high. This is where good editing makes the biggest difference, and it's what our <a href="../services.html#reels">Reels editing service</a> focuses on.</p>

<h2>7. Give people a reason to share or save</h2>
<p>Shares and saves signal that a Reel is valuable. Create content people want to send to a friend: "Best places for chai near Gorakhnath Temple", "5 things to check before buying a flat in Gorakhpur", or a quick tip list.</p>

<h2>8. Post when your Gorakhpur audience is online</h2>
<p>Check your Instagram insights for when followers are most active. Many local audiences scroll during lunch and after 7 PM, but your data is what counts. Post consistently, and don't delete and re-upload Reels that start slowly.</p>

<h2>9. Write a caption with a local keyword and a call to action</h2>
<p>Instagram search reads captions. Include what and where, for example "birthday cake in Gorakhpur" or "NEET coaching Gorakhpur", and finish with a clear action: "Order on WhatsApp" or "Save this for later".</p>

<div class="callout"><p><strong>Quick checklist before you post:</strong> hook in 1 second · under 20 seconds · captions on · audio that fits · vertical and well-lit · location tagged · keyword in caption · clear CTA.</p></div>

<h2>Want Reels that work without the hassle?</h2>
<p>Send us your raw clips on WhatsApp and our Gorakhpur editors will turn them into polished, trend-ready Reels, usually within 1–3 days. See samples on our <a href="../Portfolio.html">work page</a>.</p>
""",
"faqs": [
("Why did my Reels views suddenly drop?", "Common reasons are weaker hooks, longer videos, posting inconsistently, or reposting content with watermarks from other apps. Go back to short, hook-first, original Reels and post regularly."),
("Do I need an expensive camera for good Reels?", "No. A recent smartphone, good daylight and clean audio are enough. Editing quality matters far more than the camera."),
("How much does Reel editing cost in Gorakhpur?", "It depends on length and effects. Message us with a reference Reel for an exact quote, or check our monthly plans that include multiple Reels on the pricing page."),
],
},
# ---------------------------------------------------------------------------
{
"slug": "google-maps-ranking-gorakhpur-business",
"title": "Not Showing on Google Maps in Gorakhpur? How to Fix Your Google Business Profile",
"seo_title": "Not on Google Maps in Gorakhpur? Fix Your Business Profile",
"desc": "Customers search \"near me\" but find your competitors? Learn how Gorakhpur businesses can set up and optimise their Google Business Profile to show up on Google Maps and local search.",
"excerpt": "When someone in Gorakhpur searches \"near me\", does your business show up? Here's how to fix your Google Business Profile and win local searches.",
"category": "Local SEO", "cover": "cover-3", "icon": "fa-solid fa-map-location-dot", "read": 7,
"keywords": "local seo gorakhpur, google business profile gorakhpur, google maps ranking gorakhpur, near me search gorakhpur",
"body": """
<div class="callout problem"><p><strong>The problem:</strong> Someone searches "best sweet shop near me" or "dentist in Gorakhpur", and three competitors appear on the map. You don't.</p></div>
<p>Those map results come from <strong>Google Business Profile</strong> (formerly Google My Business). It's free, and for many local businesses in Gorakhpur it brings more calls than any website. Here's how to set it up properly.</p>

<h2>1. Claim and verify your profile</h2>
<p>Search your business name on Google Maps. If a listing exists, claim it; if not, add it. Complete Google's verification. Unverified listings rarely rank well and can be edited by anyone.</p>

<h2>2. Get your name, address and phone exactly right</h2>
<p>Use your real business name (no keyword stuffing like "Best Cafe Gorakhpur Cheap"). Write the full address with locality and landmark, for example <em>"Bank Road, Golghar, near St. Andrew's College, Gorakhpur 273001"</em>, and place the map pin precisely. Use the same name, address and phone on Instagram, Facebook, Justdial and your website. Consistency builds trust with Google.</p>

<h2>3. Choose the right categories</h2>
<p>Your primary category matters most. Pick the most specific one ("Coaching center" rather than "Education"). Add a few relevant secondary categories, but don't add unrelated ones.</p>

<h2>4. Add real photos and videos, often</h2>
<p>Upload your storefront (so people can find you on the street), interior, team, products and work. Short videos work too. Listings with fresh, real photos tend to get more clicks and direction requests than empty ones.</p>

<h2>5. Get more reviews, and reply to all of them</h2>
<p>Reviews are one of the strongest local signals. Ask every happy customer, and make it easy with a QR code at your counter or a review link on WhatsApp. Reply to every review, good or bad, politely and professionally. Never buy fake reviews; Google removes them and can suspend listings.</p>

<h2>6. Write a helpful description and list your services</h2>
<p>In the description, explain what you offer and which areas you serve naturally: "We serve customers across Gorakhpur including Civil Lines, Rapti Nagar and Mohaddipur." Fill in services, products, prices (if possible), opening hours and holiday hours.</p>

<h2>7. Post updates every week</h2>
<p>Use Google Posts for offers, events, new products and festival greetings. It shows Google your business is active and gives searchers a reason to choose you.</p>

<h2>8. Connect your website and social media</h2>
<p>Link a fast, mobile-friendly website with your city and services clearly mentioned. Mention your Google profile on Instagram and ask followers to leave reviews.</p>

<table>
<thead><tr><th>Common mistake</th><th>Fix</th></tr></thead>
<tbody>
<tr><td>Wrong pin location</td><td>Drag the pin to your exact entrance</td></tr>
<tr><td>Different phone numbers online</td><td>Use one primary number everywhere</td></tr>
<tr><td>Only 2–3 photos from years ago</td><td>Add new photos every month</td></tr>
<tr><td>Ignoring negative reviews</td><td>Reply calmly and offer to solve the issue</td></tr>
<tr><td>Keyword-stuffed business name</td><td>Use your real name; put keywords in description</td></tr>
</tbody>
</table>

<h2>Need help with local SEO in Gorakhpur?</h2>
<p>Our SEO specialist can audit and optimise your Google Business Profile, and our designers and editors can create the photos, videos and posts that keep it active. <a href="../about.html#contact">Contact us</a> for a free profile check.</p>
""",
"faqs": [
("Is Google Business Profile free?", "Yes, creating and managing a Google Business Profile is completely free."),
("How long does it take to rank on Google Maps in Gorakhpur?", "After verification and optimisation, many businesses see improvement within a few weeks, but competitive categories can take a few months of steady reviews, photos and posts."),
("Can I rank in areas of Gorakhpur where I don't have a shop?", "Map results depend heavily on the searcher's distance from your address. You can mention service areas, and a strong profile and website help, but you'll rank best near your actual location."),
],
},
# ---------------------------------------------------------------------------
{
"slug": "hire-video-editor-gorakhpur-guide",
"title": "How to Hire a Video Editor in Gorakhpur: Costs, Red Flags & a Checklist",
"seo_title": "How to Hire a Video Editor in Gorakhpur (Costs & Checklist)",
"desc": "Looking for a video editor in Gorakhpur? Compare freelancers vs agencies, understand typical costs, avoid common red flags and use our checklist to hire the right editor.",
"excerpt": "Freelancer or agency? What should it cost? This checklist helps you hire the right video editor in Gorakhpur without wasting money or time.",
"category": "Hiring guide", "cover": "cover-4", "icon": "fa-solid fa-film", "read": 6,
"keywords": "video editor in gorakhpur, best video editor gorakhpur, video editing gorakhpur, hire video editor",
"body": """
<div class="callout problem"><p><strong>The problem:</strong> You hired an editor who seemed cheap, but deadlines slipped, edits came back wrong, and you ended up re-doing everything yourself.</p></div>
<p>Hiring a video editor shouldn't be a gamble. Whether you're a creator, a coaching centre or a showroom in Gorakhpur, use this guide to choose someone reliable.</p>

<h2>Freelancer vs agency: which is right for you?</h2>
<table>
<thead><tr><th></th><th>Freelancer</th><th>Agency</th></tr></thead>
<tbody>
<tr><td>Cost</td><td>Usually lower per video</td><td>Higher, but includes more</td></tr>
<tr><td>Skills</td><td>One person's strengths</td><td>Editors, designers, strategists</td></tr>
<tr><td>Reliability</td><td>Depends on one person</td><td>Backup if someone is unavailable</td></tr>
<tr><td>Best for</td><td>Occasional, simple edits</td><td>Regular content and brand growth</td></tr>
</tbody>
</table>

<h2>What should video editing cost in Gorakhpur?</h2>
<p>Prices vary with length, style and effects. A simple Reel cut costs much less than a motion-graphics ad. As a reference, our single ad videos usually range from <strong>₹999 to ₹4,999</strong>, and monthly plans with multiple Reels, posts and Stories start at <strong>₹12,000</strong>. See full <a href="../Pricing.html">pricing details</a>. Be careful with prices that seem too low; they often mean templates, rushed work or missed deadlines.</p>

<h2>Red flags to watch for</h2>
<ul>
<li><strong>No real portfolio:</strong> only stock samples or other people's work.</li>
<li><strong>No clear revisions policy:</strong> you don't know how many changes are included.</li>
<li><strong>Vague timelines:</strong> "I'll send it soon" instead of a date.</li>
<li><strong>Copyright carelessness:</strong> using music or footage that can get your video muted or removed.</li>
<li><strong>Hard to reach:</strong> slow replies before you've even paid.</li>
</ul>

<h2>Your hiring checklist</h2>
<ol>
<li>Ask for <strong>3–5 samples</strong> similar to what you need (Reels, ads, YouTube).</li>
<li>Share a <strong>reference video</strong> and ask how they'd approach yours.</li>
<li>Confirm <strong>price, delivery time and number of revisions</strong> in writing (WhatsApp is fine).</li>
<li>Ask who handles <strong>captions, music and thumbnails</strong>.</li>
<li>Start with <strong>one paid test video</strong> before committing to a monthly plan.</li>
<li>Check if they can help with <strong>strategy</strong>: hooks, scripts and posting, not just editing.</li>
</ol>

<h2>Why a local Gorakhpur editor helps</h2>
<p>A local team understands your audience's language, festivals and humour, and you can meet face to face when needed. Our office is on Bank Road, Golghar, and you can <a href="../OurTeam.html">meet our editors and designers</a> before you decide.</p>
""",
"faqs": [
("How do I send raw footage to an editor?", "Upload clips to Google Drive and share the link on WhatsApp. Avoid sending through WhatsApp directly because it compresses video quality."),
("How many revisions should be included?", "Most professional editors include 1–2 rounds of revisions. Confirm this before you start."),
("Can one editor handle Reels, ads and YouTube videos?", "Some can, but each style needs different skills. An agency team usually covers all formats with specialists."),
],
},
# ---------------------------------------------------------------------------
{
"slug": "social-media-marketing-cost-gorakhpur",
"title": "Social Media Marketing Cost in Gorakhpur (2026): What Should You Pay?",
"seo_title": "Social Media Marketing Cost in Gorakhpur (2026 Guide)",
"desc": "How much does social media marketing cost in Gorakhpur? A clear breakdown of what's included at ₹12,000, ₹20,000 and ₹30,000 per month, plus how to choose the right package.",
"excerpt": "Confused by social media package prices? Here's what Gorakhpur businesses actually get at different budgets, and how to avoid overpaying.",
"category": "Pricing", "cover": "cover-5", "icon": "fa-solid fa-indian-rupee-sign", "read": 6,
"keywords": "social media marketing cost gorakhpur, social media agency gorakhpur price, digital marketing package gorakhpur, smm price",
"body": """
<div class="callout problem"><p><strong>The problem:</strong> One agency quotes ₹5,000, another ₹40,000, and you have no idea what the difference actually is.</p></div>
<p>Social media pricing feels confusing because packages include very different things. Here's a transparent breakdown so you can compare like for like.</p>

<h2>What you're actually paying for</h2>
<ul>
<li><strong>Content volume:</strong> how many posts, Reels and Stories per month.</li>
<li><strong>Quality:</strong> templates vs custom designs; basic cuts vs premium editing.</li>
<li><strong>Strategy:</strong> research, hooks, scripts and a content calendar.</li>
<li><strong>Management:</strong> posting, captions, hashtags and community replies.</li>
<li><strong>Reporting:</strong> monthly numbers and what to improve.</li>
</ul>
<p>Paid ad budget (money paid to Meta or Google) is almost always <strong>separate</strong> from the agency fee.</p>

<h2>Our packages, explained</h2>
<table>
<thead><tr><th>Plan</th><th>Price / month</th><th>Content</th><th>Best for</th></tr></thead>
<tbody>
<tr><td>Starter</td><td>₹12,000</td><td>10 posts, 8 Reels, 12 Stories</td><td>Small businesses and new brands</td></tr>
<tr><td>Growth</td><td>₹20,000</td><td>10 posts, 10 Reels, 12 Stories + custom designs, premium editing, research</td><td>Growing businesses</td></tr>
<tr><td>Premium</td><td>₹30,000</td><td>15 posts, 15 Reels, 12 Stories + strategy, campaigns, ads guidance</td><td>Established brands</td></tr>
</tbody>
</table>
<p>See every feature side by side on our <a href="../Pricing.html">pricing page</a>.</p>

<h2>How to choose the right budget</h2>
<h3>Choose Starter if…</h3>
<p>You're new to social media, need a consistent, professional presence and mainly want to look trustworthy when customers check your page.</p>
<h3>Choose Growth if…</h3>
<p>You already have some followers and want more enquiries. Better hooks, custom designs and competitor research make a real difference here.</p>
<h3>Choose Premium if…</h3>
<p>You run ads, launch campaigns or have multiple locations, and you need a team thinking about strategy every month.</p>

<h2>Is a very cheap package worth it?</h2>
<p>Very low-cost packages often reuse the same templates for many businesses, skip strategy and post without checking results. If your page looks like everyone else's, customers won't remember you. Ask any agency for samples of work made for businesses like yours.</p>

<h2>Questions to ask before you sign</h2>
<ol>
<li>Exactly how many posts, Reels and Stories do I get?</li>
<li>Are designs custom or template-based?</li>
<li>Who writes captions and replies to comments?</li>
<li>What will the monthly report show?</li>
<li>Is there a lock-in period?</li>
</ol>
<p>Want a quote for your business? <a href="../about.html#contact">Send us your details</a> and we'll recommend the right plan within a day.</p>
""",
"faqs": [
("Does the monthly fee include ad spend?", "No. Ad budget is paid directly to Meta or Google. The agency fee covers planning, content creation and management."),
("Is there a minimum contract period?", "Our plans are month to month, but we recommend at least 3 months to see meaningful growth."),
("Can I get only Reels editing without full management?", "Yes. You can book single videos or a custom editing-only package."),
],
},
# ---------------------------------------------------------------------------
{
"slug": "low-budget-video-ads-gorakhpur",
"title": "Low-Budget Video Ads That Work for Gorakhpur Businesses",
"seo_title": "Low-Budget Video Ads for Gorakhpur Businesses",
"desc": "Spent money on ads with no results? Learn how Gorakhpur businesses can create low-budget video ads that bring real calls and walk-ins, from scripting to locality targeting.",
"excerpt": "Boosted a post and got nothing back? Here's how to make small-budget video ads that bring real calls and walk-ins from across Gorakhpur.",
"category": "Advertising", "cover": "cover-6", "icon": "fa-solid fa-bullhorn", "read": 6,
"keywords": "ad video gorakhpur, video ads for local business, facebook ads gorakhpur, promotional video gorakhpur",
"body": """
<div class="callout problem"><p><strong>The problem:</strong> You pressed "Boost post", spent a few thousand rupees, got some likes, and not a single real customer.</p></div>
<p>Small budgets can work very well in a city like Gorakhpur, because you don't need to reach all of India, just people within a few kilometres of your shop. The secret is the right video and the right targeting.</p>

<h2>1. Start with one clear goal</h2>
<p>Decide what you want people to do: call, send a WhatsApp message, visit your store or book a demo class. Every part of the ad should push toward that one action.</p>

<h2>2. Use a simple, proven ad structure</h2>
<ol>
<li><strong>Hook (0–2s):</strong> call out your customer: "Planning a wedding in Gorakhpur?"</li>
<li><strong>Problem:</strong> the pain they feel: "Tired of overpriced, outdated designs?"</li>
<li><strong>Solution:</strong> show your product or service in action.</li>
<li><strong>Proof:</strong> a happy customer, a result, a number of customers served.</li>
<li><strong>Offer + action:</strong> "Visit us at Golghar this week" or "WhatsApp now for prices".</li>
</ol>

<h2>3. Show real people and real places</h2>
<p>Local audiences trust faces they recognise and places they know. Film your actual shop, team and customers (with permission). A genuine 20-second video often beats a polished stock-footage ad.</p>

<h2>4. Target by distance, not just "Gorakhpur"</h2>
<p>In Meta Ads Manager, target a radius around your location, or specific areas you serve, and choose an age range that matches your buyers. A coaching centre might target parents and students nearby; a café might target a small radius around its outlet.</p>

<h2>5. Make 2–3 versions and let the data decide</h2>
<p>Create a few versions with different hooks or offers and run them with a small budget each. After a few days, put more money into the one bringing the most messages or calls.</p>

<h2>6. Make it easy to respond</h2>
<p>Use "Send WhatsApp message" or "Call now" buttons where possible. Reply instantly. Ads only work if someone answers the enquiries.</p>

<h2>7. Avoid common budget-wasters</h2>
<ul>
<li>Boosting random posts instead of creating proper ads.</li>
<li>Targeting all of India or Uttar Pradesh when customers are local.</li>
<li>Long videos that take 10 seconds to get to the point.</li>
<li>No clear offer or next step.</li>
</ul>

<div class="callout"><p><strong>Tip:</strong> Cut each ad in vertical 9:16 for Reels and Stories and in 1:1 or 4:5 for feeds. One shoot, multiple formats.</p></div>

<h2>Get an ad video made for your business</h2>
<p>Our team scripts, edits and designs ad videos for Gorakhpur businesses, with versions sized for every placement. Single ad videos typically range from ₹999 to ₹4,999. Explore our <a href="../services.html#ad-video">ad video service</a> or <a href="../about.html#contact">ask for a quote</a>.</p>
""",
"faqs": [
("How much should a small Gorakhpur business spend on Facebook or Instagram ads?", "Start small, test a few creatives for a week, then increase spend on the version that brings real enquiries. Your ad budget is separate from the cost of making the video."),
("How long should a video ad be?", "For local businesses, 15–30 seconds usually works best, with the key message in the first 3 seconds."),
("Can I run ads only for people near my shop?", "Yes. Meta Ads lets you target a radius around your address or specific locations, which suits local businesses in Gorakhpur."),
],
},
]

for p in POSTS:
    p.setdefault("date", TODAY)
    p.setdefault("date_display", "21 Nov 2026")

from blog_more import NEW_POSTS
POSTS = NEW_POSTS + POSTS

COVER_IMG = {
    "festival-marketing-calendar-gorakhpur": "graphic-design",
    "restaurant-cafe-marketing-gorakhpur": "shoot",
    "coaching-institute-marketing-gorakhpur": "graphic-design",
    "real-estate-video-marketing-gorakhpur": "shoot",
    "instagram-marketing-gorakhpur-get-more-customers": "social-media",
    "reels-not-getting-views-gorakhpur": "editing",
    "google-maps-ranking-gorakhpur-business": "social-media",
    "hire-video-editor-gorakhpur-guide": "editing",
    "social-media-marketing-cost-gorakhpur": "social-media",
    "low-budget-video-ads-gorakhpur": "shoot",
}
for p in POSTS:
    p["img"] = COVER_IMG.get(p["slug"], "social-media")


def slugify(t):
    t = re.sub(r"<[^>]+>", "", t).lower()
    t = re.sub(r"^\d+\.\s*", "", t)
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:60]


def add_ids(body):
    toc = []
    def rep(m):
        text = m.group(1)
        sid = slugify(text)
        toc.append((sid, re.sub(r"<[^>]+>", "", text)))
        return f'<h2 id="{sid}">{text}</h2>'
    return re.sub(r"<h2>(.*?)</h2>", rep, body), toc


def build_post(p, idx):
    import pages
    body, toc = add_ids(p["body"].strip())
    toc_html = "".join(f'<li><a href="#{i}">{esc(t)}</a></li>' for i, t in toc)
    related = [q for q in POSTS if q is not p][:3]
    rel_cards = "\n".join(pages.post_card(q, RB) for q in related)
    url = f"/blog/{p['slug']}.html"
    article_schema = {
        "@type": "BlogPosting", "@id": BASE + url + "#article", "headline": p["title"], "description": p["desc"],
        "image": BASE + "/assets/images/og-image.jpg", "datePublished": p["date"], "dateModified": p["date"],
        "inLanguage": "en-IN", "articleSection": p["category"], "keywords": p["keywords"],
        "author": {"@type": "Organization", "name": "Our Edge Media", "url": BASE + "/"},
        "publisher": {"@id": ORG_ID}, "mainEntityOfPage": {"@id": BASE + url + "#webpage"},
        "about": {"@type": "Place", "name": "Gorakhpur, Uttar Pradesh"},
    }
    html_body = f"""
<article>
<header class="article-hero">
    <div class="container">
        <ol class="breadcrumb"><li><a href="{RB}">Home</a></li><li><a href="./">Blog</a></li><li aria-current="page">{p['category']}</li></ol>
        <span class="eyebrow">{p['category']}</span>
        <h1>{esc(p['title'])}</h1>
        <p class="lead">{esc(p['desc'])}</p>
        <div class="article-meta">
            <span><i class="fa-regular fa-calendar" aria-hidden="true"></i><time datetime="{p['date']}">{p['date_display']}</time></span>
            <span><i class="fa-regular fa-clock" aria-hidden="true"></i>{p['read']} min read</span>
            <span><i class="fa-regular fa-user" aria-hidden="true"></i>Our Edge Media Team, Gorakhpur</span>
        </div>
    </div>
</header>

<div class="section-tight">
    <div class="container article-wrap">
        <div class="prose">
{body}
            <h2 id="faq">Frequently asked questions</h2>
            {faq_html(p['faqs'])}
        </div>
        <aside class="aside-stack" aria-label="Article tools">
            <nav class="toc" aria-label="Table of contents"><h2>In this article</h2><ol>{toc_html}<li><a href="#faq">FAQs</a></li></ol></nav>
            <div class="aside-cta">
                <h2>Grow your Gorakhpur business</h2>
                <p>Get Reels, ads and social media handled by a local team. Free consultation.</p>
                <a class="btn btn-light" href="{RB}about.html#contact">Get a free quote</a>
                <a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener"><i class="fa-brands fa-whatsapp" aria-hidden="true"></i> WhatsApp us</a>
            </div>
        </aside>
    </div>
</div>
</article>

<section class="section section-alt" aria-labelledby="rel">
    <div class="container">
        <div class="section-head"><span class="eyebrow">Keep reading</span><h2 id="rel">More guides for Gorakhpur businesses</h2></div>
        <div class="post-grid">
            {rel_cards}
        </div>
    </div>
</section>
{cta_band(RB)}
"""
    nxt_post = POSTS[(idx + 1) % len(POSTS)]
    page(next_ch=(f"blog/{nxt_post['slug']}.html", "Next story", nxt_post["title"], nxt_post["category"]),
         file=f"blog/{p['slug']}.html", root=RB, path=url, active="blog/", og_type="article",
         title=p["seo_title"], desc=p["desc"], flush=True,
         crumbs=[("Blog", "/blog/"), (p["title"], url)], body=html_body,
         schema=[article_schema, faq_schema(p["faqs"])],
         extra_head=f'    <meta property="article:published_time" content="{p["date"]}">\n    <meta property="article:section" content="{p["category"]}">\n')


def build_index():
    import pages
    cards = "\n".join(pages.post_card(p, RB) for p in POSTS)
    topics = sorted({p["category"] for p in POSTS})
    chips = "".join(f'<li><i class="fa-solid fa-hashtag" aria-hidden="true"></i>{t}</li>' for t in topics)
    blog_schema = {"@type": "Blog", "@id": BASE + "/blog/#blog", "name": "Our Edge Media Blog",
                   "description": "Marketing, video and local SEO guides for Gorakhpur businesses.",
                   "publisher": {"@id": ORG_ID}, "inLanguage": "en-IN",
                   "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": f"{BASE}/blog/{p['slug']}.html",
                                 "datePublished": p["date"]} for p in POSTS]}
    body = f"""
<section class="page-hero">
    <div class="container">
        <ol class="breadcrumb"><li><a href="{RB}">Home</a></li><li aria-current="page">Blog</li></ol>
        <span class="eyebrow">Blog</span>
        <h1>Marketing guides for Gorakhpur businesses</h1>
        <p>Practical, no-fluff answers to the problems local business owners face online: low Reel views, no enquiries from Instagram, not showing on Google Maps, and more.</p>
        <ul class="chips mt-6" role="list">{chips}</ul>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="post-grid">
            {cards}
        </div>
    </div>
</section>
{cta_band(RB, "Have a marketing problem we haven't covered?", "Ask us on WhatsApp. We'll answer your question for free, and maybe write the next guide about it.")}
"""
    page(file="blog/index.html", root=RB, path="/blog/", active="blog/",
         title="Marketing Blog for Gorakhpur Businesses | Our Edge Media",
         desc="Free guides for Gorakhpur businesses: Instagram marketing, Reels that get views, Google Maps ranking, hiring a video editor, social media pricing and low-budget video ads.",
         crumbs=[("Blog", "/blog/")], body=body, flush=True, schema=[blog_schema])


def build_all():
    os.makedirs("blog", exist_ok=True)
    build_index()
    for i, p in enumerate(POSTS):
        build_post(p, i)
