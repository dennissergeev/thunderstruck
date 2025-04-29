"""Common objects stretched_mesh_proj."""
from dataclasses import dataclass, field
import warnings

from aeolus.calc import time_mean
from aeolus.coord import area_weights_cube
from aeolus.meta import update_metadata
from aeolus.model import um
from aeolus.region import Region
from aeolus.subset import extract_last_n_days
import iris
from iris.coord_systems import GeogCS
import matplotlib.colors as mcol
import matplotlib.patheffects as path_effects
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")

PROJECT = "thunderstruck"
LOWRES = "N96"
HIGHRES = "N1280"
ACCUM_PERIOD = iris.cube.Cube(3600 * 24, units="s")  # 1 day
CMAP_SIM6 = mcol.LinearSegmentedColormap.from_list(
    "", ["#519fd3", "#286886", "#190c09", "#7d341e", "#be6f63", "#ffadad"]
)
# ",".join([f'"{mcol.to_hex(cmap(i))}"' for i in range(cmap.N)])
# cmap = cmcrameri.cm.managua_r.resampled(6)

KW_TEXT = {
    "ha": "left",
    "weight": "bold",
    "size": "large",
    "rotation": 15,
    "path_effects": [path_effects.Stroke(linewidth=0.25, foreground="w")],
    "clip_on": False,
}
KW_DELIM_LINE = {
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


# Two groups of experiments with different lightning schemes
@dataclass
class LightParamConfig:
    """Experiment configuration for different lightning schemes."""

    title: str
    short_title: str
    ref: str
    model_res: str
    time_ave_label: str
    time_ave_func: callable
    suites: str
    file_mask: str = "*"
    kw_plt: dict = field(default_factory=dict)


M09 = LightParamConfig(
    title="M09 (Microphysics-based)",
    short_title="M09",
    ref="McCaul et al. (2009)",
    model_res=HIGHRES,
    suites="hr",
    time_ave_label="5-day mean",
    time_ave_func=lambda cube: time_mean(extract_last_n_days(cube, days=5)),
    file_mask="umglaa.p*00000*",
)
PR92 = LightParamConfig(
    title="PR92 (Convection-based)",
    short_title="PR92",
    ref="Price & Rind (1992)",
    model_res=LOWRES,
    suites="lr",
    time_ave_label="30-day mean",
    time_ave_func=lambda cube: time_mean(extract_last_n_days(cube, days=30)),
    file_mask="umglaa.pe00000*",
)

LPC = {"m09": M09, "pr92": PR92}  # store both of them in one dictionary


# Containers for simulation groups
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
    "surf": Group(
        title="Surface",
        simulations=(
            "hab1_aqua",
            "hab1_rect_b2",
            "hab1_rect_b8",
            "hab1_rect_e4",
        ),
    ),
}

# Geographical region objects
# Hemispheres
DAYSIDE = Region(-90, 90, -90, 90, name="dayside", model=um)
NIGHTSIDE = Region(90, -90, -90, 90, name="nightside", model=um)
# Rectangular continents (Lewis+18)
B2_CONT = Region(-36.25, 36.25, -19, 19, name="B2", model=um)
B8_CONT = Region(-93.75, 93.75, -49, 49, name="B8", model=um)
E4_CONT = Region(1.25, 113.75, -29, 29, name="E4", model=um)


# Individual simulations and their corresponding Rose suites
@dataclass
class Simulation:
    """UM simulation details."""

    group: str
    title: str
    diag_suites: dict = field(default_factory=dict)
    spinup_suites: dict = field(default_factory=dict)
    timestep: int = 240
    # lightning_parameterisation: str = "mccaul"
    continent: Region = None
    resolution_high: str = HIGHRES
    resolution_low: str = LOWRES
    kw_plt: dict = field(default_factory=dict)


