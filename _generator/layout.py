"""Shared layout pieces for the Our Edge Media static site generator."""
import json, html

BASE = "https://ouredgemedia.com"
PHONE = "+919196497565"
PHONE_DISPLAY = "+91 91964 97565"
EMAIL = "ouredgemedia@gmail.com"
WA = "https://wa.me/919196497565"
IG = "https://www.instagram.com/ouredgemedia/"
MAPS = "https://maps.app.goo.gl/vgLReNCvaMgz1bqB9"
ADDRESS = "Bank Road, Golghar (near St. Andrew's College), Gorakhpur, Uttar Pradesh 273001"
TODAY = "2026-11-21"

# Keyword-targeted service landing pages: (file, menu label, icon, one-line description)
LANDING = [
    ("video-editing-services-gorakhpur.html", "Video Editing", "fa-solid fa-film", "Reels, YouTube, ads & business videos"),
    ("social-media-marketing-gorakhpur.html", "Social Media Marketing", "fa-solid fa-chart-line", "Monthly management & growth"),
    ("reels-editing-gorakhpur.html", "Instagram Reels Editing", "fa-solid fa-fire", "Hook-first Reels & Shorts"),
    ("ad-video-production-gorakhpur.html", "Ad & Promo Videos", "fa-solid fa-bullhorn", "Ads that bring calls & walk-ins"),
    ("graphic-design-gorakhpur.html", "Graphic Design", "fa-solid fa-pen-nib", "Posts, banners & brand identity"),
    ("local-seo-gorakhpur.html", "Local SEO & Google Maps", "fa-solid fa-map-location-dot", "Rank in Gorakhpur searches"),
]

GSAP_JS = "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"
SCROLLTRIGGER_JS = "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"

NAV = [
    ("services.html", "Services"),
    ("Pricing.html", "Pricing"),
    ("Portfolio.html", "Our Work"),
    ("OurTeam.html", "Team"),
    ("blog/", "Blog"),
    ("about.html", "About"),
]

ORG_ID = BASE + "/#agency"


def esc(s):
    return html.escape(s, quote=True)


def head(*, root, path, title, desc, crumbs=None, schema=None, og_type="website",
         robots="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1", extra_head=""):
    url = BASE + path
    crumbs = crumbs or []
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"}]
    for i, (name, p) in enumerate(crumbs, start=2):
        items.append({"@type": "ListItem", "position": i, "name": name, "item": BASE + p})
    graph = [
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": title, "description": desc,
         "inLanguage": "en-IN", "isPartOf": {"@id": BASE + "/#website"}, "about": {"@id": ORG_ID},
         "breadcrumb": {"@id": url + "#breadcrumb"},
         "primaryImageOfPage": {"@type": "ImageObject", "url": BASE + "/assets/images/og-image.jpg"}},
        {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": items},
    ]
    if schema:
        graph.extend(schema)
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)
    return f"""<!DOCTYPE html>
<html lang="en-IN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{esc(title)}</title>
    <meta name="description" content="{esc(desc)}">
    <meta name="robots" content="{robots}">
    <link rel="canonical" href="{url}">
    <link rel="alternate" hreflang="en-IN" href="{url}">
    <link rel="alternate" hreflang="x-default" href="{url}">
    <meta name="author" content="Our Edge Media">
    <meta name="geo.region" content="IN-UP">
    <meta name="geo.placename" content="Gorakhpur">
    <meta name="geo.position" content="26.7606;83.3732">
    <meta name="ICBM" content="26.7606, 83.3732">

    <meta property="og:locale" content="en_IN">
    <meta property="og:type" content="{og_type}">
    <meta property="og:site_name" content="Our Edge Media">
    <meta property="og:title" content="{esc(title)}">
    <meta property="og:description" content="{esc(desc)}">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="{BASE}/assets/images/og-image.jpg">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:alt" content="Our Edge Media - Video Editing &amp; Social Media Agency in Gorakhpur">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{esc(title)}">
    <meta name="twitter:description" content="{esc(desc)}">
    <meta name="twitter:image" content="{BASE}/assets/images/og-image.jpg">

    <meta name="theme-color" content="#FFFFFF">
    <meta name="format-detection" content="telephone=yes">
    <link rel="icon" href="{root}favicon.ico" sizes="any">
    <link rel="icon" type="image/png" sizes="32x32" href="{root}assets/images/favicon-32.png">
    <link rel="apple-touch-icon" href="{root}assets/images/apple-touch-icon.png">
    <link rel="manifest" href="{root}site.webmanifest">
    <link rel="alternate" type="text/plain" title="LLM summary" href="{root}llms.txt">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preconnect" href="https://cdnjs.cloudflare.com" crossorigin>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lexend:wght@400;500;600;700&family=Source+Sans+3:wght@400;600;700&display=swap">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" crossorigin="anonymous" referrerpolicy="no-referrer">
    <link rel="stylesheet" href="{root}assets/css/site.css">
    <script>
        /* Hide animated elements only when motion is allowed; reveal anyway if GSAP fails to load */
        (function (d) {{
            if (window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches) return;
            d.classList.add("motion");
            var nav = null, seen = null;
            try {{ nav = sessionStorage.getItem("oem-nav"); seen = sessionStorage.getItem("oem-seen"); }} catch (e) {{}}
            if (nav || !seen) d.classList.add("curtain-on");      /* arriving from another page, or first visit */
            if (!seen) d.classList.add("curtain-intro");
            setTimeout(function () {{ d.classList.add("motion-failsafe"); }}, 3500);
        }})(document.documentElement);
    </script>
{extra_head}
    <script type="application/ld+json">
{ld}
    </script>
</head>
"""


