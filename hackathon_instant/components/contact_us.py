import reflex as rx

contact_us_html = """
<div style="display: flex; align-items: center; justify-content: center; padding: 20px; width: 1000px;">
  <div style="flex: 1; min-height: 300px; background-image: url('https://images.pexels.com/photos/2563597/pexels-photo-2563597.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'); background-size: cover; background-position: center;"></div>
  <div style="flex: 1; padding: 20px;">
    <form action="submit-your-form-handler" method="POST" style="display: flex; flex-direction: column; gap: 10px;">
      <label for="name" style="color: #333; font-weight: bold;">Name:</label>
      <input type="text" id="name" name="name" style="padding: 8px; border-radius: 4px; border: 1px solid #ccc;">

      <label for="email" style="color: #333; font-weight: bold;">Email:</label>
      <input type="email" id="email" name="email" style="padding: 8px; border-radius: 4px; border: 1px solid #ccc;">

      <label for="message" style="color: #333; font-weight: bold;">Message:</label>
      <textarea id="message" name="message" rows="4" style="padding: 8px; border-radius: 4px; border: 1px solid #ccc;"></textarea>

      <button type="submit" style="background-color: #007bff; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">Send</button>
    </form>
  </div>
</div>
"""


def contact_us() -> rx.Component:
    return rx.html(contact_us_html)
