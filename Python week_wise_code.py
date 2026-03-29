"""
╔══════════════════════════════════════════════════════════════════════════════╗
║   LIL-CAMP — Lost Item Logger System for College Campus                     ║
║   24SC2007 Python Programming | PBL Project 14                              ║
║   WEEK-WISE IMPLEMENTATION — All 12 Weeks in One File                       ║
║                                                                              ║
║   Each week builds on the previous, progressively adding Python concepts.   ║
║   Run any week independently: python week_wise_code.py                      ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

# ════════════════════════════════════════════════════════════════════════════
# WEEK 1 — Python Setup + Basic Lost-Item Record Capture
# Deliverable: stage1_basic_item.py
# Concepts: variables, input(), print(), f-strings
# ════════════════════════════════════════════════════════════════════════════

def week1_basic_capture():
    """
    WEEK 1: Basic data capture — collect all fields for a lost item
    and display a formatted record. No loops, no functions, no classes.
    """
    print("\n" + "="*60)
    print("  WEEK 1 — Basic Lost Item Record Capture")
    print("="*60)

    print("\n--- Lost Item Registration ---")
    item_name   = input("Enter item name         : ")
    description = input("Enter description       : ")
    location    = input("Enter location lost     : ")
    date_lost   = input("Enter date (DD-MM-YYYY) : ")
    contact     = input("Enter your contact no.  : ")

    print("\n--- Item Categories ---")
    print("  Documents | Electronics | Accessories | Books | Keys | "
          "Clothing | Mobile | Wallet | Others")
    category = input("Enter category          : ")

    print("\n" + "─"*60)
    print("        LOST ITEM RECORD")
    print("─"*60)
    print(f"  Item Name   : {item_name}")
    print(f"  Category    : {category}")
    print(f"  Description : {description}")
    print(f"  Location    : {location}")
    print(f"  Date Lost   : {date_lost}")
    print(f"  Contact     : {contact}")
    print("─"*60)

    # Sample Terminal Output
    # Enter item name         : Student ID Card
    # Enter description       : Green laminated ID, CSE dept
    # Enter location lost     : Library
    # Enter date (DD-MM-YYYY) : 20-03-2026
    # Enter your contact no.  : 9876543210
    # Enter category          : Documents
    #
    # ────────────────────────────────────────────────────
    #         LOST ITEM RECORD
    # ────────────────────────────────────────────────────
    #   Item Name   : Student ID Card
    #   Category    : Documents
    #   Description : Green laminated ID, CSE dept
    #   Location    : Library
    #   Date Lost   : 20-03-2026
    #   Contact     : 9876543210
    # ────────────────────────────────────────────────────


# ════════════════════════════════════════════════════════════════════════════
# WEEK 2 — Menu-Driven System
# Deliverable: stage2_menu.py
# Concepts: while loop, if/elif/else, basic user interaction
# ════════════════════════════════════════════════════════════════════════════

def week2_menu_system():
    """
    WEEK 2: Menu-driven system — Add Lost Item, Add Found Item,
    Search, Exit. Items stored in a simple list.
    """
    print("\n" + "="*60)
    print("  WEEK 2 — Menu-Driven Lost & Found System")
    print("="*60)

    # In-memory storage (plain lists)
    lost_items  = []
    found_items = []

    while True:
        print("\n--- LIL-CAMP Main Menu ---")
        print("1. Add Lost Item")
        print("2. Add Found Item")
        print("3. View All Items")
        print("4. Exit")

        choice = input("\nEnter choice (1-4): ").strip()

        if choice == "1":
            print("\n-- Add Lost Item --")
            name    = input("Item name   : ")
            loc     = input("Location    : ")
            contact = input("Contact     : ")
            lost_items.append(f"{name} | {loc} | {contact} | LOST")
            print(f"  ✔  Lost item '{name}' registered.")

        elif choice == "2":
            print("\n-- Add Found Item --")
            name   = input("Item name   : ")
            loc    = input("Location    : ")
            finder = input("Finder name : ")
            found_items.append(f"{name} | {loc} | {finder} | FOUND")
            print(f"  ✔  Found item '{name}' logged.")

        elif choice == "3":
            print("\n--- Lost Items ---")
            if lost_items:
                for idx, item in enumerate(lost_items, 1):
                    print(f"  {idx}. {item}")
            else:
                print("  No lost items on record.")

            print("\n--- Found Items ---")
            if found_items:
                for idx, item in enumerate(found_items, 1):
                    print(f"  {idx}. {item}")
            else:
                print("  No found items on record.")

        elif choice == "4":
            print("  Goodbye!")
            break
        else:
            print("  Invalid choice. Please enter 1–4.")

    # Sample Output:
    # --- LIL-CAMP Main Menu ---
    # 1. Add Lost Item  2. Add Found Item  3. View All Items  4. Exit
    # Enter choice: 1
    # Item name   : Wallet
    # Location    : Canteen
    # Contact     : 9876543210
    #   ✔  Lost item 'Wallet' registered.


# ════════════════════════════════════════════════════════════════════════════
# WEEK 3 — Strings & Lists
# Deliverable: stage3_search.py
# Concepts: string methods, list operations, search, input cleanup
# ════════════════════════════════════════════════════════════════════════════

def week3_strings_lists():
    """
    WEEK 3: String manipulation + list features.
    Add search-by-name, input normalisation, list display.
    """
    print("\n" + "="*60)
    print("  WEEK 3 — Strings & Lists")
    print("="*60)

    items = [
        "Student ID Card | Library | 9876543210 | Lost",
        "Blue Pendrive   | Computer Lab | 9123456780 | Lost",
        "Black Calculator| Exam Hall | 9988776655 | Lost",
        "Brown Wallet    | Canteen | 8765432109 | Found",
        "Python Textbook | Library | 6543210987 | Found",
    ]

    def list_all():
        print("\n--- All Items ---")
        for idx, item in enumerate(items, 1):
            print(f"  {idx}. {item}")

    def search_by_name(keyword):
        keyword = keyword.strip().lower()
        results = [i for i in items if keyword in i.lower()]
        print(f"\n--- Search Results for '{keyword}' ---")
        if results:
            for r in results:
                print(f"  ▶ {r}")
        else:
            print("  No matching items found.")

    def clean_input(text):
        """Normalise user input: strip whitespace, title-case."""
        return text.strip().title()

    def count_by_status():
        lost  = sum(1 for i in items if "Lost"  in i)
        found = sum(1 for i in items if "Found" in i)
        print(f"\n  Total Lost  : {lost}")
        print(f"  Total Found : {found}")
        print(f"  Grand Total : {len(items)}")

    # Demo
    list_all()
    keyword = input("\n  Enter keyword to search: ")
    search_by_name(keyword)
    count_by_status()

    # String operations demo
    sample = "  student id card   "
    print(f"\n  Original : '{sample}'")
    print(f"  Cleaned  : '{clean_input(sample)}'")
    print(f"  Upper    : '{sample.strip().upper()}'")
    print(f"  Words    : {sample.strip().split()}")

    # Sample Output:
    # Enter keyword to search: library
    #   ▶ Student ID Card | Library | 9876543210 | Lost
    #   ▶ Python Textbook | Library | 6543210987 | Found
    # Total Lost  : 3 | Total Found : 2 | Grand Total : 5


# ════════════════════════════════════════════════════════════════════════════
# WEEK 4 — Functional Architecture
# Deliverable: stage4_modular.py
# Concepts: functions, parameters, return values, docstrings
# ════════════════════════════════════════════════════════════════════════════

# ── Module-level in-memory store ─────────────────────────────────────────────
_w4_lost  = []
_w4_found = []
_w4_id    = [1000]

def _w4_next_id():
    _w4_id[0] += 1
    return _w4_id[0]

def week4_add_lost_item(item_name, description, category,
                        location, date, contact):
    """Register a new lost item. Returns the generated item_id."""
    item = {
        "item_id"    : _w4_next_id(),
        "item_name"  : item_name.strip().title(),
        "description": description.strip(),
        "category"   : category.strip().title(),
        "location"   : location.strip().title(),
        "date"       : date.strip(),
        "contact"    : contact.strip(),
        "status"     : "Lost",
        "type"       : "lost"
    }
    _w4_lost.append(item)
    return item["item_id"]

def week4_add_found_item(item_name, description, category,
                         location, date, contact, finder_name):
    """Register a new found item. Returns the generated item_id."""
    item = {
        "item_id"    : _w4_next_id(),
        "item_name"  : item_name.strip().title(),
        "description": description.strip(),
        "category"   : category.strip().title(),
        "location"   : location.strip().title(),
        "date"       : date.strip(),
        "contact"    : contact.strip(),
        "finder_name": finder_name.strip().title(),
        "status"     : "Found",
        "type"       : "found"
    }
    _w4_found.append(item)
    return item["item_id"]

def week4_search_item(keyword, store="both"):
    """
    Search items by keyword in name/description/location.
    store: 'lost' | 'found' | 'both'
    Returns list of matching item dicts.
    """
    kw = keyword.strip().lower()
    pool = []
    if store in ("lost",  "both"): pool += _w4_lost
    if store in ("found", "both"): pool += _w4_found
    return [i for i in pool
            if kw in i.get("item_name",  "").lower()
            or kw in i.get("description","").lower()
            or kw in i.get("location",   "").lower()]

def week4_list_items(store="both"):
    """Display all items in a formatted table."""
    def _print(items, label):
        print(f"\n--- {label} ({len(items)}) ---")
        for item in items:
            print(f"  #{item['item_id']:<5} {item['item_name']:<18} "
                  f"| {item['category']:<14} | {item['location']:<15}"
                  f"| {item['status']}")
    if store in ("lost",  "both"): _print(_w4_lost,  "Lost Items")
    if store in ("found", "both"): _print(_w4_found, "Found Items")

def week4_demo():
    """WEEK 4 demonstration."""
    print("\n" + "="*60)
    print("  WEEK 4 — Functional Architecture")
    print("="*60)

    id1 = week4_add_lost_item("Wallet","Brown leather wallet",
                               "Wallet","Canteen","22-03-2026","9876543210")
    id2 = week4_add_lost_item("ID Card","Green CSE ID card",
                               "Documents","Library","20-03-2026","9123456780")
    id3 = week4_add_found_item("Pendrive","16GB blue Kingston",
                                "Electronics","Computer Lab",
                                "21-03-2026","9000011111","Alice")

    print(f"  Registered Lost #{ id1}, #{id2} | Found #{id3}")
    week4_list_items()

    results = week4_search_item("library")
    print(f"\n  Search 'library': {len(results)} result(s)")
    for r in results:
        print(f"    ▶ #{r['item_id']} {r['item_name']}")


# ════════════════════════════════════════════════════════════════════════════
# WEEK 5 — Dictionaries & Sets
# Deliverable: stage5_dict_items.py
# Concepts: dict, set, dict methods, set operations for matching
# ════════════════════════════════════════════════════════════════════════════

def week5_dicts_sets():
    """
    WEEK 5: Store every item as a dictionary.
    Use sets for keyword matching between lost and found items.
    """
    print("\n" + "="*60)
    print("  WEEK 5 — Dictionaries & Sets")
    print("="*60)

    # Item dictionary template
    def make_item(item_name, description, location, date, contact,
                  category="Others", status="Lost"):
        return {
            "item_name"  : item_name,
            "description": description,
            "location"   : location,
            "date"       : date,
            "contact"    : contact,
            "category"   : category,
            "status"     : status,
        }

    lost_items = [
        make_item("Blue Pendrive", "16GB Kingston blue pendrive with keychain",
                  "Computer Lab", "21-03-2026", "9123456780", "Electronics"),
        make_item("ID Card", "Green CSE student ID laminated",
                  "Library", "20-03-2026", "9876543210", "Documents"),
    ]
    found_items = [
        make_item("Pendrive", "blue 16gb pendrive near lab exit",
                  "Computer Lab", "22-03-2026", "9000011111",
                  "Electronics", "Found"),
    ]

    # Set-based keyword matching
    def keywords(text):
        stop = {"a","an","the","is","with","and","or","in","at","on","of","near"}
        return {w.lower() for w in text.split() if w.lower() not in stop}

    def match_score(lost, found):
        kw_l = keywords(lost["item_name"]  + " " + lost["description"])
        kw_f = keywords(found["item_name"] + " " + found["description"])
        common  = kw_l & kw_f
        union   = kw_l | kw_f
        return round(len(common) / len(union), 2) if union else 0

    # Category summary using dict
    category_count = {}
    for item in lost_items + found_items:
        cat = item["category"]
        category_count[cat] = category_count.get(cat, 0) + 1

    print("\n  Category Summary:")
    for cat, count in category_count.items():
        print(f"    {cat:<16}: {count}")

    # Run matching
    print("\n  Matching Lost → Found:")
    for lost in lost_items:
        for found in found_items:
            score = match_score(lost, found)
            if score > 0.2:
                print(f"    MATCH ({int(score*100)}%) :"
                      f" Lost '{lost['item_name']}' ↔ "
                      f"Found '{found['item_name']}'")

    # Sample Output:
    #   Category Summary:
    #     Electronics     : 2
    #     Documents       : 1
    #   Matching Lost → Found:
    #     MATCH (50%) : Lost 'Blue Pendrive' ↔ Found 'Pendrive'


# ════════════════════════════════════════════════════════════════════════════
# WEEK 6 — OOP: Item Class
# Deliverable: models/item.py (standalone version)
# Concepts: class, __init__, methods, display(), to_dict()
# ════════════════════════════════════════════════════════════════════════════

class W6Item:
    """
    WEEK 6: OOP — Item class.
    Encapsulates all fields of a lost/found record.
    """
    _counter = [1000]

    def __init__(self, item_name, description, category,
                 location, date, contact, status="Lost"):
        W6Item._counter[0] += 1
        self.item_id     = W6Item._counter[0]
        self.item_name   = item_name.strip().title()
        self.description = description.strip()
        self.category    = category.strip().title()
        self.location    = location.strip().title()
        self.date        = date.strip()
        self.contact     = contact.strip()
        self.status      = status

    def display(self):
        print(f"\n{'─'*50}")
        print(f"  Item ID     : {self.item_id}")
        print(f"  Name        : {self.item_name}")
        print(f"  Category    : {self.category}")
        print(f"  Description : {self.description}")
        print(f"  Location    : {self.location}")
        print(f"  Date        : {self.date}")
        print(f"  Contact     : {self.contact}")
        print(f"  Status      : {self.status}")
        print(f"{'─'*50}")

    def to_dict(self):
        return {
            "item_id"    : self.item_id,
            "item_name"  : self.item_name,
            "description": self.description,
            "category"   : self.category,
            "location"   : self.location,
            "date"       : self.date,
            "contact"    : self.contact,
            "status"     : self.status,
        }

    def __str__(self):
        return (f"Item(id={self.item_id}, name={self.item_name}, "
                f"cat={self.category}, status={self.status})")

    def __repr__(self):
        return self.__str__()


def week6_oop_item():
    """WEEK 6 demonstration."""
    print("\n" + "="*60)
    print("  WEEK 6 — OOP: Item Class")
    print("="*60)

    items = [
        W6Item("Student ID Card", "Green laminated CSE ID card",
               "Documents", "Library", "20-03-2026", "9876543210"),
        W6Item("Blue Pendrive", "16GB Kingston with keychain",
               "Electronics", "Computer Lab", "21-03-2026", "9123456780"),
        W6Item("Black Calculator", "Casio FX-991EX scientific",
               "Electronics", "Exam Hall B", "18-03-2026", "9988776655"),
    ]

    for item in items:
        item.display()

    print(f"\n  Serialised (to_dict):")
    import json
    print(json.dumps(items[0].to_dict(), indent=4))


# ════════════════════════════════════════════════════════════════════════════
# WEEK 7 — Inheritance & Encapsulation
# Deliverable: models/record.py
# Concepts: inheritance, super(), private attributes, getters/setters
# ════════════════════════════════════════════════════════════════════════════

from datetime import datetime as _dt

class W7BaseRecord:
    """
    WEEK 7: Base class — timestamps and record ID.
    All campus records inherit from this.
    """
    def __init__(self):
        self.__record_id  = f"REC{id(self) % 100000:05d}"
        self.__created_at = _dt.now()
        self.__updated_at = _dt.now()

    def get_record_id(self):  return self.__record_id
    def get_created_at(self): return self.__created_at.strftime("%d-%m-%Y %H:%M")
    def get_updated_at(self): return self.__updated_at.strftime("%d-%m-%Y %H:%M")
    def _touch(self):         self.__updated_at = _dt.now()


class W7Item(W7BaseRecord):
    """WEEK 7: Item inherits BaseRecord — adds private fields + setters."""

    VALID_STATUSES = ["Lost", "Found", "Claimed", "Matched", "Closed"]

    def __init__(self, item_name, description, category,
                 location, date, contact):
        super().__init__()
        self.__item_name   = item_name.strip().title()
        self.__description = description.strip()
        self.__category    = category.strip().title()
        self.__location    = location.strip().title()
        self.__date        = date.strip()
        self.__contact     = contact.strip()
        self.__status      = "Lost"

    # Getters
    def get_item_name(self):   return self.__item_name
    def get_description(self): return self.__description
    def get_category(self):    return self.__category
    def get_location(self):    return self.__location
    def get_date(self):        return self.__date
    def get_contact(self):     return self.__contact
    def get_status(self):      return self.__status

    # Setters with validation
    def set_status(self, new_status):
        if new_status not in self.VALID_STATUSES:
            raise ValueError(f"Invalid status: {new_status}")
        self.__status = new_status
        self._touch()

    def set_location(self, loc):
        self.__location = loc.strip().title()
        self._touch()

    def display(self):
        print(f"\n{'─'*50}")
        print(f"  Record ID   : {self.get_record_id()}")
        print(f"  Name        : {self.__item_name}")
        print(f"  Category    : {self.__category}")
        print(f"  Location    : {self.__location}")
        print(f"  Description : {self.__description}")
        print(f"  Status      : {self.__status}")
        print(f"  Created     : {self.get_created_at()}")
        print(f"  Updated     : {self.get_updated_at()}")
        print(f"{'─'*50}")

    def __str__(self):
        return f"W7Item({self.__item_name}, {self.__status})"


class W7LostItem(W7Item):
    """LostItem subclass: adds urgency."""
    def __init__(self, item_name, description, category,
                 location, date, contact, urgency="Normal"):
        super().__init__(item_name, description, category,
                         location, date, contact)
        self.__urgency = urgency
    def get_urgency(self): return self.__urgency
    def __str__(self): return f"LostItem({super().__str__()}, urgency={self.__urgency})"


class W7FoundItem(W7Item):
    """FoundItem subclass: adds finder_name."""
    def __init__(self, item_name, description, category,
                 location, date, contact, finder_name):
        super().__init__(item_name, description, category,
                         location, date, contact)
        self.set_status("Found")
        self.__finder_name = finder_name.strip().title()
    def get_finder_name(self): return self.__finder_name
    def __str__(self): return f"FoundItem({super().__str__()}, finder={self.__finder_name})"


def week7_inheritance():
    """WEEK 7 demonstration."""
    print("\n" + "="*60)
    print("  WEEK 7 — Inheritance & Encapsulation")
    print("="*60)

    lost  = W7LostItem("Redmi Phone","Black Redmi Note 12, cracked corner",
                        "Mobile","Seminar Hall","23-03-2026","8900123456","Critical")
    found = W7FoundItem("Keys","4 keys with red keyring",
                         "Keys","Hostel Block A","24-03-2026","9000055555","Suman")

    lost.display()
    found.display()

    print(f"\n  Updating lost item status to 'Matched'…")
    lost.set_status("Matched")
    print(f"  Status: {lost.get_status()} | Updated: {lost.get_updated_at()}")

    print(f"\n  isinstance checks:")
    print(f"    lost  is W7Item     : {isinstance(lost,  W7Item)}")
    print(f"    found is W7Item     : {isinstance(found, W7Item)}")
    print(f"    lost  is W7BaseRecord: {isinstance(lost, W7BaseRecord)}")


# ════════════════════════════════════════════════════════════════════════════
# WEEK 8 — File Handling (CSV + JSON)
# Deliverable: storage/json_store.py (standalone version)
# Concepts: open(), json, csv, exception handling for I/O
# ════════════════════════════════════════════════════════════════════════════

import json as _json
import csv  as _csv
import os   as _os

W8_JSON_FILE = "w8_lost_items.json"
W8_CSV_FILE  = "w8_lost_items.csv"

def w8_save_json(data, filename=W8_JSON_FILE):
    """Save list of dicts to a JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        _json.dump(data, f, indent=4)
    print(f"  [JSON] Saved {len(data)} records → {filename}")

