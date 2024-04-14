import reflex as rx

carousel="""
<div style="overflow-x: auto; white-space: nowrap; padding: 20px; background-color: #f4f4f4; width: 1000px;">
    <div style="display: inline-block; width: 200px; margin-right: 20px; background-color: white; text-align: center; padding: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 10px;">
        <img src="https://images.pexels.com/photos/8947774/pexels-photo-8947774.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" style="width: 100%; border-radius: 5px;">
        <h3 style="color: #333;">Product 1</h3>
        <p style="color: #555; font-size: 14px;">Name</p>
    </div>
    <div style="display: inline-block; width: 200px; margin-right: 20px; background-color: white; text-align: center; padding: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 10px;">
        <img src="https://images.pexels.com/photos/8947774/pexels-photo-8947774.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" style="width: 100%; border-radius: 5px;">
        <h3 style="color: #333;">Product 2</h3>
        <p style="color: #555; font-size: 14px;">Name.</p>
    </div>
    <div style="display: inline-block; width: 200px; margin-right: 20px; background-color: white; text-align: center; padding: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 10px;">
        <img src="https://images.pexels.com/photos/8947774/pexels-photo-8947774.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" style="width: 100%; border-radius: 5px;">
        <h3 style="color: #333;">Product 3</h3>
        <p style="color: #555; font-size: 14px;">Name</p>
    </div>
    <div style="display: inline-block; width: 200px; margin-right: 20px; background-color: white; text-align: center; padding: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 10px;">
        <img src="https://images.pexels.com/photos/8947774/pexels-photo-8947774.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" style="width: 100%; border-radius: 5px;">
        <h3 style="color: #333;">Product 4</h3>
        <p style="color: #555; font-size: 14px;">Name</p>
    </div>
    <div style="display: inline-block; width: 200px; margin-right: 20px; background-color: white; text-align: center; padding: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 10px;">
        <img src="https://images.pexels.com/photos/8947774/pexels-photo-8947774.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" style="width: 100%; border-radius: 5px;">
        <h3 style="color: #333;">Product 5</h3>
        <p style="color: #555; font-size: 14px;">Name</p>
    </div>
    <div style="display: inline-block; width: 200px; margin-right: 20px; background-color: white; text-align: center; padding: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 10px;">
        <img src="https://images.pexels.com/photos/8947774/pexels-photo-8947774.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" style="width: 100%; border-radius: 5px;">
        <h3 style="color: #333;">Product 6</h3>
        <p style="color: #555; font-size: 14px;">Name</p>
    </div>
    <div style="display: inline-block; width: 200px; margin-right: 20px; background-color: white; text-align: center; padding: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 10px;">
        <img src="https://images.pexels.com/photos/8947774/pexels-photo-8947774.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" style="width: 100%; border-radius: 5px;">
        <h3 style="color: #333;">Product 7</h3>
        <p style="color: #555; font-size: 14px;">Name</p>
    </div>
    <div style="display: inline-block; width: 200px; margin-right: 20px; background-color: white; text-align: center; padding: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 10px;">
        <img src="https://images.pexels.com/photos/8947774/pexels-photo-8947774.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" style="width: 100%; border-radius: 5px;">
        <h3 style="color: #333;">Product 8</h3>
        <p style="color: #555; font-size: 14px;">Name</p>
    </div>
</div>
"""


def crousel()-> rx.Component:
    return rx.html(carousel)