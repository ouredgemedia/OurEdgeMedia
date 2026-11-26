from layout import *
import blog_posts as blog

R = ""  # root prefix for top-level pages

SERVICES = [
    ("reels", "fa-solid fa-fire", "Trending Reels & Shorts",
     "Scroll-stopping Reels and Shorts edited around trending audio, fast hooks and clean captions, built to get watched till the end.",
     ["Trending audio", "Hook-first editing", "Captions & subtitles", "Beat sync"]),
    ("ad-video", "fa-solid fa-bullhorn", "Ad Videos",
     "Advertising videos for Instagram, Facebook and YouTube that explain your offer fast and push people to call, visit or buy.",
     ["Motion graphics", "Product showcase", "Meta & YouTube ads", "Lead-focused CTA"]),
    ("promotion", "fa-solid fa-rocket", "Promotion Videos",
     "Launch films and promo videos for shops, events, offers and new products, so your whole city hears about it.",
     ["Brand awareness", "Product launch", "Offer & event promos", "Social media cut-downs"]),
    ("drop-effect", "fa-solid fa-wand-magic-sparkles", "Drop Effect Reels",
     "Premium cinematic edits with 3D drops, smooth transitions and beat-synced cuts that make a brand look big-budget.",
     ["3D effects", "Drop transitions", "Beat sync", "Colour grading"]),
    ("graphics", "fa-solid fa-pen-nib", "Graphic Design",
     "Posts, carousels, banners and brand identity that look consistent and professional across every platform.",
     ["Instagram posts", "Carousels", "Banners & posters", "Brand identity"]),
    ("smm", "fa-solid fa-chart-line", "Social Media Management",
     "We plan, create, post and report. You get a full monthly content calendar and a team that handles your pages end-to-end.",
     ["Content planning", "Regular posting", "Audience growth", "Monthly reports"]),
]

PLANS = [
    {"tier": "Low range", "name": "Starter", "price": "12,000", "for": "For small businesses and new brands getting started.",
     "qty": ("10", "8", "12"),
     "features": ["Basic content planning", "Template + clean designs", "Basic reel editing", "Caption writing",
                  "Hashtag research", "Monthly content calendar"]},
    {"tier": "Mid range", "name": "Growth", "price": "20,000", "for": "For growing businesses and professional brands.",
     "qty": ("10", "10", "12"), "featured": True,
     "features": ["Custom brand designs", "Premium reel editing", "Better hooks & scripts", "Competitor analysis",
                  "Audience research", "Engagement strategy", "Monthly performance report"]},
    {"tier": "High range", "name": "Premium", "price": "30,000", "for": "For established companies and premium brands.",
     "qty": ("15", "15", "12"),
     "features": ["High-end brand creatives", "Professional strategy", "Advanced video editing", "Brand voice development",
                  "Campaign planning", "Ads guidance", "Detailed monthly report", "Priority support"]},
]

WORK = [
    # (category keys, label, title, text, image (asset name or thumbs/<video>), video or None)
    ("reels", "Food Reel", "Rose Lassi Food Reel", "Hook-first food Reel with on-screen titles and close-up pours.", "thumbs/Trending1", "assets/videos/Trending1.mp4"),
    ("promo", "Promotion", "Automobile Showroom Promo", "Presenter-led promo video for a car showroom, cut for Reels.", "thumbs/Promotion1", "assets/videos/Promotion1.mp4"),
    ("reels", "Drop effect", "Restaurant Drop Effect Reel", "Cinematic drop-effect reveal of a restaurant, outside to inside.", "thumbs/DropEffect1", "assets/videos/DropEffect1.mp4"),
    ("ads", "Ad video", "Restaurant Ad Shoot", "Behind the scenes of an ad shoot at a restaurant, filmed and edited by our team.", "shoot", None),
    ("promo", "Promotion", "Showroom Walkthrough Promo", "Walkthrough promo that takes viewers inside a new store.", "thumbs/Promotion2", "assets/videos/Promotion2.mp4"),
    ("reels", "Drop effect", "Cinematic Store Reveal", "3D drop effect reveal for a store launch.", "thumbs/DropEffect2", "assets/videos/DropEffect2.mp4"),
    ("design", "Graphic design", "Brand Identity & Graphics", "Grand opening creatives and brand designs made in Photoshop by our designers.", "graphic-design", None),
    ("reels", "Food Reel", "Masala Dosa Food Reel", "Sizzling, close-up food Reel for a hotel restaurant.", "thumbs/Trending2", "assets/videos/Trending2.mp4"),
    ("smm", "Social media", "Social Media Campaign", "Content planning, editing, posting and performance tracking for brand pages.", "social-media", None),
    ("promo", "Promotion", "Boutique Brand Promo", "Presenter-led brand promo for a fashion boutique.", "thumbs/Promotion3", "assets/videos/Promotion3.mp4"),
    ("reels", "Drop effect", "Hotel Drop Effect Reel", "Beat-synced hotel promo with cinematic drops and colour.", "thumbs/DropEffect3", "assets/videos/DropEffect3.mp4"),
]
IMG_SIZE = {"editing": (1400, 933), "graphic-design": (1400, 933), "shoot": (1400, 933), "social-media": (1400, 933),
            **{"thumbs/" + v: (540, 960) for v in ["Trending1", "Trending2", "Promotion1", "Promotion2", "Promotion3", "DropEffect1", "DropEffect2", "DropEffect3"]}}

LOCALITIES = ["Golghar", "Bank Road", "Civil Lines", "Medical College Road", "Taramandal", "Rapti Nagar", "Mohaddipur",
              "Shahpur", "Betiahata", "Gorakhnath", "Asuran", "Jangal Kauria", "GIDA", "Padri Bazar"]
INDUSTRIES = [("fa-solid fa-utensils", "Restaurants & cafés"), ("fa-solid fa-graduation-cap", "Coaching institutes"),
              ("fa-solid fa-stethoscope", "Clinics & hospitals"), ("fa-solid fa-building", "Real estate"),
              ("fa-solid fa-shirt", "Boutiques & fashion"), ("fa-solid fa-dumbbell", "Gyms & fitness"),
              ("fa-solid fa-ring", "Jewellers"), ("fa-solid fa-store", "Retail & showrooms")]


THUMB_AT = {"Trending2.mp4": 13}  # seconds; best-looking frame per video (default 1.5s)


def video_thumb(video, label, root=""):
    """The video file itself is the thumbnail: lazy-loaded, muted, paused on a chosen frame."""
    t = THUMB_AT.get(video.split("/")[-1], 1.5)
    return (f'<video class="vthumb" data-src="{root}{video}#t={t}" muted playsinline preload="none" '
            f'width="720" height="1280" aria-label="{esc(label)} (preview)" tabindex="-1"></video>')


def work_card(w, lazy=True):
    cat, label, title, text, img, video = w
    if video:
        media = video_thumb(video, title, R)
    else:
        wd, ht = IMG_SIZE[img]
        media = f'<img src="{R}assets/images/{img}.webp" alt="{esc(title)} by Our Edge Media" width="{wd}" height="{ht}" loading="lazy" decoding="async">'
    if video:
        media += (f'<button class="work-play" type="button" data-video="{R}{video}" aria-label="Play video: {esc(title)}">'
                  f'<span><i class="fa-solid fa-play" aria-hidden="true"></i></span></button>')
    return f"""<article class="work-card reveal" data-cat="{cat}">
                <div class="work-media">{media}</div>
                <div class="work-body"><span class="cat">{label}</span><h3>{esc(title)}</h3><p>{esc(text)}</p></div>
            </article>"""


VIDEO_MODAL = """
<div class="modal" id="videoModal" role="dialog" aria-modal="true" aria-label="Project video">
    <div class="modal-box">
        <button class="modal-close" type="button" aria-label="Close video"><i class="fa-solid fa-xmark" aria-hidden="true"></i></button>
        <video controls playsinline preload="none"></video>
    </div>
</div>"""


def post_card(p, root):
    return f"""<a class="post-card reveal" href="{root}blog/{p['slug']}.html">
                <div class="post-cover {p['cover']}"><img src="{root}assets/images/{p['img']}.webp" alt="" width="{IMG_SIZE[p['img']][0]}" height="{IMG_SIZE[p['img']][1]}" loading="lazy" decoding="async"><i class="{p['icon']}" aria-hidden="true"></i><span>{p['category']}</span></div>
                <div class="post-body">
                    <div class="post-meta"><span>{p['date_display']}</span><span>{p['read']} min read</span></div>
                    <h3>{esc(p['title'])}</h3>
                    <p>{esc(p['excerpt'])}</p>
                    <span class="more">Read article <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></span>
                </div>
            </a>"""