def w8_load_json(filename=W8_JSON_FILE):
    """Load list of dicts from JSON. Returns [] if file missing."""
    if not _os.path.exists(filename):
        return []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return _json.load(f)
    except _json.JSONDecodeError as e:
        print(f"  [JSON] Corrupted file: {e}")
        return []

def w8_export_csv(data, filename=W8_CSV_FILE):
    """Export list of dicts to CSV."""
    if not data:
        print("  [CSV] No data to export.")
        return
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = _csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"  [CSV] Exported {len(data)} records → {filename}")

def w8_import_csv(filename=W8_CSV_FILE):
    """Import CSV records. Returns list of dicts."""
    if not _os.path.exists(filename):
        print(f"  [CSV] File not found: {filename}")
        return []
    with open(filename, "r", encoding="utf-8") as f:
        return list(_csv.DictReader(f))

def w8_backup(source=W8_JSON_FILE):
    """Create a timestamped backup copy."""
    if not _os.path.exists(source):
        print("  [Backup] Source file not found.")
        return
    import shutil as _shutil
    ts   = _dt.now().strftime("%Y%m%d_%H%M%S")
    dest = source.replace(".json", f"_backup_{ts}.json")
    _shutil.copy2(source, dest)
    print(f"  [Backup] Created: {dest}")


