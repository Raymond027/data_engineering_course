
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select defense
from "pokemon_db"."analytics_staging"."stg_pokemon"
where defense is null



  
  
      
    ) dbt_internal_test