/* Our Edge Media — GSAP storytelling layer.
   - Pages are chapters: a yellow/black curtain carries you from one page to the next.
   - Every card type has its own entrance; headings reveal word by word.
   - Content is always readable: without GSAP, or with reduced motion, nothing here runs
     and site.js / CSS show everything in its final state. */
(function () {
    "use strict";
    var root = document.documentElement;
    if (!window.gsap || !window.ScrollTrigger || !root.classList.contains("motion")) return;

    var gsap = window.gsap, ST = window.ScrollTrigger;
    gsap.registerPlugin(ST);
    root.classList.add("motion-live");
    gsap.defaults({ ease: "power3.out", duration: 0.9 });

    var $ = function (s, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(s)); };
    var finePointer = window.matchMedia("(hover: hover) and (pointer: fine)").matches;
    var store = { get: function (k) { try { return sessionStorage.getItem(k); } catch (e) { return null; } },
                  set: function (k, v) { try { sessionStorage.setItem(k, v); } catch (e) {} },
                  del: function (k) { try { sessionStorage.removeItem(k); } catch (e) {} } };

    /* ======================================================================
       1. CHAPTER CURTAIN — arrive & leave
       ====================================================================== */
    var curtain = document.querySelector(".curtain");
    var cy = curtain && curtain.querySelector(".curtain-yellow");
    var cb = curtain && curtain.querySelector(".curtain-black");
    var cInner = curtain && $(".curtain-inner > *", curtain);
    var introDelay = 0;

    if (curtain && root.classList.contains("curtain-on")) {
        var isIntro = root.classList.contains("curtain-intro");
        store.del("oem-nav"); store.set("oem-seen", "1");
        gsap.set([cy, cb], { yPercent: 0 });
        var arrive = gsap.timeline({ onComplete: function () { root.classList.remove("curtain-on", "curtain-intro"); gsap.set(curtain, { clearProps: "all" }); } });
        if (isIntro) {   // first visit: short brand intro
            arrive.fromTo(".curtain-logo", { scale: 0.4, rotate: -90, autoAlpha: 0 }, { scale: 1, rotate: 0, autoAlpha: 1, duration: 0.55, ease: "back.out(1.8)" })
                  .fromTo($(".curtain-num, .curtain-title, .curtain-line", curtain), { y: 26, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 0.4, stagger: 0.06 }, "-=0.25")
                  .to({}, { duration: 0.2 });
        } else {         // page-to-page: label already shown on the closing curtain
            arrive.set(cInner, { autoAlpha: 1 }).to({}, { duration: 0.15 });
        }
        arrive.to(cInner, { y: -30, autoAlpha: 0, duration: 0.35, stagger: 0.03, ease: "power2.in" })
              .to(cb, { yPercent: -100, duration: 0.75, ease: "expo.inOut" }, "-=0.1")
              .to(cy, { yPercent: -100, duration: 0.75, ease: "expo.inOut" }, "-=0.62");
        introDelay = arrive.duration() - 0.55;
    }

    function chapterFor(url) {
        try {
            var map = JSON.parse(curtain.getAttribute("data-map") || "{}");
            var p = url.pathname.replace(/\/+$/, "/");
            if (/\/blog\/$/.test(p)) return map["blog/"];
            if (/\/blog\/[^/]+\.html$/.test(p)) return ["Chapter 08", "Blog"];
            var file = p.split("/").pop() || "index.html";
            return map[file] || ["Our Edge Media", "Gorakhpur"];
        } catch (e) { return ["Our Edge Media", "Gorakhpur"]; }
    }

    function leaveTo(href) {
        var url = new URL(href, location.href);
        var ch = chapterFor(url);
        curtain.querySelector(".curtain-num").textContent = ch[0];
        curtain.querySelector(".curtain-title").textContent = ch[1];
        curtain.querySelector(".curtain-line").textContent = "";
        store.set("oem-nav", "1");
        root.classList.add("curtain-on");
        gsap.timeline({ onComplete: function () { location.href = href; } })
            .set(curtain, { visibility: "visible" })
            .fromTo(cy, { yPercent: 100 }, { yPercent: 0, duration: 0.5, ease: "expo.inOut" })
            .fromTo(cb, { yPercent: 100 }, { yPercent: 0, duration: 0.5, ease: "expo.inOut" }, "-=0.38")
            .fromTo(cInner, { y: 30, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 0.3, stagger: 0.04 }, "-=0.15");
    }

    if (curtain) {
        document.addEventListener("click", function (e) {
            var a = e.target.closest && e.target.closest("a[href]");
            if (!a || e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
            if (a.target === "_blank" || a.hasAttribute("download") || a.hasAttribute("data-no-curtain")) return;
            var href = a.getAttribute("href");
            if (!href || href.charAt(0) === "#" || /^(mailto:|tel:|javascript:)/i.test(href)) return;
            var url = new URL(a.href, location.href);
            if (url.origin !== location.origin) return;
            if (url.pathname === location.pathname && url.hash) return;   // same-page anchor
            if (!/(\.html|\/)$/.test(url.pathname)) return;                // files, videos, etc.
            e.preventDefault();
            if (document.body.classList.contains("nav-open")) document.body.classList.remove("nav-open");
            leaveTo(a.href);
        });
        // prefetch the next chapter on hover so it opens instantly
        var prefetched = {};
        document.addEventListener("pointerover", function (e) {
            var a = e.target.closest && e.target.closest("a[href]");
            if (!a || prefetched[a.href]) return;
            var url = new URL(a.href, location.href);
            if (url.origin !== location.origin || !/(\.html|\/)$/.test(url.pathname) || url.pathname === location.pathname) return;
            prefetched[a.href] = 1;
            var l = document.createElement("link"); l.rel = "prefetch"; l.href = url.pathname; document.head.appendChild(l);
        });
        // back/forward cache: never come back to a closed curtain
        window.addEventListener("pageshow", function (ev) {
            if (ev.persisted) { root.classList.remove("curtain-on"); gsap.set([cy, cb], { yPercent: -100 }); gsap.set(curtain, { clearProps: "visibility" }); store.del("oem-nav"); }
        });
    }

    /* ======================================================================
       2. HELPERS
       ====================================================================== */
    function splitWords(el) {
        if (!el || el.dataset.split) return [];
        el.dataset.split = "1";
        var words = [];
        Array.prototype.slice.call(el.childNodes).forEach(function (node) {
            if (node.nodeType === 3) {
                var frag = document.createDocumentFragment();
                node.textContent.split(/(\s+)/).forEach(function (part) {
                    if (!part) return;
                    if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(part)); return; }
                    var outer = document.createElement("span"); outer.className = "w";
                    var inner = document.createElement("span"); inner.className = "wi"; inner.textContent = part;
                    outer.appendChild(inner); frag.appendChild(outer); words.push(inner);
                });
                node.parentNode.replaceChild(frag, node);
            } else if (node.nodeType === 1) {
                var outer = document.createElement("span"); outer.className = "w";
                node.parentNode.insertBefore(outer, node);
                node.classList.add("wi"); outer.appendChild(node); words.push(node);
            }
        });
        return words;
    }

    /* Scroll-triggered entrance registry: every animated element is shown once,
       and a safety sweep shows anything that is already on screen. */
    var registry = [];
    function enter(selector, fromVars, toVars, opts) {
        opts = opts || {};
        var els = $(selector).filter(function (el) { return !el.__anim; });
        if (!els.length) return;
        els.forEach(function (el) { el.__anim = true; el.style.transition = "none"; });
        gsap.set(els, fromVars);
        var run = function (batch) {
            batch = batch.filter(function (el) { return !el.__done; });
            if (!batch.length) return;
            batch.forEach(function (el) { el.__done = true; });
            var v = Object.assign({ autoAlpha: 1, overwrite: true, stagger: opts.stagger != null ? opts.stagger : 0.1,
                onComplete: function () {
                    batch.forEach(function (el) { el.classList.add("in"); });
                    gsap.set(batch, { clearProps: "transform,clipPath,filter" });
                    if (opts.after) opts.after(batch);
                } }, toVars);
            gsap.to(batch, v);
            if (opts.inner) batch.forEach(function (el) { opts.inner(el); });
        };
        registry.push({ els: els, run: run });
        ST.batch(els, { start: opts.start || "top 88%", once: true, onEnter: run, onEnterBack: run, onLeave: run });
    }
    function sweep() {
        var h = window.innerHeight;
        registry.forEach(function (r) {
            var due = r.els.filter(function (el) { return !el.__done && el.getBoundingClientRect().top < h; });
            if (due.length) r.run(due);
        });
    }
    ST.addEventListener("scrollEnd", sweep);
    ST.addEventListener("refresh", sweep);

    /* ======================================================================
       3. HEROES
       ====================================================================== */
    var hero = document.querySelector(".hero");
    if (hero) {
        var hw = splitWords(hero.querySelector("h1"));
        var tl = gsap.timeline({ delay: introDelay, defaults: { ease: "expo.out" } });
        tl.fromTo(".hero-badge", { y: -16, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 0.7 })
          .fromTo(hw, { yPercent: 115 }, { yPercent: 0, duration: 1.1, stagger: 0.06 }, "-=0.35")
          .fromTo(".hero-lead", { y: 20, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 0.8 }, "-=0.75")
          .fromTo(".hero-actions > *", { y: 18, autoAlpha: 0 }, { y: 0, autoAlpha: 1, stagger: 0.1, duration: 0.7 }, "-=0.6")
          .fromTo(".hero-proof > div", { y: 18, autoAlpha: 0 }, { y: 0, autoAlpha: 1, stagger: 0.08, duration: 0.7 }, "-=0.55")
          .fromTo(".hero-visual figure", { clipPath: "inset(100% 0% 0% 0% round 22px)" }, { clipPath: "inset(0% 0% 0% 0% round 22px)", duration: 1.3, stagger: 0.12, ease: "expo.inOut" }, 0.2)
          .fromTo(".hero-visual img", { scale: 1.3 }, { scale: 1, duration: 1.6, stagger: 0.12 }, 0.35)
          .fromTo(".hero-chip", { y: 24, scale: 0.9, autoAlpha: 0 }, { y: 0, scale: 1, autoAlpha: 1, duration: 0.8, ease: "back.out(1.6)" }, "-=0.6");
        $(".hero-visual figure").forEach(function (fig, i) {
            gsap.to(fig, { yPercent: (i % 2 ? -12 : -6), ease: "none", scrollTrigger: { trigger: hero, start: "top top", end: "bottom top", scrub: true } });
        });
        gsap.to(".hero-chip", { y: -10, duration: 2.4, ease: "sine.inOut", yoyo: true, repeat: -1, delay: 2 + introDelay });
        // story: hero content drifts away as the next chapter scrolls in
        gsap.to(hero.querySelector(".hero-grid > div"), { yPercent: -12, autoAlpha: 0.25, ease: "none",
            scrollTrigger: { trigger: hero, start: "center top+=30%", end: "bottom top", scrub: true } });
    }

    $(".page-hero h1, .article-hero h1, .landing-hero h1").forEach(function (h) {
        var w = splitWords(h), parent = h.parentElement;
        gsap.timeline({ delay: introDelay, defaults: { ease: "expo.out" } })
            .fromTo(w, { yPercent: 115 }, { yPercent: 0, duration: 1, stagger: 0.045 })
            .fromTo($(".breadcrumb, .eyebrow", parent), { autoAlpha: 0, y: -10 }, { autoAlpha: 1, y: 0, duration: 0.6, stagger: 0.08 }, 0)
            .fromTo($(":scope > p, .lead, .article-meta, .stack-actions, .chips, .landing-points, .team-stats", parent), { autoAlpha: 0, y: 18 }, { autoAlpha: 1, y: 0, stagger: 0.08, duration: 0.8 }, "-=0.7");
    });

    /* ======================================================================
       4. HEADINGS — every section title reveals word by word
       ====================================================================== */
    $(".section-head").forEach(function (head) {
        var h2 = head.querySelector("h2");
        var w = splitWords(h2);
        head.__anim = true; head.__done = true; head.style.transition = "none";
        gsap.set(head, { autoAlpha: 1, y: 0 });
        var rest = $(".eyebrow, p, .btn", head);
        gsap.set(w, { yPercent: 115 }); gsap.set(rest, { autoAlpha: 0, y: 16 });
        var play = function () {
            if (head.__played) return; head.__played = true;
            gsap.timeline({ defaults: { ease: "expo.out" } })
                .fromTo(head.querySelector(".eyebrow"), { "--eb": 0 }, { "--eb": 1, duration: 0.8 }, 0)
                .to(w, { yPercent: 0, duration: 1, stagger: 0.05 }, 0)
                .to(rest, { autoAlpha: 1, y: 0, duration: 0.7, stagger: 0.08 }, 0.25);
        };
        ST.create({ trigger: head, start: "top 88%", once: true, onEnter: play, onEnterBack: play, onLeave: play });
        registry.push({ els: [head], run: function () { play(); } });
    });
    $(".split-copy h2, .showreel-copy h2, .cta-band h2, .statement-title").forEach(function (h) {
        var w = splitWords(h);
        gsap.fromTo(w, { yPercent: 115 }, { yPercent: 0, duration: 1, stagger: 0.05, ease: "expo.out",
            scrollTrigger: { trigger: h, start: "top 88%", once: true } });
    });

    /* ======================================================================
       5. CARDS — each card type has its own entrance
       ====================================================================== */
    // Service cards fold down like pages of a book
    enter(".service-card", { autoAlpha: 0, rotateX: -70, y: 50, transformOrigin: "50% 0%", transformPerspective: 900 },
          { rotateX: 0, y: 0, duration: 1.1, stagger: 0.12, ease: "expo.out" });
    // Portfolio cards unmask from the bottom while the media settles
    enter(".work-card", { autoAlpha: 0, clipPath: "inset(100% 0% 0% 0% round 14px)", y: 40 },
          { clipPath: "inset(0% 0% 0% 0% round 14px)", y: 0, duration: 1.1, stagger: 0.1, ease: "expo.out" },
          { inner: function (el) { var m = el.querySelector(".work-body"); if (m) gsap.fromTo(m.children, { y: 20, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 0.6, stagger: 0.06, delay: 0.35 }); } });
    // Blog cards slide up with a slight tilt
    enter(".post-card", { autoAlpha: 0, y: 80, rotate: 2.5 }, { y: 0, rotate: 0, duration: 1, stagger: 0.12, ease: "expo.out" });
    // Pricing plans rise in 3D, the featured plan lands last with a bounce
    enter(".plan", { autoAlpha: 0, y: 90, rotateX: 25, transformPerspective: 1000 }, { y: 0, rotateX: 0, duration: 1.1, stagger: 0.14, ease: "back.out(1.3)" });
    // Industry cards pop in from the centre
    enter(".industry", { autoAlpha: 0, scale: 0.6, rotate: -6 }, { scale: 1, rotate: 0, duration: 0.8, stagger: { each: 0.07, from: "center" }, ease: "back.out(1.7)" });
    // Feature list: alternate from left and right
    $(".feature-list li").forEach(function (li, i) { li.classList.add(i % 2 ? "from-r" : "from-l"); });
    enter(".feature-list li.from-l", { autoAlpha: 0, x: -60 }, { x: 0, duration: 0.9, stagger: 0.1 });
    enter(".feature-list li.from-r", { autoAlpha: 0, x: 60 }, { x: 0, duration: 0.9, stagger: 0.1 });
    // Deliverables zig-zag
    $(".deliverables li").forEach(function (li, i) { li.classList.add(i % 2 ? "from-r" : "from-l"); });
    enter(".deliverables li.from-l", { autoAlpha: 0, x: -50 }, { x: 0, duration: 0.8, stagger: 0.08 });
    enter(".deliverables li.from-r", { autoAlpha: 0, x: 50 }, { x: 0, duration: 0.8, stagger: 0.08 });
    // Services page rows: image and copy slide in from opposite sides
    $(".split-row").forEach(function (row) {
        var flip = row.classList.contains("flip");
        var media = row.querySelector(".split-media"), copy = row.querySelector(".split-copy");
        if (media) { media.classList.add(flip ? "from-r" : "from-l"); }
        if (copy) { copy.classList.add(flip ? "from-l" : "from-r"); }
    });
    enter(".split-media.from-l", { autoAlpha: 0, x: -80, clipPath: "inset(0% 100% 0% 0% round 22px)" }, { x: 0, clipPath: "inset(0% 0% 0% 0% round 22px)", duration: 1.2, ease: "expo.inOut" }, { stagger: 0 });
    enter(".split-media.from-r", { autoAlpha: 0, x: 80, clipPath: "inset(0% 0% 0% 100% round 22px)" }, { x: 0, clipPath: "inset(0% 0% 0% 0% round 22px)", duration: 1.2, ease: "expo.inOut" }, { stagger: 0 });
    enter(".split-copy.from-l", { autoAlpha: 0, x: -50 }, { x: 0, duration: 1, delay: 0.15 }, { stagger: 0 });
    enter(".split-copy.from-r", { autoAlpha: 0, x: 50 }, { x: 0, duration: 1, delay: 0.15 }, { stagger: 0 });
    // Showreel and CTA band open from the centre
    enter(".showreel", { autoAlpha: 0, clipPath: "inset(12% 12% 12% 12% round 40px)" }, { clipPath: "inset(0% 0% 0% 0% round 22px)", duration: 1.3, ease: "expo.inOut" }, { stagger: 0 });
    enter(".cta-band", { autoAlpha: 0, scale: 0.88, y: 40 }, { scale: 1, y: 0, duration: 1.1, ease: "expo.out" }, { stagger: 0 });
    // Stats band counts up block by block
    enter(".stats-band > div, .stats > div", { autoAlpha: 0, y: 40 }, { y: 0, duration: 0.8, stagger: 0.1 });
    // FAQ, contact list, link cards, generic cards
    enter(".faq details", { autoAlpha: 0, x: 40 }, { x: 0, duration: 0.7, stagger: 0.07 });
    enter(".contact-list li", { autoAlpha: 0, x: -40 }, { x: 0, duration: 0.7, stagger: 0.08 });
    enter(".link-cards a", { autoAlpha: 0, y: 30, scale: 0.95 }, { y: 0, scale: 1, duration: 0.7, stagger: 0.07 });
    enter(".card", { autoAlpha: 0, y: 60, rotateY: 12, transformPerspective: 900 }, { y: 0, rotateY: 0, duration: 1, stagger: 0.1 });
    enter(".form-card", { autoAlpha: 0, y: 60, scale: 0.97 }, { y: 0, scale: 1, duration: 1 }, { stagger: 0 });
    // Chips pop one after another
    $(".chips").forEach(function (list) {
        var items = $("li", list);
        if (!items.length || list.closest(".page-hero, .landing-hero")) return;
        gsap.fromTo(items, { scale: 0, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, duration: 0.45, stagger: 0.035, ease: "back.out(2)",
            scrollTrigger: { trigger: list, start: "top 92%", once: true } });
    });
    // Anything else marked .reveal: soft rise
    enter(".reveal", { autoAlpha: 0, y: 34 }, { y: 0, duration: 0.9, stagger: 0.09 });

    /* ======================================================================
       6. SCROLL STORY — counters, marquee, process, media, statement
       ====================================================================== */
    $("[data-count]").forEach(function (el) {
        var end = parseFloat(el.getAttribute("data-count")), suffix = el.getAttribute("data-suffix") || "", obj = { v: 0 };
        el.textContent = "0" + suffix;
        gsap.to(obj, { v: end, duration: 2, ease: "power2.out", delay: el.closest(".hero, .page-hero") ? introDelay : 0,
            scrollTrigger: { trigger: el, start: "top 92%", once: true },
            onUpdate: function () { el.textContent = Math.round(obj.v).toLocaleString("en-IN") + suffix; } });
    });

    $(".marquee-track").forEach(function (track) {
        var tween = gsap.fromTo(track, { xPercent: 0 }, { xPercent: -50, duration: parseFloat(track.getAttribute("data-speed") || 40), ease: "none", repeat: -1 });
        ST.create({ trigger: track, start: "top bottom", end: "bottom top", onToggle: function (self) { self.isActive ? tween.play() : tween.pause(); },
            onUpdate: function (self) { var v = Math.min(Math.abs(self.getVelocity()) / 600, 3); gsap.to(tween, { timeScale: (self.direction || 1) * (1 + v), duration: 0.3, overwrite: true }); gsap.to(tween, { timeScale: 1, duration: 1, delay: 0.3 }); } });
    });

    $(".process-wrap").forEach(function (wrap) {
        var bar = wrap.querySelector(".process-bar span");
        if (bar) gsap.fromTo(bar, { scaleX: 0 }, { scaleX: 1, ease: "none", scrollTrigger: { trigger: wrap, start: "top 75%", end: "bottom 60%", scrub: 0.6 } });
        var steps = $(".process li", wrap);
        gsap.fromTo(steps, { y: 60, autoAlpha: 0, rotateX: -40, transformPerspective: 800, transformOrigin: "50% 0%" },
            { y: 0, autoAlpha: 1, rotateX: 0, stagger: 0.15, duration: 1, ease: "expo.out", scrollTrigger: { trigger: wrap, start: "top 82%", once: true } });
    });

    $(".work-media img, .work-media video, .showreel-media img, .showreel-media video, .split-media img, .split-media video").forEach(function (m) {
        gsap.fromTo(m, { scale: 1.18 }, { scale: 1, ease: "none", scrollTrigger: { trigger: m, start: "top bottom", end: "bottom 40%", scrub: true } });
    });

    $(".statement").forEach(function (el) {
        var w = splitWords(el);
        gsap.fromTo(w, { opacity: 0.15, y: 8 }, { opacity: 1, y: 0, stagger: 0.05, ease: "none",
            scrollTrigger: { trigger: el, start: "top 80%", end: "bottom 45%", scrub: true } });
    });

    // Dark sections fade the page into night and back, like scene changes
    $(".section-navy").forEach(function (sec) {
        gsap.fromTo(sec, { clipPath: "inset(6% 4% 6% 4% round 32px)" }, { clipPath: "inset(0% 0% 0% 0% round 0px)", ease: "none",
            scrollTrigger: { trigger: sec, start: "top bottom", end: "top 35%", scrub: true } });
    });

    /* ======================================================================
       7. NEXT CHAPTER block
       ====================================================================== */
    $(".next-chapter").forEach(function (sec) {
        var title = sec.querySelector(".next-title");
        var w = splitWords(title);
        gsap.timeline({ scrollTrigger: { trigger: sec, start: "top 85%", once: true } })
            .fromTo(sec.querySelector(".next-kicker"), { y: 20, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 0.6 })
            .fromTo(w, { yPercent: 115 }, { yPercent: 0, duration: 1.1, stagger: 0.07, ease: "expo.out" }, "-=0.3")
            .fromTo(sec.querySelector(".next-line"), { y: 20, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 0.6 }, "-=0.6");
        gsap.fromTo(title, { xPercent: 6 }, { xPercent: -4, ease: "none", scrollTrigger: { trigger: sec, start: "top bottom", end: "bottom top", scrub: true } });
    });

    /* ======================================================================
       8. STORY CUES — reading progress
       ====================================================================== */
    var prog = document.querySelector(".read-progress span");
    if (prog) gsap.fromTo(prog, { scaleX: 0 }, { scaleX: 1, ease: "none", scrollTrigger: { start: 0, end: "max", scrub: 0.3 } });


    /* ======================================================================
       9. MOUSE — magnetic buttons, 3D tilt cards, spotlight
       ====================================================================== */
    if (finePointer) {
        $(".btn-primary, .btn-light, .fab").forEach(function (btn) {
            var xTo = gsap.quickTo(btn, "x", { duration: 0.5 }), yTo = gsap.quickTo(btn, "y", { duration: 0.5 });
            btn.addEventListener("mousemove", function (e) { var r = btn.getBoundingClientRect(); xTo((e.clientX - r.left - r.width / 2) * 0.22); yTo((e.clientY - r.top - r.height / 2) * 0.3); });
            btn.addEventListener("mouseleave", function () { xTo(0); yTo(0); });
        });
        $(".card, .plan, .post-card, .work-card, .industry, .member").forEach(function (c) {
            c.addEventListener("pointermove", function (e) {
                var r = c.getBoundingClientRect(), px = (e.clientX - r.left) / r.width - 0.5, py = (e.clientY - r.top) / r.height - 0.5;
                c.style.setProperty("--mx", (e.clientX - r.left) + "px"); c.style.setProperty("--my", (e.clientY - r.top) + "px");
                if (!c.__done && c.__anim) return;   // wait until its entrance has finished
                gsap.to(c, { rotateY: px * 8, rotateX: -py * 8, y: -6, transformPerspective: 900, duration: 0.5, ease: "power2.out", overwrite: "auto" });
            });
            c.addEventListener("pointerleave", function () { gsap.to(c, { rotateY: 0, rotateX: 0, y: 0, duration: 0.7, ease: "elastic.out(1, 0.6)", overwrite: "auto" }); });
        });
    }

    /* ======================================================================
       10. HEADER hides on scroll down, returns on scroll up
       ====================================================================== */
    var header = document.querySelector(".site-header");
    if (header) {
        var showHeader = gsap.fromTo(header, { yPercent: -100 }, { yPercent: 0, paused: true, duration: 0.35, ease: "power2.out" }).progress(1);
        ST.create({ start: "top -120", end: "max", onUpdate: function (self) {
            if (document.body.classList.contains("nav-open")) return;
            self.direction === -1 ? showHeader.play() : showHeader.reverse();
        } });
    }

    window.addEventListener("load", function () { ST.refresh(); });
    setTimeout(sweep, 1500 + introDelay * 1000);
})();