def week8_file_handling():
    """WEEK 8 demonstration."""
    print("\n" + "="*60)
    print("  WEEK 8 — File Handling (JSON + CSV + Backup)")
    print("="*60)

    sample_data = [
        {"item_id": 1001, "item_name": "Student ID Card",
         "category": "Documents", "location": "Library",
         "date": "20-03-2026", "contact": "9876543210", "status": "Lost"},
        {"item_id": 1002, "item_name": "Blue Pendrive",
         "category": "Electronics", "location": "Computer Lab",
         "date": "21-03-2026", "contact": "9123456780", "status": "Matched"},
        {"item_id": 1003, "item_name": "Black Calculator",
         "category": "Electronics", "location": "Exam Hall B",
         "date": "18-03-2026", "contact": "9988776655", "status": "Lost"},
    ]

    # Save → Load → Export → Backup
    w8_save_json(sample_data)
    loaded = w8_load_json()
    print(f"  Loaded {len(loaded)} records from JSON.")
    w8_export_csv(loaded)
    w8_backup()

    # Show CSV contents
    csv_data = w8_import_csv()
    print(f"\n  CSV preview (first row):")
    if csv_data:
        print(f"    {csv_data[0]}")


# ════════════════════════════════════════════════════════════════════════════
# WEEK 9 — Multi-Module Project Structure
# Deliverable: Complete lilcamp package
# Concepts: packages, __init__.py, import paths, sys.path
# ════════════════════════════════════════════════════════════════════════════

