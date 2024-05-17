"""Common objects stretched_mesh_proj."""
from dataclasses import dataclass, field

from aeolus.model import um
from aeolus.region import Region
from aeolus.subset import DimConstr
import matplotlib.pyplot as plt

LOWRES = "n96"

DC = DimConstr(model=um)

DAYSIDE = Region(-90, 90, -90, 90, name="dayside", model=um)
NIGHTSIDE = Region(90, -90, -90, 90, name="nightside", model=um)

KW_ZERO_LINE = {
    "color": plt.rcParams["axes.edgecolor"],
    "linewidth": plt.rcParams["axes.linewidth"],
    "linestyle": "dashed",
    "dash_capstyle": "round",
}
KW_LINE_MARKERS = {
    "markevery": 0.05,
    "markersize": 5,
    "markeredgecolor": plt.rcParams["axes.facecolor"],
    "markeredgewidth": 0.5,
}


@dataclass
class Group:
    """Details for a group of simulations."""

    title: str
    simulations: tuple
    kw_plt: dict = field(default_factory=dict)


GROUPS = {
    "comp": Group(
        title="Composition",
        simulations=("hab1", "hab2", "archean_early", "archean_late"),
    ),
    "pres": Group(
        title="Pressure",
        simulations=(
            "hab1_0p25bar",
            "hab1_0p5bar",
            "hab1_1bar",
            "hab1_2bar",
            "hab1_4bar",
            "hab1_10bar",
        ),
    ),
}


@dataclass
class Simulation:
    """UM simulation details."""

    group: str
    title: str
    highres_diag_suite: str
    highres_spinup_suite: str
    lowres_spinup_suite: str
    timestep: int = 240
    lightning_parameterisation: str = "mccaul"
    resolution: str = "n1280"
    kw_plt: dict = field(default_factory=dict)


SIMULATIONS = {
    "hab1": Simulation(
        group="comp",
        title="THAI Hab 1",
        highres_diag_suite="",
        highres_spinup_suite="ct229",
        lowres_spinup_suite="co730",
        kw_plt={"color": "C7", "marker": "o"},
    ),
    "hab2": Simulation(
        group="comp",
        title="THAI Hab 2",
        highres_diag_suite="",
        highres_spinup_suite="cu096",
        lowres_spinup_suite="cr413",
        kw_plt={"color": "C1", "marker": "^"},
    ),
    "archean_early": Simulation(
        group="comp",
        title="Early Archean",
        highres_diag_suite="",
        highres_spinup_suite="cz507",
        lowres_spinup_suite="cr388",
        kw_plt={"color": "C2", "marker": "s"},
    ),
    "archean_late": Simulation(
        group="comp",
        title="Late Archean",
        highres_diag_suite="",
        highres_spinup_suite="cz508",
        lowres_spinup_suite="cr389",
        kw_plt={"color": "C3", "marker": "P"},
    ),
    "hab1_0p25bar": Simulation(
        group="pres",
        title="0.25 bar",
        highres_diag_suite="",
        highres_spinup_suite="cw021",
        lowres_spinup_suite="cq704",
        kw_plt={"color": "C4", "marker": "p"},
    ),
    "hab1_0p5bar": Simulation(
        group="pres",
        title="0.5 bar",
        highres_diag_suite="",
        highres_spinup_suite="cw375",
        lowres_spinup_suite="cq705",
        kw_plt={"color": "C5", "marker": "D"},
    ),
    "hab1_1bar": Simulation(
        group="pres",
        title="1 bar",
        highres_diag_suite="",
        highres_spinup_suite="ct229",
        lowres_spinup_suite="co730",
        kw_plt={"color": "C7", "marker": "o"},
    ),
    "hab1_2bar": Simulation(
        group="pres",
        title="2 bar",
        highres_diag_suite="",
        highres_spinup_suite="cx886",
        lowres_spinup_suite="cq706",
        kw_plt={"color": "C6", "marker": "*"},
    ),
    "hab1_4bar": Simulation(
        group="pres",
        title="4 bar",
        highres_diag_suite="",
        highres_spinup_suite="cy127",
        lowres_spinup_suite="cq707",
        kw_plt={"color": "C8", "marker": "h"},
    ),
    "hab1_10bar": Simulation(
        group="pres",
        title="10 bar",
        highres_diag_suite="",
        highres_spinup_suite="cy624",
        lowres_spinup_suite="cq708",
        kw_plt={"color": "C9", "marker": "X"},
    ),
}
