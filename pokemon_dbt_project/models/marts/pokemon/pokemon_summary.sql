{{ config(materialized='table') }}

with pokemon as (

    select *
    from {{ ref('stg_pokemon') }}

),

aggregated as (

    select

        primary_type,

        count(*) as pokemon_count,

        avg(total_stats) as avg_total_stats,

        avg(attack) as avg_attack,

        avg(defense) as avg_defense,

        avg(speed) as avg_speed,

        sum(
            case
                when is_legendary = true then 1
                else 0
            end
        ) as legendary_count

    from pokemon
    group by primary_type

)

select *
from aggregated
order by avg_total_stats desc