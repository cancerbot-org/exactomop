import io, sys, zipfile, requests, pandas as pd
import urllib.request
import certifi
import ssl

NE_STATES = {"CT","ME","MA","NH","RI","VT","NJ","NY","PA"}

# 1) ACS 2023 5-year: table B03002 (total + Non-Hispanic White alone) by ZCTA
ACS_URL = "https://api.census.gov/data/2023/acs/acs5"
VARS = ["NAME","B03002_001E","B03002_003E"]
r = requests.get(ACS_URL, params={"get": ",".join(VARS), "for": "zip code tabulation area:*"})
r.raise_for_status()
acs = pd.DataFrame(r.json()[1:], columns=VARS+["zcta"])
acs["tot"] = pd.to_numeric(acs["B03002_001E"], errors="coerce")
acs["nh_white"] = pd.to_numeric(acs["B03002_003E"], errors="coerce")
acs["nh_white_share"] = acs["nh_white"]/acs["tot"]
acs["zip"] = acs["zcta"]

# 2) ZCTA → county relationship (2020) from Census; derive state via county FIPS

ssl._create_default_https_context = ssl._create_unverified_context
rel = pd.read_csv("https://www2.census.gov/geo/docs/maps-data/data/rel2020/zcta520/tab20_zcta520_county20_natl.txt", sep="|", dtype=str)


# GEOID_COUNTY_20 = 5-digit (SSCCC). Keep a single (largest land overlap) county per ZCTA to pick state.
rel["AREALAND_PART"] = pd.to_numeric(rel["AREALAND_PART"], errors="coerce")
rel = rel.sort_values(["GEOID_ZCTA5_20","AREALAND_PART"], ascending=[True,False]).drop_duplicates("GEOID_ZCTA5_20")
rel["state_fips"] = rel["GEOID_COUNTY_20"].str[:2]

# 3) Map state FIPS → USPS
state_map = {
  "09":"CT","23":"ME","25":"MA","33":"NH","44":"RI","50":"VT",
  "34":"NJ","36":"NY","42":"PA","10":"DE","11":"DC","24":"MD","44":"RI","50":"VT"
}
rel["state"] = rel["state_fips"].map(state_map)

# 4) Join & filter to Northeast + majority non-white (Non-Hispanic White alone < 50%)
out = (acs.merge(rel[["GEOID_ZCTA5_20","state"]], left_on="zip", right_on="GEOID_ZCTA5_20", how="left")
         .dropna(subset=["state"])
         .query("state in @NE_STATES and tot > 0 and nh_white_share < 0.5")
         .loc[:,["zip","state","tot","nh_white","nh_white_share","NAME"]]
         .sort_values(["state","zip"]))

out.to_csv("northeast_majority_nonwhite_zctas.csv", index=False)
print(f"Wrote northeast_majority_nonwhite_zctas.csv with {len(out)} ZCTAs")