# =====================================================================
# HOME
# =====================================================================
HOME_FAQ = [
    ("Which is the best video editing agency in Gorakhpur?",
     "The best agency is one that understands local customers and edits for results, not just effects. Our Edge Media is a Gorakhpur-based team of 9 specialists (video editors, designers, an SEO specialist and social media managers) working from Bank Road, Golghar. You can watch our Reels, ad videos and promo films on our <a href=\"Portfolio.html\">work page</a> before you decide."),
    ("How much does social media marketing cost in Gorakhpur?",
     "Our monthly social media management plans are ₹12,000 (Starter), ₹20,000 (Growth) and ₹30,000 (Premium), covering posts, Reels, Stories, design and planning. One-off ad videos usually cost ₹999–₹4,999 depending on length and effects. See the full breakdown on our <a href=\"Pricing.html\">pricing page</a>."),
    ("Do you offer Instagram Reels editing in Gorakhpur?",
     "Yes. Reels and Shorts editing is our most-requested service: hook-first cuts, trending audio, captions, beat-synced transitions and drop effects. Learn more about our <a href=\"reels-editing-gorakhpur.html\">Reels editing service</a>."),
    ("Can you help my business rank on Google Maps in Gorakhpur?",
     "Yes. Our SEO specialist optimises Google Business Profiles, local citations and on-page SEO so you show up for \"near me\" and \"in Gorakhpur\" searches. See our <a href=\"local-seo-gorakhpur.html\">local SEO service</a>."),
    ("Do you only work with businesses in Gorakhpur?",
     "No. We're proudly based in Gorakhpur and work with brands from Golghar to GIDA, but we also edit for creators and businesses across Uttar Pradesh and India. Everything can be handled over WhatsApp, calls and Google Drive."),
    ("How fast can you deliver a Reel or ad video?",
     "Most edits are delivered within 1–3 days depending on length and complexity. Monthly clients get a fixed content calendar so posts go out on time, every time."),
    ("Do I need to shoot the videos myself?",
     "Not necessarily. Many clients send phone footage and we guide them on what to shoot. For bigger projects we can plan shoots and scripts with you. Good editing turns simple phone clips into professional content."),
    ("Can I visit your office in Gorakhpur?",
     "Yes. Our office is on Bank Road, Golghar, near St. Andrew's College, open Monday to Saturday, 10 AM to 8 PM. Message us on WhatsApp first so the right person is available to meet you."),
]

LINK_TEXT = {"reels": "Reels editing", "ad-video": "Ad video production", "promotion": "Promo videos",
             "drop-effect": "Video editing", "graphics": "Graphic design", "smm": "Social media marketing"}

SERVICE_LANDING = {"reels": "reels-editing-gorakhpur.html", "ad-video": "ad-video-production-gorakhpur.html",
                   "promotion": "ad-video-production-gorakhpur.html", "drop-effect": "video-editing-services-gorakhpur.html",
                   "graphics": "graphic-design-gorakhpur.html", "smm": "social-media-marketing-gorakhpur.html"}

INDUSTRY_DETAIL = [
    ("fa-solid fa-utensils", "Restaurants & cafés", "Mouth-watering food Reels, menu designs and offer promos that fill tables on weekends."),
    ("fa-solid fa-graduation-cap", "Coaching institutes", "Admission campaigns, result videos and faculty intros that build parents' trust."),
    ("fa-solid fa-stethoscope", "Clinics & hospitals", "Doctor explainer videos, health tips and Google Maps visibility for local patients."),
    ("fa-solid fa-building", "Real estate", "Property walkthrough videos and project ads for plots and flats across Gorakhpur."),
    ("fa-solid fa-shirt", "Boutiques & fashion", "New-arrival Reels, try-on videos and festive collection launches."),
    ("fa-solid fa-dumbbell", "Gyms & fitness", "Transformation stories, trainer Reels and membership offer ads."),
    ("fa-solid fa-ring", "Jewellers", "Premium product films and wedding-season campaigns with a luxury feel."),
    ("fa-solid fa-store", "Retail & showrooms", "Product showcases, sale promos and launch videos that drive walk-ins."),
]

MARQUEE_WORDS = ["Video Editing in Gorakhpur", "Instagram Reels Editing", "Social Media Marketing", "Ad Film Production",
                 "Graphic Design", "Local SEO", "YouTube Video Editing", "Brand Promotion Videos"]


def marquee(dark=False, speed=40):
    items = "".join(f'<span class="{"o" if i % 2 else ""}">{w}</span>' for i, w in enumerate(MARQUEE_WORDS))
    return f"""<div class="marquee{' dark' if dark else ''}" aria-hidden="true">
    <div class="marquee-track" data-speed="{speed}">{items}{items}</div>
</div>"""