def header(*, root, active):
    def link(href, label, mobile=False):
        cur = ' aria-current="page"' if href == active else ""
        arrow = '<i class="fa-solid fa-chevron-right" aria-hidden="true"></i>' if mobile else ""
        return f'<li><a href="{root}{href}"{cur}>{label}{arrow}</a></li>'
    landing_active = any(active == f for f, *_ in LANDING)
    CUR = ' aria-current="page"'
    dd_items = "".join(
        f'<li><a href="{root}{f}"{CUR if active == f else ""}><span class="dd-ic"><i class="{ic}" aria-hidden="true"></i></span>'
        f'<span><b>{lbl}</b><small>{d}</small></span></a></li>' for f, lbl, ic, d in LANDING)
    def desk_link(h, l):
        if h != "services.html":
            return link(h, l)
        cur = ' aria-current="page"' if (active == h or landing_active) else ""
        return f"""<li class="has-dd">
                    <a href="{root}services.html"{cur}>Services</a>
                    <button class="dd-toggle" type="button" aria-expanded="false" aria-controls="ddServices" aria-label="Show services menu"><i class="fa-solid fa-chevron-down" aria-hidden="true"></i></button>
                    <div class="dd" id="ddServices">
                        <ul>{dd_items}</ul>
                        <a class="dd-all" href="{root}services.html">All services <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
                    </div>
                </li>"""
    desk = "\n                ".join(desk_link(h, l) for h, l in NAV)
    mob_sub = "".join(f'<li><a href="{root}{f}">{lbl}</a></li>' for f, lbl, ic, d in LANDING)
    def mob_link(h, l):
        base = link(h, l, True)
        if h == "services.html":
            return base[:-5] + f'<ul class="mob-sub">{mob_sub}</ul></li>'
        return base
    mob = "\n                ".join(mob_link(h, l) for h, l in [("", "Home")] + NAV)
    return f"""<body>
<a class="skip-link" href="#main">Skip to content</a>

<header class="site-header">
    <div class="container header-inner">
        <a class="brand" href="{root}" aria-label="Our Edge Media home">
            <img class="brand-mark" src="{root}assets/images/logo-mark.webp" alt="" width="40" height="40">
            <span class="brand-text">Our Edge Media<small>Gorakhpur</small></span>
        </a>
        <nav class="nav-desktop" aria-label="Main">
            <ul>
                {desk}
            </ul>
        </nav>
        <a class="btn btn-primary header-cta" href="{root}about.html#contact">Get a free quote</a>
        <button class="menu-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mobileNav">
            <i class="fa-solid fa-bars" aria-hidden="true"></i>
        </button>
    </div>
</header>

<div class="mobile-nav" id="mobileNav" aria-hidden="true">
    <div class="mobile-nav-backdrop" data-close-nav></div>
    <nav class="mobile-nav-panel" aria-label="Mobile">
        <div class="mobile-nav-top">
            <a class="brand" href="{root}"><img class="brand-mark" src="{root}assets/images/logo-mark.webp" alt="" width="40" height="40"><span class="brand-text">Our Edge Media</span></a>
            <button class="menu-toggle" type="button" aria-label="Close menu" data-close-nav style="display:grid"><i class="fa-solid fa-xmark" aria-hidden="true"></i></button>
        </div>
        <ul>
                {mob}
        </ul>
        <div class="mobile-nav-foot">
            <a class="btn btn-primary btn-block" href="{root}about.html#contact" data-close-nav>Get a free quote</a>
            <a class="btn btn-wa btn-block" href="{WA}" target="_blank" rel="noopener"><i class="fa-brands fa-whatsapp" aria-hidden="true"></i> WhatsApp us</a>
            <p>Mon–Sat, 10 AM – 8 PM · Golghar, Gorakhpur</p>
        </div>
    </nav>
</div>
"""


