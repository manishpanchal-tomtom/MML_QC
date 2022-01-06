import psycopg2
import geopandas as gpd


def mml_ext(country, proj, st_date=None, end_date=None):
    # Connect global spatial file from db

    conn = psycopg2.connect("postgresql://momalight:momalight@momalightdbro.tomtomgroup.com:5432/momalight")

    # Intersect query within input point & global data
    sql = "select insert_date, sessionname, geometry FROM momalight.sessions as s " \
          "where (sessionname like '%{}%') " \
          "AND (sessionname like UPPER('%{}%')) " \
          "AND (insert_date BETWEEN '{}' AND '{}')".format(country, proj, st_date, end_date)

    # Create dataframe from intersection
    mml = gpd.read_postgis(sql, conn, geom_col='geometry')

    return mml