def build_home():
    services = "\n".join(f"""<article class="card card-hover service-card reveal" id="home-{sid}">
                <span class="num" aria-hidden="true">0{i + 1}</span>
                <div class="ic"><i class="{ic}" aria-hidden="true"></i></div>
                <h3>{t}</h3>
                <p>{d}</p>
                <a class="btn btn-ghost" href="{SERVICE_LANDING[sid]}">{LINK_TEXT[sid]} in Gorakhpur <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
            </article>""" for i, (sid, ic, t, d, _) in enumerate(SERVICES))
    work = "\n".join(work_card(w) for w in WORK[:6])
    plans = "\n".join(f"""<div class="card card-hover reveal" style="{'border:2px solid var(--primary)' if p.get('featured') else ''}">
                <span class="plan-tier">{p['tier']}</span>
                <h3 style="font-size:1.35rem;margin-top:4px">{p['name']}</h3>
                <p class="plan-price" style="margin:12px 0 6px"><strong style="font-size:2rem">₹{p['price']}</strong><span>/ month</span></p>
                <p>{p['qty'][0]} posts · {p['qty'][1]} Reels · {p['qty'][2]} Stories</p>
            </div>""" for p in PLANS)
    posts = "\n".join(post_card(p, R) for p in blog.POSTS[:3])
    chips = "".join(f'<li><i class="fa-solid fa-location-dot" aria-hidden="true"></i>{l}</li>' for l in LOCALITIES)
    inds = "".join(f'<article class="industry reveal"><i class="{i}" aria-hidden="true"></i><h3>{t}</h3><p>{d}</p></article>' for i, t, d in INDUSTRY_DETAIL)

    body = f"""
<section class="hero">
    <div class="container hero-grid">
        <div>
            <p class="hero-badge"><span>Gorakhpur</span> Video editing &amp; social media agency</p>
            <h1>Reels, ads &amp; content that <span class="hl">grow</span> your Gorakhpur business</h1>
            <p class="hero-lead">Our Edge Media is a <strong>video editing and social media marketing agency in Gorakhpur</strong>. We edit high-retention Reels, ad videos and promo films, design your graphics and run your social media, so more people find you, trust you and buy from you.</p>
            <div class="hero-actions">
                <a class="btn btn-primary" href="about.html#contact">Get a free quote <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
                <a class="btn btn-outline" href="Portfolio.html"><i class="fa-regular fa-circle-play" aria-hidden="true"></i> See our work</a>
            </div>
            <div class="hero-proof">
                <div><strong data-count="500" data-suffix="+">500+</strong><span>Projects delivered</span></div>
                <div><strong data-count="300" data-suffix="+">300+</strong><span>Happy clients</span></div>
                <div><strong data-count="5" data-suffix="+ yrs">5+ yrs</strong><span>Experience</span></div>
            </div>
        </div>
        <div class="hero-visual">
            <figure class="hv-a"><img src="assets/images/editing.webp" alt="Video editor at work in the Our Edge Media studio, Gorakhpur" width="1400" height="933" fetchpriority="high" decoding="async"></figure>
            <figure class="hv-b"><img src="assets/images/shoot.webp" alt="Our Edge Media crew filming a restaurant video shoot" width="1400" height="933" decoding="async"></figure>
            <figure class="hv-c"><img src="assets/images/graphic-design.webp" alt="Graphic designer creating a grand opening poster" width="1400" height="933" decoding="async"></figure>
            <div class="hero-chip"><span class="ic"><i class="fa-solid fa-bolt" aria-hidden="true"></i></span><div><b>1–3 day delivery</b><small>on most edits</small></div></div>
        </div>
    </div>
</section>

{marquee()}

<section class="section" aria-label="What we believe">
    <div class="container">
        <p class="statement">We help Gorakhpur businesses turn <span class="hl-blue">scrollers into customers</span> with content people actually stop, watch and share.</p>
    </div>
</section>

<section class="section section-alt" aria-labelledby="svc-title">
    <div class="container">
        <div class="section-head reveal">
            <span class="eyebrow">What we do</span>
            <h2 id="svc-title">Video editing &amp; social media services in Gorakhpur</h2>
            <p>One local team for video editing, design and social media marketing, so your content looks consistent everywhere and actually brings in enquiries.</p>
        </div>
        <div class="grid grid-3">
            {services}
        </div>
    </div>
</section>

<section class="section" aria-labelledby="reel-title">
    <div class="container">
        <div class="showreel reveal">
            <div class="showreel-copy">
                <span class="eyebrow">Showreel</span>
                <h2 id="reel-title">See what great editing does for a local brand</h2>
                <p>From a car showroom to a rose lassi, watch how we turn simple footage into scroll-stopping content for Gorakhpur businesses.</p>
                <div class="stack-actions mt-6">
                    <a class="btn btn-light" href="Portfolio.html">View full portfolio <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
                </div>
            </div>
            <div class="showreel-media">
                {video_thumb("assets/videos/Promotion1.mp4", "Automobile showroom promo by Our Edge Media")}
                <button class="work-play" type="button" data-video="assets/videos/Promotion1.mp4" aria-label="Play showreel video"><span><i class="fa-solid fa-play" aria-hidden="true"></i></span></button>
            </div>
        </div>
    </div>
</section>

<section class="section section-alt" aria-labelledby="why-title">
    <div class="container split">
        <div class="split-sticky reveal">
            <span class="eyebrow">Why Our Edge Media</span>
            <h2 id="why-title">A Gorakhpur team that edits for results, not just looks</h2>
            <p class="lead mt-4">Pretty videos don't pay bills. We plan every edit around one goal: getting the right local audience to stop scrolling and take action, whether that's a call, a WhatsApp message or a visit to your shop.</p>
            <div class="stack-actions mt-8">
                <a class="btn btn-primary" href="about.html">About our agency</a>
                <a class="btn btn-outline" href="OurTeam.html">Meet the team</a>
            </div>
        </div>
        <ul class="feature-list" role="list">
            <li class="reveal"><span class="ic"><i class="fa-solid fa-bolt" aria-hidden="true"></i></span><div><h3>Fast delivery</h3><p>Quick turnaround so you never miss a trend, festival or offer.</p></div></li>
            <li class="reveal"><span class="ic"><i class="fa-solid fa-film" aria-hidden="true"></i></span><div><h3>Premium editing</h3><p>Cinematic Reels, smooth transitions, motion graphics and viral-style cuts.</p></div></li>
            <li class="reveal"><span class="ic"><i class="fa-solid fa-arrow-trend-up" aria-hidden="true"></i></span><div><h3>Built for growth</h3><p>Hooks, captions and posting plans designed to grow followers, enquiries and sales.</p></div></li>
            <li class="reveal"><span class="ic"><i class="fa-solid fa-lightbulb" aria-hidden="true"></i></span><div><h3>Fresh ideas</h3><p>Every brand is different. We script and design content that fits yours.</p></div></li>
            <li class="reveal"><span class="ic"><i class="fa-solid fa-map-location-dot" aria-hidden="true"></i></span><div><h3>Local understanding</h3><p>We know what Gorakhpur audiences respond to, in Hindi, Hinglish or English.</p></div></li>
            <li class="reveal"><span class="ic"><i class="fa-solid fa-headset" aria-hidden="true"></i></span><div><h3>Always reachable</h3><p>Talk directly to the team on WhatsApp. No call centres, no ticket numbers.</p></div></li>
        </ul>
    </div>
</section>

<section class="section section-navy" aria-labelledby="process-title">
    <div class="container">
        <div class="stats-band reveal" style="margin-bottom:clamp(56px,8vw,96px)">
            <div><strong data-count="500" data-suffix="+">500+</strong><span>Projects delivered</span></div>
            <div><strong data-count="300" data-suffix="+">300+</strong><span>Happy clients</span></div>
            <div><strong data-count="9">9</strong><span>In-house specialists</span></div>
            <div><strong data-count="3" data-suffix=" days">3 days</strong><span>Typical max turnaround</span></div>
        </div>
        <div class="section-head reveal">
            <span class="eyebrow">How we work</span>
            <h2 id="process-title">A simple, transparent 4-step process</h2>
            <p>From first call to monthly growth reports, you always know what's happening and what's next.</p>
        </div>
        <div class="process-wrap">
            <div class="process-bar" aria-hidden="true"><span></span></div>
            <ol class="process">
                <li><h3>Consultation</h3><p>We understand your business, customers, goals and content needs.</p></li>
                <li><h3>Planning</h3><p>We build a content strategy, pick trends and prepare creative ideas for your brand.</p></li>
                <li><h3>Creation</h3><p>We guide the shoot, then edit and design Reels, ads, graphics and promo content.</p></li>
                <li><h3>Delivery &amp; growth</h3><p>After your approval we deliver optimised content and track reach and engagement.</p></li>
            </ol>
        </div>
    </div>
</section>

<section class="section" aria-labelledby="work-title">
    <div class="container">
        <div class="section-head reveal" style="display:flex;flex-wrap:wrap;justify-content:space-between;align-items:end;gap:16px;max-width:none">
            <div style="max-width:640px">
                <span class="eyebrow">Selected work</span>
                <h2 id="work-title">Recent Reels, ads &amp; designs</h2>
            </div>
            <a class="btn btn-outline" href="Portfolio.html">View all work <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
        </div>
        <div class="work-grid">
            {work}
        </div>
    </div>
</section>

<section class="section section-alt" aria-labelledby="ind-title">
    <div class="container">
        <div class="section-head reveal">
            <span class="eyebrow">Industries</span>
            <h2 id="ind-title">Marketing that fits your kind of business</h2>
            <p>We've created content for many types of local businesses in Gorakhpur. Here's how we help each one.</p>
        </div>
        <div class="industry-grid">
            {inds}
        </div>
    </div>
</section>

<section class="section" aria-labelledby="price-title">
    <div class="container">
        <div class="section-head center reveal">
            <span class="eyebrow">Pricing</span>
            <h2 id="price-title">Social media packages in Gorakhpur. No hidden charges.</h2>
            <p>Pick a plan that fits your stage. Every plan includes design, editing, captions and a content calendar.</p>
        </div>
        <div class="grid grid-3">
            {plans}
        </div>
        <div class="stack-actions center-actions mt-8"><a class="btn btn-primary" href="Pricing.html">Compare all plans</a></div>
    </div>
</section>

{marquee(dark=True, speed=55)}

<section class="section section-alt" aria-labelledby="local-title">
    <div class="container">
        <div class="section-head reveal">
            <span class="eyebrow">Digital marketing agency in Gorakhpur</span>
            <h2 id="local-title">Helping Gorakhpur businesses get noticed online</h2>
        </div>
        <div class="seo-copy reveal">
            <p>Gorakhpur is changing fast. New cafés open on Medical College Road, coaching institutes compete for students in Betiahata, and showrooms in Golghar fight for the same festive shoppers. In this market, the businesses that win are the ones customers see first on Instagram, YouTube and Google. As a <strong>digital marketing agency in Gorakhpur</strong>, that's exactly what we help you do.</p>
            <p>Our <a href="video-editing-services-gorakhpur.html">video editing services in Gorakhpur</a> cover everything from short <a href="reels-editing-gorakhpur.html">Instagram Reels and YouTube Shorts</a> to long-form YouTube videos, product showcases and festival promos. Every edit is built around a strong hook, clear captions and a call to action, because views only matter when they turn into enquiries.</p>
            <p>For brands that want consistent growth, our <a href="social-media-marketing-gorakhpur.html">social media marketing in Gorakhpur</a> handles the whole job: content calendar, posts, Reels, Stories, captions, hashtags and monthly reports. Need ads? Our <a href="ad-video-production-gorakhpur.html">ad video production</a> team scripts and edits campaigns that target customers by locality, from Civil Lines to GIDA.</p>
            <p>We also design scroll-stopping creatives through our <a href="graphic-design-gorakhpur.html">graphic design services in Gorakhpur</a>, and our SEO specialist helps you show up on Google Maps and "near me" searches with <a href="local-seo-gorakhpur.html">local SEO in Gorakhpur</a>. One team, one point of contact, and content that looks like your brand everywhere.</p>
        </div>
        <h3 class="mt-8">Areas we serve in Gorakhpur</h3>
        <ul class="chips mt-4" role="list">{chips}</ul>
    </div>
</section>

<section class="section" aria-labelledby="blog-title">
    <div class="container">
        <div class="section-head reveal" style="display:flex;flex-wrap:wrap;justify-content:space-between;align-items:end;gap:16px;max-width:none">
            <div style="max-width:640px">
                <span class="eyebrow">From the blog</span>
                <h2 id="blog-title">Marketing guides for Gorakhpur businesses</h2>
            </div>
            <a class="btn btn-outline" href="blog/">All articles <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
        </div>
        <div class="post-grid">
            {posts}
        </div>
    </div>
</section>

<section class="section section-alt" aria-labelledby="faq-title">
    <div class="container">
        <div class="section-head center reveal">
            <span class="eyebrow">FAQ</span>
            <h2 id="faq-title">Questions Gorakhpur business owners ask us</h2>
        </div>
        {faq_html(HOME_FAQ, center=True)}
    </div>
</section>
{cta_band(R)}
{VIDEO_MODAL}
"""
    page(file="index.html", root=R, path="/", active="",
         title="Video Editing & Social Media Agency in Gorakhpur | Our Edge Media",
         desc="Our Edge Media is a video editing, Reels and social media marketing agency in Golghar, Gorakhpur. Ad videos, graphic design, local SEO and monthly social media plans from ₹12,000.",
         body=body, schema=[website_schema(), org_schema(), faq_schema(HOME_FAQ)])