def week9_multimodule():
    """
    WEEK 9: Demonstrates package import structure of the full
    lilcamp project (run from lilcamp_project/ root).
    """
    print("\n" + "="*60)
    print("  WEEK 9 — Multi-Module Project Structure")
    print("="*60)

    print("""
  Package Layout:
  ─────────────────────────────────────────────
  lilcamp_project/
  ├── main.py                  ← CLI entry point
  ├── seed_data.py             ← demo data loader
  ├── week_wise_code.py        ← this file
  └── lilcamp/
      ├── __init__.py
      ├── models/
      │   ├── __init__.py
      │   ├── item.py          ← BaseRecord, Item, LostItem, FoundItem
      │   └── report.py        ← ReportRecord
      ├── utils/
      │   ├── __init__.py
      │   ├── validators.py    ← custom exceptions + validation
      │   └── text_processing.py ← keyword matching engine
      ├── storage/
      │   ├── __init__.py
      │   ├── json_store.py    ← CRUD + search
      │   ├── csv_store.py     ← export/import
      │   └── backup.py        ← auto-backup manager
      ├── analysis/
      │   ├── __init__.py
      │   └── analyzer.py      ← Pandas + NumPy analytics
      └── visual/
          ├── __init__.py
          └── charts.py        ← Matplotlib charts
  ─────────────────────────────────────────────
    """)

    print("  Import examples used in the project:")
    print("    from lilcamp.models.item      import LostItem, FoundItem")
    print("    from lilcamp.utils.validators import validate_date, validate_contact")
    print("    from lilcamp.storage.json_store import add_lost, get_lost")
    print("    from lilcamp.analysis.analyzer  import generate_report")
    print("    from lilcamp.visual.charts      import full_dashboard")


