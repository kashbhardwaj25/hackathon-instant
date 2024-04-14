import reflex as rx

featured_html = """
<div class="hero" style="width: 1000px; background-image: url('https://images.pexels.com/photos/2563597/pexels-photo-2563597.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'); height: 100vh; background-size: cover; background-position: center; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; color: white;">
  <h1>Welcome to Our World</h1>
  <p>Explore the beauty of nature with us.</p>
  <a href="#more" class="cta-button" style="padding: 12px 25px; background-color: #007bff; color: white; text-decoration: none; border-radius: 5px; font-weight: bold;">Discover More</a>
</div>
"""


def feature_section() -> rx.Component:
    return rx.html(featured_html)