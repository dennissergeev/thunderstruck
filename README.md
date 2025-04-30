<h1 align="center">
:cloud_with_lightning_and_rain: thunderstruck :cloud_with_lightning_and_rain:
</h1>
<h2 align="center">
 Lightning activity on a tidally locked terrestrial exoplanet in storm-resolving simulations for a range of surface pressures
</h2>

<p align="center">
<a href="https://arxiv.org/abs/2504.19883">
<img src="https://img.shields.io/badge/arXiv-2504.19883-red"
     alt="arXiv preprint"></a>
<a href="https://www.python.org/downloads/">
<img src="https://img.shields.io/badge/python-3.13-blue.svg"
     alt="Python 3.13"></a>
<a href="https://github.com/psf/black">
<img src="https://img.shields.io/badge/code%20style-black-000000.svg"
     alt="black"></a>
<a href="https://pixi.sh">
<img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/prefix-dev/pixi/main/assets/badge/v0.json"
     alt="Pixi badge"></a>
<a href="LICENSE">
<img src="https://img.shields.io/badge/license-MIT-green.svg"
     alt="License: MIT"></a>
</p>

<h2 align="center">Repository contents</h2>

* [`src/scripts/`](src/scripts/): Python scripts and Jupyter Notebooks
* [`src/figures/`](src/figures/): Figures

|  #  | Figure | Notebook |
|:---:|:-------|:---------|
|  1  | [Global Diagnostics](src/figures/thunderstruck__pres__num_fl_m09_t_sfc_iwp_caf_gwp_prec__global.pdf) | [Glob-Diags.ipynb](https://nbviewer.jupyter.org/github/dennissergeev/thunderstruck/blob/main/src/scripts/Glob-Diags.ipynb) |
|  2  | [Maps of lightning activity in M09](src/figures/thunderstruck__pres__m09__lfr__maps.pdf) | [Maps.ipynb](https://nbviewer.jupyter.org/github/dennissergeev/thunderstruck/blob/main/src/scripts/Maps.ipynb) |
|  3  | [Maps of cloud ice content](src/figures/thunderstruck__pres__m09__iwp__maps.pdf) | [Maps.ipynb](https://nbviewer.jupyter.org/github/dennissergeev/thunderstruck/blob/main/src/scripts/Maps.ipynb) |
|  4  | [Vertical profiles of temperature and hydrometeors](src/figures/thunderstruck__pres__temp_m_ci_m_cl_m_g__vert_prof.pdf) | [Vertical-Profiles.ipynb](https://nbviewer.jupyter.org/github/dennissergeev/thunderstruck/blob/main/src/scripts/Vertical-Profiles.ipynb) |
|  5  | [Lightning flash rate and convective cloud depths](src/figures/thunderstruck__pres__num_fl_pr92_cld_dep__global.pdf) | [Glob-Diags.ipynb](https://nbviewer.jupyter.org/github/dennissergeev/thunderstruck/blob/main/src/scripts/Glob-Diags.ipynb) |
|  6  | [Maps of lightning activity in PR92](src/figures/thunderstruck__pres__pr92__lfr__maps.pdf) | [Maps.ipynb](https://nbviewer.jupyter.org/github/dennissergeev/thunderstruck/blob/main/src/scripts/Maps.ipynb) |

<h2 align="center">How to run code</h2>

1. Install [pixi](https://pixi.sh)
2. Download / check out this repository
3. Navigate to this folder
4. Run `pixi install --all` to create the Python environment
5. Open notebooks in jupyter lab: `pixi run jupyter lab`
6. Enjoy

```
System
------------
       Pixi version: 0.46.0
           Platform: linux-64
   Virtual packages: __unix=0=0
                   : __linux=4.15.0=0
                   : __glibc=2.27=0
                   : __archspec=1=skylake_avx512
          Cache dir: /home/ds591/.cache/rattler/cache
       Auth storage: /home/ds591/.rattler/credentials.json
   Config locations: No config files found

Global
------------
            Bin dir: /home/ds591/.pixi/bin
    Environment dir: /home/ds591/.pixi/envs
       Manifest dir: /home/ds591/.pixi/manifests/pixi-global.toml

Workspace
------------
               Name: thunderstruck
            Version: 0.1
      Manifest file: /home/ds591/planets/lightning_proj/thunderstruck/pyproject.toml
       Last updated: 30-04-2025 20:49:39

Environments
------------
        Environment: default
           Features: default
           Channels: conda-forge
   Dependency count: 12
       Dependencies: python, aeolus, cartopy, ipykernel, iris, matplotlib, numpy, pandas, tqdm, mo_pack, cmocean, jupyterlab
  PyPI Dependencies: thunderstruck
   Target platforms: linux-64
              Tasks: check-dependencies
```
