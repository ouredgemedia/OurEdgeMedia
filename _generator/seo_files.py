"""Regenerates sitemap.xml and llms.txt from the generator's page lists."""
from layout import BASE, LANDING, TODAY
import blog_posts as b
import landing

def build():
    pages = [("/", "1.0", "weekly", ["og-image.jpg", "editing.webp", "shoot.webp", "graphic-design.webp", "social-media.webp"]),
             ("/services.html", "0.9", "monthly", []), ("/Pricing.html", "0.9", "monthly", [])]
    pages += [("/" + f, "0.9", "monthly", []) for f, *_ in LANDING]
    pages += [("/Portfolio.html", "0.8", "weekly", ["shoot.webp", "graphic-design.webp", "social-media.webp"]),
              ("/about.html", "0.8", "monthly", []), ("/OurTeam.html", "0.7", "monthly", ["IMG_3922.webp", "anjali.webp"]),
              ("/RegistrationForm.html", "0.6", "yearly", []), ("/blog/", "0.8", "weekly", [])]
    pages += [("/blog/%s.html" % p["slug"], "0.7", "monthly", []) for p in b.POSTS]
    lastmod = {"/blog/%s.html" % p["slug"]: p["date"] for p in b.POSTS}
    o = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
         '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">']
    for path, pr, cf, imgs in pages:
        o.append("  <url>\n    <loc>%s%s</loc>\n    <lastmod>%s</lastmod>\n    <changefreq>%s</changefreq>\n    <priority>%s</priority>"
                 % (BASE, path, lastmod.get(path, "2026-11-22"), cf, pr))
        for i in imgs:
            o.append("    <image:image><image:loc>%s/assets/images/%s</image:loc></image:image>" % (BASE, i))
        o.append("  </url>")
    o.append("</urlset>")
    open("sitemap.xml", "w", encoding="utf-8", newline="\n").write("\n".join(o) + "\n")

    svc = "".join("- [%s](%s/%s): %s\n" % (pg["h1"][0].upper() + pg["h1"][1:], BASE, pg["file"], pg["desc"]) for pg in landing.PAGES)
    posts = "".join("- [%s](%s/blog/%s.html): %s\n" % (p["title"], BASE, p["slug"], p["excerpt"]) for p in b.POSTS)
    txt = f"""# Our Edge Media

> Our Edge Media (also known as Digixlonline) is a video editing, Reels and social media marketing agency based in Golghar, Gorakhpur, Uttar Pradesh, India. We edit high-retention Instagram Reels and YouTube Shorts, YouTube long-form videos and ad/promotional videos, design graphics and brand identities, manage social media accounts, and provide local SEO (Google Business Profile) for businesses and creators in Gorakhpur and across India.

- Founder: Abhishek Rajbhar
- Location: Bank Road, Golghar, near St. Andrew's College, Gorakhpur, Uttar Pradesh 273001, India
- Phone / WhatsApp: +91 9196497565
- Email: ouredgemedia@gmail.com
- Hours: Monday to Saturday, 10:00 to 20:00 IST
- Instagram: https://www.instagram.com/ouredgemedia/
- Team: 9 in-house specialists (video editors, graphic designer, SEO specialist, ad manager, social media manager)

## Main pages

- [Home]({BASE}/): Overview of the agency, services, work, pricing and FAQs
- [Services]({BASE}/services.html): All services in detail
- [Pricing]({BASE}/Pricing.html): Monthly social media packages and single video pricing
- [Our Work]({BASE}/Portfolio.html): Reels, promotion videos, drop-effect edits, ad creatives and design samples
- [Our Team]({BASE}/OurTeam.html): The people behind Our Edge Media
- [About & Contact]({BASE}/about.html): Agency story, values, office address, map and contact form

## Services in Gorakhpur

{svc}
## Pricing summary

- Starter: ₹12,000/month (10 posts, 8 Reels, 12 Stories)
- Growth: ₹20,000/month (10 posts, 10 Reels, 12 Stories, custom designs, premium editing, research, monthly report)
- Premium: ₹30,000/month (15 posts, 15 Reels, 12 Stories, strategy, campaign planning, ads guidance, priority support)
- Single ad videos: about ₹999–₹4,999 depending on length and effects

## Blog: guides for Gorakhpur businesses

- [Blog home]({BASE}/blog/): Social media, video and local SEO guides for Gorakhpur businesses
{posts}
## Work with us

- [Start a project]({BASE}/RegistrationForm.html): Register for per-project or monthly work
- [WhatsApp](https://wa.me/919196497565): Fastest way to get a quote

## Optional

- [Sitemap]({BASE}/sitemap.xml)
"""
    open("llms.txt", "w", encoding="utf-8", newline="\n").write(txt)
    print("sitemap urls:", len(pages))

if __name__ == "__main__":
    build()
