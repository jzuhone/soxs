import astropy.units as apu
from astropy.constants import h, c, u
import numpy as np

one_arcsec = 1.0/3600.0

erg_per_eV = apu.eV.to("erg")
erg_per_keV = erg_per_eV * 1.0e3
keV_per_erg = 1.0 / erg_per_keV
eV_per_erg = 1.0 / erg_per_eV
K_per_keV = apu.keV.to("K", equivalencies=apu.temperature_energy())

hc = (h*c).to("keV*angstrom").value
clight = c.to("cm/s").value
ckms = c.to_value("km/s")

sigma_to_fwhm = 2.*np.sqrt(2.*np.log(2.))
sqrt2pi = np.sqrt(2.*np.pi)

m_u = u.to("g").value

elem_names = ["", "H", "He", "Li", "Be", "B", "C", "N", "O",
              "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S",
              "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr",
              "Mn", "Fe", "Co", "Ni", "Cu", "Zn"]

cosmic_elem = [1, 2, 3, 4, 5, 9, 11, 15, 17, 19,
               21, 22, 23, 24, 25, 27, 29, 30]
metal_elem = [6, 7, 8, 10, 12, 13, 14, 16, 18, 20, 26, 28]

atomic_weights = np.array([0.0, 1.00794, 4.00262, 6.941, 9.012182, 10.811,
                           12.0107, 14.0067, 15.9994, 18.9984, 20.1797,
                           22.9898, 24.3050, 26.9815, 28.0855, 30.9738,
                           32.0650, 35.4530, 39.9480, 39.0983, 40.0780,
                           44.9559, 47.8670, 50.9415, 51.9961, 54.9380,
                           55.8450, 58.9332, 58.6934, 63.5460, 65.3800])

abund_tables = {
    "angr": np.array([0.0, 1.00E+00, 9.77E-02, 1.45E-11, 1.41E-11, 3.98E-10,
                      3.63E-04, 1.12E-04, 8.51E-04, 3.63E-08, 1.23E-04,
                      2.14E-06, 3.80E-05, 2.95E-06, 3.55E-05, 2.82E-07,
                      1.62E-05, 3.16E-07, 3.63E-06, 1.32E-07, 2.29E-06,
                      1.26E-09, 9.77E-08, 1.00E-08, 4.68E-07, 2.45E-07,
                      4.68E-05, 8.32E-08, 1.78E-06, 1.62E-08, 3.98E-08]),
    "aspl": np.array([0.0, 1.00E+00, 8.51E-02, 1.12E-11, 2.40E-11, 5.01E-10,
                      2.69E-04, 6.76E-05, 4.90E-04, 3.63E-08, 8.51E-05,
                      1.74E-06, 3.98E-05, 2.82E-06, 3.24E-05, 2.57E-07,
                      1.32E-05, 3.16E-07, 2.51E-06, 1.07E-07, 2.19E-06,
                      1.41E-09, 8.91E-08, 8.51E-09, 4.37E-07, 2.69E-07,
                      3.16E-05, 9.77E-08, 1.66E-06, 1.55E-08, 3.63E-08]),
    "wilm": np.array([0.0, 1.00E+00, 9.77E-02, 0.00, 0.00, 0.00, 2.40E-04,
                      7.59E-05, 4.90E-04, 0.00, 8.71E-05, 1.45E-06, 2.51E-05,
                      2.14E-06, 1.86E-05, 2.63E-07, 1.23E-05, 1.32E-07,
                      2.57E-06, 0.00, 1.58E-06, 0.00, 6.46E-08, 0.00,
                      3.24E-07, 2.19E-07, 2.69E-05, 8.32E-08, 1.12E-06,
                      0.00, 0.00]),
    "feld": np.array([0.0, 1.00E+00, 9.77E-02, 1.26E-11, 2.51E-11, 3.55E-10,
                      3.98E-04, 1.00E-04, 8.51E-04, 3.63E-08, 1.29E-04,
                      2.14E-06, 3.80E-05, 2.95E-06, 3.55E-05, 2.82E-07,
                      1.62E-05, 3.16E-07, 4.47E-06, 1.32E-07, 2.29E-06,
                      1.48E-09, 1.05E-07, 1.00E-08, 4.68E-07, 2.45E-07,
                      3.24E-05, 8.32E-08, 1.78E-06, 1.62E-08, 3.98E-08]),
    "lodd": np.array([0.0, 1.00E+00, 7.92E-02, 1.90E-09, 2.57E-11, 6.03E-10,
                      2.45E-04, 6.76E-05, 4.90E-04, 2.88E-08, 7.41E-05,
                      1.99E-06, 3.55E-05, 2.88E-06, 3.47E-05, 2.88E-07,
                      1.55E-05, 1.82E-07, 3.55E-06, 1.29E-07, 2.19E-06,
                      1.17E-09, 8.32E-08, 1.00E-08, 4.47E-07, 3.16E-07,
                      2.95E-05, 8.13E-08, 1.66E-06, 1.82E-08, 4.27E-08])
}
