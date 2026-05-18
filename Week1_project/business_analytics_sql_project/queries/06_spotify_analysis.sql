SELECT 
    st.artist_name,
    AVG(st.popularity) AS avg_popularity
FROM spotify_tracks st
GROUP BY st.artist_name
ORDER BY avg_popularity DESC;
