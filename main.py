import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox,
    QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QProgressBar, QTabWidget,
    QSlider, QListWidget, QLabel, QToolBar, QStatusBar, QGridLayout
)
from PyQt5.QtGui import QIcon, QFont, QColor
from PyQt5.QtCore import Qt, QTimer, QSize

# --- Main Application Class ---
class NotepadApp(QMainWindow):
    """
    A main window class for a multi-tab application with rich features.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Harshdeep's Enhanced Notepad")
        self.setGeometry(100, 100, 800, 600)  # Set initial size
        self.current_filepath = None  # To track the open file

        # Build UI components
        self._createActions()
        self._createMenuBar()
        self._createToolBar()
        self._createStatusBar()
        self._createCentralWidget()

    # --- UI Setup Methods ---

    def _createActions(self):
        """Creates all QActions for menus and toolbar."""
        # Use simple text for icons as QIcon.fromTheme might not work everywhere
        self.openAction = QAction("Open", self)
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.triggered.connect(self.openFileDialog)

        self.saveAction = QAction("Save", self)
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.triggered.connect(self.saveFileDialog)

        self.exitAction = QAction("Exit", self)
        self.exitAction.setShortcut("Ctrl+Q")
        self.exitAction.triggered.connect(self.close)

        self.aboutAction = QAction("About", self)
        self.aboutAction.triggered.connect(self.aboutDialog)

    def _createMenuBar(self):
        """Creates the Menu Bar."""
        menubar = self.menuBar()
        menubar.setFont(QFont("Arial", 10))

        file_menu = menubar.addMenu("&File")
        file_menu.addAction(self.openAction)
        file_menu.addAction(self.saveAction)
        file_menu.addSeparator()
        file_menu.addAction(self.exitAction)

        menubar.addMenu("&Edit") # Placeholder

        help_menu = menubar.addMenu("&Help")
        help_menu.addAction(self.aboutAction)

    def _createToolBar(self):
        """Creates the Tool Bar with actions."""
        toolbar = QToolBar("Main Toolbar")
        # Increase icon size for a better look
        toolbar.setIconSize(QSize(24, 24)) 
        self.addToolBar(Qt.TopToolBarArea, toolbar)
        
        # Add a custom icon for Open (using a standard string or file path)
        self.openAction.setIcon(QIcon.fromTheme('document-open', QIcon(':/icons/open.png')))
        self.saveAction.setIcon(QIcon.fromTheme('document-save', QIcon(':/icons/save.png')))
        self.exitAction.setIcon(QIcon.fromTheme('application-exit', QIcon(':/icons/exit.png')))
        
        toolbar.addAction(self.openAction)
        toolbar.addAction(self.saveAction)
        toolbar.addSeparator()
        toolbar.addAction(self.exitAction)

    def _createStatusBar(self):
        """Creates the Status Bar at the bottom."""
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
        self.statusbar.showMessage("Ready")

    def _createCentralWidget(self):
        """Sets up the central QTabWidget with all tabs."""
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget) # Use central_widget as parent

        self.tab_widget = QTabWidget()
        self.tab_widget.setFont(QFont("Arial", 10))
        
        # Add Tabs
        self.tab_widget.addTab(self._createTextEditorTab(), "📝 Text Editor")
        self.tab_widget.addTab(self._createListProgressTab(), "📊 Progress Tracker")
        self.tab_widget.addTab(self._createControlsTab(), "🎛️ Controls")
        
        main_layout.addWidget(self.tab_widget)
        self.setCentralWidget(central_widget)
    
    # --- Tab Creation Helper Methods ---
    
    def _createTextEditorTab(self):
        """Creates the Text Editor tab (Tab 1)."""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        self.textEdit = QTextEdit()
        self.textEdit.setFont(QFont("Courier New", 12)) # Monospace font for code/text
        layout.addWidget(self.textEdit)
        return tab

    def _createListProgressTab(self):
        """Creates the List and Progress tab (Tab 2)."""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        self.listWidget = QListWidget()
        self.listWidget.setFont(QFont("Arial", 10))
        self.listWidget.addItems(["Task 1: Initialize", "Task 2: Process Data", "Task 3: Finalize"])
        layout.addWidget(self.listWidget)

        # Container for the button and progress bar
        h_layout = QHBoxLayout()
        start_button = QPushButton("Start Simulation")
        start_button.clicked.connect(self.startProgress)
        h_layout.addWidget(start_button)

        self.progressBar = QProgressBar()
        self.progressBar.setTextVisible(True)
        self.progressBar.setFormat("%p% Complete")
        h_layout.addWidget(self.progressBar)
        
        layout.addLayout(h_layout)
        return tab
    
    def _createControlsTab(self):
        """Creates the Slider and Button tab (Tab 3)."""
        tab = QWidget()
        layout = QGridLayout(tab) # Use a Grid Layout for a cleaner look
        
        # Row 0: Title
        title_label = QLabel("Adjustment Controls")
        title_label.setFont(QFont("Arial", 12, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label, 0, 0, 1, 2) # Span across 2 columns

        # Row 1: Slider and Label
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.valueChanged.connect(self.updateSliderLabel)
        layout.addWidget(self.slider, 1, 0)

        self.sliderLabel = QLabel("Value: 0")
        self.sliderLabel.setFixedWidth(80) # Fixed width for label
        layout.addWidget(self.sliderLabel, 1, 1)

        # Row 2: Button
        button = QPushButton("Read Value")
        button.clicked.connect(self.showSliderValue)
        layout.addWidget(button, 2, 0, 1, 2) # Span across 2 columns
        
        return tab

    # --- Action Handler Methods (Fixed Indentation) ---
    
    def openFileDialog(self):
        """Handles the Open File action."""
        # Note: Added 'self' as the parent for getOpenFileName
        fname, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")
        if fname:
            try:
                with open(fname, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.textEdit.setText(content)
                self.current_filepath = fname
                self.statusbar.showMessage(f"Opened: {fname}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not open file: {e}")
    
    def saveFileDialog(self):
        """Handles the Save File action."""
        # If a file is already open, use its path for saving
        default_path = self.current_filepath if self.current_filepath else ""
        fname, _ = QFileDialog.getSaveFileName(self, "Save File", default_path, "Text Files (*.txt);;All Files (*)")
        
        if fname:
            try:
                with open(fname, 'w', encoding='utf-8') as f:
                    f.write(self.textEdit.toPlainText())
                self.current_filepath = fname
                self.statusbar.showMessage(f"Saved: {fname}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not save file: {e}")

    def aboutDialog(self):
        """Shows the About dialog."""
        QMessageBox.about(self, "About NotepadApp", 
                          "**Harshdeep's Enhanced Notepad**\n\n"
                          "Powered by PyQt5 and Python.\n"
                          "Features: Text Editor, Progress Tracker, and Controls.")

    def updateSliderLabel(self, value):
        """Updates the label next to the slider."""
        self.sliderLabel.setText(f"Value: {value}")

    def showSliderValue(self):
        """Displays the current slider value in a message box."""
        value = self.slider.value()
        QMessageBox.information(self, "Slider Value", f"The current control value is: **{value}**")

    # --- Progress Bar Logic ---
    
    def startProgress(self):
        """Initializes and starts the progress simulation."""
        self.progressBar.setValue(0)
        self._progress_value = 0
        self.statusbar.showMessage("Simulation started...")
        
        # Initialize timer if it doesn't exist
        if not hasattr(self, "_progress_timer"):
            self._progress_timer = QTimer(self)
            self._progress_timer.timeout.connect(self._advanceProgress)
            
        self._progress_timer.start(25) # Timer fires every 25 milliseconds

    def _advanceProgress(self):
        """Increments the progress bar value and stops at 100."""
        self._progress_value += 1
        self.progressBar.setValue(self._progress_value)
        
        if self._progress_value >= 100:
            self._progress_timer.stop()
            self.statusbar.showMessage("Simulation complete!")
            
# --- Main Execution Block ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # --- ENHANCED DARK THEME QSS (Graphics Improvement) ---
    app.setStyleSheet("""
        /* Global Background and Text */
        QMainWindow, QTabWidget::pane { 
            background: #2D2D30; 
            color: #D4D4D4; 
        }
        
        /* Menu Bar */
        QMenuBar {
            background: #252526;
            color: #D4D4D4;
            border-bottom: 1px solid #3C3C3C;
        }
        QMenuBar::item:selected {
            background: #0E639C;
        }

        /* Tool Bar */
        QToolBar { 
            background: #3C3C3C; 
            border: none;
            padding: 5px;
            spacing: 10px;
        }
        QToolBar QToolButton {
            color: #D4D4D4;
            padding: 5px;
        }
        QToolBar QToolButton:hover {
            background: #505050;
        }
        
        /* Widgets */
        QTextEdit, QListWidget { 
            background: #1E1E1E; 
            color: #D4D4D4; 
            padding: 10px; 
            border: 1px solid #3C3C3C;
            border-radius: 4px; 
            selection-background-color: #0E639C;
        }
        
        /* Buttons */
        QPushButton { 
            background: #0E639C; 
            color: white; 
            padding: 8px 15px; 
            border-radius: 4px;
            border: none;
        }
        QPushButton:hover {
            background: #1E82C9;
        }
        QPushButton:pressed {
            background: #005A8D;
        }

        /* Tabs */
        QTabWidget::tab-bar {
            alignment: left;
        }
        QTabBar::tab {
            background: #252526;
            color: #D4D4D4;
            padding: 8px 20px;
            border: 1px solid #3C3C3C;
            border-bottom: none;
            border-top-left-radius: 4px;
            border-top-right-radius: 4px;
        }
        QTabBar::tab:selected {
            background: #2D2D30;
            border-color: #0E639C; /* Highlight selected tab */
            border-bottom-color: #2D2D30; /* Hide line at bottom of selected tab */
        }

        /* Progress Bar */
        QProgressBar {
            border: 1px solid #3C3C3C;
            border-radius: 5px;
            text-align: center;
            background-color: #252526;
            color: #D4D4D4;
        }
        QProgressBar::chunk {
            background-color: #0E639C; /* Blue progress fill */
            border-radius: 5px;
        }

        /* Slider */
        QSlider::groove:horizontal {
            border: 1px solid #3C3C3C;
            height: 8px;
            background: #252526;
            margin: 2px 0;
            border-radius: 4px;
        }
        QSlider::handle:horizontal {
            background: #D4D4D4;
            border: 1px solid #D4D4D4;
            width: 14px;
            margin: -3px 0; /* center the handle vertically */
            border-radius: 7px;
        }
        
    """)
    

# [Image of PyQt Dark Theme Application Layout]

    
    window = NotepadApp()
    window.show()
    sys.exit(app.exec_())