def cta_band(root, title="Ready to grow your business online?",
             text="Tell us about your brand. We'll reply within a few hours with ideas and a clear quote. No pressure, no lock-in."):
    return f"""
<section class="section-tight">
    <div class="container">
        <div class="cta-band reveal">
            <div>
                <h2>{title}</h2>
                <p>{text}</p>
            </div>
            <div class="actions">
                <a class="btn btn-light" href="{root}about.html#contact">Get a free quote <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
                <a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener"><i class="fa-brands fa-whatsapp" aria-hidden="true"></i> WhatsApp</a>
            </div>
        </div>
    </div>
</section>
"""


def footer(*, root, flush=False, extra_scripts=""):
    return f"""
<footer class="site-footer{' flush' if flush else ''}">
    <div class="container">
        <div class="footer-grid">
            <div>
                <a class="footer-logo" href="{root}" aria-label="Our Edge Media home"><img src="{root}assets/images/logo-full-light.webp" alt="Our Edge Media - Your growth, our edge" width="520" height="456" loading="lazy" decoding="async"></a>
                <p class="footer-about">Video editing, Reels, ad films, graphic design and social media management for businesses and creators in Gorakhpur and across India.</p>
                <div class="footer-social">
                    <a href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="fa-brands fa-whatsapp" aria-hidden="true"></i></a>
                    <a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram"><i class="fa-brands fa-instagram" aria-hidden="true"></i></a>
                    <a href="mailto:{EMAIL}" aria-label="Email"><i class="fa-solid fa-envelope" aria-hidden="true"></i></a>
                    <a href="{MAPS}" target="_blank" rel="noopener" aria-label="Google Maps location"><i class="fa-solid fa-location-dot" aria-hidden="true"></i></a>
                </div>
            </div>
            <div>
                <h2>Company</h2>
                <ul class="footer-links">
                    <li><a href="{root}about.html">About us</a></li>
                    <li><a href="{root}OurTeam.html">Our team</a></li>
                    <li><a href="{root}Portfolio.html">Our work</a></li>
                    <li><a href="{root}blog/">Blog</a></li>
                    <li><a href="{root}RegistrationForm.html">Start a project</a></li>
                </ul>
            </div>
            <div>
                <h2>Services in Gorakhpur</h2>
                <ul class="footer-links">
                    {"".join(f'<li><a href="{root}{f}">{lbl}</a></li>' for f, lbl, ic, d in LANDING)}
                    <li><a href="{root}Pricing.html">Pricing &amp; packages</a></li>
                </ul>
            </div>
            <div>
                <h2>Visit or call</h2>
                <ul class="footer-contact">
                    <li><i class="fa-solid fa-location-dot" aria-hidden="true"></i><a href="{MAPS}" target="_blank" rel="noopener">{ADDRESS}</a></li>
                    <li><i class="fa-solid fa-phone" aria-hidden="true"></i><a href="tel:{PHONE}">{PHONE_DISPLAY}</a></li>
                    <li><i class="fa-solid fa-envelope" aria-hidden="true"></i><a href="mailto:{EMAIL}">{EMAIL}</a></li>
                    <li><i class="fa-regular fa-clock" aria-hidden="true"></i><span>Mon – Sat: 10:00 AM – 8:00 PM IST</span></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <span>© <span data-year>2026</span> Our Edge Media, Gorakhpur. All rights reserved.</span>
            <span>Designed &amp; developed by Abhishek Rajbhar</span>
        </div>
    </div>
</footer>

<div class="fab-stack">
    <button class="to-top" type="button" aria-label="Back to top"><i class="fa-solid fa-arrow-up" aria-hidden="true"></i></button>
    <a class="fab fab-wa" href="{WA}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp"><i class="fa-brands fa-whatsapp" aria-hidden="true"></i></a>
    <button class="fab fab-chat" type="button" aria-label="Open quick help chat" aria-expanded="false" aria-controls="chatPanel"><i class="fa-regular fa-comment-dots" aria-hidden="true"></i></button>
</div>

<div class="chat-panel" id="chatPanel" role="dialog" aria-label="Quick help" aria-hidden="true">
    <div class="chat-head">
        <span class="av" aria-hidden="true"><i class="fa-solid fa-headset"></i></span>
        <div><b>Quick help</b><small>Our Edge Media · usually replies instantly</small></div>
        <button class="chat-close" type="button" aria-label="Close chat"><i class="fa-solid fa-xmark" aria-hidden="true"></i></button>
    </div>
    <div class="chat-body" aria-live="polite">
        <div class="chat-msg bot">Namaste! How can we help? Tap a question or type your own.</div>
        <div class="chat-quick">
            <button type="button">Pricing</button>
            <button type="button">Delivery time</button>
            <button type="button">Services</button>
            <button type="button">Office location</button>
        </div>
    </div>
    <form class="chat-form">
        <label class="sr-only" for="chatInput">Your question</label>
        <input id="chatInput" type="text" placeholder="Ask anything…" autocomplete="off" maxlength="300">
        <button type="submit" aria-label="Send"><i class="fa-solid fa-paper-plane" aria-hidden="true"></i></button>
    </form>
</div>

<script src="{GSAP_JS}" defer></script>
<script src="{SCROLLTRIGGER_JS}" defer></script>
<script src="{root}sheet-api.js" defer></script>
<script src="{root}assets/js/site.js" defer></script>
<script src="{root}assets/js/motion.js" defer></script>
{extra_scripts}
</body>
</html>
"""


