/* Our Edge Media — Team tree: growing branches, path highlight and animated profile cards */
(function () {
    "use strict";
    var org = document.getElementById("orgTree");
    var modal = document.getElementById("profileModal");
    var dataEl = document.getElementById("teamData");
    if (!org || !modal || !dataEl) return;

    var TEAM = JSON.parse(dataEl.textContent);
    var gsap = window.gsap;
    var motion = !!gsap && document.documentElement.classList.contains("motion");
    var $ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
    var nodes = $(".tnode", org);
    var trunk = org.querySelector(".ln-trunk");
    var bar = org.querySelector(".ln-bar");
    var slug = function (n) { return n.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, ""); };

    /* ---------- 1. Tree grows when scrolled into view ---------- */
    if (motion) {
        var mm = gsap.matchMedia();
        mm.add({ desk: "(min-width: 1024px)", mob: "(max-width: 1023px)" }, function (ctx) {
            var desk = ctx.conditions.desk;
            var drops = $(".ln-drop", org), spines = $(".ln-spine", org), depts = $(".tdept", org);
            var leaves = $(".tleaf .tnode", org), root = org.querySelector(".tnode-lead");
            var tl = gsap.timeline({ paused: true });
            var started = false;
            var start = function () { if (!started) { started = true; tl.play(); } };
            if ("IntersectionObserver" in window) {
                var io = new IntersectionObserver(function (en) { if (en[0].isIntersecting) { start(); io.disconnect(); } }, { threshold: 0.15 });
                io.observe(org);
            } else { start(); }
            // Backups: start whenever the tree is on screen (scroll, resize, or shortly after load)
            var check = function () {
                if (started) { window.removeEventListener("scroll", check); window.removeEventListener("resize", check); return; }
                var r = org.getBoundingClientRect();
                if (r.top < window.innerHeight * 0.85 && r.bottom > 0) start();
            };
            window.addEventListener("scroll", check, { passive: true });
            window.addEventListener("resize", check);
            setTimeout(check, 1200);
            // fromTo with explicit end states so the result never depends on values read at start-up
            tl.fromTo(root, { scale: 0.6, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, duration: 0.7, ease: "back.out(1.7)" })
              .fromTo(trunk, { scaleY: 0 }, { scaleY: 1, duration: 0.45, ease: "power2.inOut" }, "-=0.15")
              .fromTo(bar, desk ? { scaleX: 0 } : { scaleY: 0 }, desk ? { scaleX: 1, duration: 0.6, ease: "power3.inOut" } : { scaleY: 1, duration: 0.9, ease: "power2.inOut" })
              .fromTo(drops, desk ? { scaleY: 0 } : { scaleX: 0 }, desk ? { scaleY: 1, duration: 0.35, stagger: 0.12, ease: "power2.out" } : { scaleX: 1, duration: 0.3, stagger: 0.18, ease: "power2.out" }, desk ? "-=0.1" : "-=0.75")
              .fromTo(depts, { y: 16, scale: 0.85, autoAlpha: 0 }, { y: 0, scale: 1, autoAlpha: 1, duration: 0.55, stagger: 0.12, ease: "back.out(1.8)" }, "-=0.3")
              .fromTo(spines, { scaleY: 0 }, { scaleY: 1, duration: 0.7, stagger: 0.12, ease: "power2.inOut" }, "-=0.35")
              .fromTo(leaves, { x: -24, autoAlpha: 0 }, { x: 0, autoAlpha: 1, duration: 0.55, stagger: 0.07, ease: "power3.out" }, "-=0.6");
            // hand control back to CSS (hover dimming / lift) once the tree has grown
            tl.eventCallback("onComplete", function () { gsap.set([root].concat(leaves, depts), { clearProps: "transform,opacity,visibility" }); });
            return function () { tl.kill(); if (io) io.disconnect(); gsap.set([root, trunk, bar].concat(drops, spines, depts, leaves), { clearProps: "all" }); };
        });
    }

    /* ---------- 2. Light up the path from root to a member ---------- */
    function pathFor(node) {
        var lines = [trunk, bar];
        var leaf = node.closest(".tleaf");
        var branch = node.closest(".tbranch");
        if (branch) lines.push(branch.querySelector(".ln-drop"), branch.querySelector(".ln-spine"));
        else lines = lines.concat($(".ln-drop", org)); // root lights every branch
        return { lines: lines.filter(Boolean), leaf: leaf };
    }
    function light(node) {
        clearLight();
        var p = pathFor(node);
        p.lines.forEach(function (l) { l.classList.add("lit"); });
        if (p.leaf) p.leaf.classList.add("lit");
        node.classList.add("on");
        org.classList.add("focusing");
    }
    function clearLight() {
        $(".lit", org).forEach(function (el) { el.classList.remove("lit"); });
        nodes.forEach(function (n) { n.classList.remove("on"); });
        org.classList.remove("focusing");
    }
    nodes.forEach(function (n) {
        n.addEventListener("pointerenter", function () { light(n); });
        n.addEventListener("focus", function () { light(n); });
        n.addEventListener("pointerleave", function () { if (!modal.classList.contains("open")) clearLight(); });
        n.addEventListener("blur", function () { if (!modal.classList.contains("open")) clearLight(); });
    });

    /* ---------- 3. Profile modal ---------- */
    var card = modal.querySelector(".pm-card");
    var backdrop = modal.querySelector(".pm-backdrop");
    var els = {
        avatar: modal.querySelector(".pm-avatar"), dept: modal.querySelector(".pm-dept"), name: modal.querySelector("#pmName"),
        role: modal.querySelector(".pm-role"), bio: modal.querySelector(".pm-bio"), skills: modal.querySelector(".pm-skills"),
        helps: modal.querySelector(".pm-helps"), count: modal.querySelector(".pm-count"),
        prev: modal.querySelector(".pm-prev"), next: modal.querySelector(".pm-next")
    };
    var current = 0, origin = null, busy = false;

    function fill(i) {
        var m = TEAM[i];
        current = i;
        card.className = "pm-card dept-" + m.dept;
        els.avatar.innerHTML = "";
        if (m.img) { var img = new Image(); img.src = m.img; img.alt = m.name; els.avatar.appendChild(img); }
        else { els.avatar.textContent = m.initials; }
        els.dept.textContent = m.deptName;
        els.name.textContent = m.name;
        els.role.textContent = m.role;
        els.bio.textContent = m.bio;
        els.skills.innerHTML = ""; m.skills.forEach(function (s) { var li = document.createElement("li"); li.textContent = s; els.skills.appendChild(li); });
        els.helps.innerHTML = ""; m.helps.forEach(function (s) { var li = document.createElement("li"); li.textContent = s; els.helps.appendChild(li); });
        var p = TEAM[(i - 1 + TEAM.length) % TEAM.length], n = TEAM[(i + 1) % TEAM.length];
        els.prev.querySelector("span").textContent = p.name.split(" ")[0];
        els.next.querySelector("span").textContent = n.name.split(" ")[0];
        els.prev.setAttribute("aria-label", "Previous: " + p.name);
        els.next.setAttribute("aria-label", "Next: " + n.name);
        els.count.textContent = (i + 1) + " / " + TEAM.length;
        var node = nodeFor(i); if (node) light(node);
        try { history.replaceState(null, "", "#member-" + slug(m.name)); } catch (e) {}
    }
    function nodeFor(i) { return org.querySelector('.tnode[data-member="' + i + '"]'); }

    function animateContentIn(dir) {
        if (!motion) return;
        var inner = [modal.querySelector(".pm-dept"), els.name, els.role, els.bio].concat($(".pm-body h3", modal), [modal.querySelector(".pm-actions")]);
        var tl = gsap.timeline();
        tl.fromTo(els.avatar, { scale: 0.3, rotate: dir ? 0 : -25, autoAlpha: 0 }, { scale: 1, rotate: 0, autoAlpha: 1, duration: 0.7, ease: "back.out(1.8)" })
          .fromTo(".pm-orb", { scale: 0.4, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, duration: 1, stagger: 0.1, ease: "expo.out" }, 0)
          .fromTo(inner, { y: 18, x: dir ? dir * 24 : 0, autoAlpha: 0 }, { y: 0, x: 0, autoAlpha: 1, duration: 0.55, stagger: 0.05, ease: "power3.out" }, 0.1)
          .fromTo($(".pm-skills li", modal), { scale: 0.6, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, duration: 0.4, stagger: 0.05, ease: "back.out(2)" }, 0.3)
          .fromTo($(".pm-helps li", modal), { x: -16, autoAlpha: 0 }, { x: 0, autoAlpha: 1, duration: 0.45, stagger: 0.07, ease: "power3.out" }, 0.4);
        return tl;
    }

    function open(i, fromNode, clickEvt) {
        if (busy) return;
        origin = fromNode || nodeFor(i);
        fill(i);
        modal.classList.add("open");
        modal.setAttribute("aria-hidden", "false");
        document.body.classList.add("nav-open");
        modal.querySelector(".pm-close").focus({ preventScroll: true });
        if (!motion) return;
        busy = true;
        gsap.fromTo(backdrop, { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.4, ease: "power2.out" });
        var start = flipFrom(origin);
        gsap.fromTo(card, start, { x: 0, y: 0, scaleX: 1, scaleY: 1, autoAlpha: 1, borderRadius: 24, duration: 0.75, ease: "expo.out",
            onComplete: function () { busy = false; gsap.set(card, { clearProps: "transform,borderRadius" }); } });
        animateContentIn(0);
    }

    function flipFrom(node) {
        var c = card.getBoundingClientRect();
        if (!node) return { y: 40, scaleX: 0.92, scaleY: 0.92, autoAlpha: 0 };
        var n = node.getBoundingClientRect();
        return { x: (n.left + n.width / 2) - (c.left + c.width / 2), y: (n.top + n.height / 2) - (c.top + c.height / 2),
                 scaleX: Math.max(n.width / c.width, 0.2), scaleY: Math.max(n.height / c.height, 0.1), autoAlpha: 0.4, borderRadius: 16 };
    }

    function close() {
        if (!modal.classList.contains("open") || busy) return;
        var finish = function () {
            modal.classList.remove("open");
            modal.setAttribute("aria-hidden", "true");
            document.body.classList.remove("nav-open");
            gsap && gsap.set([card, backdrop], { clearProps: "all" });
            clearLight();
            var back = nodeFor(current) || origin;
            if (back) back.focus({ preventScroll: true });
            try { history.replaceState(null, "", location.pathname + location.search); } catch (e) {}
            busy = false;
        };
        if (!motion) return finish();
        busy = true;
        var target = nodeFor(current);
        var rect = target && target.getBoundingClientRect();
        var onScreen = rect && rect.bottom > 0 && rect.top < window.innerHeight;
        gsap.to(backdrop, { autoAlpha: 0, duration: 0.35, ease: "power2.in" });
        gsap.to(card, onScreen ? Object.assign(flipFrom(target), { autoAlpha: 0, duration: 0.45, ease: "expo.in", onComplete: finish })
                               : { y: 40, scale: 0.94, autoAlpha: 0, duration: 0.3, ease: "power2.in", onComplete: finish });
    }

    function go(step) {
        if (busy) return;
        var i = (current + step + TEAM.length) % TEAM.length;
        if (!motion) { fill(i); return; }
        busy = true;
        var parts = [modal.querySelector(".pm-head"), modal.querySelector(".pm-body")];
        gsap.to(parts, { x: -step * 40, autoAlpha: 0, duration: 0.22, ease: "power2.in", onComplete: function () {
            fill(i);
            gsap.set(parts, { x: 0, autoAlpha: 1 });
            card.scrollTop = 0;
            animateContentIn(step).eventCallback("onComplete", function () { busy = false; });
            gsap.fromTo(modal.querySelector(".pm-banner"), { filter: "saturate(2) brightness(1.15)" }, { filter: "none", duration: 0.6 });
        } });
    }

    /* Click: ripple + open */
    nodes.forEach(function (n) {
        n.addEventListener("click", function (e) {
            if (motion && e.clientX) {
                var r = n.getBoundingClientRect(), dot = document.createElement("span");
                dot.className = "ripple";
                dot.style.left = (e.clientX - r.left) + "px"; dot.style.top = (e.clientY - r.top) + "px";
                n.appendChild(dot);
                gsap.fromTo(dot, { width: 0, height: 0, opacity: 0.9 }, { width: r.width * 2.4, height: r.width * 2.4, opacity: 0, duration: 0.7, ease: "power2.out", onComplete: function () { dot.remove(); } });
                gsap.fromTo(n, { scale: 0.97 }, { scale: 1, duration: 0.5, ease: "elastic.out(1, 0.5)" });
            }
            open(parseInt(n.getAttribute("data-member"), 10), n, e);
        });
    });

    modal.querySelectorAll("[data-pm-close]").forEach(function (b) { b.addEventListener("click", close); });
    els.prev.addEventListener("click", function () { go(-1); });
    els.next.addEventListener("click", function () { go(1); });
    document.addEventListener("keydown", function (e) {
        if (!modal.classList.contains("open")) return;
        if (e.key === "Escape") { e.preventDefault(); close(); }
        else if (e.key === "ArrowRight") go(1);
        else if (e.key === "ArrowLeft") go(-1);
        else if (e.key === "Tab") {
            var f = $('button, a[href]', card).filter(function (el) { return el.offsetParent !== null; });
            if (!f.length) return;
            var first = f[0], last = f[f.length - 1];
            if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
            else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
        }
    });
    // swipe left/right on the card (touch)
    var sx = null;
    card.addEventListener("touchstart", function (e) { sx = e.touches[0].clientX; }, { passive: true });
    card.addEventListener("touchend", function (e) {
        if (sx === null) return;
        var dx = e.changedTouches[0].clientX - sx; sx = null;
        if (Math.abs(dx) > 60) go(dx < 0 ? 1 : -1);
    });

    /* Deep link: OurTeam.html#member-anjali-mishra opens that profile */
    var m = location.hash.match(/^#member-(.+)$/);
    if (m) {
        var idx = TEAM.findIndex(function (t) { return slug(t.name) === m[1]; });
        if (idx > -1) setTimeout(function () { open(idx, null); }, 400);
    }
})();
