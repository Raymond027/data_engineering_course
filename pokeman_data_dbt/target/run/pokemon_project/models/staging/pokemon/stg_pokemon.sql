
  create view "pokemon_db"."analytics_staging"."stg_pokemon__dbt_tmp"
    
    
  as (
    select
    pokemon_id,
    pokemon_name,
    primary_type,
    secondary_type,
    hp,
    attack,
    defense,
    speed,
    generation,
    is_legendary
from "pokemon_db"."public"."pokemon_raw"
  );