SERVICE_DETAIL = {
    "reels": ("editing", "Short-form video is where new customers discover local businesses. We turn your raw clips into Reels and Shorts that grab attention in the first second, hold it with tight pacing and captions, and end with a clear next step.",
              "Ideal for cafés, boutiques, gyms, salons, coaching centres and creators in Gorakhpur who want reach beyond their current followers."),
    "ad-video": ("shoot", "An ad has seconds to earn attention. We script and edit ad videos with a hook, a clear problem-solution story, proof and a strong offer, sized for Reels, Stories, feeds and YouTube.",
                 "Ideal for businesses running Meta or YouTube ads, launching offers, or promoting a new branch in Gorakhpur."),
    "promotion": ("shoot", "Promo films build buzz around launches, events and seasonal offers. We combine product shots, motion graphics and music to make your announcement feel big, whether it's a store opening in Golghar or a Diwali sale.",
                  "Ideal for new store openings, product launches, festive campaigns and events."),
    "drop-effect": ("editing", "Drop-effect Reels use 3D drops, smooth transitions and beat-synced cuts to give your brand a premium, big-budget feel that stands out in a crowded feed.",
                    "Ideal for jewellers, fashion labels, real estate and premium products that need a luxury look."),
    "graphics": ("graphic-design", "Consistent, professional design makes people trust you before they ever call. We design posts, carousels, banners, posters and full brand identities that look like one brand everywhere.",
                 "Ideal for businesses refreshing their look, launching a new brand, or needing regular social creatives."),
    "smm": ("social-media", "We take social media off your plate completely: planning, content creation, posting, captions, hashtags, community replies and a monthly report showing what's working.",
            "Ideal for business owners who don't have time to post consistently but want steady growth and enquiries."),
}


def build_services():
    rows = []
    for i, (sid, ic, t, d, tags) in enumerate(SERVICES):
        img, long, ideal = SERVICE_DETAIL[sid]
        wd, ht = IMG_SIZE[img]
        tg = "".join(f"<li>{x}</li>" for x in tags)
        rows.append(f"""<article class="split-row{' flip' if i % 2 else ''}" id="{sid}">
                <div class="split-media reveal"><img src="assets/images/{img}.webp" alt="{t} by Our Edge Media, Gorakhpur" width="{wd}" height="{ht}" loading="lazy" decoding="async"><span class="tag">0{i + 1} · {t}</span></div>
                <div class="split-copy reveal">
                    <span class="eyebrow"><i class="{ic}" aria-hidden="true"></i> Service 0{i + 1}</span>
                    <h2>{t} in Gorakhpur</h2>
                    <p>{d}</p>
                    <p>{long}</p>
                    <ul class="tags" role="list">{tg}</ul>
                    <p class="mt-4" style="color:var(--ink-2)"><strong>Best for:</strong> {ideal}</p>
                    <div class="stack-actions mt-6">
                        <a class="btn btn-primary" href="{SERVICE_LANDING[sid]}">Learn more</a>
                        <a class="btn btn-outline" href="about.html#contact">Get a quote</a>
                    </div>
                </div>
            </article>""")
    svc_schema = [{"@type": "Service", "name": t + " in Gorakhpur", "description": d, "serviceType": t,
                   "provider": {"@id": ORG_ID}, "areaServed": {"@type": "City", "name": "Gorakhpur"},
                   "url": BASE + "/" + SERVICE_LANDING[sid]} for sid, ic, t, d, _ in SERVICES]
    faqs = [
        ("Do you also edit YouTube long-form videos?", "Yes. Along with Reels and ads we edit YouTube long-form videos: vlogs, interviews, tutorials and podcasts with cuts, B-roll, captions, music and thumbnails on request. See our <a href=\"video-editing-services-gorakhpur.html\">video editing services</a>."),
        ("Can you help my business show up on Google in Gorakhpur?", "Yes. Our SEO specialist sets up and optimises your Google Business Profile and website so you appear in local searches like \"near me\" and on Google Maps. Read about our <a href=\"local-seo-gorakhpur.html\">local SEO service</a>."),
        ("Do you run paid ads on Instagram and Facebook?", "Our ad manager can plan and guide Meta ad campaigns, and our editors create the ad videos and creatives for them. Ads guidance is included in the Premium plan."),
        ("What do you need from me to start?", "Just your logo, brand colours (if any), raw footage or product photos, and a short call about your goals. If you don't have footage, we'll guide you on what to shoot on your phone."),
        ("Can I combine services into one package?", "Yes. Most clients combine Reels editing, graphic design and social media management in one monthly plan. We can also build a custom package around your budget."),
    ]
    link_cards = "".join(f'<a href="{f}" class="reveal"><span class="dd-ic"><i class="{ic}" aria-hidden="true"></i></span>{lbl} in Gorakhpur</a>' for f, lbl, ic, d in LANDING)
    body = f"""
<section class="page-hero">
    <div class="container">
        <ol class="breadcrumb"><li><a href="./">Home</a></li><li aria-current="page">Services</li></ol>
        <span class="eyebrow">Services</span>
        <h1>Video editing &amp; social media services in Gorakhpur</h1>
        <p>From a single Reel to complete monthly social media management, pick what you need. Our in-house Gorakhpur team handles strategy, editing, design and posting, so you can focus on running your business.</p>
        <div class="stack-actions mt-6">
            <a class="btn btn-primary" href="about.html#contact">Discuss your project</a>
            <a class="btn btn-outline" href="Pricing.html">See pricing</a>
        </div>
    </div>
</section>

{marquee(speed=50)}

<section class="section">
    <div class="container stack-rows">
        {''.join(rows)}
    </div>
</section>

<section class="section section-alt" aria-labelledby="more-title">
    <div class="container">
        <div class="section-head reveal">
            <span class="eyebrow">Also available</span>
            <h2 id="more-title">More ways we can help</h2>
        </div>
        <div class="grid grid-3">
            <div class="card card-hover reveal"><div class="ic"><i class="fa-brands fa-youtube" aria-hidden="true"></i></div><h3>YouTube long-form editing</h3><p>Vlogs, interviews, podcasts and tutorials edited with pacing, B-roll, captions and music.</p><a class="btn btn-ghost" href="video-editing-services-gorakhpur.html">Learn more <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a></div>
            <div class="card card-hover reveal"><div class="ic"><i class="fa-solid fa-magnifying-glass-location" aria-hidden="true"></i></div><h3>Local SEO &amp; Google Business Profile</h3><p>Get found on Google Maps and "near me" searches across Gorakhpur.</p><a class="btn btn-ghost" href="local-seo-gorakhpur.html">Learn more <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a></div>
            <div class="card card-hover reveal"><div class="ic"><i class="fa-solid fa-bullseye" aria-hidden="true"></i></div><h3>Paid ads guidance</h3><p>Meta ad planning, targeting by Gorakhpur localities, and creatives that convert.</p><a class="btn btn-ghost" href="ad-video-production-gorakhpur.html">Learn more <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a></div>
        </div>
        <h3 class="mt-8 reveal">Explore our Gorakhpur service pages</h3>
        <div class="link-cards mt-4">{link_cards}</div>
    </div>
</section>

<section class="section" aria-labelledby="sfaq">
    <div class="container">
        <div class="section-head center reveal"><span class="eyebrow">FAQ</span><h2 id="sfaq">Service questions</h2></div>
        {faq_html(faqs, center=True)}
    </div>
</section>
{cta_band(R, "Not sure which service you need?", "Tell us what you sell and who your customers are. We'll suggest the right mix of videos, design and social media for your budget.")}
"""
    page(file="services.html", root=R, path="/services.html", active="services.html",
         title="Video Editing & Social Media Services in Gorakhpur",
         desc="Reels and Shorts editing, ad videos, promotion videos, drop-effect reels, graphic design and social media management for businesses in Gorakhpur. Get a free quote today.",
         crumbs=[("Services", "/services.html")], body=body, schema=svc_schema + [faq_schema(faqs)])


