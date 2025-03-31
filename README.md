# Fitnest - Fitness E-Commerce Platform

<a href="static/images/homeScreen.png" target="_blank">
  <img src="static/images/homeScreen.png" alt="Fitnest Preview" />
</a>

## Table of Contents
- [Live Site](#live-site)
- [Project Goals](#project-goals)
- [Project Intentions & Planning](#project-intentions-&-planning)
- [User Stories](#user-stories)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

## Live Site
🌐 <a href="https://richards-pp5-8caee8658402.herokuapp.com/" target="_blank">Live Site: Fitnest</a>

## Project Goals
To create a comprehensive fitness e-commerce platform that:
- Provides an intuitive shopping experience
- Encourages community interaction
- Implements secure payment processing
- Maintains high performance standards
- Follows accessibility best practices

---

## Project Intentions & Planning

A detailed explanation of the **project goals, business model, and design choices** is documented in the following Google Doc:

📄 <a href="https://docs.google.com/document/d/1cNEtj40iuhMNrbCfl6m3x47SoImJv2XE/edit?usp=drive_link&ouid=116876224672419831524&rtpof=true&sd=true" target="_blank">Fitnest E-Commerce Project Documentation</a>

This document outlines the core concept of the Fitnest project, including:

- The business case and audience
- Core features and user stories
- Design decisions and layout wireframes
- Technologies and services used

It was created to support planning, testing, and assessment of the full-stack development process.


## User Stories
### Shopper Goals
- Browse and filter products by category
- Search for specific fitness items
- View detailed product information
- Add items to cart and checkout securely

### User Management
- Register and login securely
- Manage personal profile information
- View order history
- Logout securely

### Community Features
- Post comments on products
- Read other users' experiences
- Moderate comments (admin)

### Admin Functions
- Add/edit/delete products
- Manage inventory
- View all user comments
- Process orders

## Features

### Core Features
- **Responsive Product Catalog**
  - Category filtering
  - Keyword search
  - Sorting options
  - Pagination

- **User Authentication**
  - Secure registration/login
  - Password reset
  - Email verification
  - Profile management

- **Shopping Cart**
  - Add/remove items
  - Quantity adjustment
  - Persistent cart between sessions
  - Order summary

- **Checkout Process**
  - Secure Stripe payments
  - Order confirmation
  - Receipt generation

- **Community Interaction**
  - Product-specific comments
  - Comment moderation
  - User rating system

### Future Features
- Advanced product filtering
- Wishlist functionality
- Product ratings and reviews
- Enhanced admin dashboard
- Loyalty program integration

## Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript (ES6)
- Bootstrap 4.6
- jQuery 3.5.1

### Backend
- Python 3.12
- Django 5.1
- Django AllAuth
- Django Crispy Forms

### Database
- SQLite (development)
- PostgreSQL (production)

### Services
- Stripe (payments)
- Cloudinary (media storage)
- Heroku (hosting)
- GitHub (version control)

### Development Tools
- Gitpod IDE
- Chrome DevTools
- Lighthouse
- W3C Validators

# Testing

## Automated Testing

Unit tests were written in `tests.py` to validate model integrity, views, and key application functionality.

Django's built-in test runner was used to execute the tests:

```bash
python manage.py test
```

All 9 tests passed successfully, confirming the core logic is functioning as expected.

<a href="static/images/Automated%20testing.png" target="_blank">
  <img src="static/images/Automated%20testing.png" alt="Automated Tests" />
</a>

## Manual Testing

### Feature-by-Feature Tests

| Feature         | Test Case           | Result  |
|----------------|---------------------|---------|
| Registration   | New user signup     | ✅ Pass |
| Login          | Existing user login | ✅ Pass |
| Product Search | Keyword matching    | ✅ Pass |
| Cart           | Add/remove items    | ✅ Pass |
| Checkout       | Complete purchase   | ✅ Pass |

---

## Validation Testing

### HTML Validation

HTML was validated using <a href="https://validator.w3.org/" target="_blank">W3C Validator</a>. No critical issues were found.

<a href="static/images/HTML_Validation_p5.png" target="_blank">
  <img src="static/images/HTML_Validation_p5.png" alt="HTML Validation" />
</a>


### CSS Validation

CSS was validated using <a href="https://jigsaw.w3.org/css-validator/" target="_blank">W3C CSS Validator</a>. No errors were detected.

<a href="static/images/Css_validation_p5.png" target="_blank">
  <img src="static/images/Css_validation_p5.png" alt="CSS Validation" />
</a>

---

## Responsive Design

The site was tested across the following screen sizes:

- Mobile (iPhone SE, 12 Pro)
- Tablet (iPad)
- Laptop (MacBook Air)
- Desktop (1080p monitor)

The design adapted fluidly at each breakpoint.


<a href="static/images/responsiveP5.png" target="_blank">
  <img src="static/images/responsiveP5.png" alt="Responsive Design" />
</a>

---

## Performance Testing

Google Lighthouse was used to measure performance. The site scored well in all categories:

<a href="static/images/Fitnest-Lighthouse.png" target="_blank">
  <img src="static/images/Fitnest-Lighthouse.png" alt="Lighthouse Report" />
</a>

| Metric         | Score |
|----------------|-------|
| Performance    | 75    |
| Accessibility  | 94    |
| Best Practices | 96    |
| SEO            | 100   |

---

## Deployment

### Local Development

1. **Clone repository:**

   ```bash
   git clone https://github.com/dickiegog/Project_5.git
   ```

2. **Install requirements:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Create environment variables:**

   ```python
   # env.py
   import os
   os.environ['SECRET_KEY'] = 'your-secret-key'
   os.environ['STRIPE_PUBLIC_KEY'] = 'your-stripe-key'
   os.environ['STRIPE_SECRET_KEY'] = 'your-stripe-secret'
   ```

4. **Migrate database:**

   ```bash
   python manage.py migrate
   ```

5. **Run development server:**

   ```bash
   python manage.py runserver
   ```

---

### Heroku Deployment

1. Create new Heroku app  
2. Add **PostgreSQL** add-on  
3. Set config vars:

   ```
   DATABASE_URL
   SECRET_KEY
   STRIPE_PUBLIC_KEY
   STRIPE_SECRET_KEY
   CLOUDINARY_URL
   ```

4. Connect GitHub repository  
5. Enable automatic deploys  
6. Deploy branch  

---

## Credits

### Media

- Product images from <a href="https://unsplash.com" target="_blank">Unsplash</a>
- Icons from <a href="https://fontawesome.com" target="_blank">Font Awesome</a>

---

### Code

- Base template adapted from **Code Institute Boutique Ado**
- Payment system based on <a href="https://stripe.com/docs" target="_blank">Stripe documentation</a>
- <a href="https://django-allauth.readthedocs.io/en/latest/" target="_blank">Django AllAuth</a> for authentication

### Acknowledgements
- Code Institute tutors and mentors  
- Mentor reviewers  
- Unsplash photographers

---

**License**: This project is developed for educational purposes as part of Code Institute's Full Stack Developer program.
