# Asman Makero Musa - Engineering Portfolio

Personal portfolio website for **Asman Makero Musa**, Computer Science student at the University of Nairobi specializing in AI workflows, low-level systems programming (C/C++), and data architecture.

- **Live URL:** [makeromusa.me](https://makeromusa.me)
- **Backup GitHub Pages URL:** [makeromusa.github.io](https://makeromusa.github.io)

---

## 🛠️ Tech Stack & Architecture

- **Markup & Styling:** Semantic HTML5, CSS3, Modern Bootstrap 5.3, Bootstrap Icons
- **Dynamic Scripts:** Vanilla JavaScript (Typed.js, Isotope Layout, Waypoints, GLightbox, AOS)
- **Deployment:** GitHub Pages + Namecheap DNS integration (`makeromusa.me`)
- **SSL / Security:** GitHub Pages Let's Encrypt automated TLS certificate (`Enforce HTTPS`)
- **Contact Handling:** Dynamic Formspree AJAX endpoint with seamless mailto client fallback

---

## 🚀 SDLC Stages

1. **Stage 1: Discovery & Requirements Specification**
   - Profile scoping based on verified CV credentials.
   - Flattening workspace architecture to repo root for clean static hosting.
   - Initialized Git version control.

2. **Stage 2: Architecture & Content Specification**
   - Designed 7 core sections: Hero, About, Technical Expertise (Skills), Experience & Education, Technical & AI Projects, Certifications, Contact.
   - Removed generic boilerplate (Pricing, FAQs, placeholder dropdowns).
   - Integrated downloadable CV asset.

3. **Stage 3: Implementation & Customization**
   - Customized `index.html` with real-world project portfolios and credentials.
   - Appended custom CSS styles (`assets/css/main.css`) for tech badges, hero CTAs, and certification cards.
   - Form submission setup with fallback to `makeromusa17@gmail.com`.

4. **Stage 4: Quality Assurance & Optimization**
   - Tested local HTTP response (Status 200 OK across HTML, CSS, JS, and PDF).
   - Open Graph social share tags, meta description, and SEO keywords.

5. **Stage 5: Deployment & DNS Setup (Namecheap)**
   - Configured `CNAME` for `makeromusa.me`.
   - Setup Namecheap DNS records for apex and `www` subdomains.

6. **Stage 6: Maintenance & Post-Launch Handover**
   - Step-by-step instructions for adding new projects, updating credentials, and managing contact inquiries.

---

## 🌐 Namecheap DNS Configuration Reference

In Namecheap dashboard, navigate to **Domain List** -> **Manage** (`makeromusa.me`) -> **Advanced DNS**:

| Type | Host | Value | TTL |
| :--- | :--- | :--- | :--- |
| **A Record** | `@` | `185.199.108.153` | Automatic |
| **A Record** | `@` | `185.199.109.153` | Automatic |
| **A Record** | `@` | `185.199.110.153` | Automatic |
| **A Record** | `@` | `185.199.111.153` | Automatic |
| **CNAME Record** | `www` | `makeromusa.github.io.` | Automatic |

*Note: Delete any default Namecheap Parking page records.*

---

## 📄 License
Template based on DevFolio by BootstrapMade. Content and portfolio rights reserved by Asman Makero Musa.
