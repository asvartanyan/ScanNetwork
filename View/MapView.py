from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QTableView, QTableWidget, QVBoxLayout)
from PyQt5.QtWebEngineWidgets import QWebEngineView
import folium
import io



class MapView(QWidget):
    #_map = None
    def __init__(self, _map = folium.Map()):
        super().__init__()
        self._map = _map
        self.setWindowTitle('Endpoints')
        self.window_width, self.window_height = 1280, 720
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)


        #folium.Marker(location=[37.8199286, -122.4782551]).add_to(self._map)


        # save map data to data object
        data = io.BytesIO()
        self._map.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)


