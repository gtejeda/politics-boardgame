"""
Politics Board Game - Component Graphics Generator
Generates initial graphic concepts for all game components
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Output directory
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Color palette - professional political theme
COLORS = {
    'background': '#1a1a2e',
    'primary': '#16213e',
    'secondary': '#0f3460',
    'accent': '#e94560',
    'gold': '#d4af37',
    'silver': '#c0c0c0',
    'white': '#ffffff',
    'black': '#000000',
    'budget': '#2ecc71',
    'legitimacy': '#9b59b6',
    'stability': '#3498db',
    'growth': '#f39c12',
    'liberty': '#e74c3c',
    # Faction colors
    'progressives': '#8e44ad',
    'conservatives': '#2c3e50',
    'liberals': '#f1c40f',
    'nationalists': '#c0392b',
    'populists': '#27ae60',
    # Vote colors
    'yes': '#27ae60',
    'no': '#c0392b',
    'abstain': '#7f8c8d',
}

def get_font(size, bold=False):
    """Get a font, fallback to default if not available"""
    try:
        if bold:
            return ImageFont.truetype("arialbd.ttf", size)
        return ImageFont.truetype("arial.ttf", size)
    except:
        try:
            return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size)
        except:
            return ImageFont.load_default()

def draw_rounded_rect(draw, coords, radius, fill, outline=None, width=1):
    """Draw a rounded rectangle"""
    x1, y1, x2, y2 = coords
    draw.rounded_rectangle(coords, radius=radius, fill=fill, outline=outline, width=width)

def create_central_board():
    """Create the main game board with resource tracks, institutions, and timeline"""
    width, height = 1600, 1200
    img = Image.new('RGB', (width, height), COLORS['background'])
    draw = ImageDraw.Draw(img)

    # Title
    font_title = get_font(48, bold=True)
    font_header = get_font(28, bold=True)
    font_normal = get_font(18)
    font_small = get_font(14)

    draw.text((width//2, 40), "POLITICS", fill=COLORS['gold'], font=font_title, anchor="mm")
    draw.text((width//2, 85), "Central Game Board", fill=COLORS['silver'], font=font_header, anchor="mm")

    # Resource tracks section (left side)
    draw_rounded_rect(draw, (30, 120, 500, 700), 15, COLORS['primary'], COLORS['gold'], 2)
    draw.text((265, 145), "NATIONAL RESOURCES", fill=COLORS['gold'], font=font_header, anchor="mm")

    resources = [
        ('BUDGET', COLORS['budget'], '-10', '+20', '8'),
        ('LEGITIMACY', COLORS['legitimacy'], '0', '20', '10'),
        ('STABILITY', COLORS['stability'], '0', '20', '10'),
        ('GROWTH', COLORS['growth'], '-5', '+15', '5'),
        ('LIBERTY', COLORS['liberty'], '0', '20', '10'),
    ]

    y_pos = 190
    for name, color, min_val, max_val, start in resources:
        # Resource name
        draw.text((60, y_pos), name, fill=color, font=font_normal)
        # Track background
        draw_rounded_rect(draw, (60, y_pos + 25, 470, y_pos + 55), 5, COLORS['secondary'])
        # Track markers
        for i in range(21):
            x = 70 + i * 19
            draw.ellipse((x-4, y_pos+32, x+4, y_pos+48), fill=COLORS['background'], outline=color)
        # Labels
        draw.text((60, y_pos + 60), f"Min: {min_val}", fill=COLORS['silver'], font=font_small)
        draw.text((400, y_pos + 60), f"Max: {max_val}", fill=COLORS['silver'], font=font_small)
        draw.text((230, y_pos + 60), f"Start: {start}", fill=COLORS['white'], font=font_small)
        y_pos += 100

    # Inequality counter (special)
    draw.text((60, y_pos), "INEQUALITY", fill=COLORS['accent'], font=font_normal)
    draw_rounded_rect(draw, (60, y_pos + 25, 470, y_pos + 55), 5, COLORS['secondary'])
    for i in range(11):
        x = 80 + i * 35
        draw.ellipse((x-8, y_pos+30, x+8, y_pos+50), fill=COLORS['background'], outline=COLORS['accent'])
        draw.text((x, y_pos+40), str(i), fill=COLORS['accent'], font=font_small, anchor="mm")

    # Institution strengths section (right side)
    draw_rounded_rect(draw, (520, 120, 990, 700), 15, COLORS['primary'], COLORS['gold'], 2)
    draw.text((755, 145), "INSTITUTIONS", fill=COLORS['gold'], font=font_header, anchor="mm")

    institutions = ['LEGISLATURE', 'JUDICIARY', 'EXECUTIVE', 'MARKETS', 'PUBLIC OPINION', 'CIVIL SOCIETY']

    y_pos = 190
    for inst in institutions:
        draw.text((540, y_pos), inst, fill=COLORS['white'], font=font_normal)
        # Strength track (1-5)
        for i in range(1, 6):
            x = 540 + i * 80
            draw_rounded_rect(draw, (x-25, y_pos+25, x+25, y_pos+55), 8, COLORS['secondary'], COLORS['silver'])
            draw.text((x, y_pos+40), str(i), fill=COLORS['white'], font=font_normal, anchor="mm")
        y_pos += 80

    # Timeline section (bottom)
    draw_rounded_rect(draw, (30, 720, 990, 900), 15, COLORS['primary'], COLORS['gold'], 2)
    draw.text((510, 745), "DELAYED EFFECTS TIMELINE", fill=COLORS['gold'], font=font_header, anchor="mm")

    # Timeline slots
    rounds = ['Current', '+1', '+2', '+3', '+4', '+5', '+6']
    for i, r in enumerate(rounds):
        x = 80 + i * 125
        draw_rounded_rect(draw, (x, 780, x+110, 880), 10, COLORS['secondary'], COLORS['silver'])
        draw.text((x+55, 800), r, fill=COLORS['white'], font=font_normal, anchor="mm")
        draw.text((x+55, 840), "Effects", fill=COLORS['silver'], font=font_small, anchor="mm")

    # Approval meter (Public Opinion detail)
    draw_rounded_rect(draw, (1010, 120, 1570, 300), 15, COLORS['primary'], COLORS['gold'], 2)
    draw.text((1290, 145), "PUBLIC APPROVAL", fill=COLORS['gold'], font=font_header, anchor="mm")

    # Approval track 0-10
    for i in range(11):
        x = 1040 + i * 48
        color = COLORS['yes'] if i >= 7 else (COLORS['growth'] if i >= 4 else COLORS['no'])
        draw_rounded_rect(draw, (x-18, 180, x+18, 230), 5, color)
        draw.text((x, 205), str(i), fill=COLORS['white'], font=font_normal, anchor="mm")

    draw.text((1290, 260), "Below 3: Governing faction loses 1 Influence/round", fill=COLORS['silver'], font=font_small, anchor="mm")

    # Round tracker
    draw_rounded_rect(draw, (1010, 320, 1570, 450), 15, COLORS['primary'], COLORS['gold'], 2)
    draw.text((1290, 345), "ROUND TRACKER", fill=COLORS['gold'], font=font_header, anchor="mm")

    for i in range(1, 13):
        x = 1030 + ((i-1) % 6) * 88
        y = 380 + ((i-1) // 6) * 40
        draw_rounded_rect(draw, (x, y, x+80, y+35), 5, COLORS['secondary'], COLORS['silver'])
        draw.text((x+40, y+17), str(i), fill=COLORS['white'], font=font_normal, anchor="mm")

    # Quick reference
    draw_rounded_rect(draw, (1010, 470, 1570, 900), 15, COLORS['primary'], COLORS['accent'], 2)
    draw.text((1290, 495), "COLLAPSE CONDITIONS", fill=COLORS['accent'], font=font_header, anchor="mm")

    conditions = [
        "Budget <= 0 for 2 rounds",
        "Legitimacy <= 2",
        "Stability <= 2",
        "Liberty <= 3 + Security policy",
        "Inequality >= 10 & Stability <= 5"
    ]

    y_pos = 540
    for cond in conditions:
        draw.text((1040, y_pos), f"X  {cond}", fill=COLORS['accent'], font=font_normal)
        y_pos += 40

    # Feedback loops reminder
    draw.text((1290, 750), "FEEDBACK LOOPS", fill=COLORS['gold'], font=font_header, anchor="mm")
    loops = ["Growth>10: Budget+1", "Growth<0: Budget-1, Stability-1", "Stability<5: Legitimacy-1"]
    y_pos = 790
    for loop in loops:
        draw.text((1040, y_pos), f"• {loop}", fill=COLORS['silver'], font=font_small)
        y_pos += 25

    # Footer
    draw.text((width//2, height-30), "Politics Board Game - Central Board v1.0", fill=COLORS['silver'], font=font_small, anchor="mm")

    img.save(os.path.join(OUTPUT_DIR, 'central_board.png'), quality=95)
    print("Created: central_board.png")

def create_faction_boards():
    """Create the 5 faction player boards"""
    factions = [
        ('The Progressives', COLORS['progressives'], 'Social Reform', '+1 Legitimacy on Social policies'),
        ('The Conservatives', COLORS['conservatives'], 'Stability Focus', '+1 Stability when blocking rapid change'),
        ('The Liberals', COLORS['liberals'], 'Market & Liberty', '+1 Growth on Economic deregulation'),
        ('The Nationalists', COLORS['nationalists'], 'Security & Sovereignty', '+1 Stability on Security policies'),
        ('The Populists', COLORS['populists'], 'Anti-establishment', '+1 Legitimacy opposing institutional policies'),
    ]

    for faction_name, color, lean, bonus in factions:
        width, height = 800, 500
        img = Image.new('RGB', (width, height), COLORS['background'])
        draw = ImageDraw.Draw(img)

        font_title = get_font(36, bold=True)
        font_header = get_font(22, bold=True)
        font_normal = get_font(16)
        font_small = get_font(12)

        # Border
        draw_rounded_rect(draw, (10, 10, width-10, height-10), 20, COLORS['primary'], color, 4)

        # Faction name and emblem area
        draw_rounded_rect(draw, (30, 30, 350, 130), 15, color)
        draw.text((190, 60), faction_name.upper(), fill=COLORS['white'], font=font_title, anchor="mm")
        draw.text((190, 100), lean, fill=COLORS['white'], font=font_normal, anchor="mm")

        # Bonus box
        draw_rounded_rect(draw, (370, 30, 770, 130), 15, COLORS['secondary'], color, 2)
        draw.text((570, 55), "FACTION BONUS", fill=color, font=font_header, anchor="mm")
        draw.text((570, 90), bonus, fill=COLORS['white'], font=font_normal, anchor="mm")

        # Influence track
        draw_rounded_rect(draw, (30, 150, 770, 260), 15, COLORS['secondary'], COLORS['gold'], 2)
        draw.text((100, 175), "INFLUENCE", fill=COLORS['gold'], font=font_header)

        for i in range(16):
            x = 50 + i * 46
            draw_rounded_rect(draw, (x, 205, x+40, 245), 8, COLORS['background'], COLORS['gold'])
            draw.text((x+20, 225), str(i), fill=COLORS['gold'], font=font_normal, anchor="mm")

        # Legacy priorities section
        draw_rounded_rect(draw, (30, 280, 400, 480), 15, COLORS['secondary'], COLORS['silver'], 2)
        draw.text((215, 305), "LEGACY PRIORITIES", fill=COLORS['silver'], font=font_header, anchor="mm")
        draw.text((215, 335), "(Choose 2 secretly)", fill=COLORS['silver'], font=font_small, anchor="mm")

        legacies = ['Prosperity', 'Equality', 'Freedom', 'Order', 'Institutions', 'Influence']
        for i, leg in enumerate(legacies):
            x = 60 + (i % 2) * 170
            y = 360 + (i // 2) * 35
            draw.rectangle((x, y, x+20, y+20), outline=COLORS['silver'], width=2)
            draw.text((x+30, y+10), leg, fill=COLORS['white'], font=font_normal, anchor="lm")

        # Policy hand area
        draw_rounded_rect(draw, (420, 280, 770, 480), 15, COLORS['secondary'], color, 2)
        draw.text((595, 305), "POLICY HAND", fill=color, font=font_header, anchor="mm")
        draw.text((595, 335), "(Max 5 cards)", fill=COLORS['silver'], font=font_small, anchor="mm")

        # Card slots representation
        for i in range(5):
            x = 445 + i * 62
            draw_rounded_rect(draw, (x, 360, x+55, 460), 5, COLORS['background'], color)

        filename = f"faction_board_{faction_name.lower().replace(' ', '_').replace('the_', '')}.png"
        img.save(os.path.join(OUTPUT_DIR, filename), quality=95)
        print(f"Created: {filename}")

def create_policy_card():
    """Create policy card template"""
    width, height = 400, 560
    img = Image.new('RGB', (width, height), COLORS['primary'])
    draw = ImageDraw.Draw(img)

    font_title = get_font(24, bold=True)
    font_header = get_font(16, bold=True)
    font_normal = get_font(14)
    font_small = get_font(11)

    # Card border
    draw_rounded_rect(draw, (5, 5, width-5, height-5), 15, COLORS['primary'], COLORS['gold'], 3)

    # Category banner
    draw_rounded_rect(draw, (15, 15, 280, 50), 10, COLORS['stability'])
    draw.text((147, 32), "[CATEGORY]", fill=COLORS['white'], font=font_header, anchor="mm")

    # Cost circle
    draw.ellipse((300, 10, 385, 55), fill=COLORS['accent'])
    draw.text((342, 32), "COST", fill=COLORS['white'], font=font_small, anchor="mm")

    # Policy name
    draw_rounded_rect(draw, (15, 60, width-15, 110), 10, COLORS['secondary'])
    draw.text((width//2, 85), "POLICY NAME", fill=COLORS['gold'], font=font_title, anchor="mm")

    # Effects section
    draw_rounded_rect(draw, (15, 120, width-15, 350), 10, COLORS['background'])

    draw.text((25, 135), "IMMEDIATE:", fill=COLORS['yes'], font=font_header)
    draw.text((25, 160), "[Immediate effect description]", fill=COLORS['white'], font=font_normal)
    draw.text((25, 185), "[Resource changes: +X / -Y]", fill=COLORS['silver'], font=font_small)

    draw.line((25, 210, width-25, 210), fill=COLORS['secondary'], width=1)

    draw.text((25, 225), "DELAYED (Xr):", fill=COLORS['growth'], font=font_header)
    draw.text((25, 250), "[Effect that triggers X rounds later]", fill=COLORS['white'], font=font_normal)
    draw.text((25, 275), "[Delayed resource changes]", fill=COLORS['silver'], font=font_small)

    draw.line((25, 300, width-25, 300), fill=COLORS['secondary'], width=1)

    draw.text((25, 315), "TRADEOFF:", fill=COLORS['accent'], font=font_header)
    draw.text((25, 340), "[Negative consequence]", fill=COLORS['accent'], font=font_normal)

    # Requirements
    draw_rounded_rect(draw, (15, 360, width-15, 430), 10, COLORS['secondary'])
    draw.text((25, 375), "REQUIRES:", fill=COLORS['silver'], font=font_header)
    draw.text((25, 400), "Legislature Vote + Judiciary Review", fill=COLORS['white'], font=font_normal)

    # Footer
    draw.line((15, 445, width-15, 445), fill=COLORS['gold'], width=2)

    # Ideology indicator
    draw_rounded_rect(draw, (15, 460, 120, 500), 8, COLORS['progressives'])
    draw.text((67, 480), "LEFT", fill=COLORS['white'], font=font_small, anchor="mm")

    draw_rounded_rect(draw, (140, 460, 260, 500), 8, COLORS['secondary'])
    draw.text((200, 480), "CENTER", fill=COLORS['white'], font=font_small, anchor="mm")

    draw_rounded_rect(draw, (280, 460, 385, 500), 8, COLORS['nationalists'])
    draw.text((332, 480), "RIGHT", fill=COLORS['white'], font=font_small, anchor="mm")

    # Card ID
    draw.text((width//2, 530), "#POL-001", fill=COLORS['silver'], font=font_small, anchor="mm")

    img.save(os.path.join(OUTPUT_DIR, 'policy_card_template.png'), quality=95)
    print("Created: policy_card_template.png")

def create_event_card():
    """Create event card template"""
    width, height = 400, 560
    img = Image.new('RGB', (width, height), COLORS['secondary'])
    draw = ImageDraw.Draw(img)

    font_title = get_font(22, bold=True)
    font_header = get_font(14, bold=True)
    font_normal = get_font(13)
    font_small = get_font(11)

    # Card border
    draw_rounded_rect(draw, (5, 5, width-5, height-5), 15, COLORS['secondary'], COLORS['accent'], 3)

    # Severity banner
    draw_rounded_rect(draw, (15, 15, 180, 50), 10, COLORS['accent'])
    draw.text((97, 32), "SEVERITY", fill=COLORS['white'], font=font_header, anchor="mm")

    # Category
    draw_rounded_rect(draw, (200, 15, 385, 50), 10, COLORS['stability'])
    draw.text((292, 32), "[CATEGORY]", fill=COLORS['white'], font=font_header, anchor="mm")

    # Event name
    draw_rounded_rect(draw, (15, 60, width-15, 110), 10, COLORS['background'])
    draw.text((width//2, 85), "EVENT NAME", fill=COLORS['accent'], font=font_title, anchor="mm")

    # Narrative text
    draw_rounded_rect(draw, (15, 120, width-15, 200), 10, COLORS['primary'])
    draw.text((25, 135), "[Narrative description of the event", fill=COLORS['silver'], font=font_normal)
    draw.text((25, 155), "that sets the scene and explains", fill=COLORS['silver'], font=font_normal)
    draw.text((25, 175), "what is happening in the nation.]", fill=COLORS['silver'], font=font_normal)

    # Effect
    draw_rounded_rect(draw, (15, 210, width-15, 280), 10, COLORS['background'])
    draw.text((25, 225), "EFFECT:", fill=COLORS['gold'], font=font_header)
    draw.text((25, 250), "[What happens automatically]", fill=COLORS['white'], font=font_normal)

    # Response options
    draw_rounded_rect(draw, (15, 290, width-15, 490), 10, COLORS['primary'])
    draw.text((width//2, 310), "RESPONSE OPTIONS", fill=COLORS['gold'], font=font_header, anchor="mm")

    responses = [
        ('A)', '[Choice A]:', '[Consequence A]', COLORS['yes']),
        ('B)', '[Choice B]:', '[Consequence B]', COLORS['growth']),
        ('C)', 'Ignore:', '[Consequence if ignored]', COLORS['no']),
    ]

    y_pos = 335
    for letter, choice, consequence, color in responses:
        draw_rounded_rect(draw, (25, y_pos, 370, y_pos+45), 8, COLORS['background'])
        draw.text((35, y_pos+10), letter, fill=color, font=font_header)
        draw.text((60, y_pos+10), choice, fill=COLORS['white'], font=font_normal)
        draw.text((35, y_pos+28), consequence, fill=COLORS['silver'], font=font_small)
        y_pos += 50

    # Timing
    draw.line((15, 505, width-15, 505), fill=COLORS['accent'], width=2)
    draw_rounded_rect(draw, (120, 515, 280, 545), 8, COLORS['accent'])
    draw.text((200, 530), "IMMEDIATE", fill=COLORS['white'], font=font_header, anchor="mm")

    img.save(os.path.join(OUTPUT_DIR, 'event_card_template.png'), quality=95)
    print("Created: event_card_template.png")

def create_voting_tokens():
    """Create voting tokens (Yes, No, Abstain)"""
    tokens = [
        ('YES', COLORS['yes'], '+1'),
        ('NO', COLORS['no'], '-1'),
        ('ABSTAIN', COLORS['abstain'], '0'),
    ]

    for name, color, value in tokens:
        size = 150
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        font_title = get_font(24, bold=True)
        font_value = get_font(32, bold=True)

        # Token circle
        draw.ellipse((5, 5, size-5, size-5), fill=color, outline=COLORS['white'], width=3)

        # Inner ring
        draw.ellipse((15, 15, size-15, size-15), outline=COLORS['white'], width=2)

        # Text
        draw.text((size//2, size//2 - 15), name, fill=COLORS['white'], font=font_title, anchor="mm")
        draw.text((size//2, size//2 + 20), value, fill=COLORS['white'], font=font_value, anchor="mm")

        img.save(os.path.join(OUTPUT_DIR, f'token_vote_{name.lower()}.png'), quality=95)

    print("Created: token_vote_yes.png, token_vote_no.png, token_vote_abstain.png")

def create_resource_markers():
    """Create resource marker tokens"""
    resources = [
        ('Budget', COLORS['budget'], '$'),
        ('Legitimacy', COLORS['legitimacy'], 'L'),
        ('Stability', COLORS['stability'], 'S'),
        ('Growth', COLORS['growth'], 'G'),
        ('Liberty', COLORS['liberty'], 'F'),
    ]

    for name, color, symbol in resources:
        size = 80
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        font = get_font(36, bold=True)

        # Cube representation (isometric-ish)
        # Top face
        draw.polygon([(size//2, 10), (size-10, size//3), (size//2, size//2), (10, size//3)],
                    fill=color, outline=COLORS['white'])
        # Left face
        draw.polygon([(10, size//3), (size//2, size//2), (size//2, size-10), (10, size-25)],
                    fill=color, outline=COLORS['white'])
        # Right face
        draw.polygon([(size//2, size//2), (size-10, size//3), (size-10, size-25), (size//2, size-10)],
                    fill=color, outline=COLORS['white'])

        # Symbol on top
        draw.text((size//2, size//3), symbol, fill=COLORS['white'], font=font, anchor="mm")

        img.save(os.path.join(OUTPUT_DIR, f'marker_{name.lower()}.png'), quality=95)

    print("Created resource markers: marker_budget.png, marker_legitimacy.png, etc.")

def create_influence_tokens():
    """Create influence tokens"""
    size = 100
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    font = get_font(28, bold=True)
    font_small = get_font(14)

    # Star shape for influence
    from math import cos, sin, pi

    # Outer points of star
    points = []
    center = size // 2
    outer_r = 45
    inner_r = 20

    for i in range(10):
        angle = (i * 36 - 90) * pi / 180
        r = outer_r if i % 2 == 0 else inner_r
        x = center + r * cos(angle)
        y = center + r * sin(angle)
        points.append((x, y))

    draw.polygon(points, fill=COLORS['gold'], outline=COLORS['white'], width=2)
    draw.text((center, center), "I", fill=COLORS['background'], font=font, anchor="mm")

    img.save(os.path.join(OUTPUT_DIR, 'token_influence.png'), quality=95)
    print("Created: token_influence.png")

def create_delayed_effect_markers():
    """Create numbered markers 1-10 for delayed effects"""
    for num in range(1, 11):
        size = 80
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        font = get_font(32, bold=True)
        font_small = get_font(10)

        # Hexagon shape
        from math import cos, sin, pi

        points = []
        center = size // 2
        radius = 35

        for i in range(6):
            angle = (i * 60 - 30) * pi / 180
            x = center + radius * cos(angle)
            y = center + radius * sin(angle)
            points.append((x, y))

        draw.polygon(points, fill=COLORS['growth'], outline=COLORS['white'], width=2)
        draw.text((center, center-5), str(num), fill=COLORS['white'], font=font, anchor="mm")
        draw.text((center, center+18), "DELAY", fill=COLORS['white'], font=font_small, anchor="mm")

        img.save(os.path.join(OUTPUT_DIR, f'marker_delay_{num}.png'), quality=95)

    print("Created: marker_delay_1.png through marker_delay_10.png")

def create_first_player_marker():
    """Create the first player marker"""
    width, height = 120, 150
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    font_title = get_font(14, bold=True)
    font_num = get_font(48, bold=True)

    # Shield/banner shape
    points = [
        (10, 10), (width-10, 10),  # Top
        (width-10, 100),  # Right side
        (width//2, height-10),  # Bottom point
        (10, 100)  # Left side
    ]

    draw.polygon(points, fill=COLORS['gold'], outline=COLORS['white'], width=3)

    # Inner decoration
    inner_points = [
        (20, 20), (width-20, 20),
        (width-20, 90),
        (width//2, height-25),
        (20, 90)
    ]
    draw.polygon(inner_points, outline=COLORS['background'], width=2)

    draw.text((width//2, 35), "FIRST", fill=COLORS['background'], font=font_title, anchor="mm")
    draw.text((width//2, 75), "1", fill=COLORS['background'], font=font_num, anchor="mm")
    draw.text((width//2, 110), "PLAYER", fill=COLORS['background'], font=font_title, anchor="mm")

    img.save(os.path.join(OUTPUT_DIR, 'marker_first_player.png'), quality=95)
    print("Created: marker_first_player.png")

def create_tracking_sheet():
    """Create a tracking sheet template"""
    width, height = 800, 1100
    img = Image.new('RGB', (width, height), COLORS['white'])
    draw = ImageDraw.Draw(img)

    font_title = get_font(28, bold=True)
    font_header = get_font(16, bold=True)
    font_normal = get_font(12)

    # Title
    draw.rectangle((0, 0, width, 60), fill=COLORS['primary'])
    draw.text((width//2, 30), "POLITICS - Game Tracking Sheet", fill=COLORS['gold'], font=font_title, anchor="mm")

    # Game info section
    draw.text((30, 80), "Game Date: _______________", fill=COLORS['black'], font=font_normal)
    draw.text((300, 80), "Players: _______________", fill=COLORS['black'], font=font_normal)
    draw.text((550, 80), "Rounds: _______________", fill=COLORS['black'], font=font_normal)

    # Round tracking table
    draw.text((30, 120), "ROUND-BY-ROUND TRACKING", fill=COLORS['primary'], font=font_header)

    # Table header
    headers = ['Round', 'Budget', 'Legit.', 'Stab.', 'Growth', 'Liberty', 'Ineq.', 'Approval', 'Notes']
    col_widths = [50, 60, 60, 60, 60, 60, 50, 70, 250]

    x = 30
    y = 145
    for i, header in enumerate(headers):
        draw.rectangle((x, y, x+col_widths[i], y+25), fill=COLORS['primary'])
        draw.text((x + col_widths[i]//2, y+12), header, fill=COLORS['white'], font=font_normal, anchor="mm")
        x += col_widths[i]

    # Table rows
    for row in range(12):
        x = 30
        y = 170 + row * 30
        for i, w in enumerate(col_widths):
            draw.rectangle((x, y, x+w, y+30), outline=COLORS['black'])
            if i == 0:
                draw.text((x + w//2, y+15), str(row+1), fill=COLORS['black'], font=font_normal, anchor="mm")
            x += w

    # Delayed effects section
    y_section = 550
    draw.text((30, y_section), "DELAYED EFFECTS LOG", fill=COLORS['primary'], font=font_header)

    effect_headers = ['#', 'Effect Description', 'Triggers Round', 'Status']
    effect_widths = [30, 450, 100, 100]

    x = 30
    y = y_section + 25
    for i, header in enumerate(effect_headers):
        draw.rectangle((x, y, x+effect_widths[i], y+25), fill=COLORS['secondary'])
        draw.text((x + effect_widths[i]//2, y+12), header, fill=COLORS['white'], font=font_normal, anchor="mm")
        x += effect_widths[i]

    for row in range(10):
        x = 30
        y = y_section + 50 + row * 25
        for i, w in enumerate(effect_widths):
            draw.rectangle((x, y, x+w, y+25), outline=COLORS['black'])
            if i == 0:
                draw.text((x + w//2, y+12), str(row+1), fill=COLORS['black'], font=font_normal, anchor="mm")
            x += w

    # Player influence tracking
    y_section = 830
    draw.text((30, y_section), "PLAYER INFLUENCE TRACKING", fill=COLORS['primary'], font=font_header)

    player_headers = ['Player/Faction', 'Start', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'Final']
    player_widths = [140] + [45] * 12

    x = 30
    y = y_section + 25
    for i, header in enumerate(player_headers):
        draw.rectangle((x, y, x+player_widths[i], y+25), fill=COLORS['gold'])
        draw.text((x + player_widths[i]//2, y+12), header, fill=COLORS['black'], font=font_normal, anchor="mm")
        x += player_widths[i]

    for row in range(5):
        x = 30
        y = y_section + 50 + row * 30
        for i, w in enumerate(player_widths):
            draw.rectangle((x, y, x+w, y+30), outline=COLORS['black'])
            x += w

    # Footer
    draw.text((width//2, height-30), "Politics Board Game - Tracking Sheet v1.0", fill=COLORS['silver'], font=font_normal, anchor="mm")

    img.save(os.path.join(OUTPUT_DIR, 'tracking_sheet.png'), quality=95)
    print("Created: tracking_sheet.png")

def create_dice_concept():
    """Create a dice concept illustration"""
    size = 200
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    font = get_font(48, bold=True)
    font_small = get_font(14)

    # 3D cube representation
    # Front face
    draw.polygon([(30, 60), (120, 60), (120, 150), (30, 150)],
                fill=COLORS['accent'], outline=COLORS['white'], width=2)
    # Top face
    draw.polygon([(30, 60), (120, 60), (170, 30), (80, 30)],
                fill=COLORS['nationalists'], outline=COLORS['white'], width=2)
    # Right face
    draw.polygon([(120, 60), (170, 30), (170, 120), (120, 150)],
                fill=COLORS['secondary'], outline=COLORS['white'], width=2)

    # Dots on front face (showing 6)
    dot_positions = [(50, 80), (75, 80), (100, 80), (50, 130), (75, 130), (100, 130)]
    for x, y in dot_positions:
        draw.ellipse((x-6, y-6, x+6, y+6), fill=COLORS['white'])

    # Label
    draw.text((size//2, 175), "2 × D6", fill=COLORS['white'], font=font_small, anchor="mm")

    img.save(os.path.join(OUTPUT_DIR, 'dice_concept.png'), quality=95)
    print("Created: dice_concept.png")

def main():
    print("=" * 50)
    print("Politics Board Game - Component Generator")
    print("=" * 50)
    print(f"Output directory: {OUTPUT_DIR}")
    print()

    create_central_board()
    create_faction_boards()
    create_policy_card()
    create_event_card()
    create_voting_tokens()
    create_resource_markers()
    create_influence_tokens()
    create_delayed_effect_markers()
    create_first_player_marker()
    create_tracking_sheet()
    create_dice_concept()

    print()
    print("=" * 50)
    print("All components generated successfully!")
    print("=" * 50)

if __name__ == "__main__":
    main()
