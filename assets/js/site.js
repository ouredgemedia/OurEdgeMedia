/* Our Edge Media — shared site behaviour (no dependencies) */
(function () {
    "use strict";
    document.documentElement.classList.add("js");
    var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    /* ---------- Header shadow + back-to-top ---------- */
    var header = document.querySelector(".site-header");
    var toTop = document.querySelector(".to-top");
    function onScroll() {
        var y = window.scrollY || document.documentElement.scrollTop;
        if (header) header.classList.toggle("scrolled", y > 8);
        if (toTop) toTop.classList.toggle("show", y > 600);
    }
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
    if (toTop) toTop.addEventListener("click", function () {
        window.scrollTo({ top: 0, behavior: reduceMotion ? "auto" : "smooth" });
    });

    /* ---------- Mobile navigation ---------- */
    var nav = document.getElementById("mobileNav");
    var openBtn = document.querySelector(".menu-toggle");
    if (nav && openBtn) {
        var closeEls = nav.querySelectorAll("[data-close-nav]");
        var setNav = function (open) {
            nav.classList.toggle("open", open);
            nav.setAttribute("aria-hidden", open ? "false" : "true");
            openBtn.setAttribute("aria-expanded", open ? "true" : "false");
            document.body.classList.toggle("nav-open", open);
            if (open) { var f = nav.querySelector("a, button"); if (f) f.focus(); } else { openBtn.focus(); }
        };
        openBtn.addEventListener("click", function () { setNav(true); });
        closeEls.forEach(function (el) { el.addEventListener("click", function () { setNav(false); }); });
        document.addEventListener("keydown", function (e) { if (e.key === "Escape" && nav.classList.contains("open")) setNav(false); });
    }

    /* ---------- Reveal on scroll ---------- */
    var reveals = document.querySelectorAll(".reveal");
    var gsapReady = !!(window.gsap && window.ScrollTrigger) && !reduceMotion;
    if (gsapReady) {
        /* motion.js animates these with GSAP */
    } else if ("IntersectionObserver" in window && !reduceMotion) {
        var io = new IntersectionObserver(function (entries) {
            entries.forEach(function (en) {
                // Reveal when visible, or when a fast scroll/jump skipped right past it
                if (en.isIntersecting || en.boundingClientRect.top < 0) { en.target.classList.add("in"); io.unobserve(en.target); }
            });
        }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
        reveals.forEach(function (el) { io.observe(el); });
        // Backup: on scroll, reveal anything that has reached the viewport
        var pending = Array.prototype.slice.call(reveals);
        var revealCheck = function () {
            var limit = window.innerHeight;
            pending = pending.filter(function (el) {
                if (el.classList.contains("in")) return false;
                if (el.getBoundingClientRect().top < limit) { el.classList.add("in"); return false; }
                return true;
            });
            if (!pending.length) window.removeEventListener("scroll", revealCheck);
        };
        window.addEventListener("scroll", revealCheck, { passive: true });
    } else {
        reveals.forEach(function (el) { el.classList.add("in"); });
    }

    /* ---------- Services dropdown (desktop) ---------- */
    document.querySelectorAll(".has-dd").forEach(function (item) {
        var btn = item.querySelector(".dd-toggle");
        if (!btn) return;
        var set = function (open) { item.classList.toggle("open", open); btn.setAttribute("aria-expanded", open ? "true" : "false"); };
        btn.addEventListener("click", function (e) { e.stopPropagation(); set(!item.classList.contains("open")); });
        item.addEventListener("mouseenter", function () { btn.setAttribute("aria-expanded", "true"); });
        item.addEventListener("mouseleave", function () { set(false); });
        item.addEventListener("focusout", function (e) { if (!item.contains(e.relatedTarget)) set(false); });
        document.addEventListener("click", function (e) { if (!item.contains(e.target)) set(false); });
        document.addEventListener("keydown", function (e) { if (e.key === "Escape" && item.classList.contains("open")) { set(false); btn.focus(); } });
    });

    /* ---------- Footer year ---------- */
    document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

    /* ---------- Portfolio filters ---------- */
    var filterBtns = document.querySelectorAll(".filter-btn");
    filterBtns.forEach(function (btn) {
        btn.addEventListener("click", function () {
            var f = btn.getAttribute("data-filter");
            filterBtns.forEach(function (b) { b.setAttribute("aria-pressed", b === btn ? "true" : "false"); });
            document.querySelectorAll(".work-card[data-cat]").forEach(function (card) {
                card.hidden = !(f === "all" || card.getAttribute("data-cat").indexOf(f) !== -1);
            });
        });
    });

    /* ---------- Video thumbnails = the videos themselves ----------
       Each card holds a muted <video> paused on a chosen frame. It only starts
       loading when it comes near the screen; on desktop it previews on hover. */
    var vthumbs = Array.prototype.slice.call(document.querySelectorAll("video.vthumb[data-src]"));
    var loadThumb = function (v) {
        if (v.getAttribute("src")) return;
        v.preload = "metadata";
        v.src = v.getAttribute("data-src");
    };
    if ("IntersectionObserver" in window) {
        var vio = new IntersectionObserver(function (entries) {
            entries.forEach(function (en) { if (en.isIntersecting) { loadThumb(en.target); vio.unobserve(en.target); } });
        }, { rootMargin: "400px 0px" });
        vthumbs.forEach(function (v) { vio.observe(v); });
    } else {
        vthumbs.forEach(loadThumb);
    }
    if (window.matchMedia("(hover: hover) and (pointer: fine)").matches && !reduceMotion) {
        vthumbs.forEach(function (v) {
            var box = v.parentElement;
            var start = function () { var m = (v.getAttribute("data-src") || "").match(/#t=([\d.]+)/); return m ? parseFloat(m[1]) : 0; };
            box.addEventListener("mouseenter", function () { loadThumb(v); var p = v.play(); if (p && p.catch) p.catch(function () {}); });
            box.addEventListener("mouseleave", function () { v.pause(); try { v.currentTime = start(); } catch (e) {} });
        });
    }

    /* ---------- Video modal ---------- */
    var modal = document.getElementById("videoModal");
    if (modal) {
        var video = modal.querySelector("video");
        var closeBtn = modal.querySelector(".modal-close");
        var lastTrigger = null;
        var closeModal = function () {
            modal.classList.remove("open");
            video.pause(); video.removeAttribute("src"); video.load();
            document.body.classList.remove("nav-open");
            if (lastTrigger) lastTrigger.focus();
        };
        document.querySelectorAll("[data-video]").forEach(function (btn) {
            btn.addEventListener("click", function () {
                lastTrigger = btn;
                if (btn.getAttribute("data-poster")) video.poster = btn.getAttribute("data-poster"); else video.removeAttribute("poster");
                video.src = btn.getAttribute("data-video");
                video.setAttribute("aria-label", btn.getAttribute("aria-label") || "Project video");
                modal.classList.add("open");
                document.body.classList.add("nav-open");
                closeBtn.focus();
                var p = video.play(); if (p && p.catch) p.catch(function () {});
            });
        });
        closeBtn.addEventListener("click", closeModal);
        modal.addEventListener("click", function (e) { if (e.target === modal) closeModal(); });
        document.addEventListener("keydown", function (e) { if (e.key === "Escape" && modal.classList.contains("open")) closeModal(); });
    }

    /* ---------- Chat assistant ---------- */
    var chatBtn = document.querySelector(".fab-chat");
    var panel = document.getElementById("chatPanel");
    if (chatBtn && panel) {
        var body = panel.querySelector(".chat-body");
        var form = panel.querySelector(".chat-form");
        var input = form.querySelector("input");
        var setChat = function (open) {
            panel.classList.toggle("open", open);
            panel.setAttribute("aria-hidden", open ? "false" : "true");
            chatBtn.setAttribute("aria-expanded", open ? "true" : "false");
            if (open) setTimeout(function () { input.focus(); }, 50);
        };
        chatBtn.addEventListener("click", function () { setChat(!panel.classList.contains("open")); });
        panel.querySelector(".chat-close").addEventListener("click", function () { setChat(false); chatBtn.focus(); });

        var addMsg = function (text, who) {
            var d = document.createElement("div");
            d.className = "chat-msg " + who;
            d.textContent = text;
            body.appendChild(d);
            body.scrollTop = body.scrollHeight;
        };
        var replyFor = function (t) {
            if (/price|rate|cost|charge|kitna|paisa|fee|plan|package/.test(t))
                return "Monthly social media plans: Starter ₹12,000 · Growth ₹20,000 · Premium ₹30,000. Single ad videos start around ₹999–₹4,999 depending on length and effects. See the Pricing page for everything included.";
            if (/deliver|time|days|kab|turnaround/.test(t))
                return "Most edits are delivered in 1–3 days, depending on the project size. Monthly clients get a fixed posting calendar.";
            if (/edit|video|reel|short|ad\b|ads|youtube/.test(t))
                return "We edit Reels & Shorts, ad videos, promotion videos, YouTube long-form, drop-effect reels and graphics, plus full social media management.";
            if (/portfolio|work|sample|example/.test(t))
                return "You can see our latest projects (with videos) on the Our Work page.";
            if (/where|location|address|office|gorakhpur/.test(t))
                return "Our office is at Bank Road, Golghar (near St. Andrew's College), Gorakhpur 273001. Open Mon–Sat, 10 AM – 8 PM.";
            if (/contact|whatsapp|call|phone|number|baat/.test(t))
                return "WhatsApp or call us on +91 91964 97565, or use the contact form on the About page. We usually reply within a few hours.";
            if (/hi|hello|hey|namaste/.test(t))
                return "Namaste! Ask me about pricing, services, delivery time or how to reach us.";
            return "Thanks! For a quick, exact answer, message us on WhatsApp at +91 91964 97565 and our team will help you.";
        };
        var handle = function (text) {
            var clean = (text || "").trim();
            if (!clean) return;
            addMsg(clean, "user");
            var reply = replyFor(clean.toLowerCase());
            setTimeout(function () {
                addMsg(reply, "bot");
                if (typeof sendToGoogleSheet === "function") {
                    sendToGoogleSheet({ formType: "chat", query: clean, reply: reply });
                }
            }, 350);
        };
        form.addEventListener("submit", function (e) { e.preventDefault(); handle(input.value); input.value = ""; });
        panel.querySelectorAll(".chat-quick button").forEach(function (b) {
            b.addEventListener("click", function () { handle(b.textContent); });
        });
    }
})();