def faq_html(faqs, center=False):
    out = [f'<div class="faq{" center" if center else ""}">']
    for q, a in faqs:
        out.append(f'<details class="reveal"><summary>{esc(q)}</summary><div class="answer"><p>{a}</p></div></details>')
    out.append("</div>")
    return "\n".join(out)


def faq_schema(faqs):
    import re
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in faqs]}


def org_schema():
    return {
        "@type": "ProfessionalService", "@id": ORG_ID, "name": "Our Edge Media", "alternateName": "Digixlonline",
        "description": "Video editing, Reels, ad video production, graphic design and social media management agency in Gorakhpur, Uttar Pradesh.",
        "url": BASE + "/", "logo": BASE + "/assets/images/icon-512.png", "image": BASE + "/assets/images/og-image.jpg",
        "telephone": PHONE, "email": EMAIL, "priceRange": "₹₹",
        "founder": {"@type": "Person", "name": "Abhishek Rajbhar"},
        "address": {"@type": "PostalAddress", "streetAddress": "Bank Road, Golghar, near St. Andrew's College",
                    "addressLocality": "Gorakhpur", "addressRegion": "Uttar Pradesh", "postalCode": "273001", "addressCountry": "IN"},
        "geo": {"@type": "GeoCoordinates", "latitude": 26.7606, "longitude": 83.3732},
        "hasMap": MAPS,
        "areaServed": [{"@type": "City", "name": "Gorakhpur"}, {"@type": "AdministrativeArea", "name": "Uttar Pradesh"}, {"@type": "Country", "name": "India"}],
        "openingHoursSpecification": {"@type": "OpeningHoursSpecification",
                                      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
                                      "opens": "10:00", "closes": "20:00"},
        "knowsAbout": ["Video editing", "Reels editing", "YouTube video editing", "Ad video production",
                       "Graphic design", "Social media management", "Local SEO", "Instagram marketing"],
        "sameAs": [IG],
    }


def website_schema():
    return {"@type": "WebSite", "@id": BASE + "/#website", "url": BASE + "/", "name": "Our Edge Media",
            "inLanguage": "en-IN", "publisher": {"@id": ORG_ID}}


