import pvlib
from pvlib import location, irradiance, clearsky
import pandas as pd

# Definir localização (latitude, longitude, fuso horário, altitude)
latitude = -3.71722
longitude = -38.5434
tz = "America/Fortaleza"
altitude = 10

site_location = location.Location(latitude=latitude, longitude=longitude, tz=tz, altitude=altitude)

# Criar um DataFrame com timestamps (horas) para um dia
times = pd.date_range("2024-06-06 00:00", "2024-06-06 23:59", freq="1h", tz=site_location.tz)  # Use "1h" em vez de "1H"

# Calcular a posição solar
solpos = site_location.get_solarposition(times)

# Obter a turbidez de Linke
linke_turbidity = pvlib.clearsky.lookup_linke_turbidity(times, latitude, longitude)

# Calcular a irradiância extraterrestre
dni_extra = irradiance.get_extra_radiation(times)

# Calcular a irradiância global horizontal (GHI) assumindo atmosfera clara usando modelo Ineichen
cs = clearsky.ineichen(times, site_location, linke_turbidity=linke_turbidity, dni_extra=dni_extra)

ghi = cs['ghi']
dhi = cs['dhi']
dni = cs['dni']

# Calcular a irradiância no plano inclinado
total_irradiance = irradiance.get_total_irradiance(
    surface_tilt=30,
    surface_azimuth=180,
    dni=dni,
    ghi=ghi,
    dhi=dhi,
    solar_zenith=solpos['apparent_zenith'],
    solar_azimuth=solpos['azimuth']
)

# Exibir a irradiância no plano inclinado
print(total_irradiance)