# ════════════════════════════════════════════════════════════════════════════
# WEEK 10 — Exceptions & Robustness
# Deliverable: utils/validators.py (standalone demo)
# Concepts: try/except/finally, custom exceptions, raise
# ════════════════════════════════════════════════════════════════════════════

# ── Custom Exception Classes ──────────────────────────────────────────────────

class W10LILError(Exception):
    """Base exception for LIL-CAMP."""
    pass

class W10InvalidDateError(W10LILError):
    """Invalid date format."""
    pass

class W10InvalidCategoryError(W10LILError):
    """Invalid item category."""
    pass

class W10InvalidContactError(W10LILError):
    """Invalid contact number."""
    pass

class W10InvalidItemNameError(W10LILError):
    """Invalid item name."""
    pass

class W10CorruptedFileError(W10LILError):
    """Corrupted JSON/CSV file."""
    pass


# ── Validators ────────────────────────────────────────────────────────────────

_W10_CATEGORIES = [
    "Documents", "Electronics", "Accessories", "Books",
    "Keys", "Clothing", "Mobile", "Wallet", "Others"
]

def w10_validate_item_name(name):
    import re
    if not name or len(name.strip()) < 2:
        raise W10InvalidItemNameError("Name must be at least 2 characters.")
    if not re.match(r'^[A-Za-z0-9 \-]+$', name.strip()):
        raise W10InvalidItemNameError("Name contains invalid characters.")
    return name.strip().title()

