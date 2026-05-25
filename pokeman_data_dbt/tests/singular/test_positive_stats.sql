select *
from {{ ref('stg_pokemon') }}

where hp < 0
   or attack < 0
   or defense < 0
   or speed < 0