# =====================================================================
# PRICING
# =====================================================================
def build_pricing():
    cards = []
    for p in PLANS:
        feats = "".join(f'<li><i class="fa-solid fa-check" aria-hidden="true"></i>{f}</li>' for f in p["features"])
        badge = '<span class="plan-badge">Recommended</span>' if p.get("featured") else ""
        cls = "plan featured" if p.get("featured") else "plan"
        btn = "btn-primary" if p.get("featured") else "btn-outline"
        cards.append(f"""<article class="{cls} reveal">
                {badge}
                <span class="plan-tier">{p['tier']}</span>
                <h2 style="font-size:1.5rem;margin-top:6px">{p['name']}</h2>
                <p class="plan-price"><strong>₹{p['price']}</strong><span>/ month</span></p>
                <p class="plan-for">{p['for']}</p>
                <div class="plan-qty">
                    <div><b>{p['qty'][0]}</b><small>Posts</small></div>
                    <div><b>{p['qty'][1]}</b><small>Reels</small></div>
                    <div><b>{p['qty'][2]}</b><small>Stories</small></div>
                </div>
                <ul class="checklist" role="list">{feats}</ul>
                <a class="btn {btn} btn-block" href="RegistrationForm.html">Choose {p['name']}</a>
            </article>""")
    rows = [
        ("Posts / month", "10", "10", "15"), ("Reels / month", "8", "10", "15"), ("Stories / month", "12", "12", "12"),
        ("Content calendar & planning", 1, 1, 1), ("Caption writing & hashtags", 1, 1, 1),
        ("Custom brand designs", 0, 1, 1), ("Premium / advanced reel editing", 0, 1, 1),
        ("Hooks & scripts", 0, 1, 1), ("Competitor & audience research", 0, 1, 1),
        ("Monthly performance report", 0, 1, "Detailed"), ("Brand voice & campaign planning", 0, 0, 1),
        ("Ads guidance", 0, 0, 1), ("Priority support", 0, 0, 1),
    ]
    def cell(v):
        if v == 1: return '<td><i class="fa-solid fa-check yes" aria-hidden="true"></i><span class="sr-only">Included</span></td>'
        if v == 0: return '<td><i class="fa-solid fa-minus no" aria-hidden="true"></i><span class="sr-only">Not included</span></td>'
        return f"<td>{v}</td>"
    trs = "".join(f"<tr><td>{r[0]}</td>{''.join(cell(v) for v in r[1:])}</tr>" for r in rows)
    faqs = [
        ("Is there a minimum contract?", "Monthly plans run month to month. We recommend at least 3 months to see real growth, because social media results compound over time."),
        ("How much does a single Reel or ad video cost?", "One-off ad videos usually range from ₹999 to ₹4,999 depending on length, effects and motion graphics. Message us on WhatsApp with a reference and we'll quote exactly."),
        ("Do the plans include paid ad budget?", "No. Ad spend is paid directly to Meta or Google. The Premium plan includes ads guidance, and we create the ad creatives for you."),
        ("Can I customise a plan?", "Yes. If you need more Reels, fewer posts or YouTube editing added, we'll build a custom plan around your goals and budget."),
        ("How do I pay?", "We share an invoice at the start of each month. UPI and bank transfer are accepted. Talk to us for details."),
    ]
    offers = [{"@type": "Offer", "name": p["name"] + " social media management plan", "price": p["price"].replace(",", ""),
               "priceCurrency": "INR", "url": BASE + "/Pricing.html",
               "priceSpecification": {"@type": "UnitPriceSpecification", "price": p["price"].replace(",", ""), "priceCurrency": "INR", "unitText": "MONTH"}}
              for p in PLANS]
    schema = [{"@type": "Service", "name": "Social Media Management in Gorakhpur", "provider": {"@id": ORG_ID},
               "areaServed": {"@type": "City", "name": "Gorakhpur"},
               "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Monthly plans", "itemListElement": offers}},
              faq_schema(faqs)]
    body = f"""
<section class="page-hero">
    <div class="container">
        <ol class="breadcrumb"><li><a href="./">Home</a></li><li aria-current="page">Pricing</li></ol>
        <span class="eyebrow">Pricing</span>
        <h1>Social media marketing packages in Gorakhpur</h1>
        <p>Simple monthly plans for local businesses and brands. Every plan includes content planning, design, reel editing and captions. Upgrade or change anytime.</p>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="pricing-grid">
            {''.join(cards)}
        </div>
        <p class="center muted mt-8">Need just one video? Single ad videos start around <strong>₹999 – ₹4,999</strong>. <a href="{WA}" target="_blank" rel="noopener">Ask on WhatsApp</a>.</p>
    </div>
</section>

<section class="section section-alt" aria-labelledby="cmp">
    <div class="container">
        <div class="section-head reveal"><span class="eyebrow">Compare</span><h2 id="cmp">What's included in each plan</h2></div>
        <div class="table-wrap reveal">
            <table class="compare">
                <thead><tr><th scope="col">Feature</th><th scope="col">Starter</th><th scope="col">Growth</th><th scope="col">Premium</th></tr></thead>
                <tbody>{trs}</tbody>
            </table>
        </div>
    </div>
</section>

<section class="section" aria-labelledby="pfaq">
    <div class="container">
        <div class="section-head center reveal"><span class="eyebrow">FAQ</span><h2 id="pfaq">Pricing questions</h2></div>
        {faq_html(faqs, center=True)}
    </div>
</section>
{cta_band(R, "Want a plan built around your budget?", "Share your goals and we'll recommend the right package, or build a custom one for your Gorakhpur business.")}
"""
    page(file="Pricing.html", root=R, path="/Pricing.html", active="Pricing.html",
         title="Social Media Packages & Pricing in Gorakhpur | Our Edge Media",
         desc="Transparent social media management pricing in Gorakhpur: Starter ₹12,000, Growth ₹20,000 and Premium ₹30,000 per month, plus single ad videos from ₹999. Compare plans.",
         crumbs=[("Pricing", "/Pricing.html")], body=body, schema=schema)


# =====================================================================
# PORTFOLIO
# =====================================================================
def build_portfolio():
    cards = "\n".join(work_card(w) for w in WORK)
    videos = [{"@type": "VideoObject", "name": w[2], "description": w[3],
               "thumbnailUrl": BASE + "/assets/images/og-image.jpg", "contentUrl": BASE + "/" + w[5],
               "uploadDate": "2026-11-21", "publisher": {"@id": ORG_ID}} for w in WORK if w[5]]
    body = f"""
<section class="page-hero">
    <div class="container">
        <ol class="breadcrumb"><li><a href="./">Home</a></li><li aria-current="page">Our Work</li></ol>
        <span class="eyebrow">Portfolio</span>
        <h1>Our work: Reels, ads &amp; designs</h1>
        <p>A selection of video edits, promo films and designs made by our Gorakhpur team. Tap any video to play it.</p>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="filters" role="group" aria-label="Filter projects">
            <button class="filter-btn" type="button" data-filter="all" aria-pressed="true">All</button>
            <button class="filter-btn" type="button" data-filter="reels" aria-pressed="false">Reels</button>
            <button class="filter-btn" type="button" data-filter="promo" aria-pressed="false">Promotion</button>
            <button class="filter-btn" type="button" data-filter="ads" aria-pressed="false">Ads</button>
            <button class="filter-btn" type="button" data-filter="design" aria-pressed="false">Design</button>
            <button class="filter-btn" type="button" data-filter="smm" aria-pressed="false">Social media</button>
        </div>
        <div class="work-grid">
            {cards}
        </div>
    </div>
</section>
{cta_band(R, "Like what you see?", "Let's create content like this for your brand. Share your idea and we'll send a plan and quote.")}
{VIDEO_MODAL}
"""
    page(file="Portfolio.html", root=R, path="/Portfolio.html", active="Portfolio.html",
         title="Our Work: Reels, Ads & Design Portfolio | Our Edge Media",
         desc="See Reels, drop-effect edits, promotion videos, ad creatives and graphic design work by Our Edge Media, a video editing agency in Gorakhpur.",
         crumbs=[("Our Work", "/Portfolio.html")], body=body, schema=videos)