SIMULATIONS = {
    "hab1": Simulation(
        group="comp",
        title="THAI Hab 1",
        diag_suites={"hr": "dg272", "lr": "do191"},
        spinup_suites={"hr": "ct229", "lr": "co730"},
        kw_plt={"color": "C7", "marker": "o"},
    ),
    "hab2": Simulation(
        group="comp",
        title="THAI Hab 2",
        diag_suites={"hr": "dg306", "lr": "do262"},
        spinup_suites={"hr": "cu096", "lr": "cr413"},
        kw_plt={"color": "C5", "marker": "^"},
    ),
    "archean_early": Simulation(
        group="comp",
        title="Early Archean",
        diag_suites={"hr": "dg936", "lr": "do263"},
        spinup_suites={"hr": "cz507", "lr": "cr388"},
        kw_plt={"color": "C6", "marker": "p"},
    ),
    "archean_late": Simulation(
        group="comp",
        title="Late Archean",
        diag_suites={"hr": "dg937", "lr": "do264"},
        spinup_suites={"hr": "cz508", "lr": "cr389"},
        kw_plt={"color": "C8", "marker": "P"},
    ),
    "hab1_0p25bar": Simulation(
        group="pres",
        title="0.25 bar",
        diag_suites={"hr": "dg321", "lr": "do255"},
        spinup_suites={"hr": "cw021", "lr": "cq704"},
        kw_plt={"color": "#519fd3", "marker": "s"},
    ),
    "hab1_0p5bar": Simulation(
        group="pres",
        title="0.5 bar",
        diag_suites={"hr": "dg931", "lr": "do257"},
        spinup_suites={"hr": "cw375", "lr": "cq705"},
        kw_plt={"color": "#286886", "marker": "X"},
    ),
    "hab1_1bar": Simulation(  # Deliberate duplicate
        group="pres",
        title="1 bar",
        diag_suites={"hr": "dg272", "lr": "do191"},
        spinup_suites={"hr": "ct229", "lr": "co730"},
        kw_plt={"color": "#190c09", "marker": "o"},
    ),
    "hab1_2bar": Simulation(
        group="pres",
        title="2 bar",
        diag_suites={"hr": "dg932", "lr": "do258"},
        spinup_suites={"hr": "cx886", "lr": "cq706"},
        kw_plt={"color": "#7d341e", "marker": "^"},
    ),
    "hab1_4bar": Simulation(
        group="pres",
        title="4 bar",
        diag_suites={"hr": "dg935", "lr": "do259"},
        spinup_suites={"hr": "cy127", "lr": "cq707"},
        kw_plt={"color": "#be6f63", "marker": "h"},
    ),
    "hab1_10bar": Simulation(
        group="pres",
        title="10 bar",
        diag_suites={"hr": "dg333", "lr": "do260"},
        spinup_suites={"hr": "cy624", "lr": "cq708"},
        kw_plt={"color": "#ffadad", "marker": "P"},
    ),
    "hab1_aqua": Simulation(  # Deliberate duplicate
        group="surf",
        title="Aquaplanet",
        diag_suites={"hr": "dg272", "lr": "do191"},
        spinup_suites={"hr": "ct229", "lr": "co730"},
        kw_plt={"color": "C7", "marker": "o"},
    ),
    "hab1_rect_b2": Simulation(
        group="surf",
        title="B2 continent",
        diag_suites={"hr": "di560", "lr": "do274"},
        spinup_suites={"hr": "dg758", "lr": "cr577"},
        continent=B2_CONT,
        kw_plt={"color": "C1", "marker": "D"},
    ),
    "hab1_rect_b8": Simulation(
        group="surf",
        title="B8 continent",
        diag_suites={"hr": "di561", "lr": "do275"},
        spinup_suites={"hr": "dg759", "lr": "cr578"},
        continent=B8_CONT,
        kw_plt={"color": "C2", "marker": "P"},
    ),
    "hab1_rect_e4": Simulation(
        group="surf",
        title="E4 continent",
        diag_suites={"hr": "di562", "lr": "do276"},
        spinup_suites={"hr": "dg760", "lr": "cr579"},
        continent=E4_CONT,
        kw_plt={"color": "C3", "marker": "X"},
    ),
}


# Project-specific functions
def callback_coord_system(cube, field, filename, const, model=um):
    """Attach a Coordinate System to the cube coordinates."""
    coord_system = GeogCS(semi_major_axis=const.radius.data)
    for coord_name in [model.x, model.y]:
        cube.coord(coord_name).coord_system = coord_system


@update_metadata(name="flash_rate", units="km-2 yr-1")
def calc_flash_rate(cubelist, accum_period):
    """Convert number of lightning flashes to flash rate (per km2 per year)."""
    num_fl = cubelist.extract_cube(
        iris.Constraint(
            name="Number_of_lightning_flashes",
            cube_func=lambda cube: cube.shape[-2:] != (1, 1),
        )
    )

    fl_pa_pyr = num_fl / area_weights_cube(num_fl) / accum_period
    fl_pa_pyr.coord(um.x).bounds = None
    fl_pa_pyr.coord(um.y).bounds = None
    return fl_pa_pyr


@update_metadata(name="total_flash_rate", units="s-1")
def calc_total_flash_rate(cubelist, accum_period):
    """Convert number of lightning flashes to flash rate (per km2 per year)."""
    num_fl = cubelist.extract_cube(
        iris.Constraint(
            name="Number_of_lightning_flashes",
            cube_func=lambda cube: cube.shape[-2:] != (1, 1),
        )
    )
    num_fl_tot = num_fl / accum_period
    # num_fl_tot = spatial(num_fl_tot, "mean")
    num_fl_tot = num_fl_tot.collapsed([um.x, um.y], iris.analysis.SUM)

    return num_fl_tot


@update_metadata(name="convective_cloud_depth", units="m")
def calc_cloud_depth(cubelist):
    """Calculate convective cloud depth from 2-224 and 2-225."""
    cld_base_h = cubelist.extract_cube("m01s05i224").copy()
    cld_base_h.units = "kft"
    cld_top_h = cubelist.extract_cube("m01s05i225").copy()
    cld_top_h.units = "kft"
    cld_dep = cld_top_h - cld_base_h
    return cld_dep


@update_metadata(name="convective_cloud_top_height", units="m")
def conv_cloud_top(cubelist):
    """Convective cloud top height (STASH 2-225)."""
    cld_top = cubelist.extract_cube("m01s05i225").copy()
    cld_top.units = "kft"
    return cld_top


@update_metadata(name="cloud_to_ground_flash_rate_ratio", units="1")
def extract_lfr_ratio(cubelist):
    """Extract lightning flash ratio and update its metadata."""
    cube = cubelist.extract_cube("m01s21i099")
    return cube
