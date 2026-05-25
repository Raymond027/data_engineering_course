
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select generation
from "pokemon_db"."analytics_staging"."stg_pokemon"
where generation is null



  
  
      
    ) dbt_internal_test