# =====================================================================
# TEAM
# =====================================================================
TEAM = [
    # name, role, bio, photo, department key, skills, helps-you-with
    ("Abhishek Rajbhar", "Founder & CEO", "Creative director and video editor driving digital growth and branding for businesses in Gorakhpur and beyond.", "IMG_3922.webp", "lead",
     ["Creative direction", "Video editing", "Brand strategy", "Client growth"],
     ["Plans your brand's overall content strategy", "Reviews major projects before delivery", "Your go-to person for big decisions"]),
    ("Tanvi Gupta", "Ad Manager", "Specialist in lead generation, ad performance and paid social campaigns that scale return on spend.", None, "growth",
     ["Meta ads", "Lead generation", "Campaign analytics", "Budget optimisation"],
     ["Sets up ad campaigns that bring enquiries", "Targets customers by Gorakhpur locality", "Tracks what your ad money returns"]),
    ("Anjali Mishra", "SEO Specialist", "Optimises organic discoverability, keyword strategy and local search presence for client brands.", "anjali.webp", "growth",
     ["Local SEO", "Google Business Profile", "Keyword research", "On-page SEO"],
     ["Gets you found on Google Maps", "Improves your \"near me\" visibility", "Optimises your website for local searches"]),
    ("Arohi Yadav", "Social Media Manager", "Manages content schedules, community interaction, engagement growth and hashtag strategy.", None, "growth",
     ["Content calendars", "Community management", "Hashtag strategy", "Engagement growth"],
     ["Plans and posts your monthly content", "Replies to comments and grows engagement", "Keeps your pages active every week"]),
    ("Shwet Gupta", "Video Editor", "Masters viral transitions, pacing, sound design and trending Instagram styles.", None, "creative",
     ["Viral transitions", "Pacing", "Sound design", "Trending styles"],
     ["Edits trend-ready Reels and Shorts", "Adds hooks, captions and music", "Keeps your videos fast and watchable"]),
    ("Syarn", "Video Editor", "Specialises in cinematic colour grading, motion graphics, storytelling and high-retention reels.", None, "creative",
     ["Colour grading", "Motion graphics", "Storytelling", "High-retention edits"],
     ["Gives your videos a cinematic look", "Builds motion graphics for ads", "Tells your brand story on screen"]),
    ("Kashif", "Video Editor", "Crafts high-impact promotional edits, 3D drops, beat-synced visuals and business teasers.", None, "creative",
     ["Promo edits", "3D drop effects", "Beat sync", "Business teasers"],
     ["Creates launch and offer promos", "Adds premium drop effects", "Makes teasers that build hype"]),
    ("Alka Dubey", "Graphic Designer", "Designs promotional visuals, carousel posts, brand identities and eye-catching social creatives.", None, "creative",
     ["Social creatives", "Carousels", "Brand identity", "Posters & banners"],
     ["Designs your posts and carousels", "Creates logos and brand identity", "Makes banners, menus and posters"]),
    ("Danish Aalam", "Manager", "Oversees project workflows, client relations and delivery timelines to keep quality consistent.", None, "ops",
     ["Project management", "Client communication", "Delivery timelines", "Quality control"],
     ["Your single point of contact", "Makes sure work arrives on time", "Coordinates the whole team for you"]),
]

DEPTS = [
    ("creative", "Creative Studio", "fa-solid fa-clapperboard", "Video editing & design"),
    ("growth", "Growth & Marketing", "fa-solid fa-arrow-trend-up", "Ads, SEO & social media"),
    ("ops", "Operations", "fa-solid fa-people-arrows", "Projects & client success"),
]
DEPT_NAME = {"lead": "Leadership", **{k: n for k, n, *_ in DEPTS}}

TEAM_SCRIPT = """<script src="assets/js/team.js" defer></script>"""


def _initials(n):
    return "".join(w[0] for w in n.split()[:2]).upper()


def _node(i, m, lead=False):
    n, r, d, img, dept, skills, helps = m
    av = (f'<img src="assets/images/{img}" alt="" width="800" height="800" loading="{"eager" if lead else "lazy"}" decoding="async">'
          if img else f'<span>{_initials(n)}</span>')
    return f"""<button class="tnode{' tnode-lead' if lead else ''}" type="button" data-member="{i}" data-dept="{dept}" aria-haspopup="dialog" aria-label="View profile: {n}, {r}">
                    <span class="tnode-av dept-{dept}">{av}</span>
                    <span class="tnode-txt"><b>{n}</b><small>{r}</small></span>
                    <span class="tnode-go" aria-hidden="true"><i class="fa-solid fa-arrow-right"></i></span>
                </button>"""


def build_team():
    import json as _json
    lead = _node(0, TEAM[0], lead=True)
    branches = []
    for key, name, ic, sub in DEPTS:
        members = [(i, m) for i, m in enumerate(TEAM) if m[4] == key]
        leaves = "".join(f'<li class="tleaf">{_node(i, m)}</li>' for i, m in members)
        branches.append(f"""<div class="tbranch" data-dept="{key}">
                <span class="ln ln-drop" aria-hidden="true"></span>
                <div class="tdept dept-{key}"><span class="tdept-ic"><i class="{ic}" aria-hidden="true"></i></span><div><b>{name}</b><small>{sub} · {len(members)} {'person' if len(members) == 1 else 'people'}</small></div></div>
                <div class="tleaves-wrap"><span class="ln ln-spine" aria-hidden="true"></span><ul class="tleaves" role="list">{leaves}</ul></div>
            </div>""")
    data = [{"name": n, "role": r, "bio": d, "img": (f"assets/images/{img}" if img else None), "initials": _initials(n),
             "dept": dept, "deptName": DEPT_NAME[dept], "skills": s, "helps": h} for n, r, d, img, dept, s, h in TEAM]
    team_json = _json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    people = [{"@type": "Person", "name": n, "jobTitle": r, "description": d, "knowsAbout": s, "worksFor": {"@id": ORG_ID}}
              for n, r, d, img, dept, s, h in TEAM]
    body = f"""
<section class="page-hero team-hero">
    <div class="container">
        <ol class="breadcrumb"><li><a href="./">Home</a></li><li aria-current="page">Team</li></ol>
        <span class="eyebrow">Our team</span>
        <h1>Meet the people behind Our Edge Media</h1>
        <p>Nine specialists across three departments, working together from our office in Golghar, Gorakhpur. Tap anyone in the tree to see what they do and how they help your brand grow.</p>
        <ul class="team-stats" role="list">
            <li><strong data-count="9">9</strong><span>Specialists</span></li>
            <li><strong data-count="3">3</strong><span>Departments</span></li>
            <li><strong data-count="1">1</strong><span>Office in Gorakhpur</span></li>
        </ul>
    </div>
</section>

<section class="section team-tree-section" aria-labelledby="tree-title">
    <div class="container">
        <div class="section-head center reveal">
            <span class="eyebrow">The Our Edge Media tree</span>
            <h2 id="tree-title">One root, three branches, nine specialists</h2>
            <p>Every project grows from the same root: a clear strategy. Our creative, growth and operations teams branch out from there to deliver it.</p>
        </div>

        <div class="org" id="orgTree">
            <div class="troot">{lead}</div>
            <span class="ln ln-trunk" aria-hidden="true"></span>
            <div class="tbranches">
                <span class="ln ln-bar" aria-hidden="true"></span>
                {''.join(branches)}
            </div>
        </div>
        <p class="tree-hint center muted mt-8"><i class="fa-regular fa-hand-pointer" aria-hidden="true"></i> Tap or click any team member to open their profile</p>
    </div>
</section>

<section class="section section-navy" aria-labelledby="join">
    <div class="container split">
        <div class="reveal">
            <span class="eyebrow">How we work together</span>
            <h2 id="join">One team. Every skill your brand needs.</h2>
        </div>
        <div class="reveal">
            <p class="lead" style="color:var(--on-navy-muted)">Instead of hiring a separate editor, designer, SEO expert and social media manager, you get one coordinated team with a single point of contact. Strategy flows from the root, the right specialists pick it up, and you get faster delivery and a brand that looks the same everywhere.</p>
            <div class="stack-actions mt-6"><a class="btn btn-light" href="RegistrationForm.html">Start a project</a><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener"><i class="fa-brands fa-whatsapp" aria-hidden="true"></i> Talk to the team</a></div>
        </div>
    </div>
</section>
{cta_band(R, "Want this team working on your brand?", "Tell us about your business and we'll put the right specialists on it. Reply within a few hours.")}

<div class="pmodal" id="profileModal" role="dialog" aria-modal="true" aria-labelledby="pmName" aria-hidden="true">
    <div class="pm-backdrop" data-pm-close></div>
    <article class="pm-card">
        <button class="pm-close" type="button" aria-label="Close profile" data-pm-close><i class="fa-solid fa-xmark" aria-hidden="true"></i></button>
        <div class="pm-banner"><span class="pm-orb"></span><span class="pm-orb pm-orb2"></span></div>
        <div class="pm-head">
            <div class="pm-avatar"></div>
            <div class="pm-id">
                <span class="pm-dept"></span>
                <h2 id="pmName"></h2>
                <p class="pm-role"></p>
            </div>
        </div>
        <div class="pm-body">
            <p class="pm-bio"></p>
            <h3>Skills</h3>
            <ul class="pm-skills" role="list"></ul>
            <h3>How they help your brand</h3>
            <ul class="pm-helps" role="list"></ul>
            <div class="pm-actions">
                <a class="btn btn-primary" href="about.html#contact">Work with our team</a>
                <a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener"><i class="fa-brands fa-whatsapp" aria-hidden="true"></i> WhatsApp</a>
            </div>
        </div>
        <div class="pm-nav">
            <button type="button" class="pm-prev" aria-label="Previous team member"><i class="fa-solid fa-arrow-left" aria-hidden="true"></i> <span></span></button>
            <span class="pm-count" aria-live="polite"></span>
            <button type="button" class="pm-next" aria-label="Next team member"><span></span> <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></button>
        </div>
    </article>
</div>
<script type="application/json" id="teamData">{team_json}</script>
"""
    page(file="OurTeam.html", root=R, path="/OurTeam.html", active="OurTeam.html",
         title="Our Team: Editors & Marketers in Gorakhpur | Our Edge Media",
         desc="Meet the Our Edge Media team in Gorakhpur: video editors, a graphic designer, SEO specialist, ad manager and social media manager, led by founder Abhishek Rajbhar.",
         crumbs=[("Team", "/OurTeam.html")], body=body, schema=people, extra_scripts=TEAM_SCRIPT)


