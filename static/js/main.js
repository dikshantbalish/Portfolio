/* =========================================================
   DIKSHANT BALISH — PORTFOLIO
   Main JavaScript
   ========================================================= */

document.addEventListener("DOMContentLoaded", () => {
    "use strict";

    /* =====================================================
       01. ELEMENTS
    ===================================================== */

    const header = document.querySelector(".site-header");
    const menuToggle = document.querySelector(".menu-toggle");
    const mobileNavigation = document.querySelector(".mobile-navigation");

    const pointerGlow = window.matchMedia(
        "(hover: hover) and (pointer: fine)"
    );

    if (pointerGlow.matches) {
        let pointerX = window.innerWidth * 0.5;
        let pointerY = window.innerHeight * 0.18;
        let targetX = pointerX;
        let targetY = pointerY;

        window.addEventListener("pointermove", (event) => {
            targetX = event.clientX;
            targetY = event.clientY;
        }, { passive: true });

        const easePointerGlow = () => {
            pointerX += (targetX - pointerX) * 0.08;
            pointerY += (targetY - pointerY) * 0.08;

            document.documentElement.style.setProperty(
                "--pointer-x",
                `${pointerX}px`
            );

            document.documentElement.style.setProperty(
                "--pointer-y",
                `${pointerY}px`
            );

            window.requestAnimationFrame(easePointerGlow);
        };

        easePointerGlow();
    }

    /* =====================================================
       02. SCROLLED HEADER
    ===================================================== */

    const updateHeader = () => {
        if (!header) return;

        if (window.scrollY > 20) {
            header.classList.add("scrolled");
        } else {
            header.classList.remove("scrolled");
        }
    };

    updateHeader();

    window.addEventListener("scroll", updateHeader, {
        passive: true
    });


    /* =====================================================
       03. MOBILE NAVIGATION
    ===================================================== */

    if (menuToggle && mobileNavigation) {

        const closeMenu = () => {
            menuToggle.classList.remove("active");
            mobileNavigation.classList.remove("active");

            menuToggle.setAttribute("aria-expanded", "false");
            document.body.classList.remove("menu-open");
        };


        const openMenu = () => {
            menuToggle.classList.add("active");
            mobileNavigation.classList.add("active");

            menuToggle.setAttribute("aria-expanded", "true");
            document.body.classList.add("menu-open");
        };


        menuToggle.addEventListener("click", () => {
            const isOpen = menuToggle.classList.contains("active");

            if (isOpen) {
                closeMenu();
            } else {
                openMenu();
            }
        });


        /* Close after selecting a mobile navigation link */

        const mobileLinks =
            mobileNavigation.querySelectorAll("a");

        mobileLinks.forEach((link) => {
            link.addEventListener("click", () => {
                closeMenu();
            });
        });


        /* Close with Escape */

        document.addEventListener("keydown", (event) => {
            if (event.key === "Escape") {
                closeMenu();
            }
        });


        /* Close when clicking outside the navigation */

        document.addEventListener("click", (event) => {

            if (
                !mobileNavigation.contains(event.target) &&
                !menuToggle.contains(event.target)
            ) {
                closeMenu();
            }

        });

    }


    /* =====================================================
       04. SMOOTH SCROLLING
    ===================================================== */

    const internalLinks = document.querySelectorAll(
        'a[href^="#"]'
    );

    internalLinks.forEach((link) => {

        link.addEventListener("click", (event) => {

            const targetId = link.getAttribute("href");

            if (!targetId || targetId === "#") {
                return;
            }

            const target = document.querySelector(targetId);

            if (!target) {
                return;
            }

            event.preventDefault();

            const headerOffset = header
                ? header.offsetHeight
                : 0;

            const targetPosition =
                target.getBoundingClientRect().top +
                window.scrollY -
                headerOffset;

            window.scrollTo({
                top: targetPosition,
                behavior: "smooth"
            });

        });

    });


    /* =====================================================
       05. CURRENT YEAR
    ===================================================== */

    const yearElements = document.querySelectorAll(
        "[data-current-year]"
    );

    const currentYear = new Date().getFullYear();

    yearElements.forEach((element) => {
        element.textContent = currentYear;
    });


    /* =====================================================
       06. EXTERNAL LINKS
    ===================================================== */

    const externalLinks = document.querySelectorAll(
        'a[href^="http://"], a[href^="https://"]'
    );

    externalLinks.forEach((link) => {

        const currentHost = window.location.hostname;

        try {

            const linkUrl = new URL(link.href);

            if (
                linkUrl.hostname !== currentHost &&
                !link.hasAttribute("target")
            ) {
                link.setAttribute("target", "_blank");
                link.setAttribute("rel", "noopener noreferrer");
            }

        } catch (error) {
            /* Ignore invalid URLs */
        }

    });


    /* =====================================================
       07. PROJECT CARD HOVER
    ===================================================== */

    const projectCards = document.querySelectorAll(
        ".project-card, .project-list-item"
    );

    projectCards.forEach((card) => {

        card.addEventListener("mouseenter", () => {
            card.classList.add("is-hovered");
        });

        card.addEventListener("mouseleave", () => {
            card.classList.remove("is-hovered");
        });

    });


    /* =====================================================
       08. COPY EMAIL
    ===================================================== */

    const copyButtons = document.querySelectorAll(
        "[data-copy-email]"
    );

    copyButtons.forEach((button) => {

        button.addEventListener("click", async () => {

            const email =
                button.getAttribute("data-copy-email");

            if (!email) {
                return;
            }

            try {

                await navigator.clipboard.writeText(email);

                const originalText =
                    button.textContent;

                button.textContent = "Copied";

                setTimeout(() => {
                    button.textContent = originalText;
                }, 1600);

            } catch (error) {

                window.location.href =
                    `mailto:${email}`;

            }

        });

    });


    /* =====================================================
       09. FORM SUBMISSION STATE
    ===================================================== */

    const contactForm =
        document.querySelector(".contact-form");

    if (contactForm) {

        contactForm.addEventListener("submit", () => {

            const submitButton =
                contactForm.querySelector(
                    'button[type="submit"], input[type="submit"]'
                );

            if (!submitButton) {
                return;
            }

            submitButton.classList.add("is-loading");

            if (submitButton.tagName === "BUTTON") {
                submitButton.disabled = true;
            }

        });

    }


    /* =====================================================
       10. REVEAL ON SCROLL
    ===================================================== */

    const revealElements =
        document.querySelectorAll(
            ".reveal, .fade-up"
        );

    if ("IntersectionObserver" in window) {

        const revealObserver =
            new IntersectionObserver(
                (entries, observer) => {

                    entries.forEach((entry) => {

                        if (!entry.isIntersecting) {
                            return;
                        }

                        entry.target.classList.add("visible");

                        observer.unobserve(entry.target);

                    });

                },
                {
                    threshold: 0.12,
                    rootMargin: "0px 0px -40px 0px"
                }
            );

        revealElements.forEach((element) => {
            revealObserver.observe(element);
        });

    } else {

        revealElements.forEach((element) => {
            element.classList.add("visible");
        });

    }


    /* =====================================================
       11. IMAGE LOADING
    ===================================================== */

    const images = document.querySelectorAll("img");

    images.forEach((image) => {

        image.addEventListener("load", () => {
            image.classList.add("loaded");
        });

        image.addEventListener("error", () => {
            image.classList.add("image-error");
        });

    });


    /* =====================================================
       12. PREVENT BODY SCROLL WHEN MOBILE MENU IS OPEN
    ===================================================== */

    const updateBodyOverflow = () => {

        if (
            mobileNavigation &&
            mobileNavigation.classList.contains("active")
        ) {
            document.body.style.overflow = "hidden";
        } else {
            document.body.style.overflow = "";
        }

    };

    if (menuToggle) {

        menuToggle.addEventListener(
            "click",
            updateBodyOverflow
        );

    }


    /* =====================================================
       13. PAGE READY
    ===================================================== */

    document.documentElement.classList.add("js");

});