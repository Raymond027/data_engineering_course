{{ config(materialized='view') }}

with source_data as (

    select *
    from {{ source('raw', 'pokemon') }}

),

cleaned as (

    select

        cast(id as integer) as pokemon_id,

        trim(name) as pokemon_name,

        lower(type1) as primary_type,

        lower(type2) as secondary_type,

        cast(total as integer) as total_stats,

        cast(hp as integer) as hp,

        cast(attack as integer) as attack,

        cast(defense as integer) as defense,

        cast(speed as integer) as speed,

        cast(generation as integer) as generation,

        cast(legendary as boolean) as is_legendary

    from source_data

    where name is not null

)

select *
from cleaned