# =====================================================================
# ABOUT + CONTACT
# =====================================================================
CONTACT_SCRIPT = """<script>
async function handleContactSubmit(event) {
    event.preventDefault();
    const form = event.target;
    const btn = document.getElementById("contactSubmitBtn");
    const original = btn.innerHTML;
    const val = (id) => (document.getElementById(id) ? document.getElementById(id).value.trim() : "");
    if (val("contactWebsite")) { form.reset(); return; }
    const name = val("contactName");
    btn.disabled = true;
    btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin" aria-hidden="true"></i> Sending…';
    const saved = await sendToGoogleSheet({
        formType: "contact",
        name: name,
        email: val("contactEmail"),
        phone: val("contactPhone"),
        subject: val("contactSubject"),
        message: val("contactMessage"),
        page: window.location.href
    });
    btn.disabled = false;
    btn.innerHTML = original;
    if (saved) {
        form.reset();
        showFormPopup("success", "Message sent!", "Thank you" + (name ? ", " + name : "") + "! We've received your message and will get back to you within 24 hours.");
    } else {
        showFormPopup("error", "Message not sent", "Something went wrong while sending your message. Your text is still in the form, so please try again, or reach us directly on WhatsApp.");
    }
}
</script>"""


def build_about():
    body = f"""
<section class="page-hero">
    <div class="container">
        <ol class="breadcrumb"><li><a href="./">Home</a></li><li aria-current="page">About</li></ol>
        <span class="eyebrow">About us</span>
        <h1>A creative media agency from Gorakhpur, built to grow brands</h1>
        <p>Our Edge Media (Digixlonline) helps businesses, brands and creators build a strong online presence through premium video editing, design, branding and social media marketing.</p>
    </div>
</section>

<section class="section">
    <div class="container split">
        <div class="reveal">
            <span class="eyebrow">Our mission</span>
            <h2>Turn your social media into a real business asset</h2>
            <div class="about-logo"><img src="assets/images/logo-full-light.webp" alt="Our Edge Media logo" width="520" height="456" loading="lazy" decoding="async"></div>
        </div>
        <div class="reveal">
            <p class="lead">Most local businesses post randomly and hope for the best. We started Our Edge Media to change that, giving Gorakhpur brands the same quality of content, strategy and consistency that big national brands have.</p>
            <p class="mt-4 muted">Our mission is simple: create content that attracts customers, builds trust and increases sales. Every Reel, ad and post we make has a clear job to do.</p>
            <ul class="chips mt-6" role="list">
                <li><i class="fa-solid fa-check" aria-hidden="true"></i>Social media management</li>
                <li><i class="fa-solid fa-check" aria-hidden="true"></i>Professional video editing</li>
                <li><i class="fa-solid fa-check" aria-hidden="true"></i>Graphic design</li>
                <li><i class="fa-solid fa-check" aria-hidden="true"></i>Instagram growth strategy</li>
                <li><i class="fa-solid fa-check" aria-hidden="true"></i>Brand identity</li>
                <li><i class="fa-solid fa-check" aria-hidden="true"></i>Paid advertising</li>
            </ul>
        </div>
    </div>
    <div class="container mt-8">
        <div class="stats reveal">
            <div><strong>500+</strong><span>Projects delivered</span></div>
            <div><strong>300+</strong><span>Happy clients</span></div>
            <div><strong>5+</strong><span>Years experience</span></div>
            <div><strong>9</strong><span>In-house specialists</span></div>
        </div>
    </div>
</section>


<section class="section section-alt" aria-labelledby="values-title">
    <div class="container">
        <p class="statement" style="margin-bottom:clamp(40px,6vw,72px)">Big-city content quality, <span class="hl-blue">built in Gorakhpur</span>, for businesses that want to grow here and beyond.</p>
        <div class="section-head reveal">
            <span class="eyebrow">What we stand for</span>
            <h2 id="values-title">How we work with every client</h2>
        </div>
        <div class="grid grid-4">
            <div class="card card-hover reveal"><div class="ic"><i class="fa-solid fa-bullseye" aria-hidden="true"></i></div><h3>Results first</h3><p>Every Reel, post and ad has a job: more enquiries, visits or sales.</p></div>
            <div class="card card-hover reveal"><div class="ic"><i class="fa-solid fa-handshake" aria-hidden="true"></i></div><h3>Honest advice</h3><p>Clear pricing, realistic timelines and no fake followers or reviews. Ever.</p></div>
            <div class="card card-hover reveal"><div class="ic"><i class="fa-solid fa-bolt" aria-hidden="true"></i></div><h3>Speed</h3><p>Most edits delivered in 1–3 days, so you never miss a trend or festival.</p></div>
            <div class="card card-hover reveal"><div class="ic"><i class="fa-solid fa-people-group" aria-hidden="true"></i></div><h3>One local team</h3><p>Editors, designers and marketers under one roof in Golghar, Gorakhpur.</p></div>
        </div>
        <div class="seo-copy reveal mt-8">
            <p>Our Edge Media started with a simple idea: businesses in Gorakhpur deserve the same quality of content and strategy that big national brands use. Too many local shops, cafés, clinics and coaching institutes were posting randomly, using generic templates, or paying for editing that looked good but brought no customers.</p>
            <p>Today our team of video editors, graphic designers, an SEO specialist, an ad manager and social media managers works from Bank Road, Golghar. We help local businesses and creators with <a href="video-editing-services-gorakhpur.html">video editing</a>, <a href="social-media-marketing-gorakhpur.html">social media marketing</a>, <a href="graphic-design-gorakhpur.html">graphic design</a> and <a href="local-seo-gorakhpur.html">local SEO in Gorakhpur</a>, and we work with clients across Uttar Pradesh and India.</p>
        </div>
    </div>
</section>

<section class="section " id="contact" aria-labelledby="contact-title">
    <div class="container">
        <div class="section-head reveal">
            <span class="eyebrow">Contact</span>
            <h2 id="contact-title">Let's grow your business together</h2>
            <p>Send us a message and we'll reply within 24 hours, usually much sooner. Prefer to talk? Call or WhatsApp us.</p>
        </div>
        <div class="grid grid-2" style="align-items:start;gap:32px">
            <div class="reveal">
                <ul class="contact-list" role="list">
                    <li><span class="ic"><i class="fa-solid fa-phone" aria-hidden="true"></i></span><div><small>Phone / WhatsApp</small><a href="tel:{PHONE}">{PHONE_DISPLAY}</a></div></li>
                    <li><span class="ic"><i class="fa-solid fa-envelope" aria-hidden="true"></i></span><div><small>Email</small><a href="mailto:{EMAIL}">{EMAIL}</a></div></li>
                    <li><span class="ic"><i class="fa-brands fa-instagram" aria-hidden="true"></i></span><div><small>Instagram</small><a href="{IG}" target="_blank" rel="noopener">@ouredgemedia</a></div></li>
                    <li><span class="ic"><i class="fa-solid fa-location-dot" aria-hidden="true"></i></span><div><small>Office</small><a href="{MAPS}" target="_blank" rel="noopener">{ADDRESS}</a></div></li>
                    <li><span class="ic"><i class="fa-regular fa-clock" aria-hidden="true"></i></span><div><small>Hours</small><span class="v">Mon – Sat, 10:00 AM – 8:00 PM</span></div></li>
                </ul>
                <div class="map-frame mt-6">
                    <iframe src="https://maps.google.com/maps?q=Digixlonline%2C+Gorakhpur&amp;t=&amp;z=15&amp;ie=UTF8&amp;iwloc=&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Our Edge Media office location on Google Maps"></iframe>
                </div>
            </div>

            <form id="contactForm" class="form-card reveal" onsubmit="handleContactSubmit(event)" novalidate style="position:relative">
                <h3 style="font-size:1.35rem">Send us a message</h3>
                <p class="muted mt-2" style="margin-bottom:22px">Fields marked * are required.</p>
                <div class="form-grid two">
                    <div class="field"><label for="contactName">Your name *</label><input type="text" id="contactName" name="name" autocomplete="name" maxlength="100" required></div>
                    <div class="field"><label for="contactPhone">Phone / WhatsApp</label><input type="tel" id="contactPhone" name="phone" autocomplete="tel" inputmode="tel" pattern="[0-9+\\s\\(\\)\\-]{{7,20}}" maxlength="20" placeholder="+91"></div>
                    <div class="field full"><label for="contactEmail">Email *</label><input type="email" id="contactEmail" name="email" autocomplete="email" maxlength="150" required></div>
                    <div class="field full"><label for="contactSubject">Subject <span class="opt">(optional)</span></label><input type="text" id="contactSubject" name="subject" maxlength="150" placeholder="e.g. Reels for my café in Golghar"></div>
                    <div class="field full"><label for="contactMessage">Message *</label><textarea id="contactMessage" name="message" maxlength="3000" required placeholder="Tell us about your business and what you need"></textarea></div>
                </div>
                <input type="text" id="contactWebsite" name="website" class="hp-field" tabindex="-1" autocomplete="off" aria-hidden="true">
                <button type="submit" id="contactSubmitBtn" class="btn btn-primary btn-block mt-6">Send message <i class="fa-solid fa-paper-plane" aria-hidden="true"></i></button>
                <p class="form-note"><i class="fa-solid fa-lock" aria-hidden="true"></i>Your details are only used to reply to you. We never share them.</p>
            </form>
        </div>
    </div>
</section>
"""
    # native validation for required fields while keeping custom submit
    body = body.replace(' novalidate style="position:relative"', ' style="position:relative"')
    page(file="about.html", root=R, path="/about.html", active="about.html",
         title="About & Contact | Our Edge Media, Golghar, Gorakhpur",
         desc="Our Edge Media (Digixlonline) is a creative video editing and social media agency on Bank Road, Golghar, Gorakhpur. Call +91 91964 97565 or send us a message.",
         crumbs=[("About", "/about.html")], body=body, flush=True, extra_scripts=CONTACT_SCRIPT,
         schema=[{"@type": ["AboutPage", "ContactPage"], "@id": BASE + "/about.html#about", "url": BASE + "/about.html", "mainEntity": {"@id": ORG_ID}}, org_schema()])


