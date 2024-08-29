# def get_stylesheet():
#     return """
#     QMainWindow {
#         background-color: #2c3e50;
#     }
#     QLabel {
#         font-size: 14px;
#         color: white;
#     }
#     QLineEdit {
#         background-color: white;
#         color: black;
#         padding: 5px;
#         border-radius: 5px;
#         font-size: 14px;
#     }
#     QPushButton {
#         background-color: #3498db;
#         color: white;
#         padding: 10px;
#         border-radius: 5px;
#         font-size: 14px;
#     }
#     QPushButton:hover {
#         background-color: #2980b9;
#     }
#     QTableWidget {
#         background-color: white;
#         font-size: 14px;
#     }
#     QHeaderView::section {
#         background-color: #3498db;
#         color: white;
#         padding: 5px;
#         border: none;
#         font-size: 14px;
#     }
#     QStatusBar {
#         background-color: #34495e;
#         color: white;
#     }
#     QMenuBar {
#         background-color: #34495e;
#         color: white;
#     }
#     QMenuBar::item {
#         background-color: #34495e;
#         color: white;
#     }
#     QMenuBar::item:selected {
#         background-color: #2c3e50;
#     }
#     QMenu {
#         background-color: #34495e;
#         color: white;
#     }
#     QMenu::item {
#         background-color: #34495e;
#         color: white;
#     }
#     QMenu::item:selected {
#         background-color: #2c3e50;
#     }
#     """
def get_stylesheet():
    return """
    QMainWindow {
        background-color: #f0f0f0;
    }
    QLabel {
        font-size: 14px;
        color: #333333;
    }
    QLineEdit {
        background-color: white;
        border: 1px solid #cccccc;
        border-radius: 4px;
        padding: 5px;
        font-size: 14px;
    }
    QPushButton {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 8px 16px;
        text-align: center;
        text-decoration: none;
        font-size: 14px;
        margin: 4px 2px;
        border-radius: 4px;
    }
    QPushButton:hover {
        background-color: #45a049;
    }
    QTableWidget {
        background-color: white;
        border: 1px solid #cccccc;
    }
    QHeaderView::section {
        background-color: #f2f2f2;
        color: #333333;
        padding: 5px;
        border: 1px solid #cccccc;
    }
    QGroupBox {
        border: 1px solid #cccccc;
        border-radius: 4px;
        margin-top: 10px;
        font-size: 14px;
    }
    QGroupBox::title {
        subcontrol-origin: margin;
        left: 10px;
        padding: 0 3px 0 3px;
    }
    QStatusBar {
        background-color: #f2f2f2;
        color: #333333;
    }
    QMenuBar {
        background-color: #f2f2f2;
        color: #333333;
    }
    QMenuBar::item:selected {
        background-color: #e0e0e0;
    }
    QMenu {
        background-color: white;
        color: #333333;
    }
    QMenu::item:selected {
        background-color: #e0e0e0;
    }
    """

def get_dark_stylesheet():
    return """
    QMainWindow {
        background-color: #2c3e50;
    }
    QLabel {
        font-size: 14px;
        color: #ecf0f1;
    }
    QLineEdit {
        background-color: #34495e;
        border: 1px solid #7f8c8d;
        border-radius: 4px;
        padding: 5px;
        font-size: 14px;
        color: #ecf0f1;
    }
    QPushButton {
        background-color: #3498db;
        color: white;
        border: none;
        padding: 8px 16px;
        text-align: center;
        text-decoration: none;
        font-size: 14px;
        margin: 4px 2px;
        border-radius: 4px;
    }
    QPushButton:hover {
        background-color: #2980b9;
    }
    QTableWidget {
        background-color: #34495e;
        border: 1px solid #7f8c8d;
        color: #ecf0f1;
    }
    QHeaderView::section {
        background-color: #2c3e50;
        color: #ecf0f1;
        padding: 5px;
        border: 1px solid #7f8c8d;
    }
    QGroupBox {
        border: 1px solid #7f8c8d;
        border-radius: 4px;
        margin-top: 10px;
        font-size: 14px;
        color: #ecf0f1;
    }
    QGroupBox::title {
        subcontrol-origin: margin;
        left: 10px;
        padding: 0 3px 0 3px;
    }
    QStatusBar {
        background-color: #34495e;
        color: #ecf0f1;
    }
    QMenuBar {
        background-color: #34495e;
        color: #ecf0f1;
    }
    QMenuBar::item:selected {
        background-color: #2c3e50;
    }
    QMenu {
        background-color: #34495e;
        color: #ecf0f1;
    }
    QMenu::item:selected {
        background-color: #2c3e50;
    }
    QGraphicsView {
        background-color: #2c3e50;
        border: 1px solid #7f8c8d;
    }
    QScrollBar:vertical {
        border: none;
        background: #34495e;
        width: 14px;
        margin: 15px 0 15px 0;
        border-radius: 0px;
    }
    QScrollBar::handle:vertical {
        background-color: #3498db;
        min-height: 30px;
        border-radius: 7px;
    }
    QScrollBar::handle:vertical:hover {
        background-color: #2980b9;
    }
    QScrollBar::sub-line:vertical {
        border: none;
        background-color: #34495e;
        height: 15px;
        border-top-left-radius: 7px;
        border-top-right-radius: 7px;
        subcontrol-position: top;
        subcontrol-origin: margin;
    }
    QScrollBar::add-line:vertical {
        border: none;
        background-color: #34495e;
        height: 15px;
        border-bottom-left-radius: 7px;
        border-bottom-right-radius: 7px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
    }
    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
        background: none;
    }
    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: none;
    }
    """