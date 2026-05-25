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
from {{ source('pokemon_source', 'pokemon_raw') }}