def w10_validate_date(date_str):
    from datetime import datetime as dt
    try:
        parsed = dt.strptime(date_str.strip(), "%d-%m-%Y")
    except ValueError:
        raise W10InvalidDateError(
            f"'{date_str}' is not valid. Use DD-MM-YYYY.")
    if parsed > dt.now():
        raise W10InvalidDateError("Date cannot be in the future.")
    return date_str.strip()

def w10_validate_category(category):
    cat = category.strip().title()
    if cat not in _W10_CATEGORIES:
        raise W10InvalidCategoryError(
            f"'{cat}' invalid. Choose: {', '.join(_W10_CATEGORIES)}")
    return cat

def w10_validate_contact(contact):
    import re
    c = contact.strip().replace(" ","").replace("-","")
    if c.startswith("+91"): c = c[3:]
    elif c.startswith("91") and len(c) == 12: c = c[2:]
    if not re.match(r'^[6-9]\d{9}$', c):
        raise W10InvalidContactError(f"'{c}' is not a valid Indian mobile number.")
    return c


def week10_exceptions():
    """WEEK 10 demonstration — try/except/raise/finally."""
    print("\n" + "="*60)
    print("  WEEK 10 — Exceptions & Robustness")
    print("="*60)

    test_cases = [
        ("Item Name",   w10_validate_item_name,  ["AB", "X", "Valid-Item@#"]),
        ("Date",        w10_validate_date,        ["20-03-2026","32-13-2026","01-01-2099"]),
        ("Category",    w10_validate_category,    ["Electronics","Gadgets","Documents"]),
        ("Contact",     w10_validate_contact,     ["9876543210","1234567890","9001234567"]),
    ]

    for label, func, inputs in test_cases:
        print(f"\n  Testing {label}:")
        for val in inputs:
            try:
                result = func(val)
                print(f"    ✔  '{val}' → '{result}'")
            except W10LILError as e:
                print(f"    ✘  '{val}' → {type(e).__name__}: {e}")
            finally:
                pass    # always runs — useful for cleanup / logging

    # Demonstrate chained exception handling
    print("\n  Chained exception handling demo:")
    def process_item(name, date, cat, contact):
        try:
            n = w10_validate_item_name(name)
            d = w10_validate_date(date)
            c = w10_validate_category(cat)
            p = w10_validate_contact(contact)
            print(f"    ✔  All valid: {n} | {d} | {c} | {p}")
        except W10InvalidItemNameError as e:
            print(f"    ✘  Name Error   : {e}")
        except W10InvalidDateError as e:
            print(f"    ✘  Date Error   : {e}")
        except W10InvalidCategoryError as e:
            print(f"    ✘  Category Err : {e}")
        except W10InvalidContactError as e:
            print(f"    ✘  Contact Err  : {e}")
        except W10LILError as e:
            print(f"    ✘  General Err  : {e}")

    process_item("Blue Pendrive", "21-03-2026", "Electronics", "9123456780")
    process_item("X",             "21-03-2026", "Electronics", "9123456780")
    process_item("Wallet",        "21-13-2026", "Wallet",      "9123456780")


# ════════════════════════════════════════════════════════════════════════════
# WEEK 11 — NumPy Analytics & Pandas Reporting
# Deliverable: analysis/forecasting.py
# Concepts: NumPy arrays, Pandas DataFrames, groupby, describe
# ════════════════════════════════════════════════════════════════════════════

