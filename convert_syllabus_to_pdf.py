"""
Convert syllabus.md to syllabus.pdf
Style: clean document look matching the reference image.
  - Large title with emoji, dark blue bold
  - Subtitle in a left-bordered callout box (light blue bg)
  - Module headings: large, dark blue
  - Goal text: italic, grey
  - Tables: white background, blue bold headers (no fill), light border grid
  - Inline code: monospace, teal colour, light grey background
  - Generous padding, open feel
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, Flowable
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# ── Output ────────────────────────────────────────────────────────────────────
OUTPUT = "python-for-kids/syllabus.pdf"

# ── Colours (matching reference image) ───────────────────────────────────────
C_TITLE      = colors.HexColor("#1A237E")   # very dark blue  — title
C_MODULE     = colors.HexColor("#1565C0")   # medium dark blue — module headings
C_HEADER_TXT = colors.HexColor("#1565C0")   # blue text in table header row
C_CODE       = colors.HexColor("#00838F")   # teal — inline code text
C_CODE_BG    = colors.HexColor("#F0F4F8")   # very light grey-blue — code bg
C_CALLOUT_BG = colors.HexColor("#EEF4FB")   # light blue — subtitle callout bg
C_CALLOUT_BAR= colors.HexColor("#90CAF9")   # medium blue — left bar of callout
C_RULE       = colors.HexColor("#BDBDBD")   # light grey — horizontal rules
C_GRID       = colors.HexColor("#CFD8DC")   # table grid lines
C_ITALIC     = colors.HexColor("#555555")   # grey — italic goal text
C_BODY       = colors.HexColor("#212121")   # near-black — body text

# ── Page setup ────────────────────────────────────────────────────────────────
PAGE_W, PAGE_H = A4
LM = RM = 2.2 * cm
TM = BM = 2.0 * cm
USABLE_W = PAGE_W - LM - RM   # ≈ 16.6 cm

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    leftMargin=LM, rightMargin=RM,
    topMargin=TM,  bottomMargin=BM,
    title="Python for Kids — Syllabus",
    author="Python for Kids",
)

# ── Styles ────────────────────────────────────────────────────────────────────
base = getSampleStyleSheet()

def ps(name, parent="Normal", **kw):
    return ParagraphStyle(name, parent=base[parent], **kw)

title_style = ps("DocTitle",
    fontSize=22, fontName="Helvetica-Bold",
    textColor=C_TITLE, spaceAfter=2, leading=28)

subtitle_callout = ps("Callout",
    fontSize=10, fontName="Helvetica",
    textColor=C_BODY, leading=16,
    leftIndent=12, rightIndent=8,
    spaceBefore=0, spaceAfter=0)

module_style = ps("ModuleH",
    fontSize=16, fontName="Helvetica-Bold",
    textColor=C_MODULE, spaceBefore=18, spaceAfter=4, leading=22)

goal_style = ps("Goal",
    fontSize=10, fontName="Helvetica-Oblique",
    textColor=C_ITALIC, spaceAfter=8, leading=15)

body_style = ps("Body",
    fontSize=9.5, fontName="Helvetica",
    textColor=C_BODY, leading=14, spaceAfter=4)

bold_body = ps("BoldBody",
    fontSize=9.5, fontName="Helvetica-Bold",
    textColor=C_BODY, leading=14, spaceAfter=4)

bullet_style = ps("Bullet",
    fontSize=9.5, fontName="Helvetica",
    textColor=C_BODY, leading=14, leftIndent=14, spaceAfter=3)

note_style = ps("Note",
    fontSize=9, fontName="Helvetica-Oblique",
    textColor=C_ITALIC, leading=13, spaceAfter=3)

section_h = ps("SectionH",
    fontSize=13, fontName="Helvetica-Bold",
    textColor=C_MODULE, spaceBefore=14, spaceAfter=4, leading=18)

# ── Callout box (left blue bar + light bg) ────────────────────────────────────
class CalloutBox(Flowable):
    """A paragraph inside a left-bordered callout box."""
    def __init__(self, text, width, bar_color=C_CALLOUT_BAR, bg=C_CALLOUT_BG):
        super().__init__()
        self.text = text
        self._width = width
        self.bar_color = bar_color
        self.bg = bg
        self._para = Paragraph(text, subtitle_callout)
        self._para_w = width - 20   # 4px bar + 8px gap + 8px right pad

    def wrap(self, availW, availH):
        w, h = self._para.wrap(self._para_w, availH)
        self._h = h + 16   # top + bottom padding
        return self._width, self._h

    def draw(self):
        c = self.canv
        # background
        c.setFillColor(self.bg)
        c.rect(0, 0, self._width, self._h, fill=1, stroke=0)
        # left bar
        c.setFillColor(self.bar_color)
        c.rect(0, 0, 4, self._h, fill=1, stroke=0)
        # paragraph
        self._para.drawOn(c, 16, 8)


# ── Inline code helper ────────────────────────────────────────────────────────
def code(text):
    """Return text formatted as inline code (monospace, teal, light bg)."""
    # We use a small rounded-rect illusion via XML markup in Paragraph
    return (f'<font name="Courier" color="#00838F">'
            f'<font backColor="#F0F4F8"> {text} </font></font>')


# ── Table cell paragraph ──────────────────────────────────────────────────────
def _cell_style(bold=False, color=C_BODY, size=9):
    return ParagraphStyle(
        f"cell_{'b' if bold else 'n'}_{id(color)}",
        parent=base["Normal"],
        fontSize=size,
        fontName="Helvetica-Bold" if bold else "Helvetica",
        textColor=color,
        leading=13,
        wordWrap="CJK",
    )

def cell(text, bold=False, color=C_BODY, size=9):
    return Paragraph(text, _cell_style(bold=bold, color=color, size=size))

def hcell(text):
    """Header cell: bold, blue."""
    return cell(text, bold=True, color=C_HEADER_TXT, size=9)


# ── Build a module table ──────────────────────────────────────────────────────
def module_table(rows, col_widths):
    """
    rows: list of 4-tuples (lesson_no, title, key_concepts, scratch)
    Each field is a string; backtick-wrapped tokens become inline code.
    """
    import re

    def fmt(text):
        """Replace `token` with inline code markup."""
        return re.sub(r'`([^`]+)`', lambda m: code(m.group(1)), text)

    header = [hcell("Lesson"), hcell("Title"),
              hcell("Key Concepts"), hcell("Scratch\nConnection")]
    data = [header]
    for row in rows:
        data.append([cell(fmt(str(c))) for c in row])

    tbl = Table(data, colWidths=col_widths, repeatRows=1)
    tbl.setStyle(TableStyle([
        # Header row: white bg, blue bold text (already set via hcell)
        ("BACKGROUND",   (0, 0), (-1, 0),  colors.white),
        ("LINEBELOW",    (0, 0), (-1, 0),  1.2, C_MODULE),   # thick blue line under header
        # Data rows: white bg
        ("BACKGROUND",   (0, 1), (-1, -1), colors.white),
        # Grid: light grey
        ("GRID",         (0, 0), (-1, -1), 0.5, C_GRID),
        # Outer border: slightly darker
        ("BOX",          (0, 0), (-1, -1), 0.8, C_GRID),
        # Padding
        ("TOPPADDING",   (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 8),
        ("LEFTPADDING",  (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("VALIGN",       (0, 0), (-1, -1), "TOP"),
    ]))
    return tbl


# ── Column widths for module tables ──────────────────────────────────────────
CW = [1.4*cm, 3.8*cm, 7.4*cm, 4.0*cm]   # Lesson / Title / Key Concepts / Scratch


# ── Story ─────────────────────────────────────────────────────────────────────
story = []

# ── Title ─────────────────────────────────────────────────────────────────────
story.append(Spacer(1, 0.2*cm))
story.append(Paragraph("🐍 Python for Kids — Syllabus", title_style))
story.append(Spacer(1, 0.25*cm))
story.append(HRFlowable(width="100%", thickness=0.8, color=C_RULE))
story.append(Spacer(1, 0.3*cm))

# ── Subtitle callout ──────────────────────────────────────────────────────────
story.append(CalloutBox(
    "A Python course for students transitioning from Scratch. "
    "Focus: Logical thinking, Math, Turtle Graphics. "
    "Tool: Thonny IDE | Python 3",
    width=USABLE_W,
))
story.append(Spacer(1, 0.35*cm))
story.append(HRFlowable(width="100%", thickness=0.8, color=C_RULE))

# ─────────────────────────────────────────────────────────────────────────────
# MODULE 1
# ─────────────────────────────────────────────────────────────────────────────
story.append(Paragraph("Module 1: Hello Python! (Lessons 1–4)", module_style))
story.append(Paragraph("Goal: Get comfortable with Thonny and basic Python syntax.", goal_style))

story.append(module_table([
    ["1", "Meet Thonny &amp; Python",
     "Open Thonny, write `print()`, run a program, what is a \"program\"",
     "Scratch: green flag → `print()`"],
    ["2", "Numbers and Math",
     "`+`, `-`, `*`, `/`, `//`, `%`, `print()` with math",
     "Scratch: operators block"],
    ["3", "Variables —\nBoxes with Names",
     "Create variables, assign values, update values, naming rules",
     'Scratch: "Make a Variable"'],
    ["4", "Input — Talking to the Computer",
     "`input()`, `int()`, `float()`, build a simple calculator",
     'Scratch: "ask and wait"'],
], CW))

# ─────────────────────────────────────────────────────────────────────────────
# MODULE 2
# ─────────────────────────────────────────────────────────────────────────────
story.append(Paragraph("Module 2: Making Decisions (Lessons 5–7)", module_style))
story.append(Paragraph('Goal: Use conditions to make programs "think".', goal_style))

story.append(module_table([
    ["5", "If — Yes or No?",
     "`if`, `else`, comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)",
     'Scratch: "if / else" block'],
    ["6", "If-Elif-Else —\nMany Choices",
     "`elif`, chained conditions, nested `if`",
     "Scratch: nested if blocks"],
    ["7", "Logic: And, Or, Not",
     "`and`, `or`, `not`, combining conditions, truth tables",
     'Scratch: "and", "or", "not" blocks'],
], CW))

# ─────────────────────────────────────────────────────────────────────────────
# MODULE 3
# ─────────────────────────────────────────────────────────────────────────────
story.append(Paragraph("Module 3: Loops — Do It Again! (Lessons 8–11)", module_style))
story.append(Paragraph("Goal: Repeat actions using loops.", goal_style))

story.append(module_table([
    ["8",  "For Loop —\nCount and Repeat",
     "`for i in range()`, `range(start, stop, step)`",
     'Scratch: "repeat 10"'],
    ["9",  "While Loop —\nRepeat Until",
     "`while`, loop with condition, `break`",
     'Scratch: "repeat until"'],
    ["10", "Nested Loops",
     "Loop inside a loop, multiplication table, patterns",
     'Scratch: nested "repeat"'],
    ["11", "Loop Challenges",
     "Combine loops + conditions, number patterns, FizzBuzz",
     "—"],
], CW))

# ─────────────────────────────────────────────────────────────────────────────
# MODULE 4
# ─────────────────────────────────────────────────────────────────────────────
story.append(Paragraph("Module 4: Turtle Graphics — Draw with Code! (Lessons 12–17)", module_style))
story.append(Paragraph("Goal: Use the turtle module to draw shapes and patterns.", goal_style))

story.append(module_table([
    ["12", "Meet the Turtle",
     "`import turtle`, `forward()`, `right()`, `left()`, `penup()`, `pendown()`",
     "Scratch: pen extension"],
    ["13", "Colors and Shapes",
     "`pencolor()`, `fillcolor()`, `begin_fill()`, `end_fill()`, `circle()`",
     "—"],
    ["14", "Loops + Turtle\n= Magic",
     "Draw polygons with loops, circles, stars",
     "—"],
    ["15", "Spirals and Patterns",
     "Spiral shapes, growing patterns, rotating shapes",
     "—"],
    ["16", "Creative Drawing",
     "Houses, trees, flowers, emoji faces, scenes",
     "—"],
    ["17", "Turtle Art Project",
     "Free drawing project, combine all turtle skills",
     "—"],
], CW))

# ─────────────────────────────────────────────────────────────────────────────
# MODULE 5
# ─────────────────────────────────────────────────────────────────────────────
story.append(Paragraph("Module 5: Math Power! (Lessons 18–23)", module_style))
story.append(Paragraph("Goal: Solve math problems with Python.", goal_style))

story.append(module_table([
    ["18", "Power and Exponents",
     "`**` operator, positive/negative exponents, `pow()`",
     "—"],
    ["19", "Square Root and\nmath Module",
     "`import math`, `math.sqrt()`, `math.pow()`, perfect squares",
     "—"],
    ["20", "The Pythagorean\nTheorem",
     "a² + b² = c², calculate hypotenuse, check right triangles",
     "—"],
    ["21", "Even, Odd and\nDivisibility",
     "`%` modulo, check even/odd, GCD, LCM, divisibility rules",
     "—"],
    ["22", "Number Patterns\nand Sequences",
     "Arithmetic sequences, geometric sequences, Fibonacci",
     "—"],
    ["23", "Math Challenge Round",
     "Mixed math problems, combine all math concepts",
     "—"],
], CW))

# ─────────────────────────────────────────────────────────────────────────────
# MODULE 6
# ─────────────────────────────────────────────────────────────────────────────
story.append(Paragraph("Module 6: Lists — Organize Your Data (Lessons 24–27)", module_style))
story.append(Paragraph("Goal: Store and manage collections of data.", goal_style))

story.append(module_table([
    ["24", "Lists — Your\nFirst Collection",
     "Create lists, access items by index, `len()`, `append()`",
     "Scratch: lists"],
    ["25", "Loop Through Lists",
     "`for item in list`, `for i in range(len(list))`, find min/max",
     'Scratch: "for each"'],
    ["26", "List Operations",
     "`sort()`, `reverse()`, `remove()`, `insert()`, slicing basics",
     "—"],
    ["27", "Lists + Math",
     "Sum of list, average, filter numbers, list comprehension intro",
     "—"],
], CW))

# ─────────────────────────────────────────────────────────────────────────────
# MODULE 7
# ─────────────────────────────────────────────────────────────────────────────
story.append(Paragraph("Module 7: Functions — Build Your Own Blocks (Lessons 28–31)", module_style))
story.append(Paragraph("Goal: Write reusable code with functions.", goal_style))

story.append(module_table([
    ["28", "What is a Function?",
     "`def`, function name, call a function, DRY principle",
     'Scratch: "My Blocks"'],
    ["29", "Parameters and Return",
     "Parameters, arguments, `return`, default values",
     'Scratch: "My Blocks" with inputs'],
    ["30", "Functions + Turtle",
     "Draw shapes with functions, reusable drawing blocks",
     "—"],
    ["31", "Functions + Math",
     "Math helper functions, mini calculator, recursion intro",
     "—"],
], CW))

# ─────────────────────────────────────────────────────────────────────────────
# MODULE 8
# ─────────────────────────────────────────────────────────────────────────────
story.append(Paragraph("Module 8: Putting It All Together (Lessons 32–34)", module_style))
story.append(Paragraph("Goal: Combine everything learned into bigger programs.", goal_style))

story.append(module_table([
    ["32", "Turtle + Math Combo",
     "Math-based art: Fibonacci spiral, Pythagorean shapes",
     "—"],
    ["33", "Problem Solving\nStrategies",
     "Break down problems, pseudocode, plan before coding, debug tips",
     "—"],
    ["34", "Grand Review\n&amp; Challenge",
     "Review all concepts, mixed challenge problems",
     "—"],
], CW))

# ─────────────────────────────────────────────────────────────────────────────
# SUMMARY TABLE
# ─────────────────────────────────────────────────────────────────────────────
story.append(Spacer(1, 0.5*cm))
story.append(HRFlowable(width="100%", thickness=0.8, color=C_RULE))
story.append(Paragraph("Course Summary", section_h))

sum_cw = [5.5*cm, 2.2*cm, 8.9*cm]
sum_header = [hcell("Module"), hcell("Lessons"), hcell("Focus")]
sum_rows_data = [
    ["1. Hello Python!",           "1–4",   "Basics: print, math, variables, input"],
    ["2. Making Decisions",        "5–7",   "if / elif / else, logic"],
    ["3. Loops",                   "8–11",  "for, while, nested loops"],
    ["4. Turtle Graphics",         "12–17", "Drawing with code"],
    ["5. Math Power!",             "18–23", "Exponents, roots, Pythagorean, patterns"],
    ["6. Lists",                   "24–27", "Collections, list operations"],
    ["7. Functions",               "28–31", "def, parameters, return"],
    ["8. Putting It All Together", "32–34", "Combine all skills"],
]
sum_data = [sum_header] + [[cell(c) for c in r] for r in sum_rows_data]
sum_tbl = Table(sum_data, colWidths=sum_cw, repeatRows=1)
sum_tbl.setStyle(TableStyle([
    ("BACKGROUND",    (0, 0), (-1, 0),  colors.white),
    ("LINEBELOW",     (0, 0), (-1, 0),  1.2, C_MODULE),
    ("BACKGROUND",    (0, 1), (-1, -1), colors.white),
    ("GRID",          (0, 0), (-1, -1), 0.5, C_GRID),
    ("BOX",           (0, 0), (-1, -1), 0.8, C_GRID),
    ("TOPPADDING",    (0, 0), (-1, -1), 7),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ("LEFTPADDING",   (0, 0), (-1, -1), 8),
    ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
    ("VALIGN",        (0, 0), (-1, -1), "TOP"),
]))
story.append(sum_tbl)
story.append(Spacer(1, 0.2*cm))
story.append(Paragraph(
    "<b>Total: 34 lessons (~34 weeks at 1 lesson/week, 75 minutes each)</b>",
    body_style))

# ─────────────────────────────────────────────────────────────────────────────
# HOMEWORK STRUCTURE
# ─────────────────────────────────────────────────────────────────────────────
story.append(Spacer(1, 0.4*cm))
story.append(HRFlowable(width="100%", thickness=0.8, color=C_RULE))
story.append(Paragraph("Homework Structure", section_h))
story.append(Paragraph(
    "Every lesson includes homework with 3 difficulty levels:", body_style))

hw_cw = [2.8*cm, 9.8*cm, 3.8*cm]
hw_header = [hcell("Level"), hcell("Description"), hcell("Exercises")]
hw_rows_data = [
    ["🟢 Easy",   "Practice the basics from the lesson",         "5–7 exercises"],
    ["🟡 Medium", "Apply concepts in new situations",            "5–7 exercises"],
    ["🔴 Hard",   "Problem solving — real-world story problems", "5–7 exercises"],
]
hw_data = [hw_header] + [[cell(c) for c in r] for r in hw_rows_data]
hw_tbl = Table(hw_data, colWidths=hw_cw, repeatRows=1)
hw_tbl.setStyle(TableStyle([
    ("BACKGROUND",    (0, 0), (-1, 0),  colors.white),
    ("LINEBELOW",     (0, 0), (-1, 0),  1.2, C_MODULE),
    ("BACKGROUND",    (0, 1), (-1, -1), colors.white),
    ("GRID",          (0, 0), (-1, -1), 0.5, C_GRID),
    ("BOX",           (0, 0), (-1, -1), 0.8, C_GRID),
    ("TOPPADDING",    (0, 0), (-1, -1), 7),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ("LEFTPADDING",   (0, 0), (-1, -1), 8),
    ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
    ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
]))
story.append(hw_tbl)
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>Exercise Format</b>", bold_body))
for item in [
    "<b>Problem description</b> — what to do",
    "<b>Input</b> — what the program receives, with constraints",
    "<b>Output</b> — what the program should print",
    "<b>Example</b> — sample input → sample output",
]:
    story.append(Paragraph("• " + item, bullet_style))

story.append(Spacer(1, 0.2*cm))
story.append(Paragraph(
    "Hard exercises follow a <b>problem-solving format</b> inspired by competitive "
    "programming for kids: a real-world story, clear input/output specification, "
    "and example test cases.",
    body_style))
story.append(Paragraph(
    "Answers are provided in a separate answers.md file for each lesson.",
    note_style))

# ─────────────────────────────────────────────────────────────────────────────
# NOTES FOR TEACHERS
# ─────────────────────────────────────────────────────────────────────────────
story.append(Spacer(1, 0.4*cm))
story.append(HRFlowable(width="100%", thickness=0.8, color=C_RULE))
story.append(Paragraph("Notes for Teachers", section_h))
for note in [
    "Each lesson is <b>75 minutes</b>.",
    "Students type slowly — allow extra time for coding.",
    "Use Thonny's <b>variable inspector</b> to help students visualize values.",
    "Connect every new concept back to <b>Scratch</b> when possible.",
    "Encourage students to <b>experiment and make mistakes</b>.",
    "Hard exercises can be assigned as homework or used as extension activities.",
]:
    story.append(Paragraph("• " + note, bullet_style))

story.append(Spacer(1, 0.5*cm))
story.append(HRFlowable(width="100%", thickness=0.8, color=C_RULE))
story.append(Spacer(1, 0.2*cm))
story.append(Paragraph("Python for Kids — Happy Coding! 🐍", note_style))

# ── Build ─────────────────────────────────────────────────────────────────────
doc.build(story)
print(f"PDF created: {OUTPUT}")