# ---------------------------------------------------------------------------
# Storytelling: every page is a chapter, and each page leads into the next one.
# ---------------------------------------------------------------------------
CHAPTERS = [  # (file, href-from-root, short name, chapter line)
    ("index.html", "", "Home", "Where it begins"),
    ("services.html", "services.html", "Services", "What we do"),
    ("Portfolio.html", "Portfolio.html", "Our Work", "The proof"),
    ("Pricing.html", "Pricing.html", "Pricing", "The plan"),
    ("OurTeam.html", "OurTeam.html", "Team", "The people"),
    ("about.html", "about.html", "About & Contact", "Our story"),
    ("RegistrationForm.html", "RegistrationForm.html", "Start a project", "Your chapter"),
    ("blog/index.html", "blog/", "Blog", "Keep learning"),
]


def chapter_of(file):
    """(number label, name, line) for the curtain on this page."""
    for i, (f, h, n, line) in enumerate(CHAPTERS, start=1):
        if f == file:
            return f"Chapter {i:02d}", n, line
    for f, lbl, ic, d in LANDING:
        if f == file:
            return "Deep dive", lbl + " in Gorakhpur", "Chapter 02 · Services"
    if file.startswith("blog/"):
        return "Chapter 08", "Blog", "A story for your business"
    return "Our Edge Media", "Gorakhpur", ""


def default_next(file):
    """Where the 'Next chapter' block leads from this page."""
    files = [c[0] for c in CHAPTERS]
    if file in files:
        i = files.index(file)
        f, h, n, line = CHAPTERS[(i + 1) % len(CHAPTERS)]
        return h, f"Chapter {((i + 1) % len(CHAPTERS)) + 1:02d}", n, line
    if any(file == f for f, *_ in LANDING):
        return "Pricing.html", "Chapter 04", "Pricing", "See what it costs"
    return "", "Chapter 01", "Home", "Back to the beginning"


def chapter_map_json(root):
    m = {}
    for i, (f, h, n, line) in enumerate(CHAPTERS, start=1):
        m[h or "index.html"] = [f"Chapter {i:02d}", n]
    for f, lbl, ic, d in LANDING:
        m[f] = ["Deep dive", lbl]
    return json.dumps(m, ensure_ascii=False)


def curtain(root, file):
    num, name, line = chapter_of(file)
    return f"""<div class="curtain" aria-hidden="true" data-map='{chapter_map_json(root)}'>
    <div class="curtain-panel curtain-yellow"></div>
    <div class="curtain-panel curtain-black">
        <div class="curtain-inner">
            <img class="curtain-logo" src="{root}assets/images/logo-mark.webp" alt="" width="64" height="64">
            <span class="curtain-num">{num}</span>
            <span class="curtain-title">{esc(name)}</span>
            <span class="curtain-line">{esc(line)}</span>
        </div>
    </div>
</div>
<div class="read-progress" aria-hidden="true"><span></span></div>
"""


def next_chapter(root, nxt):
    href, num, name, line = nxt
    return f"""
<section class="next-chapter" aria-label="Next chapter">
    <a class="next-link" href="{root}{href}">
        <span class="next-kicker"><span class="next-dot"></span> Next · {num}</span>
        <span class="next-title">{esc(name)}</span>
        <span class="next-line">{esc(line)} <i class="fa-solid fa-arrow-right-long" aria-hidden="true"></i></span>
    </a>
</section>
"""


def page(*, file, root, path, title, desc, active, body, crumbs=None, schema=None, og_type="website", flush=False,
         extra_scripts="", robots=None, extra_head="", next_ch=None):
    kw = {}
    if robots:
        kw["robots"] = robots
    doc = head(root=root, path=path, title=title, desc=desc, crumbs=crumbs, schema=schema, og_type=og_type,
               extra_head=extra_head, **kw)
    doc += header(root=root, active=active).replace("<body>\n", "<body>\n" + curtain(root, file), 1)
    story_end = "" if file == "404.html" else next_chapter(root, next_ch or default_next(file))
    doc += '<main id="main">\n' + body + story_end + "\n</main>\n"
    doc += footer(root=root, flush=flush, extra_scripts=extra_scripts)
    with open(file, "w", encoding="utf-8", newline="\n") as f:
        f.write(doc)
    print("wrote", file)