def week11_numpy_pandas():
    """WEEK 11: Analytics with NumPy and Pandas."""
    print("\n" + "="*60)
    print("  WEEK 11 — NumPy Analytics & Pandas Reporting")
    print("="*60)

    try:
        import numpy  as np
        import pandas as pd
    except ImportError:
        print("  Install: pip install numpy pandas")
        return

    # ── Seed data ─────────────────────────────────────────────────────────────
    records = [
        {"item_name":"ID Card",    "category":"Documents",   "location":"Library",      "date":"20-03-2026","status":"Lost"},
        {"item_name":"Pendrive",   "category":"Electronics", "location":"Computer Lab", "date":"21-03-2026","status":"Matched"},
        {"item_name":"Calculator", "category":"Electronics", "location":"Exam Hall",    "date":"18-03-2026","status":"Lost"},
        {"item_name":"Wallet",     "category":"Wallet",      "location":"Canteen",      "date":"22-03-2026","status":"Lost"},
        {"item_name":"Water Bottle","category":"Accessories","location":"Sports Ground","date":"19-03-2026","status":"Lost"},
        {"item_name":"Textbook",   "category":"Books",       "location":"Library",      "date":"17-03-2026","status":"Claimed"},
        {"item_name":"Keys",       "category":"Keys",        "location":"Hostel",       "date":"24-03-2026","status":"Lost"},
        {"item_name":"Phone",      "category":"Mobile",      "location":"Seminar Hall", "date":"23-03-2026","status":"Lost"},
        {"item_name":"ID Card",    "category":"Documents",   "location":"Cafeteria",    "date":"15-03-2026","status":"Found"},
        {"item_name":"Earphones",  "category":"Electronics", "location":"Computer Lab", "date":"16-03-2026","status":"Found"},
    ]

    df = pd.DataFrame(records)
    df["parsed_date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")
    df["month"]       = df["parsed_date"].dt.strftime("%b %Y")

    print("\n  Full DataFrame:")
    print(df[["item_name","category","location","status","month"]].to_string(index=False))

    # ── Aggregations ──────────────────────────────────────────────────────────
    print("\n  Category Distribution:")
    cat_counts = df["category"].value_counts()
    print(cat_counts.to_string())

    print("\n  Status Distribution:")
    print(df["status"].value_counts().to_string())

    print("\n  Location Hot-Spots (top 4):")
    print(df["location"].value_counts().head(4).to_string())

    # ── NumPy Stats ───────────────────────────────────────────────────────────
    total     = np.array(len(df[df["status"] == "Lost"]),  dtype=float)
    claimed   = np.array(len(df[df["status"].isin(["Claimed","Matched"])]), dtype=float)
    rec_rate  = round(float(claimed / total * 100), 2) if total > 0 else 0

    print(f"\n  NumPy Recovery Rate : {rec_rate}%")
    print(f"  Total Lost          : {int(total)}")
    print(f"  Total Recovered     : {int(claimed)}")

    # ── GroupBy ───────────────────────────────────────────────────────────────
    print("\n  Category × Status Cross-Tab:")
    ct = pd.crosstab(df["category"], df["status"])
    print(ct.to_string())

    # ── Monthly Trend ─────────────────────────────────────────────────────────
    print("\n  Monthly Trend:")
    print(df.groupby("month")["item_name"].count().to_string())


# ════════════════════════════════════════════════════════════════════════════
# WEEK 12 — Matplotlib Visualizations
# Deliverable: visual/charts.py (standalone demo)
# Concepts: pyplot, bar/pie/line charts, subplots, savefig
# ════════════════════════════════════════════════════════════════════════════

