import os
from PIL import Image, ImageDraw

icons_dir = os.path.join(os.path.dirname(__file__), "icons")
os.makedirs(icons_dir, exist_ok=True)

size = (200, 200)

def create_total_emp():
    # Blue group/team icon
    img = Image.new("RGBA", size, (255, 255, 255, 0))
    d = ImageDraw.Draw(img)
    # Center head
    d.ellipse([75, 30, 125, 80], fill="#0078D7")
    # Center body
    d.pieslice([45, 85, 155, 195], 180, 0, fill="#0078D7")
    # Left head
    d.ellipse([30, 50, 70, 90], fill="#0F3C88")
    # Left body
    d.pieslice([10, 95, 90, 175], 180, 0, fill="#0F3C88")
    # Right head
    d.ellipse([130, 50, 170, 90], fill="#0F3C88")
    # Right body
    d.pieslice([110, 95, 190, 175], 180, 0, fill="#0F3C88")
    img.save(os.path.join(icons_dir, "icon_total_employees.png"))

def create_active_emp():
    # Bright cyan active user icon
    img = Image.new("RGBA", size, (255, 255, 255, 0))
    d = ImageDraw.Draw(img)
    # Head
    d.ellipse([65, 25, 135, 95], fill="#00B4D8")
    # Body
    d.pieslice([30, 105, 170, 245], 180, 0, fill="#00B4D8")
    # Small check badge
    d.ellipse([125, 115, 175, 165], fill="#10B981")
    d.line([138, 140, 148, 152, 165, 130], fill="#FFFFFF", width=6)
    img.save(os.path.join(icons_dir, "icon_active_employees.png"))

def create_attrition_count():
    # Warning triangle icon (attrition alert)
    img = Image.new("RGBA", size, (255, 255, 255, 0))
    d = ImageDraw.Draw(img)
    # Triangle
    pts = [(100, 25), (180, 165), (20, 165)]
    d.polygon(pts, fill="#0284C7")
    # Exclamation mark
    d.line([100, 70, 100, 120], fill="#FFFFFF", width=12)
    d.ellipse([94, 135, 106, 147], fill="#FFFFFF")
    img.save(os.path.join(icons_dir, "icon_attrition_count.png"))

def create_attrition_rate():
    # Line chart analytics icon
    img = Image.new("RGBA", size, (255, 255, 255, 0))
    d = ImageDraw.Draw(img)
    # Rounded container
    d.rounded_rectangle([20, 20, 180, 180], radius=24, fill="#E0F2FE", outline="#0284C7", width=6)
    # Trend line with arrow
    d.line([45, 140, 85, 110, 120, 130, 155, 65], fill="#0284C7", width=10)
    # Nodes
    for pt in [(45, 140), (85, 110), (120, 130), (155, 65)]:
        d.ellipse([pt[0]-9, pt[1]-9, pt[0]+9, pt[1]+9], fill="#0F3C88")
    img.save(os.path.join(icons_dir, "icon_attrition_rate.png"))

def create_avg_age():
    # Age demographic circle
    img = Image.new("RGBA", size, (255, 255, 255, 0))
    d = ImageDraw.Draw(img)
    d.ellipse([20, 20, 180, 180], fill="#1E3A8A")
    # White adult silhouette
    d.ellipse([70, 45, 105, 80], fill="#FFFFFF")
    d.pieslice([50, 85, 125, 160], 180, 0, fill="#FFFFFF")
    # Child / younger silhouette
    d.ellipse([115, 65, 140, 90], fill="#38BDF8")
    d.pieslice([102, 95, 153, 160], 180, 0, fill="#38BDF8")
    img.save(os.path.join(icons_dir, "icon_average_age.png"))

def create_avg_exp():
    # Experience / Brain gear profile
    img = Image.new("RGBA", size, (255, 255, 255, 0))
    d = ImageDraw.Draw(img)
    # Head silhouette
    d.ellipse([30, 25, 140, 135], fill="#334155")
    d.polygon([(110, 80), (160, 105), (140, 135), (110, 125)], fill="#334155")
    d.pieslice([40, 120, 160, 240], 180, 0, fill="#334155")
    # Gear inside head
    d.ellipse([65, 55, 105, 95], fill="#FFFFFF")
    d.ellipse([75, 65, 95, 85], fill="#334155")
    img.save(os.path.join(icons_dir, "icon_average_experience.png"))

if __name__ == "__main__":
    create_total_emp()
    create_active_emp()
    create_attrition_count()
    create_attrition_rate()
    create_avg_age()
    create_avg_exp()
    print("All 6 KPI icons generated successfully in 03_powerbi_dashboards/icons/")
