import py3Dmol
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView


class MolecularViewer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.web = QWebEngineView(self)
        layout.addWidget(self.web)

    def load_xyz(self, xyz_string):
        view = py3Dmol.view(width="100%", height="100%")
        view.addModel(xyz_string, "xyz")

        # Estilo general (ball-and-stick estable)
        view.setStyle({}, {"sphere": {"scale": 0.28}, "stick": {"radius": 0.15}})

        # Sobrescribir color para N
        view.setStyle({"elem": "N"}, {"sphere": {"color": "#3050F8", 'scale': 0.28},
                                      "stick": {"color": "#3050F8", 'radius': 0.15}
                                      }
        )

        view.zoomTo()
        self.web.setHtml(view._make_html())