def week12_matplotlib():
    """
    WEEK 12: Matplotlib charts for campus analytics.
    Saves all charts as PNG files.
    """
    print("\n" + "="*60)
    print("  WEEK 12 — Matplotlib Visualizations")
    print("="*60)

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import numpy             as np
    except ImportError:
        print("  Install: pip install matplotlib numpy")
        return

    # ── Sample aggregated data ────────────────────────────────────────────────
    categories = ["Documents","Electronics","Wallet","Accessories","Books","Keys","Mobile"]
    lost_counts = [12, 18,  8,  6,  4,  5,  9]
    found_counts = [ 7,  9,  3,  4,  2,  4,  5]
    months       = ["Jan","Feb","Mar","Apr","May","Jun"]
    monthly_lost = [3, 6, 10, 8, 12, 9]

    # ── 2×2 Dashboard ─────────────────────────────────────────────────────────
    fig, axes = plt.subplots(2, 2, figsize=(16, 10))
    fig.suptitle("LIL-CAMP — Week 12 Campus Analytics Dashboard",
                 fontsize=15, fontweight="bold")

    # [0,0] Category bar chart
    ax = axes[0, 0]
    x   = np.arange(len(categories))
    w   = 0.35
    b1  = ax.bar(x - w/2, lost_counts,  w, label="Lost",  color="#e74c3c")
    b2  = ax.bar(x + w/2, found_counts, w, label="Found", color="#2ecc71")
    ax.set_title("Lost vs Found by Category")
    ax.set_xticks(x); ax.set_xticklabels(categories, rotation=30)
    ax.set_ylabel("Count"); ax.legend()

    # [0,1] Recovery pie
    ax = axes[0, 1]
    total_lost    = sum(lost_counts)
    total_claimed = sum(found_counts)
    ax.pie([total_claimed, total_lost - total_claimed],
           labels=["Recovered","Unrecovered"],
           colors=["#2ecc71","#e74c3c"],
           autopct="%1.1f%%", startangle=90, shadow=True)
    ax.set_title(f"Recovery Rate ({round(total_claimed/total_lost*100,1)}%)")

    # [1,0] Monthly trend line
    ax = axes[1, 0]
    ax.plot(months, monthly_lost, marker="o", color="#e74c3c",
            linewidth=2, label="Lost")
    ax.fill_between(months, monthly_lost, alpha=0.15, color="#e74c3c")
    ax.set_title("Monthly Loss Trend"); ax.set_ylabel("Items Lost")
    ax.legend(); ax.grid(axis="y", linestyle="--", alpha=0.5)

    # [1,1] Location hot-spots (horizontal bar)
    locations = ["Library","Computer Lab","Canteen","Exam Hall","Hostel","Sports Ground"]
    counts    = [15, 12, 9, 8, 6, 5]
    ax = axes[1, 1]
    colors = plt.cm.YlOrRd(np.linspace(0.3, 0.9, len(locations)))
    ax.barh(locations[::-1], counts[::-1], color=colors, edgecolor="black")
    ax.set_title("Campus Hot-Spots"); ax.set_xlabel("Items Lost")

    plt.tight_layout()
    path = "week12_dashboard.png"
    plt.savefig(path, dpi=130, bbox_inches="tight")
    plt.close()
    print(f"\n  ✔  Dashboard saved → {path}")

    # Individual charts
    # 1. Simple category bar
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(categories, lost_counts, color=plt.cm.Set3(np.linspace(0,1,len(categories))))
    ax.set_title("Lost Items by Category")
    ax.set_ylabel("Count"); plt.tight_layout()
    plt.savefig("week12_category_bar.png", dpi=120)
    plt.close()
    print("  ✔  Saved → week12_category_bar.png")

    # 2. Pie chart
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(lost_counts, labels=categories, autopct="%1.1f%%", startangle=90)
    ax.set_title("Category Distribution")
    plt.tight_layout()
    plt.savefig("week12_category_pie.png", dpi=120)
    plt.close()
    print("  ✔  Saved → week12_category_pie.png")

    print("\n  Chart files generated:")
    print("    • week12_dashboard.png")
    print("    • week12_category_bar.png")
    print("    • week12_category_pie.png")


# ════════════════════════════════════════════════════════════════════════════
# RUNNER — Execute all weeks sequentially (non-interactive weeks only)
# ════════════════════════════════════════════════════════════════════════════

def run_all_noninteractive():
    """Run all non-interactive week demonstrations."""
    week4_demo()
    week5_dicts_sets()
    week6_oop_item()
    week7_inheritance()
    week8_file_handling()
    week9_multimodule()
    week10_exceptions()
    week11_numpy_pandas()
    week12_matplotlib()


# ════════════════════════════════════════════════════════════════════════════
# MAIN — Week selector
# ════════════════════════════════════════════════════════════════════════════

WEEK_MENU = {
    "1" : ("Week 1  — Basic Item Capture",          week1_basic_capture),
    "2" : ("Week 2  — Menu-Driven System",           week2_menu_system),
    "3" : ("Week 3  — Strings & Lists",              week3_strings_lists),
    "4" : ("Week 4  — Functional Architecture",      week4_demo),
    "5" : ("Week 5  — Dictionaries & Sets",          week5_dicts_sets),
    "6" : ("Week 6  — OOP: Item Class",              week6_oop_item),
    "7" : ("Week 7  — Inheritance & Encapsulation",  week7_inheritance),
    "8" : ("Week 8  — File Handling (CSV + JSON)",   week8_file_handling),
    "9" : ("Week 9  — Multi-Module Structure",       week9_multimodule),
    "10": ("Week 10 — Exceptions & Robustness",      week10_exceptions),
    "11": ("Week 11 — NumPy & Pandas Analytics",     week11_numpy_pandas),
    "12": ("Week 12 — Matplotlib Visualizations",    week12_matplotlib),
    "0" : ("Run ALL non-interactive weeks",          run_all_noninteractive),
}


if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════════╗
║   LIL-CAMP — Week-Wise Implementation Reference             ║
║   24SC2007 Python Programming | PBL Project 14              ║
╚══════════════════════════════════════════════════════════════╝
""")
    print("  Select a week to run:\n")
    for k, (label, _) in WEEK_MENU.items():
        print(f"    {k:>2}. {label}")
    print()

    choice = input("  Enter week number (or 0 for all): ").strip()
    if choice in WEEK_MENU:
        label, func = WEEK_MENU[choice]
        print(f"\n  Running: {label}")
        print("  " + "─"*55)
        func()
    else:
        print("  Invalid choice.")
