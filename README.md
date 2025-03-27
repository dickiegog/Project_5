# Fitnest

Fitnest is a full-stack e-commerce web application designed to provide users with access to premium fitness products, community interaction, and a seamless shopping experience. The project is developed using **Django**, deployed to **Heroku**, and uses **Stripe** for secure payments and **Cloudinary** for media storage.

![Site Preview](static/images/Fitnest-Lighthouse.png)

## Table of Contents

- [Live Site](#live-site)
- [User Stories](#user-stories)
- [Features](#features)
  - [Homepage](#homepage)
  - [Products](#products)
  - [Cart & Checkout](#cart--checkout)
  - [User Profiles](#user-profiles)
  - [Community Comments](#community-comments)
- [Site Architecture](#site-architecture)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
  - [Lighthouse](#lighthouse)
  - [Manual Testing](#manual-testing)
  - [Automated Testing](#automated-testing)
- [Deployment](#deployment)
- [Facebook Page](#facebook-page)
- [Credits](#credits)

---

## Live Site

You can visit the deployed application here:  
[https://richards-pp5-8caee8658402.herokuapp.com/](https://richards-pp5-8caee8658402.herokuapp.com/)

---

## User Stories

All user stories were documented and tracked using GitHub Issues and linked to project goals in a Kanban-style board.

Key user stories include:
- As a user, I want to browse and filter products easily.
- As a user, I want to search for products by keyword.
- As a user, I want to register, log in, and manage my profile.
- As a user, I want to view and add products to my cart.
- As a user, I want to securely checkout using Stripe.
- As a user, I want to leave and read community comments.
- As an admin, I want to add, edit, and delete products.
- As an admin, I want to view user comments and moderate if necessary.

---

## Features

### Homepage
- Branded carousel with high-performance hero images (WebP + lazy loading)
- Clear navigation and CTA to "Shop Now"
- Mission and brand message

### Products
- Dynamic catalog with category filtering, search, and sorting
- Product cards with image, price, and description
- Admin controls for adding/editing/deleting products

### Cart & Checkout
- Fully functional cart system with quantity and total updates
- Stripe integration with test keys
- Order summary page and success message

### User Profiles
- Register/login/logout using Django AllAuth
- Edit profile page with saved data
- View past orders (future improvement planned)

### Community Comments
- Users can post comments on products
- Comments are displayed per product and moderated

---

## Site Architecture

- **Frontend**: HTML, CSS (Bootstrap 4), JavaScript (minimal)
- **Backend**: Django, Python
- **Database**: SQLite (dev), PostgreSQL (prod via Heroku)
- **Media Storage**: Cloudinary
- **Deployment**: GitHub → Heroku
- **Authentication**: AllAuth
- **Payments**: Stripe

---

## Technologies Used

- Python 3.12
- Django 5.1
- Cloudinary for image hosting
- Stripe for payment processing
- Bootstrap 4.6
- jQuery for limited interactivity
- GitHub for version control
- Gitpod as the development environment
- Heroku for deployment
- AOS.js for animations

---

## Testing

### Lighthouse

The site was tested using Lighthouse with the following results:

![Lighthouse Results](static/images/Fitnest-Lighthouse.png)

- **Performance**: 75 (optimized with image compression and lazy loading)
- **Accessibility**: 94
- **Best Practices**: 96
- **SEO**: 100

Areas optimized:
- WebP image format used
- Lazy loading added for all non-LCP images
- Critical CSS deferred
- Fonts preloaded

---

### Manual Testing

Performed across:
- Desktop (Chrome, Firefox, Safari)
- Mobile (iOS Safari, Android Chrome)
- Responsiveness verified using Chrome DevTools
- Cart logic tested manually (add, remove, update quantity)
- Stripe tested using test keys
- User flow: register → login → add product → checkout → logout

---

### Automated Testing

Basic unit tests are written in `tests.py`:
- URL resolution
- Product model creation
- Cart calculations
- Page rendering

More comprehensive testing is planned.

---

## Deployment

### Heroku

- Deployed to Heroku using GitHub integration
- Environment variables set in Heroku Config Vars:
  - `STRIPE_PUBLIC_KEY`
  - `STRIPE_SECRET_KEY`
  - `CLOUDINARY_CLOUD_NAME`
  - `CLOUDINARY_API_KEY`
  - `CLOUDINARY_API_SECRET`
- Static and media files managed via Cloudinary
- `gunicorn` and `dj_database_url` used in production
- PostgreSQL used as live database
- Secret key and debug settings configured for production

### Cloudinary

All product images and default media are served via Cloudinary:

- Cloud Name: `det85sh4x`
- Publicly accessible URLs
- Fast CDN delivery

---

## Facebook Page

A Facebook page was created to fulfill the deployment criteria and represent the brand on social media:

![Facebook Page Screenshot](static/images/FB-Fitnest.png)

Page includes:
- Fitnest branding
- Direct links to the live project
- Description of the application
- Cover and profile images sourced from Cloudinary

---

## Credits

- Product imagery: Unsplash
- Carousel code and template tweaks: Bootstrap examples
- Payment: Stripe test account
- Hosting: Heroku
- Icons: Font Awesome
- AllAuth setup: Code Institute walkthrough (adapted)

---

## Future Improvements

- Pagination for large product catalogs
- Wishlist and saved products
- User order history
- Ratings and product reviews
- Admin dashboard for insights

---

## Repository

GitHub Repository: [https://github.com/dickiegog/Project_5](https://github.com/dickiegog/Project_5)

---

## License

This project is for educational use and part of a Full Stack Software Development course through Code Institute.