# =====================================================================
# REGISTRATION
# =====================================================================
REG_SCRIPT = """<script>
async function handleRegistrationSubmit(event) {
    event.preventDefault();
    const form = event.target;
    const btn = document.getElementById("regSubmitBtn");
    const original = btn.innerHTML;
    const val = (id) => (document.getElementById(id) ? document.getElementById(id).value.trim() : "");
    if (val("regWebsite")) { form.reset(); return; }
    const name = val("regName");
    const work = document.querySelector('input[name="work"]:checked');
    btn.disabled = true;
    btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin" aria-hidden="true"></i> Submitting…';
    const saved = await sendToGoogleSheet({
        formType: "registration",
        name: name,
        mobile: val("regMobile"),
        location: val("regLocation"),
        brand: val("regBrand"),
        workType: work ? work.value : "Freelancing"
    });
    btn.disabled = false;
    btn.innerHTML = original;
    if (saved) {
        form.reset();
        showFormPopup("success", "Application submitted!", "Thank you" + (name ? ", " + name : "") + "! Your details have been received. Our team will contact you on your mobile number soon.");
    } else {
        showFormPopup("error", "Couldn't submit", "Something went wrong while sending your application. Your details are still in the form, so please try again, or message us directly on WhatsApp.");
    }
}
</script>"""


def build_registration():
    body = f"""
<section class="page-hero">
    <div class="container">
        <ol class="breadcrumb"><li><a href="./">Home</a></li><li aria-current="page">Start a project</li></ol>
        <span class="eyebrow">Start a project</span>
        <h1>Work with Our Edge Media</h1>
        <p>Register your brand or channel and our team will call you to understand your goals. It takes less than a minute.</p>
    </div>
</section>

<section class="section">
    <div class="container grid grid-2" style="align-items:start;gap:40px">
        <div class="reveal">
            <h2 style="font-size:1.6rem">What happens next?</h2>
            <ol class="process mt-6" style="grid-template-columns:1fr;counter-reset:step">
                <li style="background:var(--surface);border-color:var(--border)"><h3>We call you</h3><p class="muted">Within one working day, someone from our team calls you on the number you share.</p></li>
                <li style="background:var(--surface);border-color:var(--border)"><h3>We understand your brand</h3><p class="muted">Your products, customers, competitors and what you want to achieve.</p></li>
                <li style="background:var(--surface);border-color:var(--border)"><h3>You get a plan &amp; quote</h3><p class="muted">A clear content plan with pricing, freelance per project or monthly.</p></li>
            </ol>
            <p class="muted mt-6">Prefer to talk now? <a href="{WA}" target="_blank" rel="noopener">WhatsApp us</a> or call <a href="tel:{PHONE}">{PHONE_DISPLAY}</a>.</p>
        </div>

        <form id="registrationForm" class="form-card reveal" onsubmit="handleRegistrationSubmit(event)" style="position:relative">
            <h2 style="font-size:1.35rem">Your details</h2>
            <p class="muted mt-2" style="margin-bottom:22px">All fields are required.</p>
            <div class="form-grid">
                <div class="field"><label for="regName">Name</label><input type="text" id="regName" autocomplete="name" maxlength="100" required></div>
                <div class="field"><label for="regMobile">Mobile number</label><input type="tel" id="regMobile" autocomplete="tel" inputmode="tel" pattern="[0-9+\\s\\(\\)\\-]{{7,20}}" maxlength="20" placeholder="+91" required></div>
                <div class="field"><label for="regLocation">City / location</label><input type="text" id="regLocation" autocomplete="address-level2" maxlength="100" placeholder="e.g. Gorakhpur" required></div>
                <div class="field"><label for="regBrand">Brand or channel name</label><input type="text" id="regBrand" autocomplete="organization" maxlength="120" required></div>
                <fieldset class="field" style="border:0;padding:0;margin:0">
                    <legend class="label">How would you like to work with us?</legend>
                    <div class="radio-cards">
                        <label><input type="radio" name="work" value="Freelancing" checked> Per project</label>
                        <label><input type="radio" name="work" value="Monthly"> Monthly plan</label>
                    </div>
                </fieldset>
            </div>
            <input type="text" id="regWebsite" class="hp-field" tabindex="-1" autocomplete="off" aria-hidden="true">
            <button type="submit" id="regSubmitBtn" class="btn btn-primary btn-block mt-6">Submit application <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></button>
            <p class="form-note"><i class="fa-solid fa-lock" aria-hidden="true"></i>We'll only use your number to discuss your project.</p>
        </form>
    </div>
</section>
"""
    page(file="RegistrationForm.html", root=R, path="/RegistrationForm.html", active="RegistrationForm.html",
         title="Start a Project | Our Edge Media Gorakhpur",
         desc="Register your brand or channel with Our Edge Media, Gorakhpur. Choose per-project or monthly video editing and social media management and we'll call you back.",
         crumbs=[("Start a project", "/RegistrationForm.html")], body=body, flush=True, extra_scripts=REG_SCRIPT)


# =====================================================================
# 404
# =====================================================================
def build_404():
    body = """
<section class="section">
    <div class="container center">
        <p class="eyebrow" style="justify-content:center">Error 404</p>
        <h1>Page not found</h1>
        <p class="lead mt-4" style="margin-inline:auto">Sorry, this page doesn't exist. It may have moved, or the link may be wrong.</p>
        <div class="stack-actions center-actions mt-8">
            <a class="btn btn-primary" href="/">Go to home</a>
            <a class="btn btn-outline" href="/services.html">Our services</a>
            <a class="btn btn-outline" href="/blog/">Read the blog</a>
        </div>
    </div>
</section>"""
    page(file="404.html", root="/", path="/404.html", active="404", title="Page Not Found | Our Edge Media",
         desc="The page you were looking for could not be found.", body=body, robots="noindex, follow")


if __name__ == "__main__":
    build_home(); build_services(); build_pricing(); build_portfolio(); build_team(); build_about(); build_registration(); build_404()
    blog.build_all()
    import landing
    landing.build_all()
