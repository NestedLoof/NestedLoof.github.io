/* lutherwilliamson.co.uk — small progressive enhancements. Original code, no dependencies. */
(function () {
  "use strict";
  var root = document.documentElement;
  root.classList.remove("no-js");
  root.classList.add("js");

  // Mobile navigation toggle
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    var setOpen = function (open) {
      toggle.setAttribute("aria-expanded", String(open));
      nav.classList.toggle("is-open", open);
    };
    toggle.addEventListener("click", function () {
      setOpen(toggle.getAttribute("aria-expanded") !== "true");
    });
    nav.addEventListener("click", function (e) {
      if (e.target.closest("a")) setOpen(false);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("is-open")) { setOpen(false); toggle.focus(); }
    });
  }

  // Header hairline once the page has scrolled
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () { header.classList.toggle("is-scrolled", window.scrollY > 8); };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  // YouTube: show a thumbnail and load the (no-cookie) player only when clicked
  Array.prototype.forEach.call(document.querySelectorAll("a[data-yt]"), function (a) {
    a.addEventListener("click", function (e) {
      e.preventDefault();
      var frame = document.createElement("iframe");
      frame.src = "https://www.youtube-nocookie.com/embed/" + a.getAttribute("data-yt") + "?autoplay=1&rel=0";
      frame.title = a.getAttribute("aria-label") || "YouTube video";
      frame.allow = "autoplay; encrypted-media; picture-in-picture; fullscreen";
      frame.allowFullscreen = true;
      var box = a.querySelector(".ratio");
      box.innerHTML = "";
      box.appendChild(frame);
      var holder = document.createElement("div");
      holder.className = a.className;
      holder.appendChild(box);
      a.replaceWith(holder);
      frame.focus();
    });
  });

  // Open a collapsed <details> when a link points at something inside it
  var openTarget = function () {
    var id = decodeURIComponent(location.hash.slice(1));
    var el = id && document.getElementById(id);
    var d = el && el.closest("details");
    if (d && !d.open) { d.open = true; el.scrollIntoView(); }
  };
  window.addEventListener("hashchange", openTarget);
  openTarget();

  // Enlarge images in a native <dialog>; links still open the image without JS
  var links = document.querySelectorAll("a[data-zoom]");
  if (links.length && typeof HTMLDialogElement === "function") {
    var dialog = document.createElement("dialog");
    dialog.className = "lightbox";
    dialog.innerHTML = '<button class="lightbox__close" type="button">Close</button><img alt=""><p></p>';
    document.body.appendChild(dialog);
    var img = dialog.querySelector("img");
    var cap = dialog.querySelector("p");
    dialog.querySelector("button").addEventListener("click", function () { dialog.close(); });
    dialog.addEventListener("click", function (e) { if (e.target === dialog) dialog.close(); });
    Array.prototype.forEach.call(links, function (a) {
      a.addEventListener("click", function (e) {
        e.preventDefault();
        var thumb = a.querySelector("img");
        img.src = a.getAttribute("href");
        img.alt = thumb ? thumb.alt : "";
        cap.textContent = a.getAttribute("data-caption") || "";
        dialog.showModal();
      });
    });
  }

  // Gentle reveal for section headings (skipped when reduced motion is preferred)
  var reveals = document.querySelectorAll(".reveal");
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reveals.length && "IntersectionObserver" in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add("is-in"); io.unobserve(entry.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px" });
    Array.prototype.forEach.call(reveals, function (el) { io.observe(el); });
  } else {
    Array.prototype.forEach.call(reveals, function (el) { el.classList.add("is-in"); });
  }
})();
