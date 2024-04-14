import reflex as rx

navbar_html = """
<div style="width: 1000px; background-color: #333; overflow: hidden; display: flex; justify-content: space-between; align-items: center; padding: 10px 20px;">
  <div style="float: left; color: white; text-align: center; padding: 14px 16px; text-decoration: none; font-size: 17px;">
    <b>SiteName</b>
  </div>
  <div style="display: flex; float: right;">
    <a href="#home" style="color: white; text-align: center; padding: 14px 16px; text-decoration: none; font-size: 17px; display: block;">Home</a>
    <a href="#services" style="color: white; text-align: center; padding: 14px 16px; text-decoration: none; font-size: 17px; display: block;">Services</a>
    <a href="#about" style="color: white; text-align: center; padding: 14px 16px; text-decoration: none; font-size: 17px; display: block;">About</a>
    <a href="#contact" style="color: white; text-align: center; padding: 14px 16px; text-decoration: none; font-size: 17px; display: block;">Contact</a>
  </div>
</div>
"""


def navbar() -> rx.Component:
    return rx.html(